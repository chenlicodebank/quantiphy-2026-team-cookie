# q_2538: width of the table (cm). captured_0032, lab video at 24 fps (file fps = question fps)

## Method
The camera is f = 0.5959 x 1280 = 762.8 px with the principal point at (640, 360). The table is seen at a grazing angle:
the camera is about 17 cm above the tabletop. Because of that, its size had to come from a 3D reconstruction of the
tabletop plane, not from a single pixel extent.
1. `edges.py` and `geom.py` (frame 12, where the balls are static): a wood-colour mask of the tabletop, plus
   sub-pixel gradient edges.
   - Left side line: x = -1.877 y + 1370 (rms 1.7 px). Right side line: x = 1.593 y + 167 (rms 4.2 px, noisier).
     The side edges meet at a vanishing point of about (719, 347).
   - Near top edge: y = 0.0250 x + 471.1 (rms 0.3 px). Far edge: y = 0.0095 x + 419.1. These two lines meet at a
     left-right vanishing point of about (-3360, 387).
   - Near edge ends: x = 464.3 to 963.5 px, taken from the front face's horizontal extent.
2. `balls.py`: ball centres at frame 36 (t = 1.5 s).
   - Tennis ball: (583.5, 435), about 44 px across.
   - Ping-pong ball: (721.2, 432.7), about 21 px across.
   Both were back-projected with the given depths of 1.183 m and 1.353 m. The ball radii are 3.35 cm (from the prior)
   and 2.0 cm (standard ping-pong ball). The balls' apparent sizes match these depths to within about 2 % for the
   tennis ball.
3. `solve.py` and `final.py`: the tabletop plane is found two ways.
   - Route A: the plane normal is the cross product of the two vanishing directions. Its height comes from each ball's
     contact point (each ball centre minus its radius along the normal). The two balls give 0.167 m and 0.171 m, which
     agree to within 2 %.
   - Route B: the plane uses the side vanishing direction, and its tilt and height are solved from both balls'
     contact points. The normal agrees with route A to within 1 degree.
   The corner rays are then intersected with the plane.

## Results
These are medians over both routes, with each ball centre's vertical position varied by ±1 px.
- Left-right extent (near edge): **0.596 m** (range 0.584–0.609).
- Front-to-back extent: 0.72 m (range 0.70–0.74).
- Under route A the far edge comes out the same length as the near edge (0.58–0.59 m). This fits a rectangular top.
- The angle between the two edge directions is 85 degrees, close to square.

The table is therefore about 60 x 72 cm, with its long side running front-to-back from the camera.
- Width read as the shorter horizontal extent (the convention used here): **59.6 cm**, the left-right side.
- The other reading, front-to-back depth: about 72 cm. That side is the longer one here, so the desk rule
  ("width = front-to-back") does not override the shorter-extent rule.

## Checks and caveats
- The near edge sits at about 0.85–0.98 m depth. The near edge's 500 px length x about 0.92 m / 763 is about 0.60 m,
  which matches.
- The balls at rest near the far edge at frame 0 (from their pixel size: yellow about 1.70 m, white about 1.85 m) look
  about 6 % farther away than the plane predicts (1.59–1.63 m). This part is sensitive at grazing angles, but it
  mainly affects the front-to-back value, not the left-right width.

Confidence: the left-right width is good to about ±3 %. The main uncertainty is the plane height (±2 %).
