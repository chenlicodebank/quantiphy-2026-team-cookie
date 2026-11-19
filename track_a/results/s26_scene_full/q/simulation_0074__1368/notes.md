# q1368 – width of the purple car (simulation_0074)

Answer: **1.78 m**. The purple car is parked and does not move. It is a Mercedes W123-style sedan, so the
question asks for the horizontal extent across its long axis.

## Camera calibration (3D scene, static camera; file fps = question fps = 24)
- I fitted the road/kerb boundaries from a colour mask of the sidewalk (kerbfit.py). Each line fits to about 0.5–0.9 px rms.
  The edges on opposite sides of the junction are collinear, which is consistent.
  - Vanishing point 1 is at (-1322, -267) and vanishing point 2 at (2683, -257), so the horizon is nearly level.
  - If the roads cross at 90° and the principal point is the image centre, f = 1791 px (horizontal FOV 62°)
    and the camera is pitched 24° down (cam.py).
- Independent check from the vertical vanishing point of 8 poles (poles.py): f ≈ 1795 from the three precise far lamp
  posts, and 1830–1870 when all poles are included. So f ≈ 1790–1850, and the roads really do cross at 90°.
- Camera height comes from depth_info (depth_hc.py, fscan2.py). Each origin is taken as the ground point under
  the vehicle centre (from the wheel contacts) plus 0.5 m of height:
  - van 9.48 / 9.62, bike 9.44 / 9.51, taxi 9.27, pedestrian 9.74.
  - I used Hc = 9.45 m.
- Check against the prior (van length 6 m): fitting a 3D box to the van silhouette at frames 14 and 38
  (vanfit.py, IoU 0.92–0.93) gives L = 6.43 and 6.07 m.
  - The box centre distances are 31.99 and 27.89 m, against the given depths of 31.28 and 27.72.
  - So the depth scale and the prior agree to within a few percent.
  - An earlier wheel-contact method gave L ≈ 5.0 m. That method is unreliable: the wheel-contact pixels are uncertain,
    and the wheelbase changed from 3.5 to 4.1 m between two plausible picks.

## Purple car (static; measured on a median background frame)
- Near-side wheel contacts are at (453, 365) and (556, 402.4).
  - The car's axis lies along road direction 1 (yaw 179.6°).
  - Wheelbase = 2.82–2.83 m.
- Bumper-to-bumper length = 4.59–4.66 m (points on the near body plane, taken as the tyre line + 0.15 m).
- Front-face method (front plane fixed by the near front corner, far silhouette extreme on that plane; this is
  insensitive to the 0.15 m offset, frontface.py):
  - bumper width 1.62–1.66 m
  - hood front edge 1.43 m
- The far hood edge at the measured hood-corner height (0.95 m) gives 1.54 m at the front and 1.675 m near the
  windshield, widening toward the cabin. These are lower bounds on the body width. Any method that uses the far
  silhouette depends strongly on the assumed height (±0.1 m per 0.05 m of height).
- Silhouette box fits (carfit.py, mask IoU 0.89–0.93):
  - single box: W = 1.76 (yaw drifts to 173°)
  - body + cabin model: W = 1.58 with a low body height (0.85)
  - The far lower body is hidden, so W trades off against height in these fits.
- Real-scale check: measured wheelbase 2.83 and length 4.66 against the W123's 2.795 and 4.725, so the model is at
  about 1.00× real scale. The W123's width/wheelbase and width/length ratios give 1.81 and 1.76 m.
- No side mirror is clearly visible on the near side. There may be a small one at the far A-pillar base. If the
  bounding box included a mirror, the width would be about 1.85–1.9.

## Result
- The body width comes out at 1.75–1.81 m: from the direct lower bounds (front face 1.63–1.66, shoulder ≥ 1.675),
  the single-box fit (1.76) and the proportion routes (1.76–1.81).
- Answer: 1.78 m.
- Confidence: moderate, about ±5%. The main risks are the near-body-side assumption, whether the bounding box
  includes mirrors, and about 2% scale uncertainty from f and Hc.
