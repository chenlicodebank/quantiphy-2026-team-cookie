# q1137 – height of the orange car (m)

Answer: **1.41 m** (world AABB height: tyre contact to the top of the roof/antenna).

Time base: question_fps = 30 (the file is 30.0055 fps; the difference is negligible). Frames are taken from the record's frame column.

## Scale (prior: a = -2.86 m/s^2)
- The record's wheel axle-midpoint track (ref_x, Hough wheel centres) was fitted with a quadratic over f10-53 (rms 1.5 px).
  This gives a = 0.5228 px/frame^2 = 470.5 px/s^2, so s_w = 0.006079 m/px **at the near-side wheel-face depth**.
  Frames 1-9 were dropped because they are derived from the front bumper, whose visible front face is distorted by perspective.
- Depth route (depth_info, orange car: 12.048 m at f0 and 10.432 m at f30). The car moves at a constant depth, so d0^2 - d1^2 = s^2 [(u0-cx)^2 - (u1-cx)^2].
  This gives s = 0.00624 for the origin at the axle midpoint and 0.00611 for the origin 20 px rearward (bbox centre; the rear overhang is longer than the front).
  This agrees with the acceleration route within 0.5-2.6 %.

## Corrections to the record
- The record gives y_top = 742, which is the **shark-fin antenna** (narrow orange blob, ~25 px wide). The roof silhouette (darker roof surface seen from above) begins at y ≈ 740-742.
- The record gives y_ground = 982, which is the **rim's** lower lip (Hough r ≈ 52 px is the rim, not the tyre). From the column profiles, the rim spans y 890-980 (centre ≈ 934.5).
  The tyre is dark down to y ≈ 1000, and the tyre's horizontal half-width is ≈ 64 px. Ground contact: y ≈ 999.5 ± 2.
- So the true pixel extent is ≈ 258 px, not 240.

## Perspective (the car is ~1 m thick in depth and the camera sits above the roof)
- The antenna is on the centreline (depth z), and the wheels are at the near face (depth z_w).
  Antenna x vs wheel x is linear with slope 0.898 (n = 30, rms 1.65 px). The ratio of the antenna's and the wheels' pixel accelerations is 0.885. So rho = z_w/z ≈ 0.89-0.90.
- The camera is level (verticals are vertical), with cy = 540. Camera height H = (999.5-540) s_w ≈ 2.79 m. The ground contact is at the wheel-face depth.
- Antenna top: h = H - (742.5-540) s_w/rho = **1.40-1.42 m**.
- Roof crown: the silhouette at y = 741 lies on the far roof edge (assumed ~0.4 m beyond the centreline, ~2.5 cm below the crown). With z ≈ 10.22 and f ≈ 1490-1510 (from d1), this gives h ≈ **1.38-1.41 m**.
- A naive single-scale estimate (258 px x s_w) would give 1.57 m. That overestimates because of the near tyres and the far roof edge.

## Checks
- f ≈ 1500 px. The lamp-post base (u 193, v 890, on the sidewalk) then gives a camera distance of 12.0-12.7 m for a curb height of 0.15-0.0 m (given: 12.325). This is consistent.
- The car is a Kia-Stinger-like fastback, whose real height is 1.40 m. This is a plausible sanity check.

Confidence: moderate-high. Error budget: about ±2 % from the scale, ±1 % from the ground row, ±1.5 % from rho and the roof model. Result: 1.41 ± 0.03 m.
