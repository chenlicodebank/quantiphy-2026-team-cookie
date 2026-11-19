# q1293 — speed of the yellow car (taxi) at t = 2.5 s (frame 60 at 24 fps; the file is also 24 fps)

**Answer: 3.95 m/s**

## Method (3D, ground-plane pinhole)
- Camera is static. The principal point is assumed to be at the image centre (1080, 540). Horizon v_h = 531, from two identical lamp posts
  (A: top 343 / foot 837; right: top 401 / foot 742 → v_h 530.3), the man's feet-vs-height fit (532.3) and the van
  roof (~526, approximately at camera height). The camera is pitched down slightly.
- Ground point at pixel (u,v): Z ≈ K/(v − v_h), with K = f·Hc (geom.py does the exact back-projection, including pitch).
- **K from the taxi's own given distances** (calib_K.py): I refined the tyre-contact edges in code (refine_pts.py):
  f14: near-side wheels (285,737.5), (585,730.2). The taxi origin is placed at the centre of the near pair plus half the track (1.6 m) toward the far side.
  f38: all four contacts (597,736.5) (810,756) (725,725.6) (930,741.5), and the origin is their centroid.
  Origin height is taken as 0.5 m; this changes the distance by about 0.1%. Results: K = 4728 (f38) and 4688 (f14) at f = 2300, so they agree within 1%.
- **Focal length** (affects only the lateral part of the speed): the taxi's near-side wheelbase measures the same at f14, f38 and f60
  for f ≈ 2200–2500 (2.90/3.09/2.97 m at f=2300; 2.93 m at f=2500). Sanity checks: Hc = 2.05 m ≈ van roof height, and the man comes out at about 1.65–1.77 m.
  The van check is rough: its rear-edge pixel speed with this scale gives an acceleration of about 3–5 m/s², consistent with the prior of 4 m/s².
  The van turns away and its bottom is mostly estimated in the record, so this check was not refined.
- **Taxi track** (track_wheel.py → wheels.json): template-matched the near-front and near-rear tyres over f40–71
  (scores 0.97–1.0 near f60). The tyre-bottom edge is found in code, then back-projected to the ground. Speed is the one-frame backward difference of the
  mid-point of the two near-side contacts, after a local polynomial fit over ±5–8 frames (speed.py). Heading changes by only about 0.2°/frame near f60,
  so wheel-point velocity ≈ origin velocity.

## Results (speed at f60, m/s)
| f | 1900 | 2100 | 2300 | 2500 | 2800 |
|---|---|---|---|---|---|
| mid, ±6 deg2 | 4.08 | 4.00 | 3.94 | 3.89 | 3.84 |
Front wheel alone gives 3.97 and rear wheel alone 3.92 (f=2300). Raw per-frame speeds at f58–62 are 4.07, 4.16, 4.07, 3.90, 3.75.

## Second route
Average speed from the two given-distance positions (f14 → f38, origins as above): net 3.85 m/s, a lower bound because the path curves.
Early lateral pixel speed (~15.5 px/frame at Z ≈ 24 m) gives ≈ 3.9 m/s. The taxi's speed looks nearly constant (3.5–4.1 m/s from f46 to f66;
the dip near f46 is during the turn). These agree with 3.9–4.0.

## Notes on the scene record
The taxi bbox bottom includes a growing contact shadow late in the clip, so I used tyre-edge tracking instead. The record's horizon (532) agrees with the lamp posts.
A first attempt that took f from the ratio of the given distances is too weakly conditioned to use: d ≈ Z for a narrow FOV, about 50°.

Confidence: moderate-high, about ±5% (from the horizon, K, and f in the 2100–2500 range).
