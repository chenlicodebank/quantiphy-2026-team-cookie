# q_2537: speed of the white (ping-pong) ball at t = 1.6 s, in cm/s

- Time: question_fps = 24, the same as the file. t = 1.6 s is frame 38. The record notes a dropped frame between
  frames 35 and 36. The velocity window used here (forward differences 36→40) does not cross it.
- Camera: lab convention, f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Track: scene/tracks/white_ball.csv mask centroids. I checked them on crops (crops.py) and they sit on the ball.
- Anchors: at frame 36 the white ball is 1.353 m away and the tennis ball 1.183 m. Back-projecting both gives the
  3D centres.
- Why the depth needs care: the ball rolls right and toward the camera. Most of its 3D speed is along the depth
  axis, so the depth must be tracked frame by frame.

## Route 1 (main): table-plane geometry
- Fitted the table-top edges to sub-pixel accuracy (tableedges.py, median of frames 2–18):
  - The two side edges meet at a vanishing point of (717.2, 350.6).
  - The near edge is straight to 0.24 px rms.
- The second direction is the one orthogonal to the side-edge direction that lies on the near-edge line. This gives
  a table normal n = (0.0070, −0.9999, −0.0131).
- Check against the given depths: n·(P_tennis − P_white) = 0.0087 m, against the expected radius difference of
  0.0135 m. That is consistent to 5 mm.
- The white ball's centre moves in the plane through its frame-36 position with normal n. Intersecting each frame's
  ray with that plane (plane3.py) gives:
  - distances 1.353 / 1.257 / 1.159 / 1.067 m at frames 36 / 40 / 44 / 48;
  - steady steps of 60–67 cm/s over frames 37–48;
  - v(38) = 62.3 cm/s (mean of the forward differences 36→40).
- Variants of the normal:
  - using the far edge instead of the near edge: 62.8 cm/s;
  - a normal forced to satisfy the ball-height constraint exactly: 66.3 cm/s.
- Check on the tennis ball: the plane predicts its size as 30.2 px at frame 0, 43.2 at frame 36 and 47.7 at
  frame 41. Measured: about 30–32, 43.8 and 47.7 px.

## Route 2 (independent): apparent size
- The white ball's horizontal half-max width is to first order unaffected by motion blur (sizes.py). It goes from
  22.7 px at frame 36 to 28.7 px at frame 48. The prediction for a 4.0 cm ball at 1.353 m is 22.5 px, which matches.
- Depth was taken as 1.353 × 22.7 / width, with 1/width smoothed linearly over frames 36–48 (size_route.py).
  - Result: v(38) = 61.0 cm/s. The raw net speed over 36→48 is 60.9 cm/s.
  - Shorter fit windows are noisier: 51–55 cm/s.

## Answer
62.5 cm/s.

Confidence: moderate, about ±8%. The main uncertainty is the depth component, which depends on how the table plane
is tilted and rolled.
