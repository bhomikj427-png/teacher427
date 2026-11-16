#!/usr/bin/env python3
"""auto-v2.py: run this project's sprint/hand-off workflow unattended, with a small start-up.

auto-v2 = auto.py plus a lean session (2026-11-16; learner: a session must boot in 20-25k tokens).
Measured start-up of a one-line session: 38.0k (auto.py) -> 7.6k with the cuts below (+1-2k for web tools):
  - CLAUDE.md not auto-loaded (CLAUDE_CODE_DISABLE_CLAUDE_MDS=1); auto-v2-contract.md is pasted
    into the kickoff instead (only the rules a sprint needs)
  - auto-memory off (CLAUDE_CODE_DISABLE_AUTO_MEMORY=1)
  - only the tools a sprint uses (--tools: Bash Read Edit Write Grep Glob WebSearch WebFetch)
  - no skills / slash commands (--disable-slash-commands); no claude.ai connectors (--strict-mcp-config)
Each session's start-up cost is logged ("boot") and flagged if it is over BOOT_WARN.
  - 5-minute prompt cache (FORCE_PROMPT_CACHING_5M=1); the contract asks for fewer, bigger steps (2026-11-17)
State, lock, hook and stop flags are shared with auto.py (.claude/auto/), so `stop`/`status` work
from either script and the two can never run at once.

What you used to do by hand          What auto.py does instead
---------------------------------    ------------------------------------------
open a new Claude Code window        start a fresh `claude -p` session
type the kickoff for a subject       send the same kickoff (+ unattended rules)
wait; it writes the hand-off; stops  same: the session still decides where to stop
go back to step 1                    commit, check the brakes, start the next one

Usage (from any folder; the project root is this file's folder):
  python auto-v2.py run sem-3/01-statistics-and-probability [--until "S10 done"] [--check "<cmd>"] [--sessions 5]
                 [--hours 6] [--session-timeout 60] [--soft-limit 150000]
                 [--hard-limit 210000] [--wait-on-limit] [--yes] [--no-commit]
                 [--no-review] [--claude-bin PATH]
  python auto.py stop          # graceful: the session wraps up, no new one starts
  python auto.py stop --now    # kill the running session's process tree now
  python auto.py status

Python standard library only. Everything auto.py writes lives in .claude/auto/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import json
import os
import re
import tempfile
import shutil
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

# =============================================================================
# PERMISSIONS for unattended sessions (written into the per-run settings file)
# =============================================================================
# These MERGE with your own settings (.claude/settings.json, ~/.claude/...): your
# allow rules still apply, and a deny rule here always beats an allow anywhere.
#
# Path rules were tested in a sandbox copy of this project (path contains an
# apostrophe). Findings that shaped the form used below:
#   - "Edit(./X)", "Edit(X)", "Edit(**/X)"  -> work (relative to the cwd = root)
#   - "Edit(/X)"                            -> relative to THIS settings file
#                                              (.claude/auto/), so useless here
#   - "Edit(//c/abs/path)"                  -> works, but NOT when the path has
#                                              an apostrophe, like ece'
#   - "Write(...)" rules                    -> no effect; Edit rules cover Write
# Writes into .claude/ are additionally refused by Claude Code's own built-in
# sensitive-file guard; the deny rule below is a second layer.

# Shell commands your sessions actually used (audited from past transcripts).
BASH_ALLOWED_COMMANDS = [
    "python", "python3", "py",                      # scripts, pypdf, lookups
    "cat", "head", "tail", "sed", "awk", "grep", "cut", "tr", "sort", "uniq",
    "wc", "ls", "find", "file", "du", "diff", "md5sum", "sha256sum",
    "cd", "echo", "printf", "date", "pwd", "which", "cygpath", "basename", "dirname",
    "mkdir", "cp", "mv", "rm", "touch",               # scratchpad file juggling
    "curl",                                          # papers / abstracts
    "pdftotext", "pdfinfo", "timeout",
]
GIT_READ_ONLY = ["status", "diff", "log", "show"]
OTHER_ALLOWED_TOOLS = ["WebSearch", "WebFetch"]       # research needs the web

# Git subcommands that change something. Denied explicitly because your
# project settings ALLOW git add/commit/push, and deny beats allow.
GIT_DENIED = [
    "add", "commit", "push", "pull", "fetch", "merge", "rebase", "reset",
    "checkout", "switch", "restore", "stash", "branch", "tag", "clean", "rm",
    "mv", "init", "clone", "config", "remote", "cherry-pick", "revert", "am",
    "apply", "gc", "prune", "update-ref", "update-index", "worktree",
    "submodule", "notes", "filter-branch", "replace", "commit-tree",
    "symbolic-ref", "reflog",
]
# Core config a session must never edit (+ auto.py and its own folder, so a
# session can't switch off its own brakes).
EDIT_DENIED_PATHS = [
    "./CLAUDE.md", "**/CLAUDE.md", "./CLAUDE.local.md", "./.mcp.json",
    "./.claude/**",            # settings*.json, hooks, commands, skills, auto/
    "./auto.py", "./auto-v2.py", "./auto-v2-contract.md",
]
OTHER_DENIED = [
    "Bash(git -C *)", "Bash(git -c *)",        # forms that dodge the list above
    "Bash(*auto.py*)", "Bash(*auto-v2*)",       # no running/reading auto.py / auto-v2.py
    "Bash(claude)", "Bash(claude *)", "Bash(*claude.exe*)", "Bash(*claude -p*)",
    "AskUserQuestion",                          # nobody is there to answer
    "EnterWorktree", "ExitWorktree",            # no branch/worktree switching
    "CronCreate", "ScheduleWakeup", "RemoteTrigger",   # no self-scheduling
]


def permission_rules():
    allow = []
    for c in BASH_ALLOWED_COMMANDS:
        allow += ["Bash(%s)" % c, "Bash(%s *)" % c]
    for g in GIT_READ_ONLY:
        allow += ["Bash(git %s)" % g, "Bash(git %s *)" % g]
    allow += OTHER_ALLOWED_TOOLS
    deny = []
    for g in GIT_DENIED:
        deny += ["Bash(git %s)" % g, "Bash(git %s *)" % g]
    deny += ["Edit(%s)" % p for p in EDIT_DENIED_PATHS]
    deny += OTHER_DENIED
    return allow, deny


# The final review session may only look, never touch.
# (no sed/find/sort: `sed -i`, `find -delete`, `sort -o` can write)
REVIEW_BASH = ["cat", "head", "tail", "grep", "wc", "ls", "cut", "uniq"]

# =============================================================================
# Kickoff text
# =============================================================================
# Your kickoff (your wording, set 2026-11-15). A fresh -p
# session finds the hand-off by itself (CLAUDE.md -> progress-log.md ->
# sprints.md "Current hand-off"; verified in a sandbox), so the kickoff does NOT
# tell it to read the hand-off - that would load it twice.
# auto-v2: CLAUDE.md is not loaded, so the kickoff names the plan file itself
# and auto-v2-contract.md (pasted above it) carries the rules a sprint needs.
KICKOFF_TEMPLATE = ("{subject}, work on automated sprints without getting dumb "
                    "from too much context. The plan and the *Current hand-off* are in "
                    "{subject_dir}sprints.md (grep its headings, read by line range).")

UNATTENDED_RULES = """\
--- Running under auto.py (unattended) ---
- You are running unattended. Nobody will answer questions.
- Use BLOCKED only when there is no reasonable default AND a wrong guess would be costly or hard to undo (put the question in the handoff). Otherwise pick the most reasonable option, record it in the handoff under "Assumptions to review", and keep going. Do the unblocked parts first; use BLOCKED only when nothing useful is left.
- Never run commands that wait for keyboard input.
- Temporary files (downloads, transcripts, PDFs, helper scripts) go in {scratch}/ (use that exact path; /tmp, $TEMP and other folders outside the project are blocked). It is not committed.
- Shell commands are checked automatically and refused when they can't be verified, so keep them simple: no `$VAR`/`${{...}}` variables, no `for`/`while` loops, no `git -C`, and no `cd` combined with a command that writes files. For anything more involved, write a small Python script into {scratch}/ and run it with `python -I <script>`.
- Don't run git commands that change anything. auto.py commits after you finish (this replaces the commit + push steps in the sprint steps and sprints.md). Uncommitted changes outside {subject_dir} belong to other work: leave them alone.
- You'll get context notices. When one tells you to wrap up: finish the current step, stop at a clean point, and write the handoff the usual way.
- Always write the handoff before ending, even for DONE. End your final message with exactly these two lines:
SUMMARY: <one line: what you did; for BLOCKED, the question>
STATUS: CONTINUE | DONE | BLOCKED"""

MILESTONE_RULE = """\
- Milestone for this run: {until}
  Work toward it (it may take several sessions). Use STATUS: DONE only when it is fully reached; don't go beyond it."""

