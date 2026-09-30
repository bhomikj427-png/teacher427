#!/usr/bin/env bash
# Screenshots of the river prototype. usage: bash shoot-river.sh <name> <desktop|phone> "<query>#<hash>" [budget-ms]
cd "$(dirname "$0")"
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
HERE="$(cygpath -m "$PWD")"
name=$1; kind=$2; qh=$3; bud=${4:-4000}
q="${qh%%#*}"; hsh="${qh#*#}"
mkdir -p shots/river
if [ "$kind" = phone ]; then
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=$bud --window-size=600,844 \
    --screenshot="$(cygpath -w "$PWD/shots/river/$name.png")" "file:///$HERE/phone-river.html?$q#$hsh" 2>/dev/null
  python -c "from PIL import Image; im=Image.open('shots/river/$name.png'); im.crop((0,0,390,844)).save('shots/river/$name.png')"
else
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=$bud --window-size=1440,900 \
    --screenshot="$(cygpath -w "$PWD/shots/river/$name.png")" "file:///$HERE/river.html?$q#$hsh" 2>/dev/null
fi
