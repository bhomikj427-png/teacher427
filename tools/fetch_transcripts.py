#!/usr/bin/env python3
"""
fetch_transcripts.py — automated NPTEL (or any YouTube) lecture-transcript puller.

The verified-automated content path for the ece' engine (see subject-research-protocol.md §2,
"Practical ingestion note"). NPTEL course/archive web pages do NOT fetch cleanly (JS tabs, 404s),
but NPTEL's own YouTube lectures carry auto-captions that yt-dlp can pull and we can clean into
teachable plain text.

WHAT IT DOES
  1. Takes a YouTube playlist URL (an NPTEL course == one playlist), a single video URL, or a
     `ytsearch` query.
  2. Downloads English captions (manual subs preferred; falls back to auto-captions).
  3. Cleans each VTT into deduplicated plain text (strips timestamps, tags, rolling-caption dupes).
  4. Writes one numbered <NN>-<title>.txt per lecture into the output dir, plus a manifest.

USAGE
  python tools/fetch_transcripts.py "<playlist-or-video-url>" "<output_dir>"
  python tools/fetch_transcripts.py "ytsearch20:NPTEL signals and systems IIT" "<output_dir>"

REQUIRES
  pip install yt-dlp     (pure Python; no ffmpeg needed for captions-only)

⚠ HONESTY CAVEAT (carried into the engine):
  Auto-captions are ASR output, not a verified transcript. They mangle math, symbols, and numbers
  ("1024" -> "1 024", a formula -> words). So a transcript is a Tier-1 source WITH CAVEATS: good
  for narrative/structure/intuition, but every load-bearing specific (formula, number, definition)
  must be triangulated against the canonical textbook before it is taught as settled (§1, §5).
"""
import os
import re
import sys
import json
import glob
import subprocess
import tempfile


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def clean_vtt(path):
    """VTT -> deduplicated plain text."""
    raw = open(path, encoding="utf-8", errors="replace").read()
    out, last = [], None
    for ln in raw.splitlines():
        if "-->" in ln or not ln.strip():
            continue
        if ln.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        ln = re.sub(r"<[^>]+>", "", ln)        # <c>, <timestamp> tags
        ln = re.sub(r"\[.*?\]", "", ln).strip()  # [Music], [Applause]
        if not ln or ln == last:
            continue
        out.append(ln)
        last = ln
    text = re.sub(r"\s+", " ", " ".join(out)).strip()
    return text


def safe(name, n=60):
    name = re.sub(r"[^\w\s-]", "", name).strip()
    name = re.sub(r"\s+", "-", name)
    return name[:n] or "lecture"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    source, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)

    SEP = "=#="   # delimiter that is legal in Windows filenames (| and : are not)

    def lang_rank(lang):
        """Lower is better: prefer plain en, then regional en, then auto 'orig', then other."""
        lang = lang.lower()
        if lang == "en":
            return 0
        if lang in ("en-us", "en-gb"):
            return 1
        if lang.startswith("en") and "orig" not in lang:
            return 2
        if lang.startswith("en"):
            return 3
        return 4

    with tempfile.TemporaryDirectory() as tmp:
        # Prefer manual English subs; fall back to auto-captions.
        cmd = [
            "yt-dlp", "--skip-download",
            "--write-subs", "--write-auto-subs",
            "--sub-langs", "en.*", "--sub-format", "vtt",
            "--ignore-errors",
            "-o", os.path.join(tmp, f"%(playlist_index)s{SEP}%(title)s{SEP}%(id)s.%(ext)s"),
            source,
        ]
        print(f"[*] Fetching captions for: {source}")
        r = run(cmd)
        if r.returncode != 0 and not glob.glob(os.path.join(tmp, "*.vtt")):
            print("[!] yt-dlp error:\n" + (r.stderr or r.stdout)[-1500:])
            sys.exit(2)

        vtts = glob.glob(os.path.join(tmp, "*.vtt"))
        if not vtts:
            print("[!] No captions found for this source. Try a different course/playlist, "
                  "or supply the transcript PDF manually.")
            sys.exit(3)

        # One video can yield several en tracks (en, en-US, en-orig). Keep the best per video id.
        best = {}   # vid -> (rank, idx, title, vtt_path)
        for vtt in vtts:
            base = os.path.basename(vtt)
            m = re.match(r"\.([\w-]+)\.vtt$", "." + base.split(SEP)[-1].split(".", 1)[1]) \
                if SEP in base else None
            lang = m.group(1) if m else "en"
            stem = re.sub(r"\.[\w-]+\.vtt$", "", base)   # drop ".<lang>.vtt"
            parts = stem.split(SEP)
            idx = parts[0].strip() if parts and parts[0].strip().isdigit() else "0"
            title = parts[1] if len(parts) > 1 else stem
            vid = parts[2] if len(parts) > 2 else stem
            rank = lang_rank(lang)
            if vid not in best or rank < best[vid][0]:
                best[vid] = (rank, idx, title, vtt)

        manifest = []
        for i, (vid, (rank, idx, title, vtt)) in enumerate(
                sorted(best.items(), key=lambda kv: int(kv[1][1]) or 10**6), start=1):
            text = clean_vtt(vtt)
            if len(text.split()) < 30:    # skip empty/near-empty caption tracks
                continue
            n = int(idx) if idx.isdigit() and idx != "0" else i
            fname = f"{n:02d}-{safe(title)}.txt"
            header = (f"# {title}\n# source: https://youtu.be/{vid}\n"
                      f"# AUTO-CAPTION — verify formulas/numbers against textbook before teaching\n\n")
            open(os.path.join(outdir, fname), "w", encoding="utf-8").write(header + text)
            manifest.append({"index": n, "title": title, "video": vid,
                             "file": fname, "words": len(text.split())})
            print(f"  [+] {fname}  ({len(text.split())} words)")

        manifest.sort(key=lambda m: m["index"])
        with open(os.path.join(outdir, "_manifest.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        total = sum(m["words"] for m in manifest)
        print(f"\n[done] {len(manifest)} transcripts, {total:,} words -> {outdir}")


if __name__ == "__main__":
    main()
