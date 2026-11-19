# q1134 – height of the person (simulation_0033)

Video file fps 30.005, question_fps 30 (used for all frame/time conversions; t=1 s -> frame 30).
Static, level camera, 1080x1080, principal point assumed (540,540).

## Focal length (car: depth_info + prior)
- carfit.py: near-side wheel centres (Hough, f10-53, wheelbase 509 px) -> axle-mid quadratic fit:
  u(0)=1506.0, u(30)=546.6 (959.4 px moved), a_px = 469.9 px/s^2 (bootstrap sd 3.5), rms 1.5 px.
- Car moves laterally at constant depth: d0^2 - d1^2 = X0^2 - X1^2 -> X0 = 6.027 m, X1 = 0.041 m
  -> Z_near/f = 0.006240 (f/Z_near = 160.3).
- Prior check: 469.9 px/s^2 x 0.006240 = 2.93 m/s^2 vs prior 2.86 (2.5 % off) -> consistent.
  Prior alone gives f/Z_near = 164.3; used 162.3.
- Z_c = sqrt(d1^2 - X1^2 - Y^2) = 10.06-10.22 m (Y = camera height above car origin, 2.1-2.8 m);
  the wheel plane is ~0.9 m nearer than the car origin -> Z_near ~ 9.24 m -> f ~ 1500 px (range 1478-1529).
- Independent check: lamp-post and hydrant bases on the ground plane (camera height 2.74-2.77 m from the
  tyre contact row 982) plus their given distances -> f = 1493-1495 px. Agrees.

## Pedestrian
- Depth (pelvis, u=135.5, v~765 at t=0): Z/f = 13.78 / sqrt(f^2 + 404.5^2 + 225^2) = 0.008778 m/px at f=1500
  (t=1: 13.651 at u=185.5 gives Z=13.18 vs 13.21 at t=0 -> consistent, walks parallel to the image).
- Pixel height: head top 650 (highest during gait, f14-18), shoe sole 866-867 (f18, zoomed crop; the darker
  patch below is the wet-ground reflection) -> 217 px walking max; rest height ~218 px (record: 215-221).
- Height = 218 x 0.008778 = 1.91 m (217 -> 1.905, 219 -> 1.92; f 1478-1529 -> 1.88-1.94).

## Second-route / discrepancy
- Using f from lamp/hydrant (1493): 1.92 m.
- A ground-plane route (camera height 2.74 m / (feet row 866 - 540)) would place the feet at Z~12.6 m and give
  ~1.82 m; it disagrees with the given human distance (Z 13.2 m). The lamp/hydrant vs pedestrian row ratio is
  inconsistent with their given distances for any f, so a static-object origin (or ground level) assumption is off;
  the question's own exact human depth was trusted.

Answer: 1.91 m. Confidence moderate (±4 % from f, ±2 % pixel height; ground-route disagreement noted).
