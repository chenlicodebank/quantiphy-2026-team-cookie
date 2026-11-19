# q_1756 – height of the moving bicycle (handlebar to ground)

Answer: **1.41 m**. The file fps and question_fps are both 33, so t=1 s is frame 33.

## Method (3D pinhole, scripts in this folder)
- **Camera pitch:** I fitted the kiosk's vertical edges (`kiosk_vp.py`). Their vanishing point is at about (1032, 6000), so f·cot(pitch) ≈ 5600-6100 and the pitch is about 11-14°.
  A second check: the walker's displacement between t=1 and t=2 (back-projected with depth_info) is level at a pitch of about 13.5° (`levelcheck.py`).
  The bike's level check gives about 22°, but it relies on the extrapolated pelvis pixel at t=2 (the bike is cut off there), so I did not use it.
- **Focal length (`solve.py`):** from the walker (H=1.8 m, pelvis at about 0.95 m) with head-top and foot pixels and depth_info at each time:
  t=1 (200 px, d=11.926) gives f≈1224, and t=2 (212 px, d=10.817) gives f≈1181 (pitch 12.5°). These differ by about 4%, so I used the mean, f≈1202.
- **Bike at t=1 (frame 33), mask = non-white pixels with x>1600 (`bikemask.py`):**
  - The front-wheel bottom is at v=559.5.
  - The handlebar centre/stem is at v≈433. The bar ends under the hands are at v≈426, but they are farther back (swept bar).
  - Model: wheel contact G on its pixel ray. The handlebar point is G + H·up − k·H·m, where m is the horizontal direction toward the camera and k is the handlebar's setback behind the front contact (0.2-0.45 × H).
  - The bike origin (≈ bike centre) is at depth 16.4919. I solved for H.
- **Result:** H = 1.37-1.46 across pitch 11-14°, f from t1/t2/mean, the handlebar point and k, and origin at the centre or at a ground root. The central value is 1.41.

## Checks
- An approximate formula gives H ≈ Δv·Z/(f(cosφ + k sinφ)) = 126.5·13.85/1202/1.029 = 1.42.
- Bike depths are consistent with the image: handlebar width 68 px → 96 px from t=1 to t=2 (×1.41), against a Z ratio of 1.39.
  The linear depth at frame 50 (14.14) predicts the handlebar–wheel pixel growth of ×1.17, which matches.
- The bike is clearly scaled up relative to the walker (rider + bike ≈ 2.5 m tall). It is not on the walker's ground plane, so only the camera (f, pitch) is shared between the two.
- Confidence: moderate, about ±4%. The main uncertainties are f (the walker's two times disagree by 4%) and the handlebar point/setback.
