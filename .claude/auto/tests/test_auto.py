#!/usr/bin/env python3
"""Offline tests for auto.py: 0 tokens, a fake `claude`, throwaway git projects.

Run:  python .claude/auto/tests/test_auto.py        (add -v for names)
Every test builds its own small git project in the system temp folder (with an
apostrophe in its path, like the real one), copies auto.py + hook.py into it,
runs auto.py with tiny timers, then deletes the project.
"""
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC_ROOT = HERE.parents[2]                 # the folder that holds auto.py
PY = sys.executable
WIN = os.name == "nt"
ENC = dict(encoding="utf-8", errors="replace")

CONT = "Did a sprint.\nSUMMARY: S1 done → hand-off written ✓\nSTATUS: CONTINUE"
DONE = "All finished.\n**SUMMARY:** subject finished\n**STATUS:** `DONE`"
BLOCKED = "SUMMARY: Which taxonomy should be the spine?\nSTATUS: BLOCKED"
WORK = {"edit": "subjects/demo/work.md", "text": "more work\n"}
HAND = {"handoff": True}


def rmtree(path):
    """shutil.rmtree that also removes git's read-only object files on Windows."""
    import stat
    def onerr(func, p, exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(path, onerror=onerr)


def S(final, *steps, rc=0):
    return {"steps": list(steps), "final": final, "rc": rc}


class Proj:
    def __init__(self, name):
        self.base = Path(tempfile.mkdtemp(prefix="auto-test-%s-" % name))
        self.dir = self.base / "ece'"
        d = self.dir
        (d / "subjects" / "demo").mkdir(parents=True)
        (d / "subjects" / "other").mkdir(parents=True)
        (d / ".claude").mkdir()
        (d / "CLAUDE.md").write_text("# contract\n", encoding="utf-8")
        (d / ".claude" / "settings.json").write_text('{"permissions": {}}\n', encoding="utf-8")
        (d / "subjects" / "demo" / "sprints.md").write_text(
            "# Sprints\n\n## Current hand-off\n\nSprint: S0 done\n", encoding="utf-8")
        (d / "subjects" / "demo" / "progress-log.md").write_text("# log\n", encoding="utf-8")
        (d / "subjects" / "demo" / "work.md").write_text("work\n", encoding="utf-8")
        (d / "subjects" / "other" / "x.md").write_text("x\n", encoding="utf-8")
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "core.autocrlf", "false")
        self.git("add", "-A")
        self.git("commit", "-qm", "init")
        shutil.copy(SRC_ROOT / "auto.py", d / "auto.py")
        (d / ".claude" / "auto").mkdir()
        for f in ("hook.py", ".gitignore"):
            shutil.copy(SRC_ROOT / ".claude" / "auto" / f, d / ".claude" / "auto" / f)
        shutil.copy(HERE / "fake_claude.py", self.base / "fake_claude.py")
        if WIN:   # a .cmd shim, like an npm-installed claude
            self.fake = self.base / "fake_claude.cmd"
            self.fake.write_text('@"%s" "%%~dp0fake_claude.py" %%*\r\n' % PY, encoding="utf-8")
        else:
            self.fake = self.base / "fake_claude.py"
        self.scn = self.base / "scenario.json"

    def git(self, *a):
        return subprocess.run(["git", *a], cwd=self.dir, capture_output=True, **ENC)

    def scenario(self, sessions, **kw):
        self.scn.write_text(json.dumps(dict(sessions=sessions, **kw)), encoding="utf-8")

    def env(self):
        e = dict(os.environ, FAKE_SCENARIO=str(self.scn), AUTO_POLL="0.05", PYTHONIOENCODING="utf-8")
        e.pop("CLAUDECODE", None)
        return e

    def argv(self, *extra, defaults=True):
        a = [PY, str(self.dir / "auto.py"), "run", "demo", "--claude-bin", str(self.fake)]
        if defaults:
            a += ["--crash-wait", "0.2", "--stop-grace", "0.05", "--session-timeout", "0.5",
                  "--no-review"]
        return a + list(extra)

    def run(self, *extra, input="", timeout=120, defaults=True):
        # cwd = somewhere else on purpose: auto.py must work from any folder.
        return subprocess.run(self.argv(*extra, defaults=defaults), input=input,
                              capture_output=True, env=self.env(), cwd=self.base,
                              timeout=timeout, **ENC)

    def popen(self, *extra, **kw):
        return subprocess.Popen(self.argv(*extra), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, env=self.env(), cwd=self.base, **ENC, **kw)

    def cmd(self, *a):
        return subprocess.run([PY, str(self.dir / "auto.py"), *a], capture_output=True,
                              env=self.env(), cwd=self.base, **ENC)

    def log(self):
        p = self.dir / ".claude" / "auto" / "log.jsonl"
        return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []

    def commits(self):
        return self.git("log", "--format=%s").stdout.splitlines()

    def commit_files(self, n_last):
        out = self.git("log", "-%d" % n_last, "--name-only", "--format=").stdout
        return [l for l in out.splitlines() if l.strip()]

    def kickoffs(self):
        p = Path(str(self.scn) + ".kickoffs.jsonl")
        return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []

    def state(self):
        p = self.dir / ".claude" / "auto" / "state.json"
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def wait_running(self, timeout=30):
        end = time.time() + timeout
        while time.time() < end:
            if self.state().get("session_running"):
                return True
            time.sleep(0.05)
        raise AssertionError("session never started")

    def cleanup(self):
        rmtree(self.base)


