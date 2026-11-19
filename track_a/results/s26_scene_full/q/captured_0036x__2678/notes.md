# q_2678 — ping pong ball displacement 0.9 s -> 1.4 s (cm)

File fps = question_fps = 24. t=0.9 s -> frame 22, t=1.4 s -> frame 34.
Lab camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

Ball centres (scene/tracks/ball.csv, checked on zoomed crops frames/f22.png, frames/f34.png):
- frame 22: (569.6, 453.2), depth 1.010 m -> 3D (-0.093, 0.123, 1.010) m
- frame 34: (836.5, 513.2), depth 0.716 m -> 3D (0.184, 0.144, 0.716) m
Displacement = 40.49 cm (measure.py).

Second route: 3-frame-averaged centres (21-23, 33-35) -> 40.54 cm. Depth change (29.4 cm) dominates,
so pixel errors of a few px change the answer by < 0.5 cm.
Size sanity: 4 cm ball predicted 30.2 px at 1.01 m (measured ~28 px across motion) and 42.6 px at
0.716 m (mask 56 px, inflated by motion blur / segmentation halo in frame 34) — consistent with depths.

Answer: 40.5 cm. Confidence: high (dominated by given depths).
