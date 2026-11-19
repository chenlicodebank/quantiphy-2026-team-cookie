# Q1347 — speed of the yellow car (taxi) at t = 2.5 s (frame 60 at 24 fps; file fps = question fps = 24)

Answer: **4.1 m/s**

## Camera (3D scene, static camera)
- Principal point assumed at the image centre (1080,540).
- Horizon: east–west road vanishing point from 7 Hough curb lines = (2703,-43) (`vp.py`). The roll is about 0, so the horizon is at y ≈ -43.
- Focal length from the tilt of 6 street-lamp poles, fitted to the vertical VP (`poles.py`): f = 1067, 1077, 1092, 1115, 1101, 1103 → **f ≈ 1095 px**.
  - Two independent checks agree: the orthogonal-roads VP pair gives 1080–1115 px, and the van's straight 3D track extends to the second road VP.
  - Pedestrian height comes out at 1.82–1.90 m and cyclist+bike at 1.72 m with f = 1100, which is plausible.
- Camera height above the road from the given depths with f = 1100: 6.95–7.3 m. This is consistent across the taxi, van, pedestrian and bike.
- The van-acceleration prior is roughly consistent: the plane-reconstructed van centroid gives a = 4.1–4.4 m/s² at f = 1100. That is 4.1–4.3 if the van origin is at road level, and 4.4 if it is at the centroid. The residual is attributed to the silhouette centroid sliding down the van as it recedes, which is not a fixed physical point. Fitting f to make a = 4 exactly would need f ≈ 1250–1300, which contradicts all the geometric evidence.

## Taxi tracking
- The scene/ taxi track was checked. Its occluded/van-overlap frames are biased, and its colour mask misses the pale taxi. I re-segmented with background subtraction (`seg_taxi2.py`, `taxi_mask.csv`) and inspected overlays at frames 14, 38 and 60.
- The taxi turns continuously (ground heading changes ~1.2°/frame through frames 14–66), so silhouette centroid, bbox centre and bottom point give inconsistent late speeds:
  - f = 1100: 4.0 / 4.3 / 4.5 m/s respectively.
  - These points are not fixed physical points.
- Chosen reference: the **top of the roof sign** (topmost mask point), a fixed physical point near the car centre (`bottom.py` → `taxi_points.csv`, and the scene top_x/top_y).
- Ground-plane reconstruction of a point at height z under camera height Hc (`topcheck.py`):
  - The velocity at frame 59.5 comes from a quadratic fit over frames 50–66, i.e. the backward difference between frames 59 and 60.
  - Self-calibration: the ratio v(59.5) / (roof-sign chord frames 14→38) = 1.029. It is independent of Hc and z.
  - The origin chord 14→38 from the given depths (14.7874 m, 18.3786 m) is 3.958 m.
  - So v(2.5 s) = 1.029 × 3.958 = 4.07–4.12 m/s across the three top-point tracks.
  - This chord match implies Hc ≈ 7.0–7.1 m with z ≈ 1.6–1.75 m, consistent with the depth-derived camera height.

## Second-route checks
- Taxi centroid ground track at f = 1100, Hc = 7.1: about 4.15–4.19 m/s around frames 50–62.
- The average speed over frames 14→38 from the depths alone is about 4.0 m/s (chord 3.96 m plus a ~1% arc correction). The taxi appears to move at a nearly constant ~4.0–4.2 m/s.
- If f were about 1250, the result would be about 3.9 m/s.

## Confidence
About ±5%. The main residual uncertainties are the van-prior tension on f, and the roof sign being slightly off the origin while the taxi turns.
