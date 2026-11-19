# q_3194 — displacement of the box between 2.20 s and 3.00 s

Time base: question_fps 30 and file fps 30.014 give the same frames: 66 and 90.

Scale (prior g = 9.8 m/s^2): the packet falls freely along image +x for frames 53-65 (the clip is rotated). A quadratic fit
to x(frame) (fit.py, scene/tracks/packet.csv) gives a = 10.9-11.4 px/frame^2. Centroid 53-65: 11.32 -> 10192 px/s^2;
bbox centre: 11.08 -> 9975 px/s^2. Scale = 9.8 / ~10100 = 0.00097 m/px (packet 100 px -> ~9.7 cm, which is plausible).

Positions (from the track, checked visually on frames/f66.png and f90.png):
- frame 66: centroid (1373.2, 645.2); by eye the box centre is ~(1373, 650), just after it bounces off the strip
- frame 90: centroid (1376.7, 971.9); by eye ~(1380, 968), at rest
Displacement: 326.7 px raw centroid, 326.0 px bbox centre, 332.4 px corrected for camera drift (~6 px drift). Used ~328 px.

Answer: 328 px x 0.00097 m/px ≈ 0.318 m. Second route: the bbox-centre scale (0.000982) x 326 px = 0.320 m. The
centroid scale x the drift-corrected distance = 0.320 m. These agree within about 1%. Confidence is moderate to good.
The main uncertainty is the fitted acceleration (about ±4%).