DONE_RULE = """\
- STATUS: DONE means the subject's whole plan is finished (nothing left you can do)."""

RECOVERY_TEXT = """\
The previous session was cut off before finishing. {where} First rebuild the state from the handoff and that commit, update the handoff, then continue as normal.

"""

CHECK_FAILED_TEXT = """\
- The previous session reported DONE, but the destination check `{cmd}` still fails (exit {code}). Keep working toward it. Last 50 lines of its output:
```
{output}
```"""

REVIEW_PROMPT = """\
You are reviewing work that unattended sessions (run by auto.py) just did on the subject "{subject}" ({subject_dir}). This is a read-only review: do NOT edit or write any file and do not run anything that changes files.

Commits to review (only these; other commits in between belong to unrelated work):
{commits}

Use `git show <hash>` / `git show --stat <hash>` and read files as needed.

Report, in this order:
1. What was done: a short summary per commit, in plain words.
2. Mistakes check. Look for: hand-off, sprint table and progress-log disagreeing with each other or with the files actually written; work marked done that is not in the files; source IDs cited but missing from sources.md; numbering gaps or duplicates (e.g. misconception IDs); accidental deletions or truncated files; broken markdown tables; anything that breaks the rules in auto-v2-contract.md, the sprint protocol (e.g. study-pack-sprint-protocol.md) or sprints.md; and every item under "Assumptions to review".
3. Each problem with file:line and a suggested fix.

End with exactly one line: VERDICT: CLEAN or VERDICT: ISSUES"""

# =============================================================================
# Paths and defaults
# =============================================================================
ROOT = Path(__file__).resolve().parent          # works when run from any folder
AUTO = ROOT / ".claude" / "auto"
STATE = AUTO / "state.json"
HOOK_STATE = AUTO / "hook-state.json"
LOCK = AUTO / "lock"
STOP_FLAG = AUTO / "STOP"
STOP_NOW_FLAG = AUTO / "STOP_NOW"
LOG = AUTO / "log.jsonl"
RUNS = AUTO / "runs"
RUN_SETTINGS = AUTO / "run-settings.json"
REVIEW_SETTINGS = AUTO / "review-settings.json"
HOOK = AUTO / "hook.py"
CONTRACT = ROOT / "auto-v2-contract.md"   # pasted into every kickoff
SESSION_TOOLS = "Bash,Read,Edit,Write,Grep,Glob,WebSearch,WebFetch"
REVIEW_TOOLS = "Bash,Read,Grep,Glob"
# FORCE_PROMPT_CACHING_5M: steps are seconds apart, so a 5-minute cache is enough; 1-hour cache
# writes cost ~2x input vs ~1.25x (tested 2026-11-17: the 5m TTL takes effect).
LEAN_ENV = {"CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1", "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
            "FORCE_PROMPT_CACHING_5M": "1"}
BOOT_WARN = 25_000   # first-call context above this = a cut stopped working
SUBJECTS = ROOT / "subjects"
HANDOFF_NAME = "sprints.md"          # the hand-off ("Current hand-off" block)
PROGRESS_NAME = "progress-log.md"    # also updated at every hand-off
USER_SETTINGS = Path.home() / ".claude" / "settings.json"
# Scratch space for downloads/transcripts, outside the repo (never committed).
# Granted via permissions.additionalDirectories. No apostrophe in this path.
SCRATCH_ROOT = Path(tempfile.gettempdir()) / "ece-auto"

# Limits. Your model (Opus 5.5) has a 1,000,000-token window, but quality, not
# the window, is the constraint: your past sprints wrote their hand-offs at
# ~114k-168k tokens, and auto-compact has fired as early as 218k. SOFT 150k
# lands inside the range where sprints naturally close, leaving ~60k tokens to
# finish a step and write the hand-off. HARD 210k sits below the earliest
# auto-compact seen, so even if DISABLE_AUTO_COMPACT were ignored, a session is
# killed before it can be compacted.
DEFAULT_SOFT = 150_000
DEFAULT_HARD = 210_000

SECRET_PATTERNS = [r"\.env[^/]*", r"[^/]*\.pem", r"[^/]*\.key", r"id_rsa[^/]*", r"credentials[^/]*"]
SECRET_RE = re.compile(r"(^|/)(%s)$" % "|".join(SECRET_PATTERNS), re.I)
WIN = os.name == "nt"
POLL = float(os.environ.get("AUTO_POLL", "1.0"))   # loop tick; tests set it small


# =============================================================================
# Small helpers
# =============================================================================
def now_iso():
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def say(msg=""):
    print(msg, flush=True)


def fmt_dur(sec):
    sec = int(sec)
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    return "%dh%02dm" % (h, m) if h else ("%dm%02ds" % (m, s) if m else "%ds" % s)


def sha(path: Path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except FileNotFoundError:
        return None
    except OSError:
        return "unreadable"


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_json(path: Path, data):
    # Atomic replace so the hook (another process) never reads half a file.
    # On Windows the rename can briefly fail if a reader has the file open.
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".%d.%d.tmp" % (os.getpid(), threading.get_ident()))
    tmp.write_text(json.dumps(data, indent=1), encoding="utf-8")
    for _ in range(20):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            time.sleep(0.05)
    try:
        tmp.unlink()
    except OSError:
        pass


def git(*args, check=False, input=None):
    """Run git in the project root; returns CompletedProcess with text output."""
    p = subprocess.run(["git", "-c", "core.quotepath=false", *args], cwd=ROOT,
                       input=input, capture_output=True, encoding="utf-8",
                       errors="replace")
    if check and p.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), (p.stderr or p.stdout).strip()))
    return p


def rel(p: Path) -> str:
    return p.resolve().relative_to(ROOT).as_posix()


