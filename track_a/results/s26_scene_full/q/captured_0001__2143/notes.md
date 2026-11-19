# q_2143 – displacement of the ball, 0 s to 1.5 s (cm)

File fps = question_fps = 24, so t=0 -> frame 0 and t=1.5 s -> frame 36.
Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

Ball centre (mask centroid, HSV yellow, disp.py; agrees with scene/tracks/ball.csv to <0.5 px):
- frame 0: (664.2, 332.8), depth 1.1075 m (given)
- frame 36: (661.6, 424.1), depth 0.9120 m (given); checked on a zoomed grid frame (frames/f36.png)

Back-projection, then 3D distance between the two points:
- depth taken as range along the ray: 22.94 cm
- depth taken as z: 22.76 cm
- using the scene record's centroids: 22.90 / 22.72 cm
Answer: 22.8 cm (the mean of the two depth readings, which differ by <1%).

Cross-check: apparent diameter 45.2 px at frame 0 and 51.6 px at frame 36 (motion blur) would imply a
depth of ~0.97 m at frame 36, which gives 18.4 cm. That disagrees with the given 0.912 m. The given depth_info
is what the reference uses, so I kept it. The diameter-based depth is less reliable because of blur and
segmentation. The prior (acceleration 3.0 m/s^2 at 1.6 s) is not needed for this displacement.
Confidence: moderate to high, within about 5% if the reference uses the given depths.
