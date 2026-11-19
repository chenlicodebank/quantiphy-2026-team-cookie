# q_2844: soccer ball displacement between t = 1.0 s and t = 1.4 s

**Answer: 0.46 m**

## Time base
- question_fps = 24, which is the same as the file's rate.
- t = 1.0 s is frame 24. t = 1.4 s is frame round(33.6) = 34.

## Which ball is which in depth_info
- depth_info gives the orange ball (the basketball) at t = 0.5 and 1.0 s. It gives a "white" and a "green" ball at
  t = 1.0 s, at 3.07 m and 3.04 m.
- Those last two are the small grey ball and the tennis ball. At frame 24 both are at the standing person's hands,
  and the two depths agree with each other.
- They cannot be the soccer ball. At frame 24 the soccer ball sits in the same image row as the basketball at
  t = 0.5 s (v ≈ 607), on the same floor, so it must be at roughly the basketball's depth (2.36–2.6 m), not 3.07 m.
- So the soccer ball's depth is not given and has to be derived from geometry.

## Method (scripts in this folder)
1. **Camera:** f = 0.5959 × 1280 = 763 px, principal point (640, 360).
2. **Depth convention:** I follow the method card, X = ((u−cx)/f, (v−cy)/f, 1) × depth, i.e. depth is the camera Z.
3. **Basketball anchors:**
   - Centres: frame 12 at (343, 607) px with Z = 2.3557 m, and frame 24 at (585, 683) px with Z = 1.81 m. The
     frame-24 centre comes from the top edge plus the expected ellipse half-height, because the ball is cut by the
     bottom edge.
   - Radius from the pixel width, corrected for how an off-axis sphere stretches in the image: r = 0.110 m
     (frames 12 and 24 agree).
4. **Floor plane:** I assumed the camera has no roll and only a pitch p. The plane of basketball centres plus r
   gives the camera height H.
5. **Soccer ball on the floor:** its centre is at H − r_s along the floor normal. Its radius r_s = 0.088 m comes,
   self-consistently, from its unblurred resting width (66 px, frames 18–22).
6. **Soccer ball pixel centres** (own segmentation against a clean local background; see `perframe2.py`, `fit34.py`,
   `restwidth.py`):
   - Frame 24: (152, 607.5). This is from the extents of the partly hand-covered, slightly blurred ball, checked
     on 5× crops; it matches the record's bbox centre (153, 607.5).
   - Frame 34: (66.7, 680.8), from an ellipse fit to the blurred ball contour (the record's centroid is
     (67.3, 679.6)).
7. **Pitch:**
   - The soccer ball's own size along its path (width perpendicular to the motion, corrected for off-axis
     stretch, frames 29–35 against the resting size) is consistent with the floor model at pitch ≈ 4.5°
     (`pitchfit.py`).
   - Basketball sizes over frames 11–22 give 6.5°.
   - The two given basketball points alone give 0.4° (Z convention) or 3.1° (Euclidean convention), but this is
     very sensitive to the frame-24 centre.
   - I used 4.5°.
8. **Result:** X24 = (−1.509, 0.765, 2.358) m and X34 = (−1.431, 0.801, 1.904) m, so the displacement is
   **0.462 m**.

## Checks and sensitivity (`final.py`)
- **Pitch:** 3° gives 0.49 m, 6° gives 0.43 m.
- **Frame-24 centre:** using the record's centroid (150.4, 609.7) gives 0.444 m.
- **Euclidean reading of depth** (instead of Z): 0.418 m at 4.5°.
- **Resting width ±1 px:** under 0.3% change.
- The soccer ball's size ratio and the floor model agree with each other, which supports the depth ratio between
  frames 24 and 34 (about 1.2).

## Confidence
- Moderate. Expect roughly ±10%.
- The main uncertainties are the camera pitch and roll, which cannot be read directly because the background was
  replaced, the depth convention, and the frame-24 centre (partly hidden by the hand).
