@@ warm-up-6 | Warm-up: guess first | practice | Two guesses about getting a file out.

:::q Guess first (write it down)
1. Your preview stutters. Is the exported video going to stutter too?
2. You render with the default settings. Roughly how big is a 15 s 1080p file: 5 MB, 50 MB, or several GB?
:::

@@ preview | Preview | method | Space plays. The green bar is what is ready to play in real time.

[[fig:preview_cache|The first play fills the green bar (RAM cache); after that it plays at full speed.|w=100]]

- **Space** play/stop. **B / N** limit the work area so less has to be cached.
- Slow? Lower the viewer resolution: **Ctrl+Shift+J** Half, **Ctrl+J** Full.
- **Shift+F5** saves a snapshot, **F5** shows it: before/after in one key.
- Still slow after a long session: Edit > Purge > All Memory & Disk Cache.

:::reveal Quick check: warm-up question 1
**No.** Preview is a cache at whatever resolution you set; the render computes every frame properly.
:::

@@ render-queue | Render Queue → .mp4 | method | Ctrl+M, set Output Module to H.264, choose Output To, press Render.

[[fig:render_queue|Two separate stages: render settings compute the frames, the output module encodes them.|w=100]]

1. Select the comp. **Ctrl+M** (Composition > Add to Render Queue).
2. **Render Settings**: leave "Best Settings".
3. **Output Module**: click it → Format **H.264**.
4. **Output To**: click the file name → folder + name.
5. **Render**. Wait for the bar; the file exists when it finishes.

@@ lossless-trap | Trap: the Lossless default | trap | The default output module writes a huge file. Pick H.264 for sharing.

[[fig:render_queue|Stage 4 is where the file size is decided.|w=80]]

:::trap Default = Lossless
The Output Module starts as **Lossless**: correct pixels, enormous file. For a shareable .mp4 choose **H.264** (in the Render Queue since version 23.0).
:::

:::reveal Quick check: warm-up question 2
Lossless can reach **gigabytes**: uncompressed 1080p is 1920 × 1080 × 3 bytes ≈ 6.2 MB per frame, × 450 frames ≈ 2.8 GB. H.264 at a typical web bitrate: tens of MB.
:::

H.264 has no transparency. For an overlay with a see-through background, use a format with an alpha channel (PNG sequence or ProRes 4444) and set Channels to RGB + Alpha.

@@ ame-collect | Media Encoder and Collect Files | idea | AME renders in the background; Collect Files packs the project for moving.

[[fig:render_queue|AME is an alternative route from step 2 onward.|w=70]]

- **Ctrl+Alt+M** sends the comp to **Adobe Media Encoder** (if installed): more presets, and you can keep working while it renders.
- **Composition > Save Frame As > File**: a single still (a thumbnail).
- **File > Dependencies > Collect Files**: project + all footage into one folder, for moving or backup.

@@ self-test-6 | Self-test: chapter 6 | practice | In the software, no notes.

1. Export only 2 s – 5 s of your comp as an .mp4 to your Desktop.
2. Save one frame as a PNG thumbnail.

:::reveal Answers
1. B at 2 s, N at 5 s; Ctrl+M; Render Settings ▸ Time Span **Work Area Only**; Output Module H.264; Output To Desktop; Render. 2. CTI on the frame, Composition > Save Frame As > File (it joins the Render Queue), set the output module format to PNG, Render.
:::
