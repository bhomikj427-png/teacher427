#!/usr/bin/env bash
# Screenshot aid for the v2 prototype: desktop shots direct, phone shots through phone.html (390px iframe, cropped).
# usage: bash shoot.sh <name> <desktop|phone> "<query>#<hash>" [height]
cd "$(dirname "$0")"
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
HERE="$(cygpath -m "$PWD")"
name=$1; kind=$2; qh=$3; hgt=${4:-900}
q="${qh%%#*}"; hsh="${qh#*#}"
if [ "$kind" = phone ]; then
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=6000 --window-size=600,844 \
    --screenshot="$(cygpath -w "$PWD/shots/$name.png")" "file:///$HERE/phone.html?$q#$hsh" 2>/dev/null
  python -c "from PIL import Image; im=Image.open('shots/$name.png'); im.crop((0,0,390,844)).save('shots/$name.png')"
else
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=6000 --window-size=1440,$hgt \
    --screenshot="$(cygpath -w "$PWD/shots/$name.png")" "file:///$HERE/proto.html?$q#$hsh" 2>/dev/null
fi
