# Q1522 - speed of the car at t = 0.5 s (m/s)

Video: 3D Blender render, 24 fps (file fps = question_fps = 24, no re-timing). t = 0.5 s -> frame 12; speed =
|p(12) - p(11)| x 24. Static camera (scene record). One car (yellow RX-7), starts from rest at frame 0.

## Scale
- Prior: tyre diameter 0.764 m. depth_info: camera -> right-front tyre centre = 14.244 m at t = 0.
- The car's right-front wheel is the near-side front wheel (it is the image-left wheel at f0 with the car facing the
  camera; it stays the near front wheel as the car turns to show its right side). This is the wheel I tracked.
- Rim (white face) segmented per frame 0-20 (rim.py) and its vertical extent measured to sub-pixel with half-max
  edges on columns through the centre (rim2.py): 87.1 px (f0), 97.8 (f11), 99.7 (f12), 121.9 (f20). The vertical
  extent does not depend on yaw or steering.
- Tyre/rim ratio about 1.555 (tyre outer edge on enhanced crops: f0 about 761-897 px, f20 about 735-922 px), so the
  tyre is 135.5 px at f0. With the principal point at the image centre: sqrt(f^2 + du^2 + dv^2) = 135.5 x 14.244 / 0.764
  gives f = 2346 px (HFOV 44.5 deg). Check: the hub's height above the ground plane (camera pitched so the horizon
  is at y = 829) stays constant to +-4 mm over frames 0-20, which is consistent.
- Hub 3D position: z = f x 0.764 / (1.555 x rim_h), X = (u - cx) z / f, Y = (v - cy) z / f (traj.py). Distance at
  f0 is reproduced exactly (14.244 m).

## Speed (sfit.py)
- From f2 to f20 the path is straight (max deviation 0.07 m) with heading about 36 deg. The yaw rate at f12 is about
  0.07 rad/s, so the wheel moves like the car origin (the omega x r term is about 0.1 m/s and mostly perpendicular,
  under 0.5% effect).
- Path length s(i) fitted with polynomials (degree 2-4, several windows); backward difference 11->12 x 24:
  6.44 - 6.81 m/s, median about 6.6. Raw per-frame value 6.57. The result is insensitive to the tyre/rim ratio
  (6.56-6.63 for ratios 1.52-1.59), because the depth scale is pinned by depth_info.
- The car accelerates from rest (about 1.9 m/s at f2, 6.6 at f12, 8.7 at f20).

## Second route (ecc.py, ecc2.py)
- Affine ECC registration between frames gives a per-frame vertical scale (that is, the depth ratio).
  - Wheel region: agrees with the rim half-max ratios over f6-20 (for example 10->14: 1.090 vs 1.087).
  - Front fascia (bumper, plate and lamps, car pixels only): 11->12 scale 1.0176. Using it for depth gives
    6.25 m/s. The fascia agrees with the rim up to f12 but reads lower later, as its match quality degrades
    (cc down to 0.8).
- Rim ellipse aspect vs predicted view angle: the same trend, offset by about 2 deg (rim dish/thickness). Not decisive.
- Routes: rim 6.6, fascia 6.25. Answer 6.5 m/s, weighted toward the rim, which is the depth_info object and is
  confirmed by the wheel-region ECC.

Confidence: moderate-good, about +-5%.
