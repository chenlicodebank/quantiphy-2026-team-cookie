# Q1443 – speed of the truck at t = 1.5 s (simulation_0188)

Prior: the truck's acceleration is 10.757 m/s² (uniform). Video is 30 fps, and question_fps is also 30, so t = 1.5 s is frame 45.

## Method (fit.py)
- I used the front-wheel-hub track from scene/tracks/truck.csv (frames 0–46, template-matched, ±1 px). The camera is static and level, with the horizon at y≈543 (see scene.json).
- I back-projected the hub onto its horizontal plane, in units of the camera height above the hub: X=(u−960)/(v−543), Z=f/(v−543). I then took the path length s(t) and fitted s = c0 + c1 t + c2 t².
- For any focal length from 800 to 3000 px the fit is quadratic to about 1e-4 relative RMS, the cubic term is about 0, and the start time is t0 = −c1/(2c2) = 0.000 s. So the truck starts from rest exactly at t=0 and accelerates uniformly. This matches the prior's uniform acceleration. Scaling the fit to a = 10.757 gives v(1.5) = 16.136 m/s for every f. The answer does not depend on the focal length or the depth_info.
- Benchmark convention: speed = one-frame backward difference at frame 45. For s = ½ a t² that is a·(45 − 0.5)/30 = 10.757 × 1.4833 = **15.96 m/s**. The instantaneous value is 16.14 m/s, about 1% higher.

## Second route
- The rear-hub track only covers frames 26–53, so its extrapolation to t0 is weaker. It gives t0 ≈ −0.03 to −0.08 s and v(1.5) ≈ 16.5–16.9 m/s. That is consistent within the extrapolation error.
- The pixel steps at the start of the front-hub track (0.5, 1.7, 2.6, 3.8 px/frame) also point to a start from rest at frame 0.
- I did not use the scene record's ground_centre proxy. It is not a clean ground-plane point: its fit gives a nonsensical t0 of −1 s.

## Confidence
High. The only open choice is backward-difference (15.96) versus instantaneous (16.14) speed, which differ by about 1%.
