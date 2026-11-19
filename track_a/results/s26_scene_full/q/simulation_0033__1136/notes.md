# q1136 – length of the orange car (m)

Answer: **5.07 m**. Prior: the orange car's acceleration is -2.86 m/s². The depth_info for the orange car is 12.048 m at t=0 and 10.432 m at t=1.
The file runs at 30.0055 fps; every time is converted with question_fps = 30 (t=1 is f30).

## Geometry
The camera is static and level. The car drives right to left at constant depth, parallel to the image plane, and keeps a constant apparent size.
The pixel scale is k = f/Z (px per m), and it depends on depth: points on the body nearer the camera move faster in pixels.

## Measurements (scripts in this folder)
- `track.py`: I tracked the car body from frame to frame by template shift (orange pixels, rows 750-900). The per-frame speed falls linearly, so the deceleration is constant.
  The fitted pixel acceleration of the average body surface is 460.7 px/s². The pairs occluded by the grey/green car (f26-33) are excluded. Output: `shifts.csv`.
- `bands.py`: the body bands move at different speeds at f30: roof 701, windows 709, door 723, sill 727 px/s. This is depth layering.
- `final.py`: Hough wheel centres (from the record) against the body track give wheel-hub plane = body track × 1.029. The hubs are about 3% nearer than the average body surface.
  - Pixel acceleration at the wheel plane = 474.2 px/s².
  - **k_wheel from the prior = 474.2/2.86 = 165.8 px/m**.
  - Wheelbase = 509.8 px, which is 3.075 m.
- The record's `ref_x` at f1 was wrong because the shift failed there. It is fixed by extrapolation in `final.py`.

## Second route: depth_info
The car moves along X at constant Y and Z, so d0² − d1² = X0² − X1² with X = (u_wheelplane − cx)/k, taking cx = 540.
- u(f0) = 1507.6 (extrapolated, off-screen) and u(f30) = 545.7.
- This gives k = 160.5 px/m with the origin at the axle midpoint.
- It gives k = 163.6 px/m with the origin at the bounding-box centre, about 19 px behind the axle midpoint.
- The prior gives 165.8 px/m, so the two routes agree within 1-3%. I used k_wheel ≈ 164.5 ± 1.5.

## Length
- `tips.py`: I tracked the 50%-blur crossings of the bumper silhouettes against the empty plate (frame 0).
  - Front tip: f8-28. Rear tip: f26 and f33-53.
  - At f26, the only fully visible unoccluded frame, the silhouette is 272.4 → 1039.6, so **L_px = 767.2**.
  - The record's 776-782 came from a threshold mask that includes motion blur.
- The overhangs measured from the wheel-plane axle change with position:
  - front: 404 → 364 px (f8 → f28)
  - rear: 401 → 429 px (f26 → f53)
- These changes mean the bumper silhouettes sit well behind the hub plane, close to the car's centre plane. With rounded bumpers seen at angles of 0-20°, the silhouette lies near the bumper's apex.
- So dividing L_px by k_wheel (4.63 m) underestimates the length.
- `final.py` / `planfit.py` fit a plan-view model with parabolic bumpers, using the full pinhole projection and the silhouette minimum or maximum over the width.
  - At k = 165.8 the fitted length is L = 5.035 m (range 5.032-5.037 over the assumed Zo of 10.05-10.2, hub offset 0.8-0.9 and half-width 0.9-1.0).
  - At k = 162 it is 5.153 m. At k = 159 it is 5.250 m.
  - Fit rms is 2-3.7 px.
- Check by a simpler route: silhouette tips on the centre plane give L = L_px × Zo/f = 767.2 / (165.8 × 9.25/10.1) ≈ 5.05 m.
- With k_wheel = 164.5, the answer is L ≈ 5.07 m.

## Sanity check
The car is a Kia Stinger look-alike: real length 4.83 m, wheelbase 2.905 m.
- The scene's wheelbase is 3.075-3.17 m, so the asset is about 1.06× real size. That scale gives a length of about 5.1 m, consistent with 5.07.

## Confidence
Moderate to good, about ±3%. The main uncertainties are:
- the k disagreement between the prior and depth routes (1-3%);
- the depth at which the bumper silhouettes sit.
