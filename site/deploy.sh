#!/usr/bin/env bash
# Publish site/public/ to a separate PUBLIC GitHub repo served by GitHub Pages.
# The private engine repo is never pushed there — only the generated pages.
#   one-time: create an empty public repo on github.com (e.g. "study"),
#             then Settings -> Pages -> Deploy from branch: main / (root)
#   each time: bash site/deploy.sh https://github.com/<user>/<repo>.git
set -euo pipefail
REPO="${1:?usage: bash site/deploy.sh <public-repo-git-url>}"
HERE="$(cd "$(dirname "$0")" && pwd)"
python "$HERE/build.py"
TMP="$(mktemp -d)"
cp -r "$HERE/public/." "$TMP/"
cd "$TMP"
git init -q -b main
git add -A
git commit -q -m "Publish $(date +%Y-%m-%d\ %H:%M)"
git push -f "$REPO" main
echo "pushed -> $REPO (live in ~1 min at https://<user>.github.io/<repo>/)"
rm -rf "$TMP"
