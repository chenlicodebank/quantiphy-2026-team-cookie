# q2291 – soccer ball velocity at t = 1.5 s (captured_0016x)

File fps = question_fps = 24, so t = 1.5 s is frame 36. The ball is in free flight from frame 32 to 40 (thrown, then caught at 41).
Lab camera: f = 0.5959 x 1280 = 762.8 px, cx, cy = (640, 360). depth_info: the ball is 1.402 m from the camera at frame 36.

## Measurements (measure.py -> meas.npy)
- Ball mask = low-saturation or dark pixels that aren't green, x 480-1000, y < 400; I used the largest component.
  Centroids match scene/tracks/ball.csv to within 0.3 px, so the record is right for these frames.
- Frames 32-36 are motion-blurred, so I used the blob centroid there. Frames 37-40 are sharp.
- Diameter: the blob width across the blur direction (frames 32-36) and the circle-fit diameters from the record
  (frames 37-40: 94.0, 93.8, 90.4 and 86.8 px). At frame 36 the diameter is about 92-95 px, which gives a ball
  diameter of about 0.17-0.18 m.
- Image steps per frame (px): 32->33: 79, 33->34: 64, 34->35: 59, 35->36: 89, 36->37: 34, 37->38: 28, 38->39: 23,
  39->40: 22. Frame 36 sits about 20 px ahead of a smooth path, which looks like frame-timing jitter. Smoothing
  over 5 frames averages it out.

## Route B, reference-like (routeB.py, velocity.py)
3D centre = ((u-cx)/f, (v-cy)/f, 1) x Z. Z per frame comes from 1/diameter, fitted against frame with a linear or
quadratic fit and scaled so that Z(36) = 1.402. This gives Z rising from about 1.31-1.36 m at frame 32 to about
1.50-1.55 m at frame 40, so vZ(36) is about 0.58 m/s.
- 5-frame smoothed forward difference at frame 36: 2.22-2.30 m/s
- Central difference between frames 34 and 38: 2.49-2.52 m/s
- Quadratic fit of the 3D positions over 32-40: 2.31-2.38 m/s

## Route A, constant-acceleration fits to the image track plus size (freeg.py, ballistic.py, ballistic2.py)
- With the acceleration free: |V| = 2.38-2.68 m/s, with vZ about 0.6 m/s. This agrees with the size-based depth.
- With gravity fixed at 9.8 m/s² (the prior): the camera is pitched about 45-50° down. The fit finds this pitch,
  and the catcher's feet and head positions confirm it independently (feet at y≈437 fits a pitch of about 50°).
  This fit gives |V| = 2.7-3.3 m/s, but only by making vZ 1.1-1.8 m/s. The ball's apparent size, especially in the
  sharp frames 37-40, does not support that much motion away from the camera. The fit also leaves systematic
  residuals of up to 20 px. The likely causes are non-uniform frame timing or the size not being modelled exactly.
  The reference measured depth directly and divided by the nominal 1/24 s, so I gave more weight to the
  size-depth routes.

## Answer
2.45 m/s. That is the middle of the reference-like estimates (2.22-2.52) and the free-acceleration fits
(2.38-2.68). The gravity-constrained fits (about 2.9) are the upper bound.
Confidence: moderate, about ±12%. Most of the uncertainty comes from the depth rate (vZ) around frame 36.
