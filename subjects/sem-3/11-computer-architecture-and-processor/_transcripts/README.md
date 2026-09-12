# `_transcripts/` — fetched lecture transcripts (raw, ASR, **not** a teaching source)

Pulled 2026-09-13 with `tools/fetch_transcripts.py` (yt-dlp auto-captions). Kept so that the
findings in `../video-lectures.md` §5 can be checked against the evidence rather than taken on
trust.

## ⚠ What these are

**Auto-generated speech recognition output**, not verified transcripts. ASR mangles exactly the
things this subject cares about: numbers, formulas, symbols and technical terms. Observed in these
files: *"up code"* for opcode, *"for nyman"* for von Neumann, *"AR metic"* for arithmetic,
digits split apart.

**Tier-1 with caveats** (`../../../../subject-research-protocol.md` §2): usable for **narrative,
structure and intuition**; every load-bearing specific must be triangulated against the textbook
before it is taught. Two numericals from these files were promoted into `../study-pack/10`
**only after the arithmetic was independently re-derived**.

**Nothing here is a teaching source on its own.** `../knowledge-base/` and `../study-pack/` win.

## The files, and what each actually contains

| File | Verified content | Verdict |
|---|---|---|
| `IITG-ACA-deKUGMHZjB4-MISTITLED-actually-Lec4-pipeline-hazards.txt` | opens *"Welcome to the fourth lecture… dedicated on discussion related to pipeline hazards"* — **Lec 4**, despite being titled *"Tutorial 1: Instruction Pipeline and Performance"* in the playlist | good structural-hazard walkthrough (uni-port memory, stall vs duplicate hardware); **corroborates `study-pack/10` §8(a)**. Not the tutorial its title promises |
| `IITG-ACA-MjjFqj01PzU-Tutorial-2-pipeline-hazard-analysis-VERIFIED.txt` | genuinely **Tutorial 2**, week 2: 8 true/false items + 3 numericals | **the one real find.** Two numericals extracted, verified and worked into `study-pack/10` Appendix. Uses MIPS/CPI framing, not Mano's |
| `IITG-ACA-lPoI0ZeXiQU-Tutorial-3-static-and-dynamic-scheduling.txt` | week-3 tutorial, static + dynamic scheduling | mostly **beyond MTE scope** (dynamic scheduling, Tomasulo). The static-scheduling half touches `study-pack/10`'s delayed-load material |
| `IITM-CO-F5pU5LbmLVg-L13-instruction-formats-NOT-control-unit.txt` | instruction formats, operand counts, opcode field sizing (2⁴ = 16 combinations) | **claim retracted.** `video-lectures.md` previously called this a control-unit problem exercise; it is not. Relevant to U2 instruction codes, different machine |
| `IITM-CO-hhvl7nbVpLo-L14-recap-then-memory-NOT-control-unit.txt` | conceptual recap (data path, control signals, "a microinstruction is one small step", ALU + controller = CPU), then **moves into memory** | **claim retracted.** Not a problem exercise; the memory half is U6/ETE |

## Why the filenames shout

Two of the five did not contain what their playlist titles said. The filenames record the
**verified** content so that nobody — including a future session of this engine — re-derives the
wrong conclusion from a title. That is the same rule the whole project runs on: the professor's
material sets scope, but what is *true* gets checked.

## Reproducing

```
python tools/fetch_transcripts.py "<video-or-playlist-url>" "<output_dir>"
```

If it reports HTTP 429, YouTube is rate-limiting the IP — captions still exist, and a retry with
10–30 minutes of backoff has been enough. Playlist *listing* keeps working during such a block, so
enumerate first and pull transcripts slowly. The retry driver used here was
`pull_tutorials.py` (scratchpad, not kept): it succeeded on attempt 3.
