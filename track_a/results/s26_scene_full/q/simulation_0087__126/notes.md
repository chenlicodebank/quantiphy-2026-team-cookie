# q_126: width of the car (m). Prior: car acceleration = 4.03 m/s^2

This is a 2D top-down scene with a static camera. fps = question_fps = 24, so no retiming question arises.
Scale comes from the car's pixel acceleration.

## Pixel acceleration (scripts: measure.py, fit.py, track_tm.py, mid.py)
- **Template matching** (track_tm.py): the front 130 px of the car, matched frame to frame with a sub-pixel peak.
  - Steps run from 1.05 px (f1→2) to 38.57 px (f52→53).
  - Frames 1-30: a uniform-acceleration-from-rest fit gives **0.700 px/frame²** (rms 0.07 px, very clean).
  - Frames 1-53: the quadratic fit gives 0.713. The mean change in step size, (38.57-1.81)/50, is 0.735.
  - Later frames show slightly more acceleration: the midpoint of the front and rear edges over f37-53 gives 0.77.
- **Integer front edge** (x0): the quadratic fit gives 0.71.
- **Camera check**: the cyclist's step is constant at 21.44 vs 21.51 px/frame in the two halves, so the camera is static and the later rise is real motion, not a camera effect.
- **Value used**: a_px = 0.72 px/frame² (range 0.70-0.735).
  - This is 0.72 × 576 = 414.7 px/s².
  - Scale = 4.03 / 414.7 = **0.00972 m/px**. The 0.70-0.735 range gives about ±3%.

## Width in pixels (scripts: width.py, prof.py, frame f53)
- **Wheel to wheel** (tyre outer edges, half-max on vertical profiles at x = 880 and x = 1250, f53):
  - y 579.4 to 791.2, about **212 px**.
  - The record's threshold mask gives 214 (579-792).
- **Including the side mirrors**: 250-251 px (y 563/564 to 813/814).

## Answer
- **Wheel to wheel** (the stated naming convention: a car's width runs wheel to wheel): 212.5 × 0.00972 = **2.07 m**. This is the answer.
- **Including mirrors**: 250 × 0.00972 = 2.43 m.

Sanity check: this matches a Cybertruck-like pickup (real width about 2.03-2.09 m, or 2.41 m with mirrors).

## Second route
Using the early-only acceleration (0.700) gives 2.12 m. The full-clip mean (0.735) gives 2.03 m. The answer of 2.07 is in the middle.

Confidence: moderate-high for the wheel-to-wheel reading (±3%). The main risk is whether the reference counted the mirrors (2.43 m).
