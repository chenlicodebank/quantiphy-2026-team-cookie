# Q364 — turtle length (m); prior: turtle acceleration = 2.639 m/s^2

2D scene (turtle swims right->left parallel to image plane), fps = question_fps = 24, static camera.

## Pixel acceleration (scale)
- Own tracking (`track_turtle.py`): high-pass/contrast-normalised carapace templates from frame 40 (frames 26-47)
  and frame 30 (frames 21-30), sub-pixel NCC peaks. Agrees with scene/ record within 0.5 px for frames 26-47
  (record is ~3-5 px off in 21-25). Early frames 0-20 taken from the record (head/front-shell templates).
- Template scale search (`scale_check.py`): best scale 1.00±0.01 at frames 24-47 -> no depth change, one scale is valid.
- Quadratic fits (`fit.py`): whole clip 0-47 a = 0.935 px/frame^2 with v0 = -0.08 px/frame (i.e. starts from rest,
  as expected for a generated constant-acceleration motion); 5-47: 0.926; 10-47: 0.913; 30-47: 0.886; 38-47: 0.884.
  Residuals show a ±2-3 px swim-cycle oscillation of the carapace relative to the origin, which biases short windows;
  the full-clip fit (averaging over the cycle, from-rest consistency) is used: a = 0.93 px/frame^2 = 536 px/s^2.
- Scale = 2.639 / 536 = 0.00492 m/px.

## Turtle length in pixels
- Whole-animal horizontal extent (head front to rear flipper/carapace tip), mask bbox width over fully visible frames
  22-47: 290-343 px, median ~317 px (flippers trailing in 38-47: 304-320). Checked on overlay crops (frames/crops.png).
- Carapace only ~260 px (not used; AABB covers the whole mesh).

## Answer
317 px x 0.00492 m/px = 1.56 m  -> 1.555 m.
Second route: late-window acceleration 0.884 px/frame^2 would give 1.64 m; 320 px median-of-trailing gives 1.57 m.
Confidence: moderate (~±6 %): dominated by which pose the reference AABB used and the swim-cycle bias of acceleration.
