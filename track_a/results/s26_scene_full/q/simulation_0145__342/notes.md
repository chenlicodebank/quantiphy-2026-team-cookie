# Q342: rocket acceleration at t = 1 s (frame 24, 24 fps)

Time base: the file and the question are both 24 fps, so t = 1 s is frame 24, and the acceleration is
(v24 − v23) × fps (backward differences).

## Measurements (my own, pixels)
- `measure.py` and `subpix.py`: |frame − frame0| profiles along the recorded flight axis (straight line, 39° up-left),
  with sub-pixel 50%-of-plateau crossings at the nose (frames 4-22) and the tail (frames 13 and 15-24; tail 14 is an
  outlier and was dropped). They agree with scene/tracks/rocket.csv to about 1-2 px. Nose-to-tail length is 202-203 px.
- `xcorr.py`: per-frame shifts from aligning consecutive profiles (tail and nose windows), giving an independent
  speed estimate.
- Combined speeds (px/frame), `vfit.py`: f10 29.3, f12 37.9, f15 44.7, f17 50.4, f19 54.4, f20 56.1, f21 58.2,
  f22 60.5, f23 62.0, f24 60.8.
- **The acceleration is not constant; it falls with time.** A constant-acceleration (quadratic) fit has rms 3.1 px,
  against 1.3 px for a cubic or an ease-in/out smoothstep.
- Acceleration at frame 24 (v24 − v23 convention) from each route:
  - joint cubic fit of nose + tail positions: 1.45-1.64 px/frame²
  - Bezier smoothstep fit (start at about frame 1, duration about 66-75 frames): 1.45-1.64
  - quadratic speed fit from frame 8: 1.38; from frame 12: 1.25
  - late-window fits (frames 16/18-24): 0.6-1.9 (noisy)
- Adopted value: **1.42 px/frame² = 818 px/s²**, uncertain by about ±20%.

## Scale
The prior is rocket length = 2.9 m. Following the benchmark convention (size = world AABB extent), the rocket is
tilted 39°, so its AABB "length" is the horizontal extent. `aabb.py` measures this with the 50% mask on frames 15-21:
x-extent about 166 px (y about 139 px). That gives a scale of 2.9 / 166 = 0.01747 m/px.

If the reference instead used the length along the rocket's axis (about 203 px), the answer would be about 11.7 m/s².

## Answer
a = 818 × 0.01747 ≈ **14.3 m/s²**

Confidence: moderate. The two main uncertainties are the slope of the decreasing acceleration at the end of the
visible flight, and the AABB-versus-axis interpretation of "length".
