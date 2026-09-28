# 06 — Preview & export

> Stage 1. Truth = [UG], [AE23], [LEARN]. `settled` unless marked.

## Preview [UG p.155–168]
- **Spacebar** starts/stops a preview with audio. After Effects renders frames into RAM and plays them;
  the first pass through a heavy comp is slower than real time, later passes play from cache.
- **Green bar** in the time ruler = frames cached in RAM; **blue bar** = cached to disk. [UG p.533]
- Each preview key (Space, Shift+Space, Numpad 0, Shift+Numpad 0, Alt+Numpad 0) can hold its own settings
  in the **Preview panel (Ctrl+3)**: loop, range, frame **Skip**, **Resolution** (Auto default), cache
  before playback.
- Faster previews: lower the Composition panel resolution (**Ctrl+Shift+J** = Half, **Ctrl+J** = Full),
  shorten the work area (**B / N**), solo the layer you are judging, or set Skip = 1.
- **Snapshots:** Shift+F5 stores the current view; F5 shows it again → compare before/after.
- If previews get sluggish after long work: **Edit > Purge > All Memory & Disk Cache** (or Ctrl+Alt+/ on the
  numpad for All Memory). [UG p.13, 532–534]

## Render Queue (the export path) [UG p.30, 541–549; LEARN; AE23]
1. Select the comp; **Composition > Add to Render Queue** (**Ctrl+M**; Adobe's table also lists
   **Ctrl+Shift+/**). The Render Queue panel opens.
2. **Render Settings** ("Best Settings"): quality, resolution, time span (work area or whole comp),
   frame rate. Decides *how frames are computed*.
3. **Output Module** (default "Lossless"): format, codec, size, audio. Decides *how frames are encoded
   into a file*. The Lossless default writes a very large file. **[version: 23.0+] choose H.264** (three
   bitrate presets; hardware or software encoding) for a shareable .mp4. [AE23]
4. **Output To:** click the file name to choose name and folder.
5. **Render.** A bar shows progress; the file exists when it finishes.
- One render item can have several output modules (e.g. an .mp4 and a PNG sequence) without rendering
  twice. [UG p.542]
- **Adobe Media Encoder** (**Ctrl+Alt+M**, or Composition > Add to Adobe Media Encoder Queue): more
  formats and presets, renders in the background so After Effects stays free. Needs AME installed.
- **Still frame:** Composition > Save Frame As > File [UG p.559] (**Ctrl+Alt+S** adds the current frame to the queue).
- **Transparent video** (for overlays): Output Module with an alpha-capable format and RGB + Alpha channels
  (e.g. QuickTime with Apple ProRes 4444 or a PNG sequence). H.264 has no alpha. `likely` [version].

## Handing the project on
- **File > Dependencies > Collect Files** copies the project and all footage to one folder. [UG p.549]
- Save a copy for an older version: File > Save As > Save a Copy As <previous version>. [UG p.81]

→ Stage 2: `stage-2/01-render-pipeline.md` (render settings vs output module as two separate stages;
why preview ≠ final).
