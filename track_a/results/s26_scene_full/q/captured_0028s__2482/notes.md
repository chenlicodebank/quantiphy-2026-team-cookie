# q2482 — acceleration of ping pong ball at t = 1.0 s (cm/s^2)

File fps = question fps = 24, so t = 1.0 s is frame 24. The ball is let go at about f21 and bounces at f26, so f22–25 are
free fall (f24 is in the middle of that window).
Track: scene/tracks/ball.csv mask centroids (the record's masks were checked visually). Pixel y for f22–25 is
298.67, 313.93, 337.57, 371.17. Second differences are 8.38 and 9.96 px/frame², and a 4-point quadratic gives
9.17 px/frame².

Depth: depth_info gives 1.805 m at f24, 1.557 m at f26 (t=1.1) and 1.4115 m at f31. The ball moves toward the
camera, and the size check agrees: apparent width goes from 18.3 px at f21 to about 20.5 px at f22–25 and 23 px at f31.
Back-projecting from the width (Z = 1.4115·23/18.3) gives about 1.77 m at release, so depth falls by about
0.045 m/frame. Using a constant depth would overstate the vertical acceleration because the approach term 2·v'·Z'/f
is left out.

Method (accel2.py): back-project with f = 763 px and principal point (640,360). Depth is linear in frame, from
Z(f21) ≈ 1.77–1.805 m to Z(f26) = 1.557 m. Fit a quadratic over f22–25 to get the 3D acceleration:
|a| = 986–998 cm/s² (vertical 982–994). Three-point second difference at f24: 1041–1058 cm/s².
Second route: the scale from the 40 mm diameter (0.04/20.5 m/px) with a perspective correction gives 9.17·576·0.00195 ≈ 1030 without a perspective term, and about 930 with the roughly 10%
approach correction.
Constant depth with no approach term would give 1250–1360 (rejected). Free fall predicts 981.
Answer: 985 cm/s². Confidence: moderate; the answer is consistent with g.
