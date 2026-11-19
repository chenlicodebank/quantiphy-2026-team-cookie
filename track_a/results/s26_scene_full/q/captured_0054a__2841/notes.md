# q2841 – distance orange ball (basketball) to soccer ball at t=1.0 s (frame 24, question_fps 24 = file fps)

## Which depths apply
depth_info gives the orange ball at f12 (2.3557 m) and f24 (1.8100 m), plus "white ball" 3.0735 and "green ball" 3.0390 at f24.
The green ball is the yellow/green tennis ball and the white ball is the pale ball. Both are in the standing person's hands at the back wall (~3 m), which is why their depths are almost the same.
The white ball is **not** the soccer ball. The soccer ball rests on the floor at image v≈612, lower in the image than the basketball at f12 (v≈606, Z≈2.36), so it has to be at a similar or smaller depth.
A depth of 3.07 is not consistent with the floor geometry. So the soccer ball's depth is not given and has to be estimated.

## Method (lab card: f = 0.5959*1280 = 762.8 px, principal point (640,360); P = ((u-cx)/f, (v-cy)/f, 1)*depth)
- Basketball centres: f12 (344.0, 605.7) and f24 (585.8, 680.5). The f24 centre comes from a circle fit, because the ball is cut by the bottom edge; checked on the frame (bbox x 541-631, top y 634, diameter ~90).
  - P_f24 = (-0.128, 0.759, 1.810).
- Check on scale: basketball diameter = 2.3557*74..80 px/f = 0.23-0.245 m, which fits a size-7 ball. The mean speed from f12 to f24 is 1.91 m/s; the prior is 2.21 m/s at 0.5 s, in the same range.
- Soccer ball at f24, measured on a 4x zoom crop: x 115-182, y 576-648, centre (149, 612.5), diameter ~66 px.
- Floor-plane route: both ball centres lie on planes parallel to the floor.
  - The height of the basketball-centre plane comes from the two given basketball 3D points. Camera pitch is 3-4.5 deg from the wall/floor vanishing lines (horizon v≈300).
  - The soccer centre is set 0.01-0.02 m lower, because its radius is smaller.
  - Intersecting the soccer ray with that plane gives Z_soccer ≈ 2.28-2.32 m, so P_soccer ≈ (-1.48, 0.76, 2.30).
  - The result hardly depends on pitch: 0.18-8 deg changes Z_soccer only between 2.24 and 2.30.
- Distance = |P_soccer - P_basketball(f24)| = 1.42-1.46 m. **Answer 1.436 m.**

## Second routes and disagreement
- Size route: assume a size-5 soccer ball (0.22 m) at 64-68 px. This gives Z 2.47-2.62 and a distance of 1.59-1.75 m.
  At the depth scale implied by the given basketball depths, the soccer ball comes out at 0.195-0.20 m. That is plausible for a size-4 ball, and the real ball size is not known.
  So I trust the floor route: it is tied to the given depths, and the reference also used depth-camera values.
- Euclidean-range reading of depth (instead of Z): the distance would be 1.24-1.29 m. Not used, because the method card back-projects depth as Z.
- If the "white ball" were the soccer ball (range 3.07), the distance would be 1.71 m. Rejected for the floor-geometry reason above.

Confidence: moderate (~±10%). The main uncertainty is the soccer ball's depth, which is not given.
