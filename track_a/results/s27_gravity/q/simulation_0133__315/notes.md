# q_315: apple diameter (m). Prior: g = 9.8 m/s^2.

2D video at 30 fps; question_fps is also 30. I used the scene/ apple track, which the scene notes say was checked with overlays.

- **Scale (fit.py):** I fitted a parabola to the apple's vertical centroid in free fall, frames 36-47. The apple leaves the counter at frame about 34 and hits the floor at frame 48. The pixel acceleration is 6369 px/s² (rms residual 0.16 px). Other windows (35-47, 37-47, 36-46, 38-47) give 6361-6369. Fitting the top and bottom bbox edges gives 6340-6355. I used 6365 px/s², so the scale is 9.8/6365 = 1.540e-3 m/px.
- **Pixel diameter (size.py):** I used the unoccluded frames 0-25 and 36-47. The bbox width is 63.1 px, the height 62.4 px and the area-equivalent diameter 62.2 px, so I took about 62.5 px.
- **Diameter:** 62.5 × 1.540e-3 = 0.0962 m. The different routes give 0.0958-0.0972 m.
- **Check:** about 9.6 cm is a realistic apple size, which is consistent with a real-world-scale scene.

The apple is slightly closer to the camera on the floor than on the counter, but the size was measured in the same frames as the fall, so this does not matter.

Confidence: high (about ±2%).
