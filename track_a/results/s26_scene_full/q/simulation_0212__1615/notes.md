# q1615 — black cat to camera distance at t = 0.5 s (frame 12, question_fps = file fps = 24)

Given: d(t=0) = 4.199 m, d(t=1.0 s, frame 24) = 4.481 m, cat speed 0.94 m/s.

Route 1 (constant-velocity straight line, no focal length needed):
d(t)^2 = d0^2 + 2t(p0·v) + |v|^2 t^2. Fitting d(1) gives 2 p0·v = 1.564, so d(0.5) = sqrt(18.635) = **4.317 m**.

Route 2 (pinhole triangulation, solve.py): rays come from the cat's torso-core centroid in scene/tracks/cat.csv
(frames 0, 12, 24, all clean and unoccluded) with the principal point at the image centre. I solved for the focal
length f by requiring |P24 - P0| = 0.94 m, which gives f = 2156 px (HFOV 48°). I then intersected the frame-12 ray with
the line P0-P24. The frame-12 point sits at 0.512 of the way along that line and gives **4.320 m**. The image-x steps
vary by about ±20 % per frame (gait), but over 12 frames the cat covers about half the path, so the two routes agree.

Answer: 4.318 m. Confidence: high (the routes agree to 0.1 %, and the value lies between the two given depths).
