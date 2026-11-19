# q1436 – speed of the gift box at t = 1.5 s (frame 36 at question_fps 24 = file fps)

Prior: slide acceleration 3.18 m/s^2. depth_info: |P| = 9.859 m at frame 0 and 9.741 m at frame 12.
Track: scene/tracks/gift_box.csv body_cx/body_cy (checked on the contact sheet; good). Principal point is assumed at the image centre.

## Method (fit3d.py, diag.py, scan.py, route2.py)
1. Focal length from the free fall (frames 0-8, starting at rest at t=0) with g = 9.81, back-projected from the depth at frame 0:
   f = 2132 px with pitch 0 (rms 0.13 px). Pitch check (post.py): the blue support post at x≈210-287 is vertical to within 1 px over 400 px rows,
   so |pitch| < ~1 deg. A pitch of 5 deg would give about a 12 px slant.
2. Slide: P12 = 9.741 m along ray 12. The slide line lies in the plane through the camera spanned by the track rays. Its in-plane angle phi was
   chosen so that the fitted constant acceleration of the 3D per-frame speeds = 3.18 (prior). Each frame's position is the ray ∩ line.
3. Speed(36) = |P36 - P35| x 24 = 4.814 m/s. The linear fit of speeds over frames 13-38 gives 4.814 at t = 1.5 s. The speeds are linear in t (rms 0.025 m/s).

## Second route (independent of the prior)
Choose the line so that it passes through the free-fall centre at landing (t ≈ 8.3–8.7 frames). This gives acc = 3.07–3.23 (consistent with the prior 3.18)
and v36 = 4.77–4.84. Landing gap of route 1 is only 0.036 m. The size growth z12/z38 = 1.136 is close to sqrt(area) growth of 1.118.

## Sensitivity
If the pitch is wrongly allowed to be free (19 deg, which contradicts the vertical post), v36 = 4.62. For pitch within ±5 deg, v36 = 4.80–4.81.

Answer: 4.81 m/s. Confidence: good (about ±3%).
