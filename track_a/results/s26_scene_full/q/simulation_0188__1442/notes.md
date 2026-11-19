# q1442 – speed of the truck at t = 1 s (simulation_0188)

question_fps = file fps = 30, so t = 1 s is frame 30. Prior: acceleration = 10.757 m/s^2 (exact).

## Method (fit.py)
- The truck moves on a straight 3D line (scene record: every keypoint moves on a straight image line), so a tracked
  point's image x is a projective function of its distance along the path: x = xV + alpha / (s - beta).
- I fit s = (i - i0)^2, i.e. uniform acceleration from rest at frame i0, to the scene/ template-matching keypoint tracks:
  - front wheel hub, frames 0–46: i0 = -0.016, xV = -3149 (matches the record's vanishing point ≈ -3200), rms 0.057 px
  - cab window corner, frames 0–46: i0 = 0.001, rms 0.11 px
  - rear top light, frames 33–57: i0 = 0.44, rms 0.06 px (late frames only, so i0 is less well constrained)
  - rear hub, frames 26–53: i0 = -0.9, rms 0.14 px (same)
  The long tracks that start at frame 0 both give i0 = 0.0 within 0.02 frame. So the truck is at rest at frame 0 and
  accelerates uniformly for the whole clip. That matches the prior's constant acceleration.
- Speed by the benchmark convention (one-frame backward difference at frame 30):
  v = a * (2*30 - 1) / (2*30) = 10.757 * 59/60 = 10.577 m/s. (With i0 = -0.016 it is 10.580.)
- Read as the instantaneous speed, v = a*t = 10.757 m/s; the two readings are 1.7 % apart.

## Check
- The depth_info is consistent with this: from rest, the truck travels 0.5*a*(1^2 - 0.5^2) = 4.03 m between t = 0.5 s
  and t = 1 s, while its camera distance drops 22.53 → 19.53 m (3.0 m). The motion is oblique and approaching, as the
  record's growing apparent scale shows.
- Answer: 10.58 m/s. Confidence: high (within about 2 % under either convention).
