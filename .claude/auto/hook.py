#!/usr/bin/env python3
"""PostToolUse hook for auto.py sessions: the "fuel gauge" notice.

Claude Code runs this after every tool call, but ONLY in sessions started by
auto.py: auto.py loads it through a per-run --settings file and sets
AUTO_STATE_FILE in the session's environment. Your normal interactive sessions
never see it (no settings entry), and if it somehow ran without the variable it
does nothing.

What it does: auto.py writes the session's live context size to state.json.
This hook reads that file and, when the context is past the SOFT limit (or the
operator asked the run to stop), injects a short "wrap up" notice into the
session as additionalContext. The model sees that text right after the tool
result, which is the only way to talk to a `claude -p` session mid-turn.

Why throttled: a notice on every tool call would flood the context it is trying
to protect. It fires the first time a condition appears, then again only every
`notice_every` tool calls (default 10) as a reminder.

Why it swallows every error: a hook that crashes or prints junk can break the
session it is guarding. Any problem -> exit 0, print nothing.
"""
import json
import os
import sys


def _atomic_write(path, data):
    # Write to a temp file and rename, so a parallel hook call (Claude can run
    # tools in parallel) never reads a half-written file.
    tmp = "%s.%d.tmp" % (path, os.getpid())
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f)
    os.replace(tmp, path)


def main():
    state_path = os.environ.get("AUTO_STATE_FILE")
    if not state_path:
        return  # not an auto.py session: do nothing at all
    try:
        sys.stdin.read()  # drain the hook payload; we don't need it
    except Exception:
        pass

    with open(state_path, encoding="utf-8") as f:
        st = json.load(f)
    auto_dir = os.path.dirname(state_path)

    session = st.get("session")
    ctx = int(st.get("context") or 0)
    soft = int(st.get("soft_limit") or 0)
    every = max(1, int(st.get("notice_every") or 10))

    stop_reason = None
    stop_path = os.path.join(auto_dir, "STOP")
    if os.path.exists(stop_path):
        stop_reason = "The operator asked this run to stop."
        try:
            with open(stop_path, encoding="utf-8") as f:
                stop_reason = json.load(f).get("message") or stop_reason
        except Exception:
            pass

    hs_path = os.path.join(auto_dir, "hook-state.json")
    try:
        with open(hs_path, encoding="utf-8") as f:
            hs = json.load(f)
    except Exception:
        hs = {}
    if hs.get("session") != session:
        # New session -> fresh counters (the old ones belong to a finished session).
        hs = {"session": session, "calls": 0, "last_notice_call": None,
              "kinds": [], "notices": 0}
    hs["calls"] += 1

    kind = "stop" if stop_reason else ("soft" if soft and ctx >= soft else None)
    msg = None
    if kind:
        first_time = kind not in hs["kinds"]
        due = (hs["last_notice_call"] is None
               or hs["calls"] - hs["last_notice_call"] >= every)
        if first_time or due:
            if kind == "stop":
                msg = ("[auto.py] %s Wrap up now: finish the current step, stop at "
                       "a clean point, write the handoff the usual way, and end "
                       "your final message with the SUMMARY line and "
                       "STATUS: CONTINUE." % stop_reason)
            else:
                msg = ("[auto.py] Context is at %s tokens (soft limit %s). Finish "
                       "the current step, stop at a clean point, write the handoff "
                       "the usual way, and end your final message with the SUMMARY "
                       "line and STATUS: CONTINUE." % (format(ctx, ","), format(soft, ",")))
            if first_time:
                hs["kinds"].append(kind)
            hs["last_notice_call"] = hs["calls"]
            hs["notices"] += 1
            hs["last_notice"] = msg

    _atomic_write(hs_path, hs)
    if msg:
        sys.stdout.write(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse", "additionalContext": msg}}))
        sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        pass  # never break the session
    sys.exit(0)
