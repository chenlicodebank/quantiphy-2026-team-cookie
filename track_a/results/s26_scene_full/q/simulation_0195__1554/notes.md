# q1554: orbital diameter of the Callisto model (m)

The video file and question_fps are both 30 fps. Callisto is the small moon and Europa is the big central planet. Pixel centres come from the
scene record's circle fits (cx_circ/cy_circ): planet (941.26, 489.60) is static, moon at frame 0 (1127.7, 879.0) and frame 90 (t=3 s). Principal point
assumed at the image centre (959.5, 539.5).

Method (solve.py, refine.py): back-project the planet (16.549 m) and the moon at frame 0 (13.004 m) and frame 90 (13.856 m) for a trial focal
length f. Moon distances for the frames in between are linearly interpolated in time.
- Route A (speed prior): the mean 3D speed of the smoothed moon path over frames 0-90 = 0.627 m/s gives f = 2651 px, so R0 = 4.266 m and R3 = 4.273 m, diameter 8.54 m.
- Route B (circular orbit, no prior used): |P0-C| = |P3-C| gives f = 2668 px, so R = 4.257 m, diameter 8.51 m. The swept angle is 0.4416 rad, and the arc
  length 0.627 x 3 = 1.881 m gives diameter 2 x 1.881/0.4416 = 8.52 m.
- The two routes give focal lengths within 0.6 % of each other. The radius stays constant along the track (std 0.025 m), so the orbit is centred on the planet origin.

Answer: orbital diameter = 2R ≈ 8.52 m. Confidence: high (about ±2 %).
