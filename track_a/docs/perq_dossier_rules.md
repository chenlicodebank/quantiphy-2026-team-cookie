# Per-question dossier: what may enter a question's context (draft for the user's alignment, 2026-10-22)

Session 625fd803 (Track A). The organisers' per-question rule (website notice dated 2026-10-15) asks that each
question be answered "independently, without using other questions or their associated answers or priors to infer
its answer". A per-question dossier is a folder per scored question that collects every legitimate piece of evidence
about that question; reasoning sessions read one dossier and write back to it. This file states which evidence is
legitimate, so the dossier builder can enforce it in code.

## Legitimate in question q's dossier

- **L1. q's own inputs:** its video, its text, its own prior, its own depth_info, its question_fps.
- **L2. Question-blind computation on q's video:** anything computed from the video alone, with no question, prior or
  depth_info in its input - the phase-1 scene record of `cc_agent_scene.py` (tracks, extents, events of every object),
  masks or tracks of every object, camera motion, frame cadence. It may be shared by all questions of the video
  because it depends on none of them.
- **L3. Output of any run that was given only L1 + L2 (+ L4 / L5):** any model (Opus, Sonnet, DeepSeek, GLM, ...),
  any prompt, any number of repeats, with its notes, code and trace.
- **L4. Dataset-construction knowledge that depends on no question:** the paper's annotation appendix (Blender
  conventions, the internet annotators' single-scale method, the lab label process), the appendix-B lab prop table
  (usable with disclosure, user ruling 2026-10-22), Blender and physics defaults, world knowledge of object sizes.
- **L5. Class constants fitted on aggregate data:** one value per question class, the same for every question of the
  class (the lab motion factors x1.215 / x1.19 from board reads), disclosed in the technical summary.

## Not legitimate

- **N1. Output of any session that held another question** - even its answer to q itself, because its reasoning
  could use the other questions and cannot be audited row by row (2026-10-18 reading 4): the GLM-5.3-Flash v5r
  per-video agent (one session, every question of the video, one `finish_answers`), the #186-line per-video Opus
  agent, `cc_agent_run.py` with or without `--perq`, run medians of these. Exception: the 8 test videos that carry a
  single question, where a per-video session is a per-question session.
- **N2. Another question's prior, depth_info, answer, notes or trace**, used as a fact, pool, median, consensus,
  cross-check - or as the trigger that selects q for a re-run (second-order use, reading 3). This covers sibling
  cameras, `_segmented` twins, lab `s` / `x` renders and scene families.
- **N3. Labels:** validation labels (including the 125 test rows repeated from validation) and board reads of
  single rows.
- **N4. A reasoning session that holds more than one question's dossier**, even for questions on different videos.
  "One long session reviews many questions and keeps notes" is out; token savings come from caching the shared
  static prompt text across fresh one-question sessions.
- **N5. Hand edits of single rows** (the human-check corrections in #203 / E2) are human input, not part of an
  automatic method: disclosed as such in the technical summary.

## Reproducibility (top-3 package)

- **R1.** One script fixes the dossier contents (which runs, filtered by L1-L5), the order of rounds, the flag rule
  that picks rows for a round, the adjudicator prompt, model IDs and effort, and the stop rule.
- **R2.** Every session's stream is kept and archived; the final file is rebuilt from the dossiers by a deterministic
  build script.
- **R3.** Model outputs are not bit-exact, so "reproducible" means that re-running the pipeline gives a statistically
  similar score; the archived streams reproduce the submitted file exactly.

## What this means for each source (2026-10-22)

| Source | Status | Why |
|---|---|---|
| Opus 5.5 per-question answers (26_30), re-asks (26_59, 27_3, 27_6, 27_9), repeats (26_36) | in | L3 |
| Sonnet 5.5 repeats (26_80) | in | L3 (a weaker member; evidence only) |
| DeepSeek-V4.1-Flash-1017 two-phase answers (28_3 on 479 S3 rows, 28_6, 28_7) | in | L3 |
| GLM-5.3-Flash v5r answers (most of #194 / #210) | out | N1: one session per video |
| GLM-5.3-Flash per question (26_75 two-phase) | in if run | L3, but validation .567 macro against DeepSeek's .753 (28_2), so not worth running |
| #186 / #197 per-video Opus answers | out | N1; also not usable to pick rows (N2) |
| Series 18 SAM 3 tracks | in only for objects q itself names | L2 / L3; 29_1 shows they match the scene-record tracks, so they add little |
