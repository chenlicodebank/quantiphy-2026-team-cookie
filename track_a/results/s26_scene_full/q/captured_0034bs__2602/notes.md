# q 2602 – soccer ball diameter (cm)

Prior: tennis ball diameter = 6.7 cm. depth_info: left tennis 0.706 m and right tennis 0.776 m at t=1.2 s (frame 29),
pencil bag 1.05 m, soccer ball 0.894 m. The file is 24 fps and question_fps is 24, so there is no time-base issue.

## Pixel measurements (radial2.py: radial outer-edge search + robust circle fit, overlay frames/r2_0.png)
- Soccer ball (static): centre (600.7, 317.1), diameter 93.3–94.4 px (edge-point extents 96 px). Frames 0/12/24 agree.
  The scene record's 104.9 px is too large; its bbox is 98 px.
- Tennis balls, static frame 0: A 32.7 px, B 33.0 px. Frames 12/24: 32.2–33.5 px. At frame 29 the scene track gives
  A ≈32.5 px and B ≈31 px, but motion blur affects those.

## Route 1: method card (f = 763, given depth) -> REJECTED
Soccer = 0.894 x 94 / 763 = 11.0 cm. The same formula gives the tennis ball as 0.706 x 32.7 / 763 = 3.0 cm, but the
prior says 6.7 cm (a factor of 2.2 off). The given depths also run against the image: depth_info has the pencil bag
(1.05) > soccer (0.894) > tennis (0.706), while on the table the tennis balls are the farthest back and the soccer ball
and pencil bag are nearer the camera.
## Route 2: f fitted to the tennis balls plus their depths (f ≈ 345–365) -> soccer = 0.894 x 94 / 355 ≈ 24 cm.
This is larger than a size-5 ball (22.3 cm max), gives a 29 cm pencil bag, and conflicts with the depth order on the table.
## Route 3 (adopted): table-plane geometry (geom.py, geom2.py)
- Table-top corners are treated as a rectangle, which gives the plane normal for a chosen f. The corner angle is 89.4°
  at f = 763, so the lab focal length is consistent.
- Each tennis ball's apparent size and the 6.7 cm prior fix its range, and so the table-plane distance (the ball centre
  is r above the plane). The soccer ball centre is R above the plane on its pixel ray, and its apparent radius
  (47 px) then gives R.
- Results at f = 763: frame 0, A 16.7 cm and B 16.9 cm; frame 29, A 17.0 cm and B 17.9 cm. The soccer ball is about
  12% nearer than the tennis balls.
- Sensitivity to f: 15.6–18.1 cm over f = 345–900.
- Simple check: the pixel ratio 94 / 32.7 x 6.7 = 19.3 cm if both were at equal depth. The soccer ball is nearer, so the
  true value is below 19.3 cm, which fits a size-1/2 mini ball.

Answer: 17.0 cm. Medium-low confidence: the depth_info for this clip is internally inconsistent, so I did not use it
for the scale.
