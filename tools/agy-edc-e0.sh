#!/bin/bash
# EDC E0: transcribe every EDC deck/sheet with agy (Gemini Flash), 17 jobs, at most MAX (default 6) at once; re-runs skip jobs whose output exists.
# Inputs were already extracted to $S by research-tools/deck_extract.py + render_pages.py.
# agy obeys GEMINI.md (repo root); it may write only $S/out/<job>.md. Run from the repo root:
#   bash tools/agy-edc-e0.sh
S="C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0"
mkdir -p "$S/out"; : > "$S/out/status.txt"
MAX=${MAX:-6}   # at most this many agy jobs at once
job(){ local name="$1" dir="$2" what="$3"
  [ -s "$S/out/$name.md" ] && { echo "$name skip (done)" >> "$S/out/status.txt"; return; }   # re-runs redo only missing jobs
  local task="Read GEMINI.md in the repo root and follow all its rules. Your task (rule 1): transcribe $what from the folder $S/$dir into markdown. slides.txt there has each slide's text; image files are named sNNN-* by slide number, or *-pNNN.png by page. For each slide/page write '## slide N' (or '## page N'), then its full text, equations in plain text, tables as markdown tables, and a one-line description of any circuit or graph with every component value and label. For worked examples and questions copy every given value, every step and the final answer. The only file you may write is $S/out/$name.md (end it with the Done report, rule 8). Do not edit anything in the repo; no git commands."
  timeout 1500 agy --model gemini-3.8-flash-high -p "$task" --dangerously-skip-permissions --add-dir "$S" --log-file "$S/out/agy-$name.log" < /dev/null > /dev/null 2>&1
  echo "$name exit $?" >> "$S/out/status.txt"; }
go(){ while [ "$(jobs -rp | wc -l)" -ge "$MAX" ]; do sleep 5; done; job "$@" & }   # throttle in the parent shell
go num34a NUMERICALS-U3-U4-jfet-dmosfet-emosfet-solved "pages 1-11 of the solved numericals sheet"
go num34b NUMERICALS-U3-U4-jfet-dmosfet-emosfet-solved "pages 12-21 of the solved numericals sheet"
go numh NUMERICALS-U5-h-parameter-book-pp131-145 "all 8 pages of the h-parameter book extract"
go l08 slides-U2-L08-diode-load-line-and-series-parallel "every slide (1-19)"
go l09 slides-U2-L09-diode-rectifiers "every slide (1-27)"
go l10 slides-U2-L10-diode-clippers-clampers-multipliers "every slide (1-22)"
go jfet slides-U3-jfet "every slide (1-44)"
go l2627a slides-U5-L26-27-biasing-stability-h-parameters "slides 1-27"
go l2627b slides-U5-L26-27-biasing-stability-h-parameters "slides 28-53"
go multi slides-U5-multistage-amplifier-and-darlington "every slide (1-13)"
go mostype slides-U4-mosfet-types-and-characteristics "every slide (1-29)"
go mosbias slides-U4-mosfet-biasing-and-digital-circuits "every slide (1-16)"
go ce slides-U5-L23-25-common-emitter-and-load-line "every slide (1-17)"
go fb slides-U6-feedback-amplifiers "every slide (1-51)"
go spd slides-U2-special-diodes-LED-tunnel-photodiode "every slide (1-40)"
go osc slides-U7-oscillators-RC-LC "all text runs and all 8 pictures (a .ppt export: pictures are in file order, not slide order; number them picture 1..8)"
go xtal slides-U7-crystal-oscillators "every slide (1-3)"
wait; cat "$S/out/status.txt"; git status --short
