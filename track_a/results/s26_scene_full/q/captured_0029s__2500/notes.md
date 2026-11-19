# q2500: speed of the tennis ball at 1.0 s (cm/s)

- Lab video, 24 fps (file and question fps agree), 1280x720, f = 763 px, principal point (640, 360). t = 1.0 s is frame 24.
- depth_info: 0.901 m at frame 24 (the "s" is a typo for m), 1.144 m at frame 30 (the ball hits the whiteboard), 1.027 m at frame 38.
- I checked the ball track (scene/tracks/ball.csv, colour-mask centroid) on frame 24 with a zoomed crop. The ball is sharp, with a diameter of about 57 px.
- Depth check from size: 763·0.067/d gives 0.955 m, 1.198 m and 1.061 m against the given 0.901 m, 1.144 m and 1.027 m. That is a consistent 3–6 % over-estimate (the mask is slightly small or the halo is excluded), so the shape of the depth curve agrees with the given values.
- 3D centres: the ray through (u, v) times the distance. Speed comes from the frame-to-frame differences ×24, averaged over steps 22 to 26 (5 steps centred on frame 24, before the impact at frame 30):
  - A: size-based range scaled to 0.901 m at frame 24: 123.4 cm/s (forward step 126, backward step 121).
  - B: a linear fit of the size range over frames 22 to 29, scaled to the given value: 125.4 cm/s.
  - C: linear interpolation of the given depths between frames 24 and 30: 120.4 cm/s.
- The motion is mostly away from the camera: the range rate is about 100 cm/s and the lateral speed about 46 cm/s.
- Answer: **123 cm/s**. The routes agree within ±3 %, so confidence is moderate to high.
