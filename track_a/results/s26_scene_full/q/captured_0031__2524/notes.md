# Q2524: velocity of the white ball at 1.6 s (cm/s)

The file is 24 fps and question_fps is 24, so t = 1.6 s is frame round(38.4) = 38.
For a lab video I used f = 0.5959 x 1280 = 762.8 px and principal point (640, 360).
The white ball's depth_info at frame 38 is 0.994 m (Euclidean distance to the centre), which gives Z = 0.988 m.

## Measurements
- `measure.py`: I re-measured the white ball in frames 24-48. I found sub-pixel left and right edges on the upper rows of the ball and fitted a circle to them, giving a centre (u, v) and a diameter. These agree with the scene/ track to within about 1 px. The diameter is noisy (±1 px), with a plateau around frames 40-43.
- The ball rolls mostly toward the camera, so the velocity comes almost entirely from the change in depth. I took depth as proportional to 1/diameter and anchored it to 0.994 m at frame 38.

## Routes
- A (`velocity.py`): I smoothed 1/diameter with a polynomial in time. The result depends on the fit range: 38.5 cm/s for frames 24-48, 40-42 for frames 30-48 and 32.6 for frames 32-44. This route is sensitive to the noisy diameter.
- B/C (`velocity2.py`, the main route): the ball rolls on a flat table, so 1/Z (proportional to the diameter) is an affine function of the image position. The fit is diameter = -96.6 + 0.273 v, which puts the horizon at v ≈ 354, consistent with a camera that is nearly level.
  - I smoothed u(t) and v(t) locally around frame 38, predicted the diameter and therefore Z from them, back-projected to 3D, and differentiated.
  - Across all fit ranges and windows the result is 38-42.5 cm/s, with velocity ≈ (-6.8, 0.2, -41) cm/s.
- Per-frame forward differences (route B), averaged over frames 36-40: 41.2 cm/s.
- Analytic check: dZ/dt = Z (dv/dt) / (v - v_h) = 0.988 x 34.8 / 88 ≈ 39 cm/s.

**Answer: 40 cm/s.**

## Caveat
The depth labels in depth_info look swapped. With the 6.7 cm prior, the tennis ball's pixel diameter at frame 38 (about 50.8 px) gives Z ≈ 1.01 m, not 1.19 m. The white ball (24.8 px) at 1.19 m would be about 3.9 cm, which fits a ping-pong ball. The white ball is also higher in the image, so it is farther away.

Following the instructions, I used the given 0.994 m. If the true depth of the white ball were about 1.19 m, the speed would scale up to about 48 cm/s.

Confidence: moderate. The result spans about ±5% across methods, plus the depth-label caveat above.
