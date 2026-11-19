# q1379 – distance between the two red blood cells at t = 1 s (frame 24)

File fps = question fps = 24, so frame 24 = 1 s.

## Method
- Tracks from scene/ (mask centroids). I checked frame 24 by eye: two cells at about (722,544) and (1174,551),
  with the same apparent width (246 px each), so they are at the same camera Z.
- Prior: the speed is 4.7833 m/s. depth_info gives the left cell at 17.9557 m (t=1) and 22.7150 m (t=2).
- Focal length is unknown. I back-projected the left cell at frames 24 and 48 using the given Euclidean depths
  (principal point 960,540) and solved for f so that the speed equals 4.7833 m/s:
  - Route A, two-point displacement 24→48: f = 2643 px
  - Route B, linear 3D trajectory fit over frames 2–71 (Z linear in time, anchored on the given depths): f = 2653 px
  - Route C, two-point displacement 12→60: f = 2653 px
  These give a horizontal FOV of about 39.8°, which matches Blender's default 50 mm lens on a 36 mm sensor (f = 2667 px).
- The prior has to belong to the left cell. With the same Z, the right cell's speed can never reach 4.7833 m/s
  for any f (its maximum is 4.76).
- The trajectory is linear, with residual about 0.002 m, so the speed is constant and the routes agree.

## Result
Distance at frame 24, with both cells at the same Z (≈17.9 m): 3.056 (A), 3.044 (B), 3.045 (C), and about 3.03
with f = 2667. Answer: **3.05 m**.

## Confidence
The answer is moderately sensitive because the lateral motion is a small part of the speed. Even so, three routes
and the default-camera check agree within about 1%. If the right cell were slightly farther away (its mask area is
2% smaller), the distance would rise by less than 1%.
