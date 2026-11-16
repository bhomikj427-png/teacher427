#!/usr/bin/env python3
"""A fake `claude -p` for offline tests (0 tokens).

auto.py launches it exactly like the real CLI (stdin kickoff, stream-json on
stdout). What it does is scripted by the JSON file named in $FAKE_SCENARIO:

{"sessions": [ {"steps": [...], "final": "text", "rc": 0}, ... ],
 "review": "text for the read-only review session"}

Session i (counted in <scenario>.count) uses sessions[min(i, last)].
Steps:
  {"ctx": N}                 emit an assistant message whose usage totals N tokens
  {"tool": k}                simulate k tool calls: run the REAL PostToolUse hook
                             command from the --settings file each time
  {"edit": path, "text": s}  append s to a file (path relative to the project)
  {"handoff": true}          append a line to the subject's sprints.md hand-off
  {"sleep": sec}
  {"deny": "message"}        emit a permission_denied event
  {"limit": epoch|null}      emit the real usage-limit events, then exit 1
  {"until_notice": true, "max": n, "every": sec}
                             keep making tool calls until the hook injects a
                             wrap-up notice, then hand off and end with CONTINUE
Every kickoff + argv + env is appended to <scenario>.kickoffs.jsonl for asserts.
"""
import json
import os
import subprocess
import sys
import time

args = sys.argv[1:]
kick = sys.stdin.buffer.read().decode("utf-8")
scn_path = os.environ["FAKE_SCENARIO"]
scn = json.load(open(scn_path, encoding="utf-8"))
settings = json.load(open(args[args.index("--settings") + 1], encoding="utf-8"))
review = "default" in args

with open(scn_path + ".kickoffs.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"kickoff": kick, "argv": args, "review": review,
                        "AUTO_STATE_FILE": os.environ.get("AUTO_STATE_FILE"),
                        "DISABLE_AUTO_COMPACT": os.environ.get("DISABLE_AUTO_COMPACT"),
                        "pid": os.getpid()}) + "\n")


def emit(o):
    sys.stdout.write(json.dumps(o, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def result(text, rc=0, is_error=False):
    emit({"type": "result", "subtype": "success", "is_error": is_error, "result": text,
          "permission_denials": RESULT_DENIALS, "modelUsage": {"fake": {"contextWindow": 1000000}}})
    sys.exit(rc)


RESULT_DENIALS = []
emit({"type": "system", "subtype": "init", "model": "fake"})
if review:
    result(scn.get("review", "1. Summary...\nVERDICT: CLEAN"))

cnt = scn_path + ".count"
n = int(open(cnt).read()) if os.path.exists(cnt) else 0
open(cnt, "w").write(str(n + 1))
spec = scn["sessions"][min(n, len(scn["sessions"]) - 1)]
subject = scn.get("subject", "demo")
handoff = os.path.join("subjects", subject, "sprints.md")
notices = []


def hook_call():
    """Run every PostToolUse hook command exactly as configured."""
    for grp in settings.get("hooks", {}).get("PostToolUse", []):
        for h in grp["hooks"]:
            p = subprocess.run(h["command"], shell=True, input='{"tool_name":"Bash"}',
                               capture_output=True, text=True, encoding="utf-8")
            if p.stdout.strip():
                ctx = json.loads(p.stdout)["hookSpecificOutput"]["additionalContext"]
                notices.append(ctx)
                return ctx
    return None


def write_handoff(line):
    with open(handoff, "a", encoding="utf-8") as f:
        f.write(line + "\n")


ctx_now = 1000
for st in spec.get("steps", []):
    if "ctx" in st:
        ctx_now = st["ctx"]
        emit({"type": "assistant", "parent_tool_use_id": None, "message": {
            "id": "m%d" % ctx_now, "content": [{"type": "text", "text": "working"}],
            "usage": {"input_tokens": 10, "cache_read_input_tokens": ctx_now - 20,
                      "cache_creation_input_tokens": 5, "output_tokens": 5}}})
    elif "tool" in st:
        for _ in range(st["tool"]):
            hook_call()
    elif "edit" in st:
        os.makedirs(os.path.dirname(st["edit"]) or ".", exist_ok=True)
        with open(st["edit"], "a", encoding="utf-8") as f:
            f.write(st["text"])
    elif "handoff" in st:
        write_handoff("handoff written by fake session %d" % n)
    elif "sh" in st:                     # a "shell trick" the deny rules can't see
        subprocess.run(st["sh"], shell=True, capture_output=True)
    elif "rm" in st:
        os.remove(st["rm"])
    elif "sleep" in st:
        time.sleep(st["sleep"])
    elif "deny" in st:
        emit({"type": "system", "subtype": "permission_denied", "tool_name": "Bash",
              "tool_use_id": "tu-live", "message": st["deny"]})
    elif "result_denials" in st:      # shape of the real CLI's final list
        RESULT_DENIALS.extend(st["result_denials"])
    elif "limit" in st:
        info = {"status": "rejected", "rateLimitType": "five_hour"}
        if st["limit"]:
            info["resetsAt"] = st["limit"]
        emit({"type": "rate_limit_event", "rate_limit_info": info})
        emit({"type": "assistant", "parent_tool_use_id": None, "error": "rate_limit",
              "is_api_error_message": True, "api_error": "usage_limit_reached",
              "api_error_params": {"rate_limit_info": info},
              "message": {"id": "lim", "content": [{"type": "text",
                          "text": "You've hit your limit · resets 3pm"}]}})
        result("You've hit your limit · resets 3pm", rc=1, is_error=True)
    elif "until_notice" in st:
        for _ in range(st.get("max", 10000)):
            msg = hook_call()
            if msg:
                write_handoff("wrap-up handoff after notice: " + msg[:60])
                result("Wrapped up after the notice.\nSUMMARY: wrapped up after notice\nSTATUS: CONTINUE")
            time.sleep(st.get("every", 0.05))

result(spec.get("final", ""), rc=spec.get("rc", 0))
