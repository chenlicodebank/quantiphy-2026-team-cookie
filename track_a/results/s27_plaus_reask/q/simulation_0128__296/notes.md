# q_296 — forklift length (m)

File fps 24 = question_fps 24. Prior: gravity 9.8 m/s^2 (red ball falls, frames 2-37, no impact). No depth_info.

## Prior route (2D convention)
- fit.py: quadratic fit of ball centre y (scene/tracks/red_ball.csv, frames >=1): a = 609.1 px/s^2 (rms 0.29 px;
  609.0-610.9 over different windows) -> 0.01609 m/px.
- Forklift length rear to fork tip 412.5 px (scene record, frame 0; 408-413 cross-check) -> 6.64 m; height
  241.5 px -> 3.89 m; front tyre 78 px -> 1.25 m. That is far too big for this forklift (a standard Toyota
  8-series seated counterbalance truck, about 3.5 m long, 2.1-2.2 m to the guard top): +85-90 pct, so it fails
  the plausibility check.
- Perspective doesn't fix it: the floor stripes meet at about (963, 521) (vp.py), so the camera is level with the
  horizon at about y 520-540. The ball ends in front of the floor (y 977, still falling), so it is at most about
  1.15x as far away as the forklift (tyre contact y 1055.5). That still means the forklift is at least 5.8 m long.
  A real-size forklift would put the ball behind the back wall. So the ball's pixel acceleration and a real-size
  forklift do not fit together in this scene, probably because the hall is a backdrop or the ball sits in a
  different plane. I could not reconcile them.

## Answer: scale from the standard object (forklift parts), as the instructions say to
Pixel sizes, with typical real values for a Toyota 8FGU25-class truck:
- guard height 241.5 px / 2.15 m -> 0.0089 m/px
- front tyre about 78 px / 0.68 m -> 0.0087
- rear tyre about 66 px / 0.54 m -> 0.0082
- wheelbase about 186 px / 1.60 m -> 0.0086
- forks about 118 px / 1.07 m -> 0.0091
- mean about 0.0087 m/px -> length 412.5 px x 0.0087 = 3.59 m

Cross-check: the image ratio length/wheelbase is 2.22, against 2.17 for the real truck (3.465/1.60), and the
catalogue overall length with forks is about 3.47 m. Answer: 3.55 m.

Under the other reading (one 2D scale from the gravity prior) the answer would be 6.64 m.
Confidence: moderate. It depends on whether the reference uses a real-size forklift.
