"""--check for auto-v2: exit 0 (= stop the run) when the subject is finished
or the weekly limit is >= THRESH used. Exit 1 = keep going."""
import json, glob, os, re, sys
ROOT = sys.argv[1]; SUBJ = sys.argv[2]
# Learner 2026-11-18 (after the weekly reset): stop at 80% weekly use. Set it HERE
# (this file is re-read on every check; the chain passes 0.90, which is ignored).
THRESH = 0.80
log = os.path.join(ROOT, "subjects", SUBJ, "progress-log.md")
mark = os.environ.get("DONE_MARK", r"S9 (done|complete)")
if re.search(mark, open(log, encoding="utf-8").read()):
    print("subject done (%s)" % mark); sys.exit(0)
files = sorted(glob.glob(os.path.join(ROOT, ".claude/auto/runs/*session-*.jsonl")), key=os.path.getmtime)
util = None
for f in reversed(files[-3:]):
    for line in open(f, encoding="utf-8"):
        m = re.search(r'"seven_day":\{"utilization":([0-9.]+)', line)
        if m: util = float(m.group(1))
    if util is not None: break
print("weekly utilization:", util)
sys.exit(0 if (util is not None and util >= THRESH) else 1)
