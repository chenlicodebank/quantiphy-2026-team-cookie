# Q2404: displacement of the ping pong ball, 0.6 s to 1.6 s (cm)

- Time base: question_fps = 24, which is the same as the file fps. So t = 0.6 s is frame 14 and t = 1.6 s is frame 38.
- Track: scene/tracks/ball.csv (cx, cy mask centroid). I checked it on zoomed crops of frames 14 and 38: the ball is at about (435, 394) and (408, 510).
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). depth_info is the Euclidean distance, so P = unit_ray x depth.
- The given depths are at frames 14, 19 and 29. Back-projected, the three points lie on a straight 3D line, within 4 mm (singular values 0.187 / 0.004). That fits a ball rolling straight across the table.
- No depth is given at 1.6 s. I intersected the image ray of frame 38 with that 3D line. The closest-approach gap is 4 mm, which confirms the geometry. Depth at frame 38 = 1.370 m.
- Displacement = |P38 - P14| = **44.4 cm**. Using the bbox-based centre (cx_box, cy_box) gives 44.3 cm.
- Second route: a quadratic fit of depth against frame, extrapolated to frame 38, gives depth 1.343 and displacement 46.6 cm. This is less reliable because it is extrapolation and there is a probable dropped frame at 36. The ray-line route uses the observed image position at frame 38.
- I did not use the apparent diameter (equiv_diam). The mask under-sizes the ball (diameter-based depth 1.80 m vs 1.751 m given at frame 14), and it is too noisy.
- Confidence: moderate-high, about ±5%.
