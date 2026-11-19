# q_2530 — velocity of the white ball at 1.6 s (cm/s)

t = 1.6 s -> frame round(1.6*24) = 38 (file fps = question fps = 24).
Camera: f = 0.5959*1280 = 763 px, principal point (640,360).

## Track
White ball centre from scene/tracks/white_ball.csv (edge-circle fits; checked visually on frame 38:
centre ~ (663,445), diameter ~28-29 px, matches the record 662.4,445.0, 29 px).
Ball rolls toward camera and left; motion is mostly in depth.

## Depth over time (only given at frame 38: white 0.994 m)
Z38 = 0.994 / |ray| = 0.989 m. Two routes for Z(i):
1. Diameter ratio: Z(i) = Z38 * d38/d(i) with a linear fit of diam over frames 30-47 -> speed 32.5 cm/s.
2. Level-plane geometry: ball centres move on a plane parallel to the table, so Z ∝ 1/(v - H).
   H fitted from diam ∝ (v-H): yellow ball H = 347.4, white H = 349.8 (table-edge vanishing point gave 354).
   With H = 348: speed 35.1-36.1 cm/s (fit window ±2..±4 frames); H = 354: 37.4-38.4.
Velocity = linear fit of 3D back-projected centres over ±2..±4 frames (smoothed), plus raw fwd/bwd differences
(fwd 32-39, bwd 33-40 depending on route). Answer: ~35 cm/s (mostly -Z component, ~-6.5 cm/s lateral).

## WARNING: depth_info looks swapped
- Yellow (tennis) ball at frame 38 is 54-55 px wide. With the given 1.19 m it would be 8.4 cm (prior 6.7 cm);
  with 0.994 m it is 7.06 cm (5% off). Plane geometry: the yellow ball's contact point is lower in the image
  (v≈479 vs 459), so the yellow ball is CLOSER than the white one; depth ratio from the plane ≈ 1.19-1.21,
  matching 1.19/0.994 with the labels swapped.
- Alternatives: white ball at 1.19 m -> ~41.5 cm/s; yellow ball track at 0.994 m -> ~57 cm/s.
- I answer with the depth_info as written (white = 0.994 m), since the reference answers back-project
  with the depth recorded for the white ball. Confidence: moderate (±7% from the method spread, plus the label risk).
