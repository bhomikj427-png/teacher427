"""yt_search.py — list YouTube search hits (id | channel | title | seconds) via yt-dlp.

Usage: python -I research-tools/yt_search.py "<query 1>" ["<query 2>" ...]
Then pull captions for a hit with tools/fetch_transcripts.py "https://youtu.be/<id>" <outdir>.
"""
import subprocess
import sys

for q in sys.argv[1:]:
    print("==", q)
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "--print",
                        "%(id)s | %(channel)s | %(title)s | %(duration)s", "ytsearch6:" + q],
                       capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip()[-400:])
