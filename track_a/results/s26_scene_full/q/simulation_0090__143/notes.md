# Q143: distance between the big bird (eagle) and the small bird (crow) at t = 0.3 s

- This is a 2D side-view render. The camera is static and both birds fly left at the same height. fps = question_fps = 24, so t = 0.3 s is frame round(7.2) = 7.
- **Scale from the prior** (small bird speed = 11 m/s):
  - Crow pixel speed is steady at 95.5 px/frame (`measure.py`: x0 frames 3→12 = 95.6, bbox centre = 95.7; record x0 frames 2→18 = 95.5).
  - That gives 95.5 × 24 = 2292 px/s, so the scale is 11 / 2292 = 0.00480 m/px.
- **Separation at frame 7:**
  - Bbox x-centres: eagle 700.5–701 and crow 1180–1180.5, so dx = 479.5–480 px. As a cross-check, the leading edges give 516 and the trailing edges 444, which average to 480.
  - Body-axis rows (`body_line_y`): eagle 600 and crow 608, so dy ≈ 8 px.
  - The distance is ≈ 480.1 px.
- **Answer:** 480.1 × 0.00480 = 2.30 m.
- **Second route:** my own segmentation (`measure.py`, half-resolution masks) reproduces the record's bboxes to within 1–2 px. Using the leading-edge distance instead of the centres would change the answer by ±7%, but the bbox centre is the best proxy for the origin.
- **Confidence:** high, about ±3%.
