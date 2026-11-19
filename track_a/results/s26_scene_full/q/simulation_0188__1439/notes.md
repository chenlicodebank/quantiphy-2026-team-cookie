# q 1439 – length of the truck (simulation_0188)

Prior: the truck's acceleration is 10.757 m/s² (constant). Depth_info gives 22.532 m at t=0.5 s (frame 15) and 19.525 m
at t=1.0 s (frame 30). question_fps = file fps = 30.

## Method
1. Metric scale from the acceleration (`multifit.py`). All 7 keypoint tracks from scene/ (front and rear hubs, rear
   top light, rear plate, yellow bumper pad, box logo, cab window corner) were fitted jointly as one rigid body
   moving along a 3D line: X_k(t) = O_k + s(t)·d, with s = v0·t + ½·10.757·t². The camera is a pinhole with the
   principal point at the centre and a fixed focal length f.
   Fit: rms 0.79 px, v0 = 0.03 m/s. Adding a jerk term gives jerk ≈ 0, so the acceleration really is constant,
   starting from rest. Because s is in metres, distances along d between points on the near side plane do not
   depend on f.
   (The scene/ single-hub fit has smooth 5 px residuals and a biased direction, so I did not use it: it gave
   wheelbase 4.283 m and side length 8.24 m.)
2. Focal length, from two routes:
   (a) The bottom edge of the grille is a horizontal line on the front face, which is perpendicular to d. Its slope
       at frames 38, 40, 41 and 43, set against the vanishing point of d, gives f = 2740, ~2750, 2706 and 2672
       (`grille.py`). The grille's top edge is curved or slanted, so I did not use it.
   (b) Take the origin as the bbox centre. f ≈ 2730–2745 reproduces both given distances, 22.53 and 19.53
       (`length2.py`, `centre_depth.py`).
   Result: f ≈ 2720 ± 100 px.
3. Ends of the truck at frame 40, along d (`padfront.py`, `laterals.py`):
   - Rear: the rear vertical edge of the box on the near side, at u = 298. Its ray meets the near side plane (the
     front-hub line, pushed out 0.1 m to the box side; the box keypoints sit at a lateral offset of +0.08 to
     +0.15 m) at s = −6.93 m relative to the front hub.
   - Front: the most forward part is the yellow bumper pad. Its keypoint is at s = +1.207 m (f = 2720; +1.27 at
     f = 2600, +1.14 at f = 2850). The pad's tip is 22 px further right, partly because the pad sticks out
     sideways. du/ds = 171 px/m and du/dlat = 67 px/m, so the pad's front face is about +0.08 m ahead of the
     keypoint.
   - L = 1.207 + 0.08 + 6.93 ≈ 8.21 m.

## Check by a second route
- Side length, independent of f: rear box edge to the near-side front corner of the cab (u ≈ 1395) is 7.98 m
  (side plane at 0.1 m) or 8.05 m (at 0.0 m). The pad sits about 0.15 m ahead of the cab corner, which gives about
  8.2 m. This agrees.
- Wheelbase from the joint fit: 4.31–4.32 m. Rear-light and plate keypoints: s = −6.75 and −6.34 m.

## Confidence
L = 8.21 m, ± about 0.12 m (1.5 %). The main error sources are f (±100 px moves the pad by ±0.06 m), the pad's
front edge (±0.05 m) and the offset of the side plane (±0.05 m).
