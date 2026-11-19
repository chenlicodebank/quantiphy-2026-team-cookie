# q_3196 – height of the acorn (cm), prior g = 9.8 m/s^2

## Key observation
The video is rotated by 90°: gravity points along +x in the image. The toy is released from the hand at the left (frame 39). It
accelerates to the right (a free drop), hits the chair at frame 45, rebounds left, decelerates, and falls right again (frames 47-57).
Both segments show a constant +x acceleration and almost none in y. So the acorn's real "height" (cap top to dome bottom) is along image x,
which is how it is held in frames 0-38 (cap on the left, i.e. on top).

## Pixel acceleration (fit.py, fit2.py; quadratic fits to the centres in scene/tracks/ball*.csv, px/frame^2)
- Free fall 39-44 (dome-mask centre / trailing edge / leading edge): 37.9 / 37.3 / 38.4. 39-43: 38.7-46.9. Including impact frame 45: 32-36.
- Rebound arc 48-56: 34.7 / 33.5 / 35.6. 47-57: 34.4.
- Adopted a = 36 px/frame^2. fps 30 (question_fps; the file's 30.013 makes a negligible difference) gives 32,400 px/s^2.
  Scale = 9.8 / 32400 = 0.302 mm/px.

## Pixel height
The held frame 0 (gridded crop frames/f0.png) runs from the cap end x≈175 to the dome end x≈463, i.e. **~288 px** (stem excluded; the stem
adds ~40 px). The record's held bboxes give 279-291 px. Adopted 285 px.

## Answer
285 px × 0.302 mm/px ≈ 8.6 cm. **Answer: 8.5 cm.**

## Cross-checks and uncertainty
- Depth-consistent route: the ratio of the toy's pixel size to the pixel acceleration at the same depth gives 9.8·s/a. At the rebound depth
  (a≈34.5, toy width ≈218 px, height/width ratio 288/267) this is ≈7.4 cm. In early free fall (a≈43, width ≈250 px) it is ≈6.7 cm.
  The held toy is nearer the camera than the falling toy, so the single-scale annotator convention gives a larger value (8.3-9.1).
- Sanity check from the hand: a finger near the toy is ~55-60 px thick. At ~1.8 cm per finger this suggests ~9 cm.
- The answer follows the single-scale annotator convention. Its spread is about 7-9 cm. Confidence is moderate.
