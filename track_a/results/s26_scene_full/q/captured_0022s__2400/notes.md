# Q2400 – length of the table (cm)

Lab video, 24 fps (file and question fps are the same), 1280x720, f = 0.5959*1280 = 762.8 px, principal point (640,360).
The table is a tilted rectangular top. Its long side is the left-right edge (near and far edges); the front-to-back side is shorter.

## Method (scripts: board.py, lines.py, recon.py, check.py)
1. Board mask from the median of frames 0,10,20,30,40 (brown hue vs. blue background). Lines fitted to the contour for the far,
   left and right edges and the bottom of the front face. The top of the front face (the edge of the top surface) was found
   by the brightness drop along columns (the front face is ~9.7 px thick).
   Top-surface corners: FL (281.8,420.2), FR (598.7,363.4), NR (669.9,513.7), NL (226.0,613.6). Overlay: frames/lines.png.
2. Vanishing points: far/near edges -> (4223,-286); left/right edges -> (412,-31). With f = 762.8 the two edge directions
   are 89.7° apart, so they are close to orthogonal (the focal that makes them exactly orthogonal is 751.5 px, 1.5% off).
   This confirms the camera model and the rectangle. Plane normal = cross product of the two directions (tilt 28°).
3. Ball centres back-projected with depth_info: frame 14 (t=0.6, 1.751 m), 19 (0.8, 1.687 m), 29 (1.2, 1.526 m),
   using the pixel centres from scene/tracks/ball.csv (top edge + half width). The board surface is 2 cm (the ball radius) below
   the centres along the normal. Plane offsets from the three points: 0.854, 0.856, 0.839 m (mean used).
4. Corner rays intersected with that plane: far edge 0.709 m and near edge 0.709 m (both edges agree); left and right
   sides 0.580 m each. The reconstruction is therefore a near-perfect rectangle.

## Checks
- Plane taken from a single ball point instead of the mean: length 0.713 / 0.714 / 0.700 m.
- The 3D ball path lies 3.4° out of the plane and 7° from the side-edge direction, which is consistent.
- The ball rolls from frame 0 (resting at the far edge) to frame 45 (at the near edge) and covers 0.589 m along the
  front-back direction, against a reconstructed board depth of 0.580 m. This is consistent.
- The apparent ball diameter (19/20/21 px) fits the depths given (predicted 18.1/18.8/20.9 px).

Answer: length = 70.9 cm (width/front-to-back = 58.0 cm). Confidence: good, about ±2%.
