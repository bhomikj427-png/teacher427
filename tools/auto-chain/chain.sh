#!/bin/bash
# auto-v2 chain for one subject, with handbrakes. Usage: bash tools/auto-chain/chain.sh [subject]
# Stop it: touch $C/STOP (checked between runs).
C="$(cd "$(dirname "$0")" && pwd -W)"   # this folder; logs + STOP flag live here
cd "/c/Users/bhomi/OneDrive/Desktop/claude/ece'" || exit 1
R="$(pwd -W)"
log(){ echo "[$(date '+%m-%d %H:%M')] $*" | tee -a "$C/chain.log"; }
active(){ python auto.py status 2>/dev/null | grep -q "Run active: yes"; }
stop_reason(){ tail -1 .claude/auto/log.jsonl | python -c "import sys,json;print(json.loads(sys.stdin.read()).get('stop_reason') or '')"; }
DONE_MARK="${DONE_MARK:-S9 (done|complete)}"   # ERE; EDC: DONE_MARK="E11 (done|complete)"
export DONE_MARK
done_subj(){ grep -Eq "$DONE_MARK" "subjects/$1/progress-log.md"; }
net_wait(){ until curl -s -m 10 -o /dev/null https://api.anthropic.com; do sleep 60; done; }
weekly_reset(){ python - <<'PY'
import glob,os,re,time
fs=sorted(glob.glob(".claude/auto/runs/*session-*.jsonl"),key=os.path.getmtime)
r=None
for f in reversed(fs[-3:]):
    for l in open(f,encoding="utf-8"):
        m=re.search(r'"seven_day":\{"utilization":[0-9.]+,"resetsAt":([0-9]+)',l)
        if m:r=int(m.group(1))
    if r:break
print(max(60,(r or time.time()+3600)-int(time.time())+300))
PY
}
run(){ # $1 subject, $2 extra args
  local subj="$1" crashes=0
  while :; do
    [ -f "$C/STOP" ] && { log "STOP flag: chain halted"; exit 0; }
    done_subj "$subj" && { log "$subj: Sprint S9 done"; return 0; }
    net_wait
    log "$subj: starting auto-v2 run"
    python auto-v2.py run "$subj" --soft-limit 180000 --hard-limit 210000 --sessions 12 --hours 20 \
      --wait-on-limit --yes --check "python -I \"$C/weekly_check.py\" \"$R\" $subj 0.90" < /dev/null >> "$C/run-$(basename $subj).log" 2>&1
    local why; why="$(stop_reason)"; log "$subj: run ended: $why"
    done_subj "$subj" && { log "$subj: done"; return 0; }
    case "$why" in
      *"crash"*|*"exited with code"*|*"ENOTFOUND"*)
        crashes=$((crashes+1)); [ $crashes -ge 3 ] && { log "HANDBRAKE: 3 crash-stops in a row; chain halted"; exit 1; }
        log "crash-stop $crashes/3: waiting for network, then restarting"; sleep 120 ;;
      *"destination reached"*)
        s=$(weekly_reset); log "HANDBRAKE: weekly limit >= 90%; sleeping ${s}s until the weekly reset"; sleep "$s"; crashes=0 ;;
      *"usage limit"*)
        log "usage limit stop; retrying in 1h (the new run waits for the reset itself)"; sleep 3600; crashes=0 ;;
      ""|*"--sessions"*|*"time limit"*)
        crashes=0; log "session/hour cap reached; continuing with a fresh run" ;;
      *) log "HANDBRAKE: stopped for '$why' (tamper/stuck/blocked/commit/secret): needs a human; chain halted"; exit 1 ;;
    esac
  done
}
SUBJ="${1:-sem-3/04-digital-electronics}"
log "chain start ($SUBJ); waiting for any active run to end"
while active; do sleep 120; done
run "$SUBJ"
log "chain finished: $SUBJ done"
