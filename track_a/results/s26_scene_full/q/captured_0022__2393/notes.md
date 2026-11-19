# Q2393: width of the table (cm)

The "table" is the rectangular wooden tabletop/board, tilted as a ramp. Width is its shorter side, which runs front-to-back
along the slope (the ball rolls roughly along it). Its long side is the left-right edge.
Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360), 24 fps (file and question rates agree).
The depth_info times map to frames 14 (1.751 m), 19 (1.687 m) and 29 (1.526 m). The ball centres come from scene/tracks/ball.csv.

## Method
1. **Board edges** (`edges2.py`). I made a ball-free median image of frames 2, 22, 32 and 40. For each of the 4 top-surface edges I
   took 80 perpendicular Lab-colour gradient profiles and fitted a robust line through them (residual rms 0.2-0.4 px). The front edge
   is the top-surface/thickness-band boundary. The overlay in frames/edges2.png fits the board well.
   Corners: BL (281.0, 416.7), BR (600.4, 361.4), FR (670.9, 513.0), FL (224.7, 614.1). These are within about 4 px of the record's corners.
2. **Plane orientation** (`geom.py`). I took the vanishing points of the two pairs of opposite edges and back-projected them with K.
   The two board directions come out 88.1 deg apart. They should be 90 deg for a rectangle, so this checks f and the corners.
3. **Plane offset** (scale). The ball centres back-projected with the given depths lie 2 cm (the ball radius) above the board surface.
   Frames 14 and 19 give the same offset to within 0.1%, and the plane reproduces their depths: predicted 1.750 vs 1.751, and 1.687 by construction.
   Frame 29 is 2% off: the plane predicts 1.564 against the given 1.526.
4. **Result.** With the offset from all 3 depths the board is 71.4 x 58.1 cm. With the offset from frames 14 and 19 it is 71.9 x 58.5 cm.

## Checks
- **Hybrid route** (`hybrid.py`). I used the plane through the 3D ball line from frames 14 and 19 (offset by R), rotated about that line to make the
  back-projected quad most nearly a parallelogram. It gives a width (left and right sides) of 57.6 cm, a length of 72 cm and corner angles of about 92 deg. This is consistent.
- **Frame 29 depth.** If I also include it, no plane makes a parallelogram: the back edge comes out 72.5 cm and the front edge 68.7 cm.
  The ball's path along the 3D depth line would then give a 64 cm edge-to-edge distance. The ball's apparent width (`ballsize2.py`) changes with
  image row at a rate (-0.0028 m/px) closer to the plane model (-0.0031) than to the frame-29 depth (-0.0037). I therefore treat the depth at
  frame 29 as the outlier.
- **Record corners** (scene/). They give 58.5 cm with the mean offset, or about 58.9 cm with the frame 14 and 19 offset.

## Answer
Width is about 58.5 cm. The length (long side) is about 72 cm, for reference.

Confidence: moderate, about ±4%. The main uncertainties are the plane tilt from the vanishing points and the outlying depth at frame 29. If that
depth were right instead, the width would be about 64 cm.
