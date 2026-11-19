# Q1286 – width of the turning yellow car (taxi)

The file and question are both 24 fps.

## Scale (3D pinhole, level camera, cy = 539.5)
- Prior: van acceleration is 4 m/s². The van moves parallel to the image plane. A quadratic fit to its track gives a = 307.2 px/s², stable across fit windows (van.py). That is 0.01302 m/px at the van's depth.
- Van depth: from the distances 30.065 m (f14) and 29.307 m (f38) and the pixel offsets, Z = 29.155 / 29.166, which agree. That gives f = 2240 px.
  - Depth-only route (no prior), using d1²−d2² = s²(r1²−r2²): s = 0.01293, so f = 2255. I use f = 2245 (HFOV ≈ 51°).
- Camera height from ground contacts (re-measured; the record's van ground_y = 615 is the shadow edge, and the real tyre contact is at 617.5):
  - van near tyres: h = 78 × (29.16 − 0.85) / 2245 = 0.983
  - cyclist tyre at y = 621, depth 26.98: h = 0.979
  - I use h = 0.981.
- Check against the given taxi distances: I rebuilt the taxi's 3D ground points from the tyre contacts at f14 and f38. They give a wheelbase of about 2.9 m in both frames and reproduce 24.86 / 21.72 m to within about 2%, depending on where the origin sits along the car.

## Width
At f62–f71 the taxi faces the camera head-on. Its right body edge sits on the optical axis and stays put, so its yaw is about 0. Measurements (edges.py, tyre.py; diff against the clean frame 0):

| frame | front tyre contact y | body silhouette x (px) | mirror tips x (px) |
|---|---|---|---|
| f71 | 697.0 | 784–1085 | 800–1091 |
| f62 | 681.8 | 828–1099 | 838–1103 |

- Front-axle depth = f·h/Δy: 13.98 m at f71 and 15.48 m at f62.
- **Body** (silhouette from the front fenders, about 0.5 m ahead of the axle): 1.811 m in both frames. The two frames agree only if the fender is about 0.5 m ahead of the axle, so the two-frame check fixes that offset.
- **Including the mirrors** (mirrors about 0.9 m behind the front axle, measured on the side view at f8): 1.932 m (f71) and 1.937 m (f62).

The world-AABB width of the mesh should include the mirrors (1.93 m). The body-only reading is 1.81 m. I answer **1.87 m**, which is within about 3.5% of both readings.

Confidence: moderate. The scale is good to about 2%. The main ambiguity is whether the mirrors count.
