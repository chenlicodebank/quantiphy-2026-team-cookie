# q_1773 — average speed of the bicycle (m/s)

Prior: white car (= the white van) acceleration = 4 m/s^2. depth_info: van 23.5892 → 19.9903 m, bike 19.0650 → 14.6515 m, pedestrian 21.0610 → 21.3488 m (frames 14 and 38; t = 0.58/1.58 s at 24 fps; file fps = question fps = 24).

## Observations
- Camera static (scene record). Bike (cyclist) and van move on parallel straight lines. LK-tracked rigid van points (track_van.py) give a common
  vanishing point vp = (578, 54) px (vp.py; ±20 px). The cyclist's centroid and wheel-bottom tracks pass within 5–9 px of it.
- The bike moves at constant speed from frame ~1.1 onward (t0_check.py: 4.0 px/frame early on, frame 0→1 only 0.15 px). A 3D quadratic fit gives acc ≈ 0.05 m/s², i.e. effectively 0.
- The van is at rest at frames 0–1. It then follows s = 2(t − t0)² with t0 ≈ 0 (fit i0 ≈ −0.3…+0.3 frames).

## Focal length (the key unknown)
1. Van physics (solve_f.py, ratio.py): with a = 4 and t0 ≈ 0, Δs(14→38) = 4.33–4.38 m. Combined with the van depths and the vp angle, this gives f ≈ 735–800 px (≈900 if t0 = 1 frame).
2. Pedestrian (ped_f.py): the depth change 21.06 → 21.35 versus the image distance ratio to its own motion vp on the horizon (assumed level) gives f ≈ 790–805 px (range 700–870 for horizon slope ±0.02 and different fit windows).
3. Pedestrian head→feet tilt toward the vertical vp (ped_axis2.py) gives ≈ 900 px. This is a weaker cue: gait and lean bias it.
Adopted f = 780 ± 60 px.

## Bike speed
- The bike's origin moves along dm = −ray(vp). From |P14| = 19.065 and |P14 + Δs·dm| = 14.6515, with the origin pixel taken 0–35 px above the lowest wheel point, Δs over 1 s = 5.65–5.82 m at f = 780.
- Second route: the two-point 3D chord between back-projected points gives 5.69–5.75 m. The routes agree within 1%.
- Central value: v = 5.70 m/s at f = 780 (5.55 at f = 840, 5.87 at f = 720).
- Per-frame speeds over frames 1..71: the frame 0→1 step is ≈ 0, so the mean is ≈ 70/71 · v = 5.62. The answer, 5.64, sits between v and that mean.
- The centroid track of the scene record is unreliable for the bike (the rider's upper body is missing from the mask early on). Its image depth ratio of 1.272 disagrees with the depth_info ratio of 1.29; the wheel-bottom track (1.289) matches it.

Confidence: moderate. The main uncertainty is f, which gives about ±4%.
