# q_1468 — acceleration of the car at 2.0 s (simulation_0301)

Question fps = file fps = 24, so t=1.0 s is frame 24 and t=2.0 s is frame 48. The camera is static and the scene is 3D.
Prior: forklift acceleration = 2 m/s². Depths: forklift 16.7953 m (t=1) and 19.0980 m (t=2); car 17.8278 m (t=1) and 23.1989 m (t=2).

## Method (fit2.py, fit3.py)
- Image positions come from the scene/ tracks (amodal box centre; the bottom-centre was used as an alternative). I spot-checked the
  frames on a contact sheet: both vehicles start from rest at about frame 1 and drive away to the upper left in straight lines.
- Pinhole model with principal point (1280, 720) and an unknown focal length f. For a given f, the 3D points at t=1 and t=2 are the depth
  times the unit ray. Each vehicle moves along the straight 3D line through those two points. For every frame, the position
  along that line is found by intersecting the frame's ray with the line, which gives s(frame) in metres.
- f is set so that a quadratic fit to the forklift's s(t) gives a = 2 m/s². Depending on the fit window and the reference point,
  f comes out at 3300 to 3800 px (about 3500). The forklift fits a constant-acceleration curve from rest with t0 of about 0.0 to 0.08 s.
- Car at f≈3500: the per-frame speed rises roughly linearly (5.0 m/s at t=1, 7.3 m/s at t=1.5, 10.2 m/s at t=2), so the
  acceleration is roughly constant.

## Results
- Route 1 (endpoint and depth anchored, assuming both vehicles start from rest at the same t0): a_car = 2·L_car/((2−t0)²−(1−t0)²).
  This gives 4.97 to 5.06 m/s². The result barely depends on f, because a_car ≈ 2·L_car/L_forklift.
- Route 2 (quadratic fits of the car's s(t)): 4.85 to 5.4 m/s² depending on the window. Windows centred on 2.0 s give 5.1 to 5.4, but the car is
  partly hidden there (centre accurate to about ±5-10 px). Windows 21-48 give 4.7 to 5.1.
- Speed over time: v(2.0)/(2.0−t0) ≈ 5.15 and v(1.0)/(1−t0) ≈ 5.08.

Answer: **5.0 m/s²**. Confidence is moderate to good; the likely error is about ±5-8%.

Note: the apparent-size ratios (forklift box width 644→522 px, car 795→519 px) shrink faster than the depth ratios. This is
consistent with the view angle changing as the vehicles move away. Sizes were therefore not used for the scale.
