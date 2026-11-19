# Q1547: turtle speed at t = 1 s (m/s)

Prior: the turtle's acceleration is 2.639 m/s^2, taken as uniform. question_fps = file fps = 24, so t = 1 s is frame 24.
Depth_info for the turtle: 15.232 m at t = 0 and 14.968 m at t = 0.5 s.

## Method (fit3d.py)
- Track: the core centroid of the turtle from scene/tracks/turtle.csv, frames 0–40. I checked the turtle in frames 0, 20 and 40 and on a contact sheet. The record covers the right object.
- 3D model: P(t) = P0 + d·(v0·t + ½·a·t²), straight-line motion with a fixed at the prior. P0 is the back-projection of pixel (u0, v0) at depth 15.232 m. The model is projected with a pinhole camera.
- Free parameters: focal length f, initial speed v0, direction d, and a small pixel offset between the origin and the centroid. The fit also forces |P(0.5)| = 14.968 m.
- Best fit: v0 = −0.03 m/s, f ≈ 2700 px, rms 6.7 px, which is about the noise of the core centroid.
- v0 profile, with the other parameters refit for each value: the cost is 1890 at v0 = 0, 4690 at 0.25, 9843 at 0.5 and 24530 at 1.0. The turtle starts from rest (v0 ≈ 0).
- Second check, pixel motion alone: about 25 px by frame 12, 158 px by frame 24 and 455 px by frame 40. This matches s ∝ t², so the turtle starts from rest.

## Answer
The benchmark defines speed as the one-frame backward difference at frame 24. With v0 = 0 that is
v = ½·a·(1 − (23/24)²)·24 = a·47/48 = 2.639 × 0.979 = **2.584 m/s**.
The instantaneous speed would be a·t = 2.639 m/s, about 2% higher.

Confidence: good. The answer depends mainly on v0 ≈ 0, and the fit supports that strongly.
