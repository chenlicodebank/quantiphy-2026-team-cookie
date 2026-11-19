# q_2499: width of the table (cm), captured_0029s

**Answer: 57.4 cm.** Width is the shorter horizontal extent, front to back. The length (left to right) comes out at 71.3 cm.

## Inputs
- Lab camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360). The file rate and question_fps are both 24.
- Prior: tennis ball diameter 6.7 cm, so r = 3.35 cm.
- depth_info gives the ball-centre distances: frame 24 = 0.901 m (the "0.901s" is read as metres), frame 30 = 1.144 m (hits the whiteboard), frame 38 = 1.027 m.

## Method
1. **Table corners** (`table_edges2.py`, frame 48):
   - Outline: the warmth (R−B) boundary gives the back, left and right edges with sub-pixel accuracy. The front top edge is the strongest brightness drop where the top surface meets the slab face.
   - Lines are robust fits, with residuals of 0.6 to 1.1 px. Overlays were checked in `frames/corners2_f48.png` and `frames/z2*`.
   - Corners (px): BL (448.0, 449.0), BR (917.4, 468.2), FL (212.7, 535.7), FR (1140.0, 587.4).
   - These replace the record's back-left (447, 453) and front-left (208, 541).
2. **Table plane orientation** (`vanish.py`): I assumed the top is a rectangle. The plane normal is the cross product of the two vanishing directions (front/back edge pair and left/right edge pair).
   - Check: with f = 763 the two vanishing directions are 88.6° apart, close to the 90° a rectangle needs, so f and the corners are consistent.
3. **Metric scale**:
   - Each given ball depth is back-projected along the ray through the ball centroid.
   - The ball rolls on the table, so the table plane lies r beyond the ball centre along the normal.
   - Camera-to-plane distance from frames 24, 30 and 38: 0.157, 0.158 and 0.162 m. These agree.
   - The corner rays are intersected with that plane. Width (left and right sides) by frame used for scale: 56.7, 57.2 and 58.4 cm, mean **57.4 cm**.
   - Under 1 px of corner noise the standard deviation is 0.4 cm.

## Checks
- **Frame 30 (ball hits the whiteboard):** the ball centre projects 1.9 cm in front of the back edge, against an expected r ≈ 3.4 cm if the board stands at the edge. This is consistent with the plane and scale.
- **Plane fits without the rectangle constraint** (`plane.py`):
  - Plane through the three given ball points: front-to-back distance 56.0 cm, but the left and right sides disagree (58.9 vs 53.7).
  - Least-squares plane through the ball centres of frames 23 to 48, with depth from ball size scaled to the given depths: 60.9 cm.
  - Both bracket 57.4. They are noisier because the camera is only about 16 cm above the table plane, a grazing view.
- **Ball size alone:** depths from size are about 3% larger than the given ones. The given depths were used.

## Confidence
Moderate to high, about ±3 to 4%. The main uncertainty is the camera height above the table, which comes from the ball-centre back-projection.
