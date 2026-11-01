# ECE2132 Data Structures & Algorithms Lab — lab pack

- **Read:** `pdf/ECE2132-DSA-Lab-pack.pdf` (91 pp., bookmarked) or the per-chapter PDFs in `pdf/`.
- **Edit:** `src/content/*.md` (text), `src/figures.py` (SVG figures), `src/code/*.cpp` (programs),
  `src/code/variants/t_*.cpp` (assignment functions + their tests). PDFs and `src/out/` are generated.
- **Rebuild:** `cd src && python verify.py && python build.py` (verify.py must print ALL PASS).
- **Checks:** `src/verify.py` compiles every program with g++ `-std=c++17 -Wall -Wextra -pedantic-errors -Werror -static`,
  runs 34 cases on the manual's sample inputs + edge cases, runs the 8 assignment test drivers (57 checks), and confirms
  the manual's 3 broken copies (`src/code/manual_original/`) fail to compile. The PDF quotes `src/out/` directly.
- Scope = `../exam-pack/manual/` (Exp 1–8, 10–12; no Exp 9 file — chapter 8 covers a probable stack experiment).
- Compiler: WinLibs MinGW g++ 16.2 (winget `BrechtSanders.WinLibs.POSIX.UCRT`), on the user PATH.
