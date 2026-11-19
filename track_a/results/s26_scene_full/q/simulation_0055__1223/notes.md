# q1223 – height of the orange car (simulation_0055, 3D, 30 fps file = question fps)

Answer: **1.25 m** (world AABB height, wheels to roof crest).

## Geometry (pinhole, cx = cy = 540, level camera)
- Man (constant depth, walks parallel to the image): depths 8.313 m at frame 0 and 8.189 m at frame 30, pelvis u = 1071 / 981
  -> d0^2 - d1^2 = k_m^2[(u0-cx)^2 - (u1-cx)^2] -> k_m = 0.004836 m/px; Z_m = 7.84 m; **f = 1622 px**.
- Second route for f: the car's late-segment deceleration (rear edge clean, frames 49-77, quadratic fit rms 0.15 px)
  is 438 px/s^2; with the prior 2.86 m/s^2 -> 0.00653 m/px at the car; with the car depth at t=1 (11.671 m) -> f = 1645 px.
  (Frames 28-50 give a smaller pixel deceleration, ~0.36 px/fr^2, so the motion is not exactly uniform in pixels; the
  late segment agrees with the man route.)
- Car centre depth Zc = 10.74 m (t=1 depth, u = -83, root at ground). Check: car length 739.7 px x Zc/f = 4.90 m
  (the model is a Kia Stinger, real 4.83 m), wheelbase ~480 px -> 2.94 m (real 2.905 m), so the scale is consistent.
- Camera height: man's feet (y~945) 1.97 m, hydrant base (y 896, hydrant depth 9.207) 1.94 m, car near-tyre contact
  (y 859, depth Zc - 0.92) 1.93 m -> hcam ~1.95 m. The camera is above the roof: a ~12 px strip of the roof surface is
  visible (y 644-656), as expected for a 0.7 m height difference.

## Height
Roof-crest silhouette at y = 644-647 (fine crops of frames 50 and 77, plus a mask; 645.5 used). The car's image extent
(859 - 645.5 = 213 px) is inflated by perspective because the bottom of the near tyre is ~0.9 m nearer than the crest.
H = hcam - (y_top - cy) x Zc / f = 1.95 - 105.5 x 10.74/1622 = **1.25 m** (accel-route scale: 1.26 m).
Horizon-free check (horizon fitted from the man's feet and the car's tyre contact, y_h = 526): H = 1.23 m.
The naive pixel height x scale (no perspective) would give 1.41 m. That is wrong for this camera, even though it happens to match
a real Stinger's 1.40 m.

Sensitivity: pelvis x ±3 px -> ±0.025 m; roof row ±2 px -> ±0.013 m. Confidence: moderate-good (likely within ~5 %).
The scene record's car height_px of 219 (rows 647-865) caps the bottom at the mask limit y=865. The real tyre bottom is at ~859.
