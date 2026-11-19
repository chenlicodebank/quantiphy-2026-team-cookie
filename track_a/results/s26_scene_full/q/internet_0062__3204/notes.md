# q_3204 – distance from the wallet's bottom corner to the floor at t = 2.50 s

Time base: file fps = question_fps = 30, so t = 2.50 s is frame 75.
The video is rotated 90 deg: gravity points to image +x. Wall on the left, black baseboard x 1438-1581,
wood floor from x ≈ 1582. Camera is static during the fall (scene record, < 0.5 px).

Scale (prior g = 9.8 m/s^2): quadratic fit of the pouch centroid x over free-fall frames 67-80 gives
a = 10589 px/s^2 (sub-windows 10506-10627; mean second difference ≈ 11.8 px/frame^2).
That gives 9.8 / 10589 = 9.255e-4 m/px.

Bottom (leading, max-x) corner at frame 75: bbox x1 = 756. The centroid plus the corner offset measured
while the pouch is held still (126.3 px) gives 755.2, so the corner is at ≈ 755.5 px.
Floor line: a column brightness/saturation profile on frame 75 shows the wood floor starts at x ≈ 1582
(V jumps from <35 to 109 at 1580-1584). On frame 81 the pouch's leading corner reaches about x ≈ 1590-1600,
which fits the floor being there (it lands just in front of the wall).

Distance = (1582 - 755.5) px = 826.5 px -> 826.5 x 9.255e-4 = 0.765 m.

Second check: the per-frame second-difference scale (11.8 px/frame^2 -> 9.23e-4 m/px) gives 0.763 m.
Alternative reading: if "floor" meant the top of the black baseboard (x 1438), the answer would be
683 px -> 0.632 m. I rejected this because the baseboard is part of the wall and the pouch comes to rest on the wood.
Sanity check: the pouch's long side is 246 px -> 0.23 m, a plausible size for a wallet or clutch.
Confidence: moderate-high. The main uncertainty is where exactly the annotators placed the floor line (±15 px, about 2%).
