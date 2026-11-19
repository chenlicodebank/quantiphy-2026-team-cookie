# q2925: length of the blue shopping bag (cm)

The file rate and question_fps are both 24 fps, so t = 1.4 s is frame 34. The camera is static.

**Object.** The asked object is the dark-blue tote bag with an orange "MARINE" logo. It lies flat on the floor at the right, at about px (834,331), and stays static for the whole clip. "Length" is taken as the longer side of the bag body, not counting the handles.

## Method (3D, lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360))
1. **Floor orientation.** The sliding white board is a rectangle on the floor. I took its corners from scene/tracks/white_board_corners.csv. Each pair of opposite edges gives a vanishing point, and these give the floor normal. I used frames where the two vanishing directions are orthogonal (|cos| < 0.03 in frames 34-39, 41, 46), which confirms that f is right. Floor normal n = (0.149, -0.819, -0.554). There is a small camera roll and about 34 deg of downward tilt (`board_normal.py`, `bag3d.py`).
2. **Bag corners at frame 34.** I read the body corners on a 4x zoom (`frames/bag.png`) and checked them against the mask in `seg.py`: L(772.5,310), T(826,295), R(895.5,348), B(843.8,369.5), each about ±2 px.
3. **Back-projection.** I placed the floor plane through the bag centre, back-projected with the given depth 3.307 m, and intersected the corner rays with that plane (`bag3d_manual.py`).
   - Edges: TR 0.446 m and BL 0.458 m (long sides); LT 0.348 m and RB 0.345 m (short sides).
   - Opposite sides agree to within 3%.
   - **Length = 0.45 m** (mean of the two long sides 0.452 m), and width ≈ 0.35 m.

## Checks
- **Prior reproduction (`check_prior.py`).** The same floor model with the plane set by the board's given depth (2.815 m) gives a board speed at 1.4 s of 1.87 m/s (5-frame forward smoothing). The prior is 1.934 m/s, so this is 3% low. The board's dimensions on the plane stay constant over frames 30-48 (std < 3 cm), so the floor geometry is consistent.
- **Given distances.** The plane through the bag predicts these depths:

  | object | predicted | given |
  |---|---|---|
  | board | 2.62 m | 2.815 m |
  | carton | 2.20 m | 2.08 m |
  | toy | 1.96 m | 2.02 m |

  This is consistent to about 7%: the given depths are somewhat noisy or the objects are offset from the plane.
- **Simple method-card route.** depth x pixel edge / f gives 0.40 m (BL edge, 92.8 px) and 0.38 m (TR edge). These are lower because the long side recedes along the floor, so the image foreshortens it. The ruler reference is the true length, so I used the 3D floor result.
- **Other readings.** If the plane offset is taken from the board's depth instead of the bag's depth, the length becomes 0.48 m. If the camera roll is forced to zero, it becomes 0.49 m. The answer is 45 cm, with a plausible range of 40-49 cm.

**Confidence:** moderate (about ±8%).
