# q3160: distance between the two closest tall trees

- Trees: the two large foreground palms. The left one's trunk is at x ≈ 450–540 and the right one, in front of the building, is at x ≈ 1452–1537.
- Trunk centres (trees.py; edge profiles at several heights in frame 0, plus a visual check on 2× grid crops):
  left ≈ 492 px, right ≈ 1496 px, so they are **≈ 1000 px apart** (±8 px depending on the row used).
- Scale from the prior (the rider's average speed is 2.64 m/s): this uses the scene track `cx`, which agrees within 2 % with the
  axle and tyre-edge points. Over frames 0–57 the mean per-frame speed is 323.2 px/s raw, or 327.1 px/s with the camera
  drift removed. That gives 0.00817 or 0.00807 m/px. Sanity check: the scooter is 127 px ≈ 1.03 m and the rider is about 1.6 m tall.
- Distance: 1004 px × 0.00807–0.00817 = 8.10–8.20 m. **Answer: 8.15 m.** fps is 30, the same for the file and the question.
- Caveat: the right palm is probably somewhat nearer to the camera than the rider's plane. Following the annotators'
  convention, a single planar scale is used and there is no perspective correction. Confidence: moderate (±5 %).
