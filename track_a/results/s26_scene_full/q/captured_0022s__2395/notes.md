# q2395 – ping pong ball speed at t = 0.8 s (cm/s)

File fps = question fps = 24, so t = 0.8 s is frame 19. The given depths are at frames 14, 19 and 29: 1.751, 1.687 and 1.526 m.
Lab camera: f = 0.5959·1280 = 763 px, principal point (640, 360). The 40 mm prior is not needed except as a sanity check.

## Track
Ball centres come from scene/tracks/ball.csv (x_ref, y_ref = core x-centre, core top + half width).
My own tracker (measure.py) checks them and agrees to about 1 px for frames 12–26. A zoomed crop of frame 19 shows the
ball at about (431, 413), which matches the record. The ball rolls toward the camera, moving about 4 px/frame in the image.

## Route 1 (measure.py)
- Fit a quadratic Z(frame) through the three given depths and back-project each ray, scaled to that distance.
- Speed at frame 19:
  - forward difference: 37.5–38.3 cm/s
  - 5-frame mean: 40–41 cm/s
  - linear or quadratic position fit: 39.0–39.5 cm/s
- With a single linear depth fit instead: 41.5–42.9 cm/s.
- About 33 cm/s of the speed comes from the depth rate dZ/dt and about 21 cm/s from the lateral motion.

## Route 2 (route2.py)
- The three back-projected given points are collinear to within 0.6 cm, consistent with a straight roll on the board.
- Each frame's ray is intersected with that 3D line, so depth comes from the image track itself.
- This reproduces the given depths to within 0.8 cm.
- Speed at frame 19: 5-frame mean 44.9, central difference 44.5, quadratic fit 43.8 cm/s.

## Why the routes differ
The given depths imply the depth rate increases by 26% (0.0128 to 0.0161 m/frame). The pixel steps grow only about 12%.
So route 1 puts the ball slower at frame 19 and route 2 puts it nearly constant at about 42–44 cm/s.

## Answer
41.5 cm/s, the middle of the 39.5–44 range. Confidence: moderate (about ±6%).