class Base(unittest.TestCase):
    def setUp(self):
        self.p = Proj(self._testMethodName[5:30])

    def tearDown(self):
        if not os.environ.get("KEEP"):
            self.p.cleanup()

    def assertStopped(self, out, text):
        self.assertIn("auto.py stopped: ", out)
        line = [l for l in out.splitlines() if l.startswith("auto.py stopped: ")][-1]
        self.assertIn(text, line, out[-3000:])


# ---------------------------------------------------------------- outcomes --
class Outcomes(Base):
    def test_continue_then_done(self):
        self.p.scenario([S(CONT, WORK, HAND), S(DONE, WORK, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "DONE")
        c = self.p.commits()
        self.assertEqual(c[0], "auto: demo session 2 (DONE): subject finished")
        self.assertEqual(c[1], "auto: demo session 1 (CONTINUE): S1 done → hand-off written ✓")
        k = self.p.kickoffs()
        self.assertEqual(len(k), 2)
        first = k[0]
        self.assertTrue(first["kickoff"].startswith("demo, work on automated sprints without getting dumb from too much context"))
        self.assertIn("You are running unattended", first["kickoff"])
        self.assertIn("STATUS: CONTINUE | DONE | BLOCKED", first["kickoff"])
        self.assertNotIn("cut off", first["kickoff"])
        self.assertNotIn(first["kickoff"].strip()[:30], " ".join(first["argv"]))  # stdin, not argv
        for flag in ("-p", "stream-json", "--verbose", "--settings", "acceptEdits"):
            self.assertIn(flag, first["argv"])
        self.assertEqual(first["DISABLE_AUTO_COMPACT"], "1")
        self.assertTrue(first["AUTO_STATE_FILE"].endswith("state.json"))
        # Only the subject folder is ever committed; runtime files never.
        for f in self.p.commit_files(2):
            self.assertTrue(f.startswith("subjects/demo/"), f)
        ign = self.p.git("status", "--porcelain", "--ignored").stdout
        for f in ("state.json", "log.jsonl", "runs/", "run-settings.json"):
            self.assertIn(f, ign)
        self.assertNotIn("state.json", self.p.git("ls-files").stdout)
        log = self.p.log()
        self.assertEqual([r["outcome"] for r in log], ["CONTINUE", "DONE"])
        for key in ("session", "start", "end", "peak_context", "status", "summary",
                    "crash_reason", "stop_reason", "permission_denials", "commit"):
            self.assertIn(key, log[0])
        self.assertIn("Latest hand-off", r.stdout)
        self.assertIn("Latest commit", r.stdout)

    def test_blocked(self):
        self.p.scenario([S(BLOCKED, WORK, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "BLOCKED: Which taxonomy should be the spine?")
        self.assertEqual(self.p.commits()[0], "auto: demo session 1 (BLOCKED): Which taxonomy should be the spine?")

    def test_done_check_fails_then_passes(self):
        chk = '%s -c "import os,sys; print(\'checking marker\'); sys.exit(0 if os.path.exists(\'subjects/demo/marker\') else 3)"' % PY
        self.p.scenario([S(DONE, WORK, HAND),
                         S(CONT, WORK, HAND, {"edit": "subjects/demo/marker", "text": "ok"})])
        r = self.p.run("--check", chk)
        self.assertStopped(r.stdout, "destination reached")
        k = self.p.kickoffs()
        self.assertEqual(len(k), 2)
        self.assertIn("still fails (exit 3)", k[1]["kickoff"])
        self.assertIn("checking marker", k[1]["kickoff"])

    def test_check_passes_stops(self):
        self.p.scenario([S(CONT, WORK, HAND)])
        r = self.p.run("--check", '%s -c "pass"' % PY)
        self.assertStopped(r.stdout, "destination reached")
        self.assertEqual(len(self.p.kickoffs()), 1)

    def test_until_in_kickoff(self):
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run("--until", "S3 done")
        self.assertIn("Milestone for this run: S3 done", self.p.kickoffs()[0]["kickoff"])

    def test_sessions_cap(self):
        self.p.scenario([S(CONT, WORK, HAND)])
        r = self.p.run("--sessions", "2")
        self.assertStopped(r.stdout, "--sessions 2 reached")
        self.assertEqual(len(self.p.kickoffs()), 2)


# ------------------------------------------------------------------ crashes --
class Crashes(Base):
    def test_missing_status_then_recovery(self):
        self.p.scenario([S("I forgot the status lines", WORK, HAND), S(DONE, WORK, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "DONE")
        c = self.p.commits()
        self.assertEqual(c[1], "auto: demo session 1 (CRASHED: no STATUS line)")
        h = self.p.git("log", "-1", "--skip=1", "--format=%h").stdout.strip()
        k2 = self.p.kickoffs()[1]["kickoff"]
        self.assertTrue(k2.startswith("The previous session was cut off before finishing."))
        self.assertIn("git show %s" % h, k2)
        self.assertIn("demo, work on automated sprints", k2)

    def test_continue_without_handoff_is_crash(self):
        self.p.scenario([S(CONT, WORK), S(DONE, WORK, HAND)])
        r = self.p.run()
        self.assertIn("CRASHED: CONTINUE without an updated hand-off", self.p.commits()[1])
        self.assertStopped(r.stdout, "DONE")

    def test_hard_limit_kill_then_recovery(self):
        self.p.scenario([S(CONT, WORK, HAND, {"ctx": 5000}, {"ctx": 9000}, {"sleep": 30}),
                         S(DONE, WORK, HAND)])
        t = time.time()
        r = self.p.run("--soft-limit", "4000", "--hard-limit", "8000")
        self.assertLess(time.time() - t, 25)
        self.assertIn("CRASHED: HARD limit (9,000 > 8,000 tokens)", self.p.commits()[1])
        self.assertIn("cut off", self.p.kickoffs()[1]["kickoff"])
        self.assertEqual(self.p.log()[0]["peak_context"], 9000)

    def test_hang_timeout_kill(self):
        self.p.scenario([S(CONT, WORK, {"sleep": 60}), S(DONE, WORK, HAND)])
        t = time.time()
        r = self.p.run("--session-timeout", "0.03")
        self.assertLess(time.time() - t, 30)
        self.assertIn("CRASHED: session timeout", self.p.commits()[1])
        self.assertStopped(r.stdout, "DONE")

    def test_two_crashes_stop(self):
        self.p.scenario([S("no status", WORK)])
        r = self.p.run()
        self.assertStopped(r.stdout, "2 crashes in a row")
        self.assertEqual(len(self.p.kickoffs()), 2)

    def test_stuck(self):
        self.p.scenario([S(CONT, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "stuck")
        self.assertEqual(len(self.p.kickoffs()), 2)

    def test_crash_wait_is_real(self):
        self.p.scenario([S("no status", WORK), S(DONE, WORK, HAND)])
        t = time.time()
        self.p.run("--crash-wait", "2")
        self.assertGreater(time.time() - t, 2)


# --------------------------------------------------------------- protection --
class Protection(Base):
    def test_tamper_stop_with_diff(self):
        self.p.scenario([S(CONT, WORK, HAND, {"edit": "CLAUDE.md", "text": "evil line\n"}),
                         S(DONE, WORK, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "TAMPER")
        self.assertIn("+evil line", r.stdout)
        self.assertIn('git restore --source=HEAD -- "CLAUDE.md"', r.stdout)
        self.assertEqual(len(self.p.kickoffs()), 1)                   # no new session
        self.assertIn(" M CLAUDE.md", self.p.git("status", "--porcelain").stdout)  # left uncommitted
        self.assertIn("auto: demo session 1 (CONTINUE)", self.p.commits()[0])  # other work committed
        self.assertNotIn("CLAUDE.md", self.p.commit_files(1))
        diffs = list((self.p.dir / ".claude" / "auto" / "runs").glob("*tamper.diff"))
        self.assertTrue(diffs and "evil line" in diffs[0].read_text(encoding="utf-8"))

    def test_tamper_on_hook_script(self):
        self.p.scenario([S(CONT, WORK, HAND, {"edit": ".claude/auto/hook.py", "text": "\n# off\n"})])
        r = self.p.run()
        self.assertStopped(r.stdout, "TAMPER")
        self.assertIn(".claude/auto/hook.py", r.stdout)

    def test_old_secret_warned_never_committed(self):
        (self.p.dir / "subjects" / "demo" / ".env").write_text("KEY=1", encoding="utf-8")
        (self.p.dir / "subjects" / "demo" / "work.md").write_text("dirty\n", encoding="utf-8")
        self.p.scenario([S(DONE, WORK, HAND)])
        r = self.p.run("--yes")
        self.assertIn("WARNING: secret-looking files", r.stdout)
        self.assertEqual(self.p.commits()[1], "pre-auto snapshot")
        self.assertNotIn(".env", self.p.git("ls-files").stdout)

    def test_new_secret_stops(self):
        self.p.scenario([S(CONT, WORK, HAND, {"edit": "subjects/demo/credentials.json", "text": "{}"})])
        r = self.p.run()
        self.assertStopped(r.stdout, "new secret-looking file")
        self.assertNotIn("credentials", self.p.git("ls-files").stdout)
        self.assertIn("session 1", self.p.commits()[0])

    def test_failing_commit_stops(self):
        hook = self.p.dir / ".git" / "hooks" / "pre-commit"
        hook.write_text("#!/bin/sh\necho 'rejected by pre-commit: lint failed'\nexit 1\n", encoding="utf-8")
        self.p.scenario([S(CONT, WORK, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "commit failed")
        self.assertIn("rejected by pre-commit", r.stdout)

    def test_outside_changes_not_committed(self):
        self.p.scenario([S(DONE, WORK, HAND, {"edit": "subjects/other/x.md", "text": "parallel\n"})])
        r = self.p.run()
        self.assertIn("not committed by auto.py", r.stdout)
        self.assertNotIn("subjects/other/x.md", self.p.commit_files(1))
        self.assertIn("subjects/other/x.md", self.p.git("status", "--porcelain").stdout)

    def test_parallel_staged_file_untouched(self):
        (self.p.dir / "subjects" / "other" / "x.md").write_text("staged by other window\n", encoding="utf-8")
        self.p.git("add", "subjects/other/x.md")
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run()
        self.assertNotIn("subjects/other/x.md", self.p.commit_files(1))
        self.assertIn("M  subjects/other/x.md", self.p.git("status", "--porcelain").stdout)

    def test_denials_reported(self):
        self.p.scenario([S(DONE, WORK, HAND, {"deny": "Permission to use Edit on CLAUDE.md has been denied."})])
        r = self.p.run()
        self.assertIn("DENIED: Permission to use Edit on CLAUDE.md", r.stdout)
        self.assertEqual(self.p.log()[0]["permission_denials"],
                         ["Permission to use Edit on CLAUDE.md has been denied."])

    def test_settings_file_contents(self):
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run()
        s = json.loads((self.p.dir / ".claude" / "auto" / "run-settings.json").read_text(encoding="utf-8"))
        deny = s["permissions"]["deny"]
        for rule in ("Edit(./CLAUDE.md)", "Edit(./.claude/**)", "Edit(./auto.py)",
                     "Bash(git commit *)", "Bash(git push *)", "Bash(*auto.py*)", "Bash(claude *)"):
            self.assertIn(rule, deny)
        allow = s["permissions"]["allow"]
        self.assertIn("Bash(git status *)", allow)
        self.assertNotIn("Bash(git commit *)", allow)
        cmd = s["hooks"]["PostToolUse"][0]["hooks"][0]["command"]
        self.assertIn(Path(PY).as_posix(), cmd)
        self.assertIn("/.claude/auto/hook.py", cmd)


# ------------------------------------------------------------------- limits --
class UsageLimit(Base):
    def test_limit_stops(self):
        self.p.scenario([S(CONT, WORK, {"limit": int(time.time()) + 3600})])
        r = self.p.run()
        self.assertStopped(r.stdout, "usage limit reached (resets")
        self.assertIn("CRASHED: usage limit reached", self.p.commits()[0])

    def test_limit_wait_then_continue(self):
        self.p.scenario([S(CONT, WORK, {"limit": int(time.time()) - 58}), S(DONE, WORK, HAND)])
        r = self.p.run("--wait-on-limit")
        self.assertIn("waiting", r.stdout)
        self.assertStopped(r.stdout, "DONE")
        self.assertIn("cut off", self.p.kickoffs()[1]["kickoff"])

    def test_limit_wait_unreadable_reset(self):
        self.p.scenario([S(CONT, WORK, {"limit": None})])
        r = self.p.run("--wait-on-limit")
        self.assertStopped(r.stdout, "reset time could not be read")

    def test_limit_wait_beyond_hours(self):
        self.p.scenario([S(CONT, WORK, {"limit": int(time.time()) + 7200})])
        r = self.p.run("--wait-on-limit", "--hours", "1")
        self.assertStopped(r.stdout, "after the --hours deadline")


# ----------------------------------------------------------------- stopping --
class Stopping(Base):
    def test_graceful_stop(self):
        self.p.scenario([S(CONT, WORK, {"until_notice": True}), S(DONE, WORK, HAND)])
        pr = self.p.popen()
        self.p.wait_running()
        time.sleep(0.3)
        s = self.p.cmd("stop")
        self.assertIn("Stop requested", s.stdout)
        out, _ = pr.communicate(timeout=60)
        self.assertStopped(out, "stop requested (stop command)")
        self.assertEqual(len(self.p.kickoffs()), 1)               # no new session
        self.assertIn("(CONTINUE): wrapped up after notice", self.p.commits()[0])
        self.assertIn("The operator asked this run to stop",
                      (self.p.dir / "subjects/demo/sprints.md").read_text(encoding="utf-8"))

    def test_stop_escalates_to_kill(self):
        self.p.scenario([S(CONT, WORK, {"sleep": 60})])
        pr = self.p.popen("--stop-grace", "0.02")   # 1.2 s
        self.p.wait_running()
        self.p.cmd("stop")
        t = time.time()
        out, _ = pr.communicate(timeout=60)
        self.assertLess(time.time() - t, 20)
        self.assertIn("CRASHED: did not wrap up", self.p.commits()[0])
        self.assertStopped(out, "stop requested")

    def test_stop_now_then_recovery(self):
        self.p.scenario([S(CONT, WORK, {"sleep": 60}), S(DONE, WORK, HAND)])
        pr = self.p.popen()
        self.p.wait_running()
        pid = self.p.state()["child_pid"]
        s = self.p.cmd("stop", "--now")
        self.assertIn("Killed", s.stdout)
        out, _ = pr.communicate(timeout=60)
        self.assertStopped(out, "stopped with --now")
        self.assertIn("CRASHED: stopped with --now", self.p.commits()[0])
        self.assertNotIn("REVIEW", out)
        r = self.p.run()                        # next run: recovery kickoff
        self.assertIn("cut off", self.p.kickoffs()[1]["kickoff"])
        self.assertStopped(r.stdout, "DONE")

    def test_stale_stop_flag_cleared(self):
        (self.p.dir / ".claude/auto/STOP").write_text("{}", encoding="utf-8")
        self.p.scenario([S(DONE, WORK, HAND)])
        r = self.p.run()
        self.assertStopped(r.stdout, "DONE")

    def test_hours_cap_wraps_up(self):
        self.p.scenario([S(CONT, WORK, {"until_notice": True})])
        r = self.p.run("--hours", "0.0006")           # ~2 s
        self.assertStopped(r.stdout, "time limit")
        self.assertIn("time limit (--hours) was reached",
                      (self.p.dir / "subjects/demo/sprints.md").read_text(encoding="utf-8"))

    def test_soft_limit_notice_reaches_session(self):
        self.p.scenario([S(CONT, WORK, {"ctx": 2000}, {"tool": 3}, {"ctx": 6000}, {"until_notice": True})])
        r = self.p.run("--soft-limit", "5000", "--hard-limit", "50000", "--sessions", "1")
        sp = (self.p.dir / "subjects/demo/sprints.md").read_text(encoding="utf-8")
        self.assertIn("Context is at 6,000 tokens (soft limit 5,000)", sp)
        self.assertIn("wrap-up notices delivered by the hook: 1", r.stdout)

    def test_second_instance_refused_and_status(self):
        self.p.scenario([S(CONT, WORK, {"sleep": 60})])
        pr = self.p.popen()
        self.p.wait_running()
        r2 = self.p.run()
        self.assertIn("another run is active", r2.stdout + r2.stderr)
        st = self.p.cmd("status").stdout
        for s in ("Run active: yes", "Subject: demo", "Session: 1 (running)", "Active limits:",
                  "Elapsed:", "Context now:"):
            self.assertIn(s, st)
        self.p.cmd("stop", "--now")
        pr.communicate(timeout=60)
        self.assertIn("Run active: no", self.p.cmd("status").stdout)

    def test_stale_lock_cleared(self):
        dead = subprocess.Popen([PY, "-c", "pass"])
        dead.wait()
        (self.p.dir / ".claude/auto/lock").write_text(json.dumps({"pid": dead.pid, "ctime": 1}), encoding="utf-8")
        self.p.scenario([S(DONE, WORK, HAND)])
        r = self.p.run()
        self.assertIn("Clearing a stale lock", r.stdout)
        self.assertStopped(r.stdout, "DONE")

    @unittest.skipUnless(WIN, "Windows console Ctrl+C test")
    def test_ctrl_c_once_and_twice(self):
        for presses, expect, commit in ((1, "stop requested (ctrl-c)", "(CONTINUE): wrapped up after notice"),
                                        (2, "stopped with --now", "CRASHED: stopped with --now")):
            p = Proj("ctrlc%d" % presses)
            try:
                # Once: a session that obeys the notice. Twice: one that ignores it,
                # so only the second press (the kill) can end it.
                step = {"until_notice": True, "every": 0.5} if presses == 1 else {"sleep": 60}
                p.scenario([S(CONT, WORK, step), S(DONE, WORK, HAND)])
                outf = p.base / "out.txt"
                with open(outf, "wb") as fo:
                    si = subprocess.STARTUPINFO()
                    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    si.wShowWindow = 0
                    lp = subprocess.Popen(
                        [PY, str(HERE / "ctrlc_launcher.py"), str(presses),
                         str(p.dir / ".claude/auto/state.json")] + p.argv(),
                        stdin=subprocess.DEVNULL, stdout=fo, stderr=subprocess.STDOUT,
                        env=p.env(), cwd=p.base, creationflags=subprocess.CREATE_NEW_CONSOLE,
                        startupinfo=si)
                    lp.wait(timeout=90)
                out = outf.read_text(encoding="utf-8", errors="replace")
                self.assertStopped(out, expect)
                self.assertIn(commit, p.commits()[0])
                self.assertEqual(len(p.kickoffs()), 1)
            finally:
                p.cleanup()


# ----------------------------------------------------------- start of a run --
class Start(Base):
    def dirty(self):
        (self.p.dir / "subjects/demo/work.md").write_text("uncommitted\n", encoding="utf-8")

    def test_dirty_abort(self):
        self.dirty()
        self.p.scenario([S(DONE, WORK, HAND)])
        r = self.p.run(input="a\n")
        self.assertIn("Uncommitted changes in subjects/demo", r.stdout)
        self.assertIn("Aborted", r.stdout + r.stderr)
        self.assertEqual(self.p.commits(), ["init"])
        self.assertEqual(self.p.kickoffs(), [])

    def test_dirty_commit_answer(self):
        self.dirty()
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run(input="c\n")
        self.assertEqual(self.p.commits()[1], "pre-auto snapshot")

    def test_dirty_yes(self):
        self.dirty()
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run("--yes")
        self.assertEqual(self.p.commits()[1], "pre-auto snapshot")

    def test_dirty_outside_subject_ignored(self):
        (self.p.dir / "subjects/other/x.md").write_text("other window\n", encoding="utf-8")
        self.p.scenario([S(DONE, WORK, HAND)])
        r = self.p.run()   # no prompt: only the subject folder matters
        self.assertNotIn("Uncommitted changes", r.stdout)
        self.assertStopped(r.stdout, "DONE")

    def test_no_commit(self):
        self.p.scenario([S("no status", WORK), S(DONE, WORK, HAND)])
        r = self.p.run("--no-commit")
        self.assertEqual(self.p.commits(), ["init"])
        self.assertIn("uncommitted in the working tree", self.p.kickoffs()[1]["kickoff"])

    def test_subject_without_handoff_refused(self):
        r = subprocess.run([PY, str(self.p.dir / "auto.py"), "run", "other", "--claude-bin",
                            str(self.p.fake)], capture_output=True, env=self.p.env(), **ENC)
        self.assertIn("has no sprints.md", r.stdout + r.stderr)

    def test_py_claude_bin_and_session_numbering(self):
        shutil.copy(HERE / "fake_claude.py", self.p.base / "fake2.py")
        self.p.fake = self.p.base / "fake2.py"
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run()
        self.p.run()
        self.assertEqual(self.p.commits()[0], "auto: demo session 2 (DONE): subject finished")

    def test_review_and_push(self):
        bare = self.p.base / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
        self.p.git("remote", "add", "origin", str(bare))
        self.p.git("push", "-q", "-u", "origin", "main")
        self.p.scenario([S(DONE, WORK, HAND)], review="Session 1 did X.\nVERDICT: CLEAN")
        argv = [a for a in self.p.argv() if a != "--no-review"]
        r = subprocess.run(argv, input="y\n", capture_output=True, env=self.p.env(), cwd=self.p.base, **ENC)
        self.assertIn("REVIEW", r.stdout)
        self.assertIn("VERDICT: CLEAN", r.stdout)
        rv = [k for k in self.p.kickoffs() if k["review"]]
        self.assertEqual(len(rv), 1)
        self.assertIn("read-only review", rv[0]["kickoff"])
        self.assertIn("review-settings.json", " ".join(rv[0]["argv"]))
        self.assertIn("Push now?", r.stdout)
        remote_head = subprocess.run(["git", "--git-dir", str(bare), "log", "-1", "--format=%s", "main"],
                                     capture_output=True, **ENC).stdout.strip()
        self.assertEqual(remote_head, "auto: demo session 1 (DONE): subject finished")

    def test_review_no_push_on_eof(self):
        bare = self.p.base / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
        self.p.git("remote", "add", "origin", str(bare))
        self.p.git("push", "-q", "-u", "origin", "main")
        self.p.scenario([S(DONE, WORK, HAND)])
        argv = [a for a in self.p.argv() if a != "--no-review"]
        r = subprocess.run(argv, input="", capture_output=True, env=self.p.env(), cwd=self.p.base, **ENC)
        self.assertIn("Not pushed", r.stdout)
        remote_head = subprocess.run(["git", "--git-dir", str(bare), "log", "-1", "--format=%s", "main"],
                                     capture_output=True, **ENC).stdout.strip()
        self.assertEqual(remote_head, "init")

    def test_review_from_includes_earlier_auto_commits(self):
        start = self.p.git("rev-parse", "HEAD").stdout.strip()
        self.p.scenario([S(DONE, WORK, HAND)])
        self.p.run()                                   # earlier run, review skipped
        self.p.git("commit", "-q", "--allow-empty", "-m", "other window work")
        self.p.scenario([S(DONE, WORK, HAND)])
        argv = [a for a in self.p.argv() if a != "--no-review"] + ["--review-from", start]
        subprocess.run(argv, input="", capture_output=True, env=self.p.env(), cwd=self.p.base, **ENC)
        rv = [k for k in self.p.kickoffs() if k["review"]][-1]["kickoff"]
        self.assertIn("auto: demo session 1", rv)
        self.assertIn("auto: demo session 2", rv)
        self.assertNotIn("other window work", rv)
        self.assertLess(rv.index("session 1"), rv.index("session 2"))


# ------------------------------------------- gaps found by the independent review --
class ReviewGaps(Base):
    def test_deleted_claude_file_is_tamper_not_crash(self):
        self.p.scenario([S(CONT, WORK, HAND, {"rm": ".claude/settings.json"})])
        r = self.p.run()
        self.assertNotIn("Traceback", r.stdout + r.stderr)
        self.assertStopped(r.stdout, "TAMPER")
        self.assertIn(".claude/settings.json", r.stdout)

    def test_new_claude_file_is_tamper(self):
        self.p.scenario([S(CONT, WORK, HAND, {"edit": ".claude/settings.local.json",
                                              "text": '{"disableAllHooks": true}'})])
        r = self.p.run()
        self.assertStopped(r.stdout, "TAMPER")
        self.assertIn("settings.local.json", r.stdout)
        self.assertIn("did not exist before", r.stdout)

    def test_untracked_protected_restore_command(self):
        self.p.scenario([S(CONT, WORK, HAND, {"edit": ".claude/auto/run-settings.json", "text": " "})])
        r = self.p.run()
        self.assertStopped(r.stdout, "TAMPER")
        self.assertIn("Copy-Item -LiteralPath" if WIN else "cp ", r.stdout)
        self.assertIn("ece''" if WIN else "ece'", r.stdout)     # apostrophe escaped for PowerShell

    def test_tamper_skips_review(self):
        self.p.scenario([S(CONT, WORK, HAND, {"edit": "CLAUDE.md", "text": "x"})])
        argv = [a for a in self.p.argv() if a != "--no-review"]
        r = subprocess.run(argv, input="", capture_output=True, env=self.p.env(), cwd=self.p.base, **ENC)
        self.assertIn("Skipping the review and push", r.stdout)
        self.assertEqual([k for k in self.p.kickoffs() if k["review"]], [])

    def test_review_after_graceful_stop_not_killed(self):
        self.p.scenario([S(CONT, WORK, {"until_notice": True})], review="fine\nVERDICT: CLEAN")
        argv = [a for a in self.p.argv() if a != "--no-review"]
        pr = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, env=self.p.env(), cwd=self.p.base, **ENC)
        self.p.wait_running()
        self.p.cmd("stop")
        out, _ = pr.communicate("", timeout=60)
        self.assertIn("VERDICT: CLEAN", out)
        self.assertNotIn("told to wrap up (kill", out.split("REVIEW")[-1])

    def test_stop_now_during_crash_wait(self):
        self.p.scenario([S("no status", WORK), S(DONE, WORK, HAND)])
        argv = [a for a in self.p.argv() if a != "--no-review"] + ["--crash-wait", "30"]
        pr = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, env=self.p.env(), cwd=self.p.base, **ENC)
        end = time.time() + 30
        while not self.p.log() and time.time() < end:
            time.sleep(0.05)
        time.sleep(0.3)
        (self.p.dir / ".claude/auto/STOP_NOW").write_text("{}", encoding="utf-8")
        out, _ = pr.communicate("", timeout=60)
        self.assertStopped(out, "stopped with --now")
        self.assertNotIn("REVIEW", out)
        self.assertEqual(len(self.p.kickoffs()), 1)

    def test_nonzero_exit_with_status_is_crash(self):
        self.p.scenario([S(CONT, WORK, HAND, rc=1), S(DONE, WORK, HAND)])
        self.p.run()
        self.assertIn("CRASHED: claude exited with code 1", self.p.commits()[1])

    def test_branch_change_stops(self):
        self.p.scenario([S(CONT, WORK, HAND, {"sh": "git checkout -q -b sneaky"})])
        r = self.p.run()
        self.assertStopped(r.stdout, "branch changed from main to sneaky")
        self.assertEqual(self.p.git("log", "main", "-1", "--format=%s").stdout.strip(), "init")

    def test_logs_are_per_subject(self):
        d2 = self.p.dir / "subjects" / "demo2"
        d2.mkdir()
        (d2 / "sprints.md").write_text("## Current hand-off\nx\n", encoding="utf-8")
        self.p.git("add", "-A"); self.p.git("commit", "-qm", "demo2")
        self.p.scenario([S("no status", WORK)])
        self.p.run("--sessions", "1")                                # demo: crashed
        self.p.scenario([S(DONE, {"edit": "subjects/demo2/w.md", "text": "x"}, {"edit": "subjects/demo2/sprints.md", "text": "h"})],
                        subject="demo2")
        r = subprocess.run([PY, str(self.p.dir / "auto.py"), "run", "demo2", "--claude-bin", str(self.p.fake),
                            "--no-review"], capture_output=True, env=self.p.env(), **ENC)
        k = self.p.kickoffs()[-1]["kickoff"]
        self.assertNotIn("cut off", k)                               # demo's crash isn't demo2's
        self.assertIn("auto: demo2 session 1 (DONE)", self.p.commits()[0])

    def test_auto_py_died_mid_session_recovers_from_snapshot(self):
        # Simulate a run that died: lock of a dead pid, state says a session was running,
        # and that session's partial work is still uncommitted.
        dead = subprocess.Popen([PY, "-c", "pass"]); dead.wait()
        a = self.p.dir / ".claude/auto"
        (a / "lock").write_text(json.dumps({"pid": dead.pid, "ctime": 1}), encoding="utf-8")
        (a / "state.json").write_text(json.dumps({"session_running": True, "child_pid": dead.pid,
                                                  "child_ctime": 1}), encoding="utf-8")
        (self.p.dir / "subjects/demo/work.md").write_text("half-done\n", encoding="utf-8")
        self.p.scenario([S(DONE, WORK, HAND)])
        r = self.p.run("--yes")
        snap = self.p.git("log", "--format=%h %s").stdout.splitlines()[1]
        self.assertTrue(snap.endswith("pre-auto snapshot"))
        k = self.p.kickoffs()[0]["kickoff"]
        self.assertIn("cut off", k)
        self.assertIn("git show %s" % snap.split()[0], k)

    def test_edit_denials_from_result_not_lost(self):
        self.p.scenario([S(DONE, WORK, HAND, {"deny": "Permission to use Bash with command git push has been denied."},
                           {"result_denials": [
                               {"tool_name": "Bash", "tool_use_id": "tu-live", "tool_input": {"command": "git push"}},
                               {"tool_name": "Edit", "tool_use_id": "tu-edit", "tool_input": {"file_path": "CLAUDE.md"}}]})])
        r = self.p.run()
        d = self.p.log()[0]["permission_denials"]
        self.assertEqual(len(d), 2, d)
        self.assertIn("git push has been denied", d[0])
        self.assertTrue(d[1].startswith("Edit "), d)

    def test_summary_keeps_underscores(self):
        self.p.scenario([S("SUMMARY: fixed progress_log and A3_table\nSTATUS: DONE", WORK, HAND)])
        self.p.run()
        self.assertIn("progress_log and A3_table", self.p.commits()[0])


# --------------------------------------------------------------- the hook --
class Hook(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp(prefix="auto-hook-"))
        self.state = self.d / "state.json"
        self.hook = SRC_ROOT / ".claude" / "auto" / "hook.py"

    def tearDown(self):
        rmtree(self.d)

    def call(self, stdin='{"tool_name":"Bash"}', env=True):
        e = dict(os.environ)
        e.pop("AUTO_STATE_FILE", None)
        if env:
            e["AUTO_STATE_FILE"] = str(self.state)
        p = subprocess.run([PY, str(self.hook)], input=stdin, capture_output=True, env=e, **ENC)
        self.assertEqual(p.returncode, 0)
        self.assertEqual(p.stderr, "")
        return json.loads(p.stdout)["hookSpecificOutput"]["additionalContext"] if p.stdout else None

    def put(self, ctx, soft=1000, session=1, every=10):
        self.state.write_text(json.dumps({"session": session, "context": ctx, "soft_limit": soft,
                                          "notice_every": every}), encoding="utf-8")

    def test_no_env_does_nothing(self):
        self.put(5000)
        self.assertIsNone(self.call(env=False))
        self.assertFalse((self.d / "hook-state.json").exists())

    def test_below_soft_silent(self):
        self.put(500)
        self.assertIsNone(self.call())

    def test_soft_first_then_every_10(self):
        self.put(1500)
        got = [self.call() for _ in range(21)]
        fired = [i for i, g in enumerate(got) if g]
        self.assertEqual(fired, [0, 10, 20])
        self.assertIn("Context is at 1,500 tokens (soft limit 1,000)", got[0])
        self.assertIn("STATUS: CONTINUE", got[0])

    def test_stop_flag_fires_immediately(self):
        self.put(1500)
        self.call()                      # soft notice at call 1
        self.assertIsNone(self.call())   # throttled
        (self.d / "STOP").write_text('{"by":"stop command"}', encoding="utf-8")
        msg = self.call()                # stop is a new condition -> fires now
        self.assertIn("operator asked this run to stop", msg)
        self.assertIsNone(self.call())

    def test_new_session_resets(self):
        self.put(1500, session=1)
        self.assertTrue(self.call())
        self.put(1500, session=2)
        self.assertTrue(self.call())

    def test_garbage_is_silent(self):
        self.state.write_text("{not json", encoding="utf-8")
        self.assertIsNone(self.call())
        self.put(1500)
        self.assertIsNotNone(self.call(stdin="\x00garbage"))
        (self.d / "hook-state.json").write_text("[1,2", encoding="utf-8")
        self.assertIsNotNone(self.call())
        self.state.unlink()
        self.assertIsNone(self.call())   # missing state file


if __name__ == "__main__":
    unittest.main()
