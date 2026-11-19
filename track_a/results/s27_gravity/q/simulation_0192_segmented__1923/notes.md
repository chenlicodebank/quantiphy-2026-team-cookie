# q_1923 — speed of the box at t = 0.2 s (frame 24 at 120 fps)

2D clip: the box falls straight down onto a truck roof (contact at about frame 61). Prior: the box accelerates at 9.8 m/s² before 0.6 s.
File fps and question_fps are both 120.

## Method (fit.py)
- I used scene/tracks/box.csv `front_top_y`, a sub-pixel top edge of the box face. I checked that the column values are internally consistent: the face width stays constant, so the box falls at constant depth.
- The per-frame steps are irregular: some frames repeat (frame 24 is one of these, `stalled`) and the next step is about double. A one-frame raw difference is therefore not usable. Instead I fitted a parabola to y(t) over the fall.
- Fit over frames 5–60: a = 2050 px/s², release time ≈ frame 0.7, rms 2.5 px. Other windows (5–45, 10–60, 4–58, 15–55) give 2010–2056 px/s².
- Scale from the prior: 9.8 / 2050 = 0.00478 m/px.
- Sanity check: the box face is 280.8 px = 1.34 m wide and the truck body is 566 px = 2.7 m wide. Both are plausible, so the scene is at real scale.

## Speed at frame 24
- Backward difference of the fitted parabola between frames 23 and 24: 1.86 m/s. The other fit windows give 1.856–1.907.
- Constrained free-fall model (at rest, then released at t0): v(0.2 s) = 1.90; backward difference 1.86.
- Second route, raw chord slopes centred on frame 24 (±4, ±6, ±8 frames): 1.84, 1.84, 1.86 m/s.
- If the fall started exactly at t = 0, the backward difference would be 9.8 × 23.5 / 120 = 1.92.

Answer: **1.88 m/s**.

Confidence: fairly good (about ±3 %). One risk: if the reference used the raw stalled step at frame 24, its value would be near 0. I treat that as an artifact.
