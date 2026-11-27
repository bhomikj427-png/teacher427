# chat-pack-template/ — how exam chat files ("instrV2") are made

An **instrV2 chat file** is one Markdown file that a separate chat session reads to tutor the learner
for one exam. It holds the teaching rules, the subject's trunk idea, a ranked question bank, and verified
answer keys. It is a delivery format, like the study packs, and it never overrides the five principles
in `CLAUDE.md`.

| File | Role |
|---|---|
| `generator-prompt.md` | **The build spec.** Fill in the subject, then follow it. Subject-agnostic. |
| `reference-instcV2-CAP.md` | **The frozen reference** (CAP, 26 Nov 2026): the source of the 8 teaching rules, the session-switch rule and the example-flow skeleton. Never edit it; copy its structure, never its content. |

To build one for a new subject: read `generator-prompt.md`, then follow it. Output goes to
`subjects/<…>/<subject>/chat-pack/<subject>-instrV2.md`, with its checker script and programs beside it.
Live state (which files exist, how far each session got) lives in each subject's `progress-log.md`, not here.
