# q1847 – forklift length (m)

Prior: "gravity acc = 9.8 m/s^2"; no depth_info. 2D scene, 24 fps (file fps = question_fps), 40 frames.

## Method (measure.py -> track.csv)
- Mask = min RGB < 200 on the white background. The forklift moves horizontally (wheel bottoms at y = 927-929 throughout).
- Fitted x(t) = x0 + v0 t + a t^2/2 to frames >= 3/4/6 for three rigid-ish tracks:
  sub-pixel rear (counterweight) edge: a = 526-528 px/s^2; bbox left edge x0: 527.5-529.7; mask centroid: 529-532.
  Residual rms 0.5-1 px. The fitted start-of-motion time is 0.00 +/- 0.01 s, so this is uniform acceleration from rest at t = 0,
  which matches a prescribed acceleration equal to the prior. Take a = 527 px/s^2.
- Scale = 9.8 / 527 = 0.01860 m/px.
- Length = horizontal bbox extent, 257 px at frames 0-1 (at rest, sharp), 254-259 px over frames 0-20 (shrinks to 246 px by frame 39 as the mast/fork tips change).
- Length = 257 x 0.01860 = 4.78 m.

## Checks / caveats
- Second route: the mask-centroid track gives a = 530 px/s^2 -> 4.75 m; bbox median 255 px -> 4.74 m. The routes agree within 1 pct.
- Plausibility: at this scale the front wheel (67 px) is about 1.25 m across and the height is 3.6 m, which is about 1.4-1.9x a standard
  2.5 t counterbalance forklift (about 2.5 m long without forks). The scene's motion is a clean constant acceleration from rest
  at t = 0, which fits a 2D scene where the prior's acceleration was given to the forklift, so I used the prior scale.
  The alternative real-size reading (a typical forklift) would be about 2.5-3.0 m.
- Confidence: moderate. The measurement is solid (about 1 pct). The main risk is whether the reference uses this acceleration as the scale.
