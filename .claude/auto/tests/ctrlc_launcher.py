"""Test helper (Windows): press Ctrl+C in a private console.

The test starts this script in a NEW hidden console. It runs auto.py in that
same console, waits until a session is running, then generates real Ctrl+C
events for the whole console - exactly what pressing Ctrl+C in the auto.py
window does. The fake claude was started by auto.py in its own process group,
so if the isolation works it keeps running and wraps up properly.

usage: ctrlc_launcher.py <presses> <state.json> <auto.py argv...>
"""
import ctypes
import json
import subprocess
import sys
import time

presses, state = int(sys.argv[1]), sys.argv[2]
k32 = ctypes.windll.kernel32
# Whatever started us may have disabled Ctrl+C (that flag is inherited). A real
# terminal has it enabled, so re-enable it before starting auto.py.
k32.SetConsoleCtrlHandler(None, False)
child = subprocess.Popen(sys.argv[3:])          # same console, same group as us
k32.SetConsoleCtrlHandler(None, True)           # we ignore Ctrl+C (child created before: unaffected)

end = time.time() + 30
while time.time() < end:
    try:
        if json.load(open(state, encoding="utf-8")).get("session_running"):
            break
    except Exception:
        pass
    time.sleep(0.05)
time.sleep(0.3)
for i in range(presses):
    k32.GenerateConsoleCtrlEvent(0, 0)          # CTRL_C_EVENT to the whole console
    time.sleep(0.5)
sys.exit(child.wait(timeout=80))
