# Q370: shark speed at t = 1 s (frame 24), prior: turtle acceleration = 2.639 m/s^2

2D scene, static camera, 24 fps (the file rate and question_fps agree). I used one metres-per-pixel scale, taken from the turtle's pixel acceleration.

## Measurements (fit.py on scene/tracks, check.py run independently)
- Turtle ref_x fits a quadratic (constant acceleration, starting from rest):
  - a = 0.94–0.97 px/frame² across fit windows: 0-48 gives 0.941, 0-38 gives 0.964, 12-37 gives 0.969.
  - My own high-pass template match (frames 14-35, template from frame 30) gives 1.00 px/frame², but its correlation scores were lower (0.37–1.00).
  - Adopted value: 0.96 px/frame².
- Scale = 2.639 / (0.96 × 24²) = 0.00477 m/px. Sanity check: shark length 911 px → 4.3 m; turtle about 320 px → 1.5 m. Both are plausible.
- Shark speed at frame 24 (backward difference of the quadratic fit):
  - record: 58.1 px/frame (fit windows 0-24, 10-40, 12-37);
  - my own template match: 59.2 px/frame from the fit, 58.8 px/frame from the raw step 23→24.
  - Adopted value: 58.5 px/frame.
- Speed v = 58.5 × 24 × 0.00477 = 6.70 m/s.

## Second route
I took the ratio of the two accelerations: shark 2.49 / turtle 0.96 px/frame², so the shark accelerates at 6.84 m/s². Starting from rest, its backward-difference speed at frame 24 is a × 23.5/24 = 6.70 m/s, which agrees with the first route.

## Confidence
Error is about ±4 %, set mostly by the turtle's pixel acceleration (0.95–1.00).
