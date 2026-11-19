# Q886 – width (longer side) of the AC unit

File runs at 24 fps; the question states 30 fps (question_fps), so all timing uses 30 fps on the frame index.
2D scene with a static, fronto-parallel camera (see scene/notes.md).

Scale from the prior (the plant falls at 9.8 m/s^2, frames 0–14, landing at frame 15):
- I fitted quadratics to the scene track, `measure.py`:
  - mask centroid y: a = 6.93–6.95 px/frame^2 (resid 0.3 px)
  - bbox centre: 6.91–7.01
  - bottom edge: 6.86–7.12
- Adopted a = 6.95 px/frame^2, which is 6255 px/s^2 at 30 fps. That gives 9.8 / 6255 = 1.567e-3 m/px.

AC width:
- In frame 0 the white unit spans x = 132–637 px in every row from 770 to 1050 (white mask, with gradient edges at 131 and 637).
- That is 505–506 px, so 505.5 × 1.567e-3 = **0.79 m**.

Checks:
- Real LG outdoor units are about 0.77–0.87 m wide, so the value is plausible.
- The frame width is 3.0 m at the plant's depth, which fits a room.
- Caveat: the AC's front face may be slightly nearer the camera than the plant, which falls near the back edge of the table close to the wall. The depth cannot be resolved without camera information, so I used the planar 2D convention. The possible error is a few percent.

Confidence: good (about ±5%).
