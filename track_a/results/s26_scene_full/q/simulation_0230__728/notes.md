# Q728 — ceiling height of the room (prior: chalkboard length = 5 m)

Static camera looking straight at the back wall of a classroom: the ceiling grid lines converge symmetrically, and the
floor/wall and ceiling/wall junctions are horizontal. The chalkboard, the ceiling/wall line and the floor/wall line
all lie in the back-wall plane, so one metres-per-pixel scale applies. fps = question_fps = 24, but no timing is needed.

Measurements on frame 48 (grey, light blur). Scripts: `enh.py` (CLAHE view `frames/enh.png`), `prof.py`, `prof2.py`
(edge profiles).
- Chalkboard outer frame, horizontal: left edge x≈318–320, right edge x≈1693, so **1374 px**. This matches the
  record's 1372 px. The green surface alone is 342–1670, 1329 px.
- Ceiling/back-wall junction: y = 172.5. It is the same at x 400–600, 900–1100 and 1300–1500, so it is horizontal.
- Floor/back-wall junction: y = 951.5. It is the same at x 1660–1740 and 1820–1880.
- Wall height: **779 px**.

Scale: 5 m / 1374 px = 3.64 mm/px. Ceiling height = 779 × 5 / 1374 = **2.84 m**.

Check: the second route is the green surface only (1329 px), which would give 2.93 m (+3%). I used the whole object,
frame included, because a world bounding box contains the frame. The board stands a few cm proud of the wall, which
changes the scale by under 1%. 2.8–2.9 m is a realistic classroom ceiling.

Confidence: good (about ±4%). The main uncertainty is whether the "chalkboard" length includes the frame.
