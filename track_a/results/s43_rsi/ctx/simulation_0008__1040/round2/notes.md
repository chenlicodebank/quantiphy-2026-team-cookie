# q1040: width of the wooden stairs (m), round 2 verification

The file runs at 22.802 fps and question_fps is 24, so t = 1 s is frame 24. The camera is static.

**Answer: 1.75 m.** The decision is "new". It verifies round 1's proposed 1.76 m. The submitted answer is 1.66.

## Crux
The candidates split on two points. The first is the focal length: C2 used 1300 px, C3 1075 px, and C1, C4 and round 1
about 1000 px. The second is the stairs' pixel extent: C4 used 88 px, C3 93, C2 101, round 1 98, and C1 108 px
(which includes the pale posts).

## Measurements (my own code)
**Focal length** (`focal_check.py`):
- The depth pair at constant Z (7.452 m at frame 0, 6.655 m at frame 24), with the boat origin at the box centre and
  length 648 px, gives f = 1000 px and Z_boat = 5.85 m.
- Varying the origin (0.45–0.55 of the length), the length (620–670 px) and the frame (23–25) gives f = 951–1048.
  The core range is 973–1026.
- This reproduces round 1 (1002) and C1 (999).

**Stairs extent** (`stairs_profile.py`, column profiles on the mean of all 66 frames; `zoom_enh.py` →
`frames/stairs_enh.png`):
- The left outer edge, a thin lit vertical member, is at x = 487.5 in every tread band (rows 548–575).
- The right member (lit at 584–586) ends at 586.5, where the pale post begins.
- The treads run from about 490 to about 585.
- The outer extent is **98–99 px**. The treads alone are about 94 px.

**Pale posts** (500–512.5 and 587–599):
- They are centred at x = 549.5, while the stairs are centred at 537.5.
- The 12 px offset (about 0.2 m) cannot come from perspective: the stairs are on-axis.
- The posts line up with the jetty sides. The jetty's back corners sit at x ≈ 500 and 603, centre 551.5. The same
  lateral offset seen about 15 % deeper gives exactly the post positions.
- So the posts belong to the jetty line, not to the stairs. This reproduces round 1's finding.

**Depth:**
- The stairs origin is at 17.62 m, nearly on-axis, so Z ≈ 17.6 m.
- The vertical members stand at the deck front. They are at most half a run (about 0.5 m) behind the origin.
- So Z = 17.6–18.1 m.

**Width:** W = 98 × (17.6–18.1) / 1000 = 1.72–1.77 m. With f between 973 and 1026 the range is 1.68–1.82 m.
**Answer: 1.75 m.**
- With the treads only (94 px) the width would be 1.65–1.70 m.
- With the pale posts (110 px) it would be about 1.94 m.

## Rechecks
**a. Closure:**
- At frame 0 the stem post top is at row about 620–622 and its reflection at about 870. The span is about 250 px, so
  the waterline is at row 746 and the post rises about 126 px above the water.
- 126 × 5.85 / 1000 = 0.737 m, plus a small draft inside the bounding box. That is the 0.75 m prior within −1.7 %.
- Conversely, the 0.75 m box spans 128 px.

**b. Plausibility** (round 1 values, consistent with my f):
- Door: about 1.85 m.
- Railing: about 1.06 m.
- Boat length: 648 px × 5.85 / 1000 = 3.8 m (a rowboat).
- Stairs: a rise of about 53 px, giving about 0.95 m, over 4 treads. A 1.75 m wide stair is ordinary.

**c. Units and time base:** the answer is in metres. t = 1 s is frame 24 (question_fps 24, not the file's 22.8).

**d. Fault proof:**
- **C2 (1.37):** f = 1300 = 130 px × 7.452 / 0.75. This treats the Euclidean distance as Z for a boat 774 px off-axis.
  The true Z is 5.85 m, so its f is 30 % too high.
- **C3 (1.45), the blend's B input:** f = 1075 from Z ≈ 6.3 m, against Z = 5.85 m from the depth pair (+7.5 %). It also
  used 93 px at 17.0 m and then averaged in the run (about 1.3 m). Its width reading alone would be 93 × 17.6 / 1000 =
  1.64 m.
- **C4 (1.56):** its f of 990 is fine. It took the midpoint of 80 px (tread span from 506, which misses the treads
  left of the left pale post that reach x 490) and 95 px.
- **C1 (1.9), the blend's A input:** its f of 999 is fine. Its 108 px includes the pale posts, which are aligned with the
  jetty, not with the stairs (12 px off the stairs' axis).
- **Submitted 1.66:** a geometric blend of C1 (+10 % pixel-extent error) and C3 (+7.5 % focal error plus averaging in
  the run). Its inputs carry the faults above, and it sits 5 % below my value.

## Decision
I reproduced both of round 1's fault claims: f ≈ 1000, not 1075 or 1300, and the posts are not part of the stairs. My
own value, 1.75, is within 1 % of round 1's 1.76. The change stands. **Answer: 1.75 m.**

Confidence is medium. What remains open:
- whether the vertical members belong to the stairs model (98 px) or only the treads do (94 px);
- whether the members' depth is 17.6 or 18.1 m.

Together these span 1.65–1.77 m.