# ---- process control --------------------------------------------------------
def kill_tree(pid):
    """Kill a process and everything it started. claude spawns shells, python,
    curl... killing only the top process would leave those running."""
    if not pid:
        return
    if WIN:
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)],
                       capture_output=True)
    else:
        try:
            os.killpg(os.getpgid(pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass


def proc_ctime(pid):
    """Process start time, used to tell 'our' pid from a recycled one."""
    if WIN:
        import ctypes
        from ctypes import wintypes
        k32 = ctypes.windll.kernel32
        h = k32.OpenProcess(0x1000, False, int(pid))  # QUERY_LIMITED_INFORMATION
        if not h:
            return None
        try:
            code = wintypes.DWORD()
            if not k32.GetExitCodeProcess(h, ctypes.byref(code)) or code.value != 259:
                return None  # 259 = STILL_ACTIVE
            t = [wintypes.FILETIME() for _ in range(4)]
            if not k32.GetProcessTimes(h, *[ctypes.byref(x) for x in t]):
                return 0
            return (t[0].dwHighDateTime << 32) | t[0].dwLowDateTime
        finally:
            k32.CloseHandle(h)
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return None
    except PermissionError:
        pass
    try:
        return int(Path("/proc/%d/stat" % int(pid)).read_text().split(")")[1].split()[19])
    except Exception:
        return 0


def pid_alive(pid, ctime=None):
    c = proc_ctime(pid) if pid else None
    if c is None:
        return False
    return ctime in (None, 0) or c in (0, ctime)


class KeepAwake:
    """Stop the computer from sleeping mid-run (a sleeping PC kills the
    session's network calls). Windows: SetThreadExecutionState; macOS:
    caffeinate tied to our pid."""

    def __init__(self):
        self.proc = None

    def __enter__(self):
        try:
            if WIN:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)
            elif sys.platform == "darwin" and shutil.which("caffeinate"):
                self.proc = subprocess.Popen(["caffeinate", "-i", "-w", str(os.getpid())])
        except Exception:
            pass
        return self

    def __exit__(self, *a):
        try:
            if WIN:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
            elif self.proc:
                self.proc.terminate()
        except Exception:
            pass


# =============================================================================
# Git status, scoped to the subject folder
# =============================================================================
def porcelain(pathspec=None):
    """{path: XY} for changed/untracked files (not ignored). NUL-separated, so
    odd file names can't break parsing."""
    args = ["status", "--porcelain=v1", "-z", "-uall"]
    if pathspec:
        args += ["--", pathspec]
    out = git(*args).stdout
    parts = out.split("\0")
    res, i = {}, 0
    while i < len(parts):
        e = parts[i]
        i += 1
        if len(e) < 4:
            continue
        xy, path = e[:2], e[3:]
        res[path] = xy
        if xy[0] in "RC" and i < len(parts):   # rename: next field = old path
            res[parts[i]] = "D "
            i += 1
    return res


def fingerprint(pathspec=None):
    """{path: content hash} for every changed file. Comparing two fingerprints
    tells exactly which files a session touched, committed or not."""
    return {p: (xy, sha(ROOT / p)) for p, xy in porcelain(pathspec).items()}


def changed_between(before, after):
    return sorted(p for p in set(before) | set(after) if before.get(p) != after.get(p))


def is_secret(path):
    return bool(SECRET_RE.search(path))


class CommitError(Exception):
    pass


def commit_paths(paths, message):
    """Commit exactly these paths and nothing else (a parallel window's staged
    files stay staged and uncommitted). Returns the new hash or None."""
    paths = [p for p in paths if not is_secret(p)]
    if not paths:
        return None
    spec = "".join(":(literal)%s\0" % p for p in paths)
    RUNS.mkdir(parents=True, exist_ok=True)
    msgfile = RUNS / "commit-msg.txt"
    msgfile.write_text(message + "\n", encoding="utf-8")   # UTF-8 via file, not argv
    for attempt in range(6):
        a = git("add", "-A", "--pathspec-from-file=-", "--pathspec-file-nul", input=spec)
        c = None
        if a.returncode == 0:
            c = git("commit", "-q", "--no-edit", "-F", str(msgfile),
                    "--pathspec-from-file=-", "--pathspec-file-nul", input=spec)
            if c.returncode == 0:
                return git("rev-parse", "--short", "HEAD").stdout.strip()
        err = ((c or a).stdout + (c or a).stderr).strip()
        if "nothing to commit" in err or "no changes added" in err:
            return None
        if "index.lock" in err and attempt < 5:   # another git process is busy
            time.sleep(2)
            continue
        raise CommitError(err or "git exited with an error")


# =============================================================================
# The session runner
# =============================================================================
STATUS_RE = re.compile(r"^status\s*[:=\-]\s*(.*)$", re.I)
SUMMARY_RE = re.compile(r"^summary\s*[:=\-]\s*(.*)$", re.I)
LIMIT_TEXT_RE = re.compile(r"(hit your (usage )?limit|usage limit reached|limit reached\s*[\u00b7\u2219|]\s*resets)", re.I)


def parse_status(text):
    """Find SUMMARY/STATUS in the last lines of the final message. Tolerant of
    markdown (**STATUS:** `DONE`), extra spaces and case. A line that still has
    the template's 'CONTINUE | DONE | BLOCKED' is ignored (ambiguous)."""
    status = summary = None
    lines = [l.strip() for l in (text or "").strip().splitlines() if l.strip()][-8:]
    for l in lines:
        c = re.sub(r"[*_`>#]", "", l).strip().lstrip("-").strip()
        m = STATUS_RE.match(c)
        if m:
            words = re.findall(r"\b(CONTINUE|DONE|BLOCKED)\b", m.group(1).upper())
            if len(set(words)) == 1:
                status = words[0]
        c2 = re.sub(r"[*`]", "", l).strip().lstrip("-#> ").strip()   # keep _ in summaries
        m = SUMMARY_RE.match(c2)
        if m:
            summary = m.group(1).strip()
    return status, summary


class SessionResult:
    def __init__(self):
        self.status = None          # CONTINUE / DONE / BLOCKED (as reported)
        self.summary = None
        self.final_text = ""
        self.killed = None          # reason string if auto.py killed it
        self.returncode = None
        self.peak = 0
        self.context = 0
        self.boot = 0               # context at the first model call (start-up cost)
        self.denials = []
        self.limit = None           # {"resets_at": epoch|None} if a usage limit hit
        self.context_window = None
        self.error = None
        self.notices = 0
        self.stop_requested = None


class Session:
    """One `claude -p` run. A reader thread consumes the stream-json output
    (so the pipe never fills up and blocks claude), while the main thread
    watches the clock, the hard limit and the stop flags."""

    def __init__(self, cfg, number, kickoff, settings_path, review=False):
        self.cfg = cfg
        self.n = number
        self.kickoff = kickoff
        self.settings_path = settings_path
        self.review = review
        self.r = SessionResult()
        self.lock = threading.Lock()
        self.proc = None
        self.last_texts = {}
        self.last_msg_id = None
        self._seen_denials = set()
        tag = "review" if review else "session-%03d" % number
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        RUNS.mkdir(parents=True, exist_ok=True)
        self.raw_path = RUNS / ("%s-%s.jsonl" % (stamp, tag))
        self.err_path = RUNS / ("%s-%s.stderr.txt" % (stamp, tag))

    # -- command line --------------------------------------------------------
    def command(self):
        b = self.cfg.claude_bin
        base = [sys.executable, b] if b.lower().endswith(".py") else [b]
        cmd = base + ["-p", "--output-format", "stream-json", "--verbose",
                      "--settings", str(self.settings_path)]
        cmd += ["--permission-mode", "default" if self.review else "acceptEdits"]
        # auto-v2 lean session: fewer tools, no skills, no connectors.
        cmd += ["--tools", REVIEW_TOOLS if self.review else SESSION_TOOLS,
                "--disable-slash-commands", "--strict-mcp-config"]
        return cmd

    def env(self):
        e = dict(os.environ)
        e.pop("CLAUDECODE", None)          # we are not a nested interactive session
        e["AUTO_STATE_FILE"] = str(STATE)  # tells the hook where to look
        e["DISABLE_AUTO_COMPACT"] = "1"    # mid-session compaction = "getting dumb"
        e["PYTHONIOENCODING"] = "utf-8"
        e.update(LEAN_ENV)                 # auto-v2: no CLAUDE.md, no memory index
        return e

    # -- stream parsing ------------------------------------------------------
    def _handle(self, ev):
        t = ev.get("type")
        if t == "assistant" and ev.get("parent_tool_use_id") is None:
            msg = ev.get("message") or {}
            u = msg.get("usage") or {}
            ctx = sum(int(u.get(k) or 0) for k in (
                "input_tokens", "cache_read_input_tokens",
                "cache_creation_input_tokens", "output_tokens"))
            if ctx:
                with self.lock:
                    if not self.r.boot:
                        self.r.boot = ctx
                    self.r.context = ctx
                    self.r.peak = max(self.r.peak, ctx)
                self.cfg.update_state(context=ctx, peak=self.r.peak)
            mid = msg.get("id")
            texts = [b.get("text", "") for b in msg.get("content") or []
                     if isinstance(b, dict) and b.get("type") == "text"]
            if texts:
                if mid != self.last_msg_id:
                    self.last_texts = {}
                self.last_msg_id = mid
                self.last_texts[len(self.last_texts)] = "\n".join(texts)
            # Only error events count (the model merely *mentioning* the
            # phrase must not stop the run).
            is_err = ev.get("error") or ev.get("is_api_error_message") or msg.get("error")
            if is_err and "usage_limit_reached" in json.dumps(ev):
                self.r.limit = {"resets_at": _find_resets_at(ev)}
        elif t == "rate_limit_event":
            info = ev.get("rate_limit_info") or {}
            if info.get("status") == "rejected":
                self.rate_rejected = info.get("resetsAt")
        elif t == "system" and ev.get("subtype") == "permission_denied":
            # Live event: arrives even if the session is later killed. (Verified:
            # the CLI emits these for Bash denials, not for Edit/Write ones.)
            self._seen_denials.add(ev.get("tool_use_id"))
            self.r.denials.append(ev.get("message") or ("%s denied" % ev.get("tool_name")))
        elif t == "result":
            self.result_event = ev
            # The final list has every denial (Edit/Write included); skip the
            # ones already reported live, matched by tool_use_id.
            for d in ev.get("permission_denials") or []:
                if d.get("tool_use_id") and d.get("tool_use_id") in self._seen_denials:
                    continue
                s = "%s %s" % (d.get("tool_name"), json.dumps(d.get("tool_input"), ensure_ascii=False)[:160])
                self.r.denials.append(s)
            for mu in (ev.get("modelUsage") or {}).values():
                if isinstance(mu, dict) and mu.get("contextWindow"):
                    self.r.context_window = mu["contextWindow"]

    def _reader(self):
        with open(self.raw_path, "wb") as raw:
            for line in self.proc.stdout:
                raw.write(line)
                raw.flush()
                try:
                    ev = json.loads(line.decode("utf-8", "replace"))
                except ValueError:
                    continue
                try:
                    self._handle(ev)
                except Exception as e:   # a parsing surprise must not kill the run
                    self.r.error = "stream parse: %s" % e

    # -- run -----------------------------------------------------------------
    def run(self):
        try:
            return self._run()
        finally:
            if self.proc is not None and self.proc.poll() is None:
                kill_tree(self.proc.pid)   # an exception must not orphan claude

    def _run(self):
        cfg = self.cfg
        self.result_event = None
        self.rate_rejected = None
        kwargs = {}
        if WIN:
            # Own process group: Ctrl+C in the auto.py window reaches auto.py
            # only (Windows disables Ctrl+C for a new process group).
            kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
        else:
            kwargs["start_new_session"] = True
        errf = open(self.err_path, "wb")   # a file, so a full stderr pipe can't freeze us
        try:
            self.proc = subprocess.Popen(
                self.command(), cwd=ROOT, env=self.env(), stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=errf, **kwargs)
        except OSError as e:
            errf.close()
            self.r.error = "could not start claude: %s" % e
            self.r.killed = "failed to start"
            return self.r
        cfg.update_state(child_pid=self.proc.pid, child_ctime=proc_ctime(self.proc.pid),
                         session_running=True)
        # Kickoff through stdin: Windows .cmd shims mangle long multi-line argv.
        try:
            self.proc.stdin.write(self.kickoff.encode("utf-8"))
            self.proc.stdin.close()
        except OSError:
            pass
        th = threading.Thread(target=self._reader, daemon=True)
        th.start()

        start = time.monotonic()
        stop_seen = None
        last_progress = start
        while self.proc.poll() is None:
            now = time.monotonic()
            reason = None
            if STOP_NOW_FLAG.exists():
                reason = "stopped with --now"
            elif STOP_FLAG.exists() and not self.review:
                if stop_seen is None:
                    stop_seen = now
                    self.r.stop_requested = (read_json(STOP_FLAG, {}) or {}).get("by", "stop")
                    say("  stop requested: the session has been told to wrap up "
                        "(kill in %s if it hasn't ended)" % fmt_dur(cfg.stop_grace))
                elif now - stop_seen > cfg.stop_grace:
                    reason = "did not wrap up within %s of the stop request" % fmt_dur(cfg.stop_grace)
            if reason is None and now - start > cfg.session_timeout:
                reason = "session timeout (%s)" % fmt_dur(cfg.session_timeout)
            if reason is None and not self.review and cfg.deadline_passed() and not STOP_FLAG.exists():
                # Out of wall-clock time: ask for a clean wrap-up, like `stop`.
                write_json(STOP_FLAG, {"by": "hours", "at": now_iso(),
                                       "message": "The run's time limit (--hours) was reached."})
            with self.lock:
                ctx = self.r.context
            if reason is None and ctx > cfg.hard_limit:
                reason = "HARD limit (%s > %s tokens)" % (format(ctx, ","), format(cfg.hard_limit, ","))
            if reason:
                self.r.killed = reason
                kill_tree(self.proc.pid)
                break
            if now - last_progress >= 60:
                last_progress = now
                say("  ... %s elapsed, context %s" % (fmt_dur(now - start), format(ctx, ",")))
            time.sleep(POLL)
        try:
            self.proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            kill_tree(self.proc.pid)
            self.proc.wait(timeout=30)
        th.join(timeout=30)
        errf.close()
        self.r.returncode = self.proc.returncode
        cfg.update_state(child_pid=None, session_running=False)
        if self.r.killed is None and STOP_NOW_FLAG.exists():
            # Killed from outside (`stop --now` or Ctrl+C twice) between ticks.
            self.r.killed = "stopped with --now"

        ev = self.result_event or {}
        final = ev.get("result") if isinstance(ev.get("result"), str) else None
        if final is None:
            final = "\n".join(self.last_texts[k] for k in sorted(self.last_texts))
        self.r.final_text = final or ""
        self.r.status, self.r.summary = parse_status(self.r.final_text)
        # Usage limit: structured signals first (stream-json carries them in
        # this CLI version), then the message text as a fallback.
        if self.r.status is None:
            if self.r.limit is None and self.rate_rejected:
                self.r.limit = {"resets_at": self.rate_rejected}
            if self.r.limit is None and LIMIT_TEXT_RE.search(self.r.final_text or ""):
                m = re.search(r"\|(\d{10})\b", self.r.final_text)
                self.r.limit = {"resets_at": int(m.group(1)) if m else None}
        else:
            self.r.limit = None   # finished properly; a later limit is irrelevant now
        hs = read_json(HOOK_STATE, {}) or {}
        if hs.get("session") == self.n:
            self.r.notices = hs.get("notices", 0)
        return self.r


def _find_resets_at(obj):
    """Search an event for rate_limit_info.resetsAt (epoch seconds)."""
    if isinstance(obj, dict):
        info = obj.get("rate_limit_info")
        if isinstance(info, dict) and info.get("resetsAt"):
            return int(info["resetsAt"])
        for v in obj.values():
            r = _find_resets_at(v)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _find_resets_at(v)
            if r:
                return r
    return None


# =============================================================================
# The run: loop, brakes, commits
# =============================================================================
class Run:
    def __init__(self, args):
        self.args = args
        self.subject = args.subject.strip("/\\").replace("\\", "/")
        self.subject_dir = SUBJECTS / self.subject
        self.subject_rel = rel(self.subject_dir) if self.subject_dir.exists() else "subjects/" + self.subject
        self.handoff = self.subject_dir / HANDOFF_NAME
        self.progress = self.subject_dir / PROGRESS_NAME
        self.claude_bin = args.claude_bin or shutil.which("claude") or "claude"
        self.soft_limit = args.soft_limit
        self.hard_limit = args.hard_limit
        self.session_timeout = args.session_timeout * 60
        self.stop_grace = args.stop_grace * 60
        self.crash_wait = args.crash_wait
        self.started = time.monotonic()
        self.started_iso = now_iso()
        self.deadline = self.started + args.hours * 3600
        self.run_id = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.scratch = SCRATCH_ROOT / self.subject
        self.state = {}
        self.history = []          # per-session records of this run
        self.commits = []          # (hash, message) made by this run
        self.outside_changes = set()
        self.ctrl_c = 0
        self.stop_reason = None

    # -- state file shared with the hook and `status` -------------------------
    def update_state(self, **kw):
        self.state.update(kw)
        self.state["updated"] = now_iso()
        write_json(STATE, self.state)

    def deadline_passed(self):
        return time.monotonic() >= self.deadline

    # -- setup ------------------------------------------------------------------
    def preflight(self):
        if not (ROOT / ".git").exists():
            sys.exit("auto.py: %s is not a git repository." % ROOT)
        if not self.subject_dir.is_dir():
            sys.exit("auto.py: no subject folder %s" % self.subject_rel)
        if not self.handoff.is_file():
            sys.exit("auto.py: %s has no %s, so it has no hand-off system. auto.py only "
                     "runs subjects that do (today: %s)." % (
                         self.subject_rel, HANDOFF_NAME,
                         ", ".join(sorted(rel(p.parent) for p in SUBJECTS.rglob(HANDOFF_NAME))) or "none"))
        if not HOOK.is_file():
            sys.exit("auto.py: hook script missing: %s" % HOOK)
        if not CONTRACT.is_file():
            sys.exit("auto-v2.py: %s is missing; sessions would run with no rules." % CONTRACT)
        if not (self.args.claude_bin or shutil.which("claude")):
            sys.exit("auto.py: `claude` not found on PATH; pass --claude-bin.")
        if self.hard_limit <= self.soft_limit:
            sys.exit("auto.py: --hard-limit must be higher than --soft-limit.")
        if not self.args.no_commit:
            for k in ("user.name", "user.email"):
                if not git("config", k).stdout.strip():
                    sys.exit("auto.py: git %s is not set; commits would fail." % k)
            br = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
            if br == "HEAD":
                sys.exit("auto.py: detached HEAD; check out a branch first.")
            self.branch = br
        self.base_head = git("rev-parse", "HEAD").stdout.strip()

    def write_settings(self):
        """The per-run settings file: permissions + the PostToolUse hook.
        Absolute interpreter + script paths (forward slashes, quoted) so the
        hook runs the same under Git Bash or cmd, and despite the apostrophe."""
        allow, deny = permission_rules()
        self.scratch.mkdir(parents=True, exist_ok=True)
        hook_cmd = '"%s" "%s"' % (Path(sys.executable).as_posix(), HOOK.as_posix())
        write_json(RUN_SETTINGS, {
            "permissions": {"allow": allow, "deny": deny,
                            "additionalDirectories": [self.scratch.as_posix()]},
            "hooks": {"PostToolUse": [{"matcher": "*", "hooks": [
                {"type": "command", "command": hook_cmd, "timeout": 15}]}]},
        })
        write_json(REVIEW_SETTINGS, {"permissions": {
            "allow": ["Bash(%s *)" % c for c in REVIEW_BASH]
                     + ["Bash(git %s *)" % g for g in GIT_READ_ONLY]
                     + ["Bash(git %s)" % g for g in GIT_READ_ONLY],
            "deny": ["Edit", "Write", "NotebookEdit", "Bash(python *)", "Bash(py *)",
                     "Bash(python3 *)"] + deny,
        }})

    def protected_files(self):
        """Core config + our own machinery. Hashed before/after every session."""
        files = [ROOT / "CLAUDE.md", ROOT / "CLAUDE.local.md", ROOT / ".mcp.json",
                 ROOT / "auto.py", ROOT / "auto-v2.py", CONTRACT, HOOK, RUN_SETTINGS, REVIEW_SETTINGS,
                 AUTO / ".gitignore", USER_SETTINGS]
        claude_dir = ROOT / ".claude"
        if claude_dir.is_dir():
            for p in claude_dir.rglob("*"):
                if p.is_file() and AUTO not in p.parents and \
                        (claude_dir / "worktrees") not in p.parents:
                    files.append(p)   # settings*.json, hooks, commands, skills...
        seen, out = set(), []
        for f in files:
            if f not in seen:
                seen.add(f)
                out.append(f)
        return out

    def snapshot_protected(self):
        snap = {}
        for f in self.protected_files():
            try:
                data = f.read_bytes()
            except (FileNotFoundError, OSError):
                data = None
            snap[f] = (hashlib.sha256(data).hexdigest() if data is not None else None, data)
        return snap

    def scoped_secrets(self):
        return sorted(p for p in porcelain(self.subject_rel) if is_secret(p))

    # -- run start --------------------------------------------------------------
    def handle_dirty_tree(self):
        changes = {p: xy for p, xy in porcelain(self.subject_rel).items()
                   if not is_secret(p) and p.startswith(self.subject_rel + "/")}
        if not changes or self.args.no_commit:
            return
        say("Uncommitted changes in %s:" % self.subject_rel)
        for p, xy in sorted(changes.items()):
            say("   %s %s" % (xy, p))
        if not self.args.yes:
            try:
                ans = input("Commit them as 'pre-auto snapshot' [c] or abort [a]? ").strip().lower()
            except EOFError:     # nobody to ask (no terminal / closed stdin)
                ans = ""
            if not ans.startswith("c"):
                sys.exit("Aborted; nothing changed. (Use --yes to commit without asking.)")
        try:
            h = commit_paths(list(changes), "pre-auto snapshot")
        except CommitError as e:
            sys.exit("auto.py: the snapshot commit failed:\n%s" % e)
        self.snapshot_hash = h
        if h:
            say("Committed pre-auto snapshot %s" % h)
            self.commits.append((h, "pre-auto snapshot"))

    def acquire_lock(self):
        AUTO.mkdir(parents=True, exist_ok=True)
        me = {"pid": os.getpid(), "ctime": proc_ctime(os.getpid()),
              "subject": self.subject, "started": self.started_iso,
              "stop_grace_min": self.args.stop_grace}
        for _ in range(2):
            try:
                fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    json.dump(me, f)
                return
            except FileExistsError:
                old = read_json(LOCK, {}) or {}
                if old.get("pid") and pid_alive(old.get("pid"), old.get("ctime")):
                    sys.exit("auto.py: another run is active (pid %s, subject %s, since %s). "
                             "Use `python auto.py status` / `stop`." % (
                                 old.get("pid"), old.get("subject"), old.get("started")))
                say("Clearing a stale lock from a run that died (pid %s)." % old.get("pid"))
                st = read_json(STATE, {}) or {}
                if st.get("session_running"):
                    # It died mid-session: the next session must recover.
                    self.force_recovery = "the previous auto.py run died mid-session"
                    if st.get("child_pid") and st.get("child_ctime") and \
                            pid_alive(st["child_pid"], st["child_ctime"]):
                        kill_tree(st["child_pid"])   # don't leave an orphan claude
                try:
                    LOCK.unlink()
                except FileNotFoundError:
                    pass
        sys.exit("auto.py: could not take the lock %s" % LOCK)

    def release_lock(self):
        old = read_json(LOCK, {}) or {}
        if old.get("pid") == os.getpid():
            try:
                LOCK.unlink()
            except FileNotFoundError:
                pass

    def install_ctrl_c(self):
        """Ctrl+C once = graceful stop; twice = stop --now. Implemented by
        writing the same flag files `auto.py stop` writes, so there is one
        stop path to get right."""
        def handler(signum, frame):
            self.ctrl_c += 1
            if self.ctrl_c == 1:
                write_json(STOP_FLAG, {"by": "ctrl-c", "at": now_iso()})
                say("\nCtrl+C: stopping gracefully (session wraps up, no new session). "
                    "Press Ctrl+C again to kill it now.")
            else:
                write_json(STOP_NOW_FLAG, {"by": "ctrl-c x2", "at": now_iso()})
                say("\nCtrl+C again: killing the session now.")
                kill_tree(self.state.get("child_pid"))
        signal.signal(signal.SIGINT, handler)
        if hasattr(signal, "SIGBREAK"):
            signal.signal(signal.SIGBREAK, handler)   # Ctrl+Break on Windows

    # -- kickoff -------------------------------------------------------------------
    def kickoff(self, recovery=None, check_fail=None):
        parts = []
        parts.append(CONTRACT.read_text(encoding="utf-8").strip())
        parts.append("")
        if recovery:
            parts.append(RECOVERY_TEXT.format(where=recovery))
        parts.append(KICKOFF_TEMPLATE.format(subject=self.subject,
                                             subject_dir=self.subject_rel + "/"))
        parts.append("")
        parts.append(UNATTENDED_RULES.format(subject_dir=self.subject_rel + "/",
                                             scratch=self.scratch.as_posix()))
        parts.append(MILESTONE_RULE.format(until=self.args.until) if self.args.until else DONE_RULE)
        if check_fail:
            parts.append(CHECK_FAILED_TEXT.format(cmd=self.args.check, code=check_fail[0],
                                                  output=check_fail[1]))
        return "\n".join(parts) + "\n"

    def run_check(self):
        try:
            p = subprocess.run(self.args.check, shell=True, cwd=ROOT, capture_output=True,
                               encoding="utf-8", errors="replace", timeout=600)
            out = (p.stdout or "") + (p.stderr or "")
            return p.returncode, "\n".join(out.splitlines()[-50:])
        except subprocess.TimeoutExpired:
            return 124, "(check timed out after 10 min)"

    # -- waiting that respects stop flags and the deadline --------------------
    def wait(self, seconds, why):
        say("  waiting %s (%s)..." % (fmt_dur(seconds), why))
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            if STOP_NOW_FLAG.exists():
                return "stopped with --now"
            if STOP_FLAG.exists():
                return "stop requested during wait"
            if self.deadline_passed():
                return "time limit (--hours) reached"
            time.sleep(min(POLL, max(0.01, end - time.monotonic())))
        return None

    # -- the main loop --------------------------------------------------------------
    def main(self):
        self.force_recovery = None
        self.snapshot_hash = None
        self.preflight()
        self.acquire_lock()
        try:
            for f in (STOP_FLAG, STOP_NOW_FLAG):     # stale flags from an old run
                if f.exists():
                    f.unlink()
            self.write_settings()
            secrets = self.scoped_secrets()
            if secrets:
                say("WARNING: secret-looking files in %s will never be committed by "
                    "auto.py; add them to .gitignore:\n   %s" % (self.subject_rel, "\n   ".join(secrets)))
            self.handle_dirty_tree()
            last = _last_log(self.subject)
            recovery = None
            if self.force_recovery:
                # auto.py itself died mid-session: that session never committed;
                # its partial work is what the snapshot just committed (if any).
                recovery = self.recovery_where(self.snapshot_hash)
            elif last and last.get("outcome") == "CRASH":
                recovery = self.recovery_where(last.get("commit"))
            self.update_state(pid=os.getpid(), subject=self.subject, run_id=self.run_id,
                              run_started=self.started_iso, soft_limit=self.soft_limit,
                              hard_limit=self.hard_limit, notice_every=self.args.notice_every,
                              session=None, context=0, peak=0, child_pid=None,
                              session_running=False, limits=self.limits_text(),
                              last_status=None, last_summary=None)
            self.install_ctrl_c()
            with KeepAwake():
                self.loop(recovery)
                self.final_report()
                if self.review_allowed():
                    if STOP_FLAG.exists():   # a graceful stop must not cut the review short
                        STOP_FLAG.unlink()
                    self.review_and_push()
        finally:
            self.release_lock()   # held through the review, so no second run can start

    def review_allowed(self):
        r = self.stop_reason or ""
        if self.args.no_review:
            return False
        if r.startswith("stopped with --now") or STOP_NOW_FLAG.exists():
            return False
        if r.startswith("TAMPER") or r.startswith("new secret"):
            say("Skipping the review and push: fix the problem above first "
                "(a tampered config would also be loaded by the review session).")
            return False
        return True

    def limits_text(self):
        a = self.args
        return ("soft %s / hard %s tokens, %s sessions, %sh, %s min per session%s%s" % (
            format(a.soft_limit, ","), format(a.hard_limit, ","), a.sessions, a.hours,
            a.session_timeout, ", until: %s" % a.until if a.until else "",
            ", check: %s" % a.check if a.check else ""))

    def recovery_where(self, commit):
        if self.args.no_commit:
            return ("Its partial work is uncommitted in the working tree "
                    "(see git status / git diff -- %s)." % self.subject_rel)
        if commit:
            return "Its partial work is in commit %s (git show %s)." % (commit, commit)
        return "It left no changes to commit (git log -1 shows the last state)."

    def loop(self, recovery):
        a = self.args
        n = (_last_log(self.subject) or {}).get("session", 0)
        crashes = stuck = 0
        check_fail = None
        say("auto.py: subject %s · %s" % (self.subject, self.limits_text()))
        for i in range(a.sessions):
            if STOP_FLAG.exists() or STOP_NOW_FLAG.exists():
                self.stop_reason = "stop requested"
                return
            if self.deadline_passed():
                self.stop_reason = "time limit (--hours %s) reached" % a.hours
                return
            n += 1
            kick = self.kickoff(recovery, check_fail)
            kind = "recovery" if recovery else ("check-failed" if check_fail else "normal")
            say("\n=== session %d (%s) · %s ===" % (n, kind, dt.datetime.now().strftime("%H:%M:%S")))
            recovery = check_fail = None

            # Before: everything we compare after.
            prot_before = self.snapshot_protected()
            handoff_before = sha(self.handoff)
            fp_before = fingerprint(self.subject_rel)
            out_before = fingerprint()
            secrets_before = set(self.scoped_secrets())
            write_json(HOOK_STATE, {"session": n, "calls": 0, "last_notice_call": None,
                                    "kinds": [], "notices": 0})
            self.update_state(session=n, context=0, peak=0, session_started=now_iso())
            t0 = time.monotonic()
            started = now_iso()

            res = Session(self, n, kick, RUN_SETTINGS).run()

            # After: classify.
            fp_after = fingerprint(self.subject_rel)
            changed = changed_between(fp_before, fp_after)
            handoff_files = {rel(self.handoff), rel(self.progress)}
            work_changed = [p for p in changed if p not in handoff_files]
            handoff_updated = sha(self.handoff) != handoff_before
            out_after = fingerprint()
            outside = [p for p in changed_between(out_before, out_after)
                       if not p.startswith(self.subject_rel + "/")]
            self.outside_changes.update(outside)

            crash = None
            if res.killed:
                crash = res.killed
            elif res.limit:
                crash = "usage limit reached"
            elif res.returncode not in (0, None):
                crash = "claude exited with code %s" % res.returncode
            elif res.status is None:
                crash = "no STATUS line"
            elif res.status == "CONTINUE" and not handoff_updated:
                crash = "CONTINUE without an updated hand-off"
            outcome = "CRASH" if crash else res.status

            # Tamper check (deny rules can't stop every shell trick).
            prot_after = self.snapshot_protected()
            # Union: catches deleted AND newly created files (e.g. a new
            # .claude/settings.local.json that would switch hooks off).
            tampered = [f for f in list(prot_before) + [f for f in prot_after if f not in prot_before]
                        if prot_before.get(f, (None, None))[0] != prot_after.get(f, (None, None))[0]]
            new_secrets = sorted(set(self.scoped_secrets()) - secrets_before)

            # Commit the session's subject-folder changes (never protected files,
            # which live outside it, and never secret-looking files).
            commit_hash = commit_error = None
            if crash:
                msg = "auto: %s session %d (CRASHED: %s)" % (self.subject, n, crash)
            else:
                summ = (res.summary or "").splitlines()[0][:300] if res.summary else "(no summary)"
                msg = "auto: %s session %d (%s): %s" % (self.subject, n, res.status, summ)
            branch_now = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
            if not a.no_commit and branch_now != self.branch:
                commit_error = ("branch changed from %s to %s during the session; nothing "
                                "committed (switch back, then check git status)" % (self.branch, branch_now))
            elif not a.no_commit:
                to_commit = [p for p in porcelain(self.subject_rel)
                             if p.startswith(self.subject_rel + "/")]
                try:
                    commit_hash = commit_paths(to_commit, msg)
                    if commit_hash:
                        self.commits.append((commit_hash, msg))
                except CommitError as e:
                    commit_error = str(e)

            rec = {"session": n, "run_id": self.run_id, "subject": self.subject,
                   "kickoff": kind, "start": started, "end": now_iso(),
                   "duration_s": int(time.monotonic() - t0), "peak_context": res.peak, "boot_context": res.boot,
                   "context_window": res.context_window, "status": res.status,
                   "outcome": outcome, "summary": res.summary, "crash_reason": crash,
                   "stop_reason": None, "permission_denials": res.denials,
                   "notices": res.notices, "commit": commit_hash,
                   "files_changed": changed, "outside_changes": outside,
                   "returncode": res.returncode, "resets_at": (res.limit or {}).get("resets_at")}
            self.history.append(rec)
            self.update_state(last_status=outcome, last_summary=res.summary or crash,
                              context=0)

            # One-line summary + denials, so you can widen the allowlist.
            say("[session %d] %s · boot %s · peak %s tok · %s · %s · %s" % (
                n, outcome if not crash else "CRASH (%s)" % crash, format(res.boot, ","),
                format(res.peak, ","),
                fmt_dur(rec["duration_s"]), "commit %s" % commit_hash if commit_hash
                else ("no commit (--no-commit)" if a.no_commit else "nothing to commit"),
                res.summary or ""))
            if res.boot > BOOT_WARN:
                say("  WARNING: start-up cost %s tok is over %s: a lean-session cut may have stopped "
                    "working (Claude Code update?). Check the first lines of %s." % (
                        format(res.boot, ","), format(BOOT_WARN, ","), rel(RUNS)))
            if res.notices:
                say("  wrap-up notices delivered by the hook: %d" % res.notices)
            for d in dict.fromkeys(res.denials):
                say("  DENIED: %s" % d)
            if outside:
                say("  changed outside %s (not committed by auto.py): %s" % (self.subject_rel, ", ".join(outside[:10])))

            def finish(reason):
                rec["stop_reason"] = reason
                _append_log(rec)
                self.stop_reason = reason

            # ---- brakes, most serious first ----
            if tampered:
                self.report_tamper(n, tampered, prot_before)
                return finish("TAMPER: protected file(s) changed: %s" % ", ".join(
                    _display(f) for f in tampered))
            if new_secrets:
                return finish("new secret-looking file(s) appeared (not committed): %s" % ", ".join(new_secrets))
            if commit_error:
                say("COMMIT FAILED:\n%s" % commit_error)
                return finish("commit failed: %s" % commit_error.splitlines()[-1][:200])
            if res.killed == "stopped with --now":
                return finish("stopped with --now")
            if res.limit:
                ra = res.limit.get("resets_at")
                when = dt.datetime.fromtimestamp(ra).astimezone().isoformat(timespec="minutes") if ra else None
                if not a.wait_on_limit:
                    return finish("usage limit reached%s" % (" (resets %s)" % when if when else ""))
                if not ra:
                    return finish("usage limit reached and the reset time could not be read")
                secs = max(0, ra - time.time()) + 60
                if time.monotonic() + secs > self.deadline:
                    return finish("usage limit resets %s, after the --hours deadline" % when)
                w = self.wait(secs, "usage limit; resets %s" % when)
                if w:
                    return finish(w)
                _append_log(rec)
                recovery = self.recovery_where(commit_hash)
                continue   # a usage limit is not counted as a crash

            check = None
            if a.check:
                check = self.run_check()
                say("  check `%s` -> exit %d" % (a.check, check[0]))
                if check[0] == 0:
                    return finish("destination reached (--check passed)")
            if outcome == "BLOCKED":
                return finish("BLOCKED: %s" % (res.summary or "(no question given)"))
            if outcome == "DONE":
                if not a.check:
                    return finish("DONE: %s" % (res.summary or "subject finished"))
                check_fail = check   # DONE but the check disagrees: keep going

            crashes = crashes + 1 if crash else 0
            stuck = stuck + 1 if not work_changed else 0
            if crashes >= 2:
                return finish("2 crashes in a row (last: %s)" % crash)
            if stuck >= 2:
                return finish("stuck: 2 sessions in a row changed nothing outside the hand-off files")
            if res.stop_requested or STOP_FLAG.exists() or STOP_NOW_FLAG.exists():
                by = res.stop_requested or (read_json(STOP_FLAG, {}) or {}).get("by", "stop")
                return finish("time limit (--hours %s) reached" % a.hours if by == "hours"
                              else "stop requested (%s)" % by)
            if crash:
                recovery = self.recovery_where(commit_hash)
                if i + 1 < a.sessions:
                    w = self.wait(self.crash_wait, "after a crash")
                    if w:
                        return finish(w)
                _append_log(rec)
                continue
            _append_log(rec)
        self.stop_reason = "--sessions %d reached" % a.sessions

    # -- tamper report ---------------------------------------------------------
    def report_tamper(self, n, tampered, before):
        RUNS.mkdir(parents=True, exist_ok=True)
        diff_path = RUNS / ("%s-session-%03d-tamper.diff" % (self.run_id, n))
        backup_dir = RUNS / ("%s-session-%03d-tamper-backup" % (self.run_id, n))
        chunks, cmds = [], []
        for f in tampered:
            old = before.get(f, (None, None))[1]
            try:
                new = f.read_bytes()
            except FileNotFoundError:
                new = None
            name = _display(f)
            a_txt = (old or b"").decode("utf-8", "replace").splitlines(True)
            b_txt = (new or b"").decode("utf-8", "replace").splitlines(True)
            chunks += difflib.unified_diff(a_txt, b_txt, "before/" + name, "after/" + name)
            # How to restore. Prefer git when HEAD holds exactly the old content.
            inside = ROOT in f.parents
            if inside and old is not None and git("cat-file", "-e", "HEAD:" + rel(f)).returncode == 0 \
                    and hashlib.sha256(_head_bytes(rel(f))).hexdigest() == before.get(f, (None,))[0]:
                cmds.append('git restore --source=HEAD -- "%s"' % rel(f))
            elif old is None:
                cmds.append('(it did not exist before) delete: "%s"' % f)
            else:
                b = backup_dir / (rel(f) if inside else f.name)
                b.parent.mkdir(parents=True, exist_ok=True)
                b.write_bytes(old)
                if WIN:   # PowerShell (your shell); '' escapes the apostrophe in ece'
                    cmds.append("Copy-Item -LiteralPath '%s' -Destination '%s' -Force" % (
                        str(b).replace("'", "''"), str(f).replace("'", "''")))
                else:
                    import shlex
                    cmds.append("cp %s %s" % (shlex.quote(str(b)), shlex.quote(str(f))))
        diff_path.write_text("".join(chunks), encoding="utf-8")
        say("\n!!! TAMPER CHECK FAILED: protected files changed during session %d:" % n)
        for f in tampered:
            say("   %s" % _display(f))
        say("They were NOT committed and NOT restored (it might be your own edit).")
        say("Diff saved to %s:\n" % diff_path)
        say("".join(chunks)[:6000])
        say("To restore each file:")
        for c in cmds:
            say("   " + c)

    # -- the end ----------------------------------------------------------------
    def final_report(self):
        took = fmt_dur(time.monotonic() - self.started)
        say("\n" + "=" * 72)
        say("auto.py stopped: %s" % self.stop_reason)
        say("Sessions run: %d · time taken: %s" % (len(self.history), took))
        for r in self.history:
            say("  #%d %-8s %s" % (r["session"], r["outcome"],
                                   r["summary"] or r["crash_reason"] or ""))
        block = current_handoff(self.handoff)
        say("\nLatest hand-off (%s):\n%s" % (rel(self.handoff), block))
        say("Latest commit: %s" % git("log", "-1", "--format=%h %s").stdout.strip())
        if self.commits and not git("log", "-1", "--format=%H").stdout.strip().startswith(self.commits[-1][0]):
            say("Latest auto.py commit: %s %s" % self.commits[-1])
        if self.outside_changes:
            say("\nChanged outside %s during the run (not committed by auto.py):" % self.subject_rel)
            for p in sorted(self.outside_changes):
                say("   %s" % p)
        denials = [d for r in self.history for d in r["permission_denials"]]
        if denials:
            say("\nPermission denials this run (widen the allowlist at the top of auto.py if needed):")
            for d in dict.fromkeys(denials):
                say("   %s" % d)
        say("=" * 72)

    def review_and_push(self):
        """Your end-of-run wish: a summary + mistakes check of everything the
        run committed, then push only on your explicit yes."""
        mine = [(h, m) for h, m in self.commits if m != "pre-auto snapshot"]
        if self.args.review_from:   # earlier auto.py sessions that were never reviewed
            prefix = "auto: %s session " % self.subject
            log = git("log", "--reverse", "--format=%h\x1f%s",
                      "%s..HEAD" % self.args.review_from).stdout.splitlines()
            have = {h for h, _ in mine}
            earlier = [tuple(l.split("\x1f", 1)) for l in log if "\x1f" in l]
            earlier = [(h, m) for h, m in earlier if m.startswith(prefix) and h not in have
                       and not any(h2.startswith(h) or h.startswith(h2) for h2 in have)]
            mine = earlier + mine
        if not mine:
            say("No session commits this run: nothing to review or push.")
            return
        commits = "\n".join("- %s %s" % (h, m) for h, m in mine)
        prompt = REVIEW_PROMPT.format(subject=self.subject, subject_dir=self.subject_rel,
                                      commits=commits)
        say("\nRunning the end-of-run review (read-only session)...")
        self.update_state(session="review", context=0)
        fp_before = fingerprint()
        res = Session(self, 0, prompt, REVIEW_SETTINGS, review=True).run()
        touched = changed_between(fp_before, fingerprint())
        text = res.final_text.strip() or "(the review produced no text: %s)" % (res.killed or res.error)
        out = RUNS / ("%s-review.md" % self.run_id)
        out.write_text(text + "\n", encoding="utf-8")
        say("\n" + "-" * 72 + "\nREVIEW\n" + "-" * 72)
        say(text)
        say("-" * 72 + "\n(saved to %s)" % out)
        if touched:
            say("WARNING: files changed while the review ran (it should only read): %s\n"
                "Not offering to push; look at them first." % ", ".join(touched[:10]))
            return
        if self.args.no_commit:
            return
        signal.signal(signal.SIGINT, signal.default_int_handler)   # Ctrl+C at the prompt = no
        ahead = git("rev-list", "--count", "@{u}..HEAD")
        if ahead.returncode != 0:
            say("No upstream branch; push manually when ready.")
            return
        say("Local branch is %s commit(s) ahead of its upstream (this includes any "
            "commits other windows made)." % ahead.stdout.strip())
        try:
            ans = input("Push now? [y/N] ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            ans = ""
        if ans in ("y", "yes"):
            p = git("push")
            say((p.stdout + p.stderr).strip() or "pushed.")
        else:
            say("Not pushed. When you're happy: git push")


def _head_bytes(path):
    p = subprocess.run(["git", "show", "HEAD:" + path], cwd=ROOT, capture_output=True)
    return p.stdout if p.returncode == 0 else b""


def _display(f: Path):
    try:
        return rel(f)
    except ValueError:
        return str(f)


def current_handoff(path: Path):
    """The 'Current hand-off' section of sprints.md (falls back to the tail)."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "(could not read %s)" % path
    m = re.search(r"^##\s*Current hand-off\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return (m.group(1).strip() if m else "\n".join(text.splitlines()[-25:])) + "\n"


def _last_log(subject=None):
    """Last logged session (of this subject, if given)."""
    try:
        lines = LOG.read_text(encoding="utf-8").strip().splitlines()
    except OSError:
        return None
    for line in reversed(lines):
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if subject is None or rec.get("subject") == subject:
            return rec
    return None


def _append_log(rec):
    AUTO.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


# =============================================================================
# stop / status
# =============================================================================
def cmd_stop(args):
    lock = read_json(LOCK, {}) or {}
    alive = lock.get("pid") and pid_alive(lock["pid"], lock.get("ctime"))
    if not alive:
        say("No auto.py run is active.")
        return 1
    if args.now:
        write_json(STOP_NOW_FLAG, {"by": "stop --now", "at": now_iso()})
        st = read_json(STATE, {}) or {}
        if st.get("child_pid") and pid_alive(st["child_pid"], st.get("child_ctime")):
            kill_tree(st["child_pid"])     # don't wait for auto.py's next tick
        say("Killed the running session (if any). auto.py will commit its partial "
            "work and stop; the next run starts with a recovery kickoff.")
    else:
        write_json(STOP_FLAG, {"by": "stop command", "at": now_iso()})
        say("Stop requested. The session will be told to wrap up (clean hand-off, "
            "STATUS: CONTINUE) and no new session will start. It is killed if it "
            "hasn't ended %s minutes after this request." % (lock.get("stop_grace_min") or 10))
    return 0


def cmd_status(args):
    lock = read_json(LOCK, {}) or {}
    st = read_json(STATE, {}) or {}
    alive = bool(lock.get("pid") and pid_alive(lock["pid"], lock.get("ctime")))
    last = _last_log()
    say("Run active: %s" % ("yes (pid %s)" % lock["pid"] if alive else "no"))
    if st:
        say("Subject: %s" % st.get("subject"))
        say("Session: %s%s" % (st.get("session"), " (running)" if alive and st.get("session_running") else ""))
        say("Context now: %s tokens (peak %s; soft %s, hard %s)" % (
            format(st.get("context") or 0, ","), format(st.get("peak") or 0, ","),
            format(st.get("soft_limit") or 0, ","), format(st.get("hard_limit") or 0, ",")))
        if st.get("run_started"):
            try:
                el = dt.datetime.now().astimezone() - dt.datetime.fromisoformat(st["run_started"])
                say("Elapsed: %s (run started %s)" % (fmt_dur(el.total_seconds()), st["run_started"]))
            except ValueError:
                pass
        say("Active limits: %s" % st.get("limits"))
        say("Last STATUS: %s" % st.get("last_status"))
        say("Last SUMMARY: %s" % st.get("last_summary"))
    elif last:
        say("Last logged session: #%s %s %s" % (last.get("session"), last.get("outcome"), last.get("summary")))
    else:
        say("No runs yet.")
    if STOP_FLAG.exists() and alive:
        say("A graceful stop is pending.")
    return 0


# =============================================================================
# CLI
# =============================================================================
def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")   # UTF-8 everywhere
        except Exception:
            pass
    ap = argparse.ArgumentParser(prog="auto-v2.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run sessions for a subject (resumes from its hand-off)")
    r.add_argument("subject", help="folder under subjects/, e.g. pedagogy")
    r.add_argument("--until", help='milestone, e.g. "S10 done" or "stage-2 (S13) done"')
    r.add_argument("--check", help="shell command; exit 0 = destination reached")
    r.add_argument("--sessions", type=int, default=5, help="max sessions this run (5)")
    r.add_argument("--hours", type=float, default=6.0, help="wall-clock cap incl. waits (6)")
    r.add_argument("--session-timeout", type=float, default=60.0, help="minutes per session (60)")
    r.add_argument("--soft-limit", type=int, default=DEFAULT_SOFT, help="tokens: wrap-up notice (150000)")
    r.add_argument("--hard-limit", type=int, default=DEFAULT_HARD, help="tokens: kill = crash (210000)")
    r.add_argument("--wait-on-limit", action="store_true", help="sleep through a usage limit and continue")
    r.add_argument("--yes", action="store_true", help="commit a dirty subject folder without asking")
    r.add_argument("--no-commit", action="store_true", help="never commit (testing)")
    r.add_argument("--no-review", action="store_true", help="skip the end-of-run review session")
    r.add_argument("--review-from", metavar="COMMIT",
                   help="also review this subject's auto.py commits after COMMIT (e.g. a run whose review was cut off)")
    r.add_argument("--claude-bin", help="path to claude (default: the one on PATH)")
    # Timers, mainly so tests can run in seconds:
    r.add_argument("--crash-wait", type=float, default=120.0, help="seconds to wait after a crash (120)")
    r.add_argument("--stop-grace", type=float, default=10.0, help="minutes a stopped session gets to wrap up (10)")
    r.add_argument("--notice-every", type=int, default=10, help="tool calls between repeat notices (10)")
    s = sub.add_parser("stop", help="graceful stop (or --now to kill)")
    s.add_argument("--now", action="store_true")
    sub.add_parser("status", help="show the current/last run")
    args = ap.parse_args(argv)

    if args.cmd == "stop":
        return cmd_stop(args)
    if args.cmd == "status":
        return cmd_status(args)
    run = Run(args)
    run.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
