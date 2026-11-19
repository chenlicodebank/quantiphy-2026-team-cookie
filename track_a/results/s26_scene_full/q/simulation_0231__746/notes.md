# q_746 – length of the chalkboard (m)

Prior: black cat speed = 0.714 m/s. fps = question_fps = 24 (no re-timing issue).
2D convention: the static camera looks head-on at the wall; the cat walks on the teacher's desk, which stands against the
wall (cat feet y≈741, desk rear edge y≈735, board bottom y≈737), so the cat moves at about the wall/board depth and moves parallel to it → one m/px scale.

## Cat speed (speed.py, scene/tracks/cat.csv, frames 1–49 – frame 0 has a ghost artefact)
Linear-fit slope of x(frame) for several reference points: torso_cx 8.918, cx_dark 8.999, cx_mask 8.988,
nose_x 8.898, torso_x0 8.931, torso_x1 8.905 px/frame (vertical ≈ 0). Mean ≈ 8.93 px/frame = 214.4 px/s.
Scale = 0.714 / 214.4 = 0.003330 m/px.

## Chalkboard (board.py, board2.py, frame 45 row/column profiles)
Outer wooden frame: x ≈ 322 → 1691 = 1369 px (green surface 342 → 1671 = 1329 px), matching scene record (1370 / 1328).
Length (whole object incl. frame) = 1369 × 0.003330 = 4.56 m. (Green surface only: 4.43 m.)

## Check
Different cat reference points give 212–216 px/s (±1 %) → 4.52–4.60 m. Sanity: a cat body (~146 px torso) → 0.49 m, realistic;
board 4.6 m × 1.47 m is a plausible classroom board.
Confidence: medium-high; main uncertainty is frame-vs-surface definition (~3 %) and slight depth offset of the cat in front of the wall (~1–2 %).
