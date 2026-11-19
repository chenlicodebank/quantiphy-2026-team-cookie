# q_2593: height of the pencil bag (cm). Answer: 6.0 cm

The file is 24 fps and question_fps is 24, so the time bases match. The pencil bag does not move (frames 0 and 48 match), so I averaged
11 frames (0-5 and 44-48) to reduce noise.

## Problem with depth_info
- The lab card uses f = 763 px. With the given depth_info, the tennis ball (29.3 px at 0.776 m) would be 2.98 cm, not the
  6.7 cm in the prior. The soccer ball would be 10.7 cm.
- The depth order also contradicts the image. The pencil bag (1.05 m) lies lower in the image than the soccer ball and the
  back-right tennis ball, so it is closer to the camera, yet depth_info puts it farther away.
- Conclusion: depth_info does not fit the f = 763 camera. The scale was taken from the prior (tennis ball = 6.7 cm) together with f = 763.
- Check on f = 763: the vanishing directions of the table-top corners come out 89.9 deg apart, so the top is consistent with a rectangle.
  The rectified table measures about 0.75 x 0.64 m, a plausible table size.

## Method (geom.py, model3d.py, perp.py)
1. Tennis ball depth from its apparent size: ball_right at frames 29, 31 and 33 measures 29.2-29.6 px, which gives Z = 763 x 0.067 / d,
   about 1.75-1.78 m. Its centre sits 3.35 cm above the table.
2. Table plane normal from the vanishing points of the table edges. The plane offset was set from the ball centre.
3. The bag's bottom edge line (fitted in edges.py, rms 0.4 px) was back-projected onto the table. The bag's front-bottom edge is at a
   range of 1.49 m, giving 1.95 mm/px. The view ray is 37 deg below the table plane.
4. Profile perpendicular to the bag axis (perp.py, at x = 696, using Lab b and V):
   - top outline at t = -31.5 px;
   - change from the pale zipper top to the saturated front face at t = -21 px;
   - bottom contact line at t = 0 to +1;
   - total extent across the bag: about 32 px.
5. Converting to height:
   - Cylinder model: diameter = 32 px x 1.49 m / 763 = 62-64 mm.
   - Box model (vertical front face from the bottom line to the t = -21 line): h = 56-60 mm, w = 26-31 mm.
   - Height is 5.6-6.4 cm under either shape. Answer: 6.0 cm.

## Second route
I compared the bag directly with the tennis ball and corrected for their depth ratio from the table plane (bag 1.49 m, ball 1.78 m):
32 / 29.3 x 6.7 x 0.837 = 6.1 cm. This agrees with the first route.
Sanity check: the bag's bottom edge is 21 cm long in 3D, a normal size for a pencil case.

## Rejected alternative
The literal method card (depth_info 1.05 m x 32 px / 763) gives 4.4 cm. I rejected it because the same calculation shrinks the
prior's tennis ball to 2.9 cm.

## Confidence
Moderate. The main uncertainties are the bag's cross-section shape (±5%) and the scale from the tennis-ball fit (±4%).
