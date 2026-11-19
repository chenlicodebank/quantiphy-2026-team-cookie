# q_297 — height of the forklift (m); prior: gravity 9.8 m/s^2; no depth_info

The file and question_fps are both 24 fps. The scene record's frame column was used.

## Route 1: scale from the prior (ball plane)
- fit.py: quadratic fit of the red ball's centre y (scene/tracks/red_ball.csv, frames 2–37): a = 609.1 px/s^2
  (rms 0.29 px; frames 2–20 give 606.9, frames 19–37 give 610.5; frames from 3, 5 or 10 onward give 608.9–610.9).
- Scale = 9.8 / 609.1 = 0.01609 m/px in the ball's plane. Forklift tyre-bottom to overhead-guard height = 241.5 px
  (from the scene record; I checked it on a zoomed crop of frame 37) -> **3.89 m** if the forklift is in the ball's plane.
- Plausibility check fails. That scale makes this compact Toyota counterbalance forklift 3.89 m tall and 6.6 m long.
  It would also give forks about 1.9 m long (real: 1.07–1.2 m) and a front tyre 1.25 m across (real: about 0.67 m). That is
  about 80 % too big. The forklift is in the near foreground, and the ball falls in front of the back wall, farther away.
  There are no shadows, and the hall looks like a backdrop, so the floor cannot give the depth ratio. The vanishing point
  of the floor stripes (vp2.py) is roughly (960, 540–590), which suggests a level camera.

## Route 2: scale from the forklift itself (standard object, real-world size)
Following the guidance, I took the scale from the standard object, a real-size Toyota 8-series 2–2.5 t forklift.
- Wheelbase 186 px; real is about 1.6–1.65 m -> 0.0087 m/px -> height 2.1 m.
- Front tyre diameter 78 px; real 7.00-12 is about 0.67 m -> 0.0086 m/px -> 2.07 m. Rear tyre 66 px; 6.00-9 is about 0.54 m -> 1.98 m.
- Forks about 117 px; real 1.07–1.2 m -> 0.0091–0.0103 m/px -> 2.2–2.5 m.
- The real overhead-guard height of this class is about 2.1–2.2 m. The mast top is lower than the guard, so the
  bounding-box height is the guard height.
- These estimates agree with each other at about 2.1–2.2 m. Answer: **2.15 m**.

## Confidence
Medium. The main risk is that the reference instead uses one 2D scale from the ball, which would give 3.89 m. I
rejected that value because it makes the forklift implausible by about 80 %.
