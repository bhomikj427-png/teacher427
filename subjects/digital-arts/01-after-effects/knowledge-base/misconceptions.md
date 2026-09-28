# After Effects — misconceptions and traps

> Predictable beginner errors. Each is sourced: either Adobe documents the behaviour directly (then the
> trap is "the behaviour surprises beginners"), or it follows from a documented mechanism (marked
> *derived*). There is no education-research literature on After Effects errors that we found; frequency
> claims are therefore not made. Confidence per item.

| # | The trap | What is true | Source | Conf. |
|---|---|---|---|---|
| T1 | "Rotation/scale is broken: it spins around the wrong point." | Scale and Rotation pivot on the **anchor point**. Move it with Pan Behind (Y) or Ctrl+Alt+Home. | UG p.183, 15, 23 | settled |
| T2 | Turning the stopwatch off "pauses" the animation. | It **deletes every keyframe** of that property. Adobe warns about this. | UG p.232 | settled |
| T3 | Arrow keys step through time. | Arrows **nudge the selected layer 1 px** (and create a Position keyframe if the stopwatch is on). Frame step = Page Down / Page Up or Ctrl+→ / Ctrl+←. (A 2026 third-party cheat sheet gets this wrong.) | UG p.17, 23 | settled |
| T4 | More keyframes = smoother motion. | Smoothness comes from **interpolation and easing** between few keyframes (F9, Graph Editor). Extra keyframes make jitter harder to fix. | UG p.309, 321 | settled (derived) |
| T5 | Two identical Position keyframes = the layer stays still. | With Auto Bezier spatial interpolation it can **drift (boomerang)** between them. Use Hold or Linear. | UG p.310 | settled |
| T6 | Drawing a rectangle always makes a shape. | With a **layer selected**, a shape tool draws a **mask** on it. Deselect all (F2) first to get a new shape layer. | UG p.413–414 | settled |
| T7 | The comp's background colour will be in the video. | It is a viewer aid; in a nested comp it becomes transparent. Use a solid for a real background. | UG p.91 | settled |
| T8 | An adjustment layer affects everything. | Only layers **below** it. At the bottom it does nothing. | UG p.180 | settled |
| T9 | A drop shadow keeps a fixed light direction when the layer rotates. | Effects render **before** transforms, so the shadow rotates with the layer. | UG p.100 (derived) | settled (derived) |
| T10 | Precompose options don't matter. | "Leave all attributes" keeps keyframes/effects outside and sizes the comp to the layer; "Move all attributes" moves them inside at comp size. Wrong choice = animation seems lost, or the layer is cropped. | UG p.97 | settled |
| T11 | Preview speed = final speed; a stuttering preview means a broken file. | Preview plays from a RAM cache and may skip or lower resolution; only the render is final. | UG p.155, 533 | settled |
| T12 | The default render gives a small shareable video. | The default output module is **Lossless** → huge file. Choose **H.264** (23.0+) for an .mp4. | LEARN; AE23 | settled |
| T13 | Moving footage files is harmless. | The project stores **links**; moved files go missing. Use Collect Files to move a project. | UG p.78, 549 | settled |
| T14 | Parenting passes on everything. | Opacity is **not** inherited; Position, Scale, Rotation are. | UG p.205 | settled |
| T15 | Motion blur switch on the layer is enough. | The comp's **Enable Motion Blur** switch must also be on. | UG p.193 | settled |
| T16 | Scaling a text or shape layer past 100 % blurs it. | Text and shape layers are vector and stay sharp; imported vector files (AI, PDF) need **Continuously Rasterize** to stay sharp above 100 %. | UG p.193, 405 | settled |
| T17 | A track matte must sit directly above its fill layer. | True before 23.0; since 23.0 any layer can be chosen as the matte. Older tutorials show the old rule. | AE23 | settled [version] |
