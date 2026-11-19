# q170 — length of the car (prior: car acceleration = 10 m/s^2)

2D simulation, 24 fps (file fps = question_fps, no re-timing). The car (silver Cybertruck-style pickup) drives left
from rest along a constant row (y 585-622), uniformly accelerating.

Method (measure.py): per frame, column profile of |frame - grey background| (max over RGB), with left and right
bumper edges located to sub-pixel at the 50 % crossing.
- Pixel acceleration: I fitted a quadratic x(t) to frames 2-40 (and also 3-40 and 4-40) for the centre, the left edge
  and the right edge separately: 200.5 px/s^2 (centre), 202.0 (left edge), 199.1 (right edge); fit rms 0.12 px.
  The prior gives 10 m/s^2 -> scale = 10 / 200.5 = 0.04988 m/px.
- Car length: 114.3 px in frames 0-3 (slow, no motion blur). Later frames grow to about 117 px from motion blur, so
  I did not use them. The scene record's inclusive bbox gives 113.5 px, which is 0.7 % different.
- Length = 114.3 x 0.04988 = 5.70 m.

Check: a left-edge-only or right-edge-only acceleration gives 5.66-5.74 m. A real Cybertruck is about 5.68 m long,
so the answer is plausible. Confidence: high (about ±2 %).
