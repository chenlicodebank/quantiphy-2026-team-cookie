# Q2842: distance between the green ball and the pink ball at 1.0 s

- The file and the question both run at 24 fps, so t = 1.0 s is frame 24.
- Which ball is which: the green ball is the yellow-green tennis ball (`yellow_ball` in scene/). The pink ball is the pale pinkish ball (`pale_ball`). Both were thrown together by the standing person. White = soccer ball and orange = basketball; the question does not use them.
- At f24 both balls have just been released and are in the air near the standing person's hands (see frames/f24z.png and frames/f24_pts.png).
- Pixel centres were measured in code (measure.py):
  - Green: HSV mask centroid (599.5, 291.0). The record has (599.5, 291.8).
  - Pink: the bright-top mask centroid is (569.7, 267.0), which matches the record. On the zoom, the lower half of the ball is darker and pinkish, so the full-ball centre is about (570, 271.5). The mask centroid is biased upward.
- Depth: the green ball is given as 3.039 m. The pink ball's depth is **not given**, so I assumed the same 3.039 m: it was thrown from the same hands at the same moment, and its apparent size is similar.
- Back-projection uses the lab camera: f = 763 px, principal point (640, 360), and depth taken as the Euclidean range.
  - Distance with the full-ball centre: 0.140 m.
  - Distance with the bright-part centroid: 0.151 m.
  - **Answer: 0.145 m.**
- Sensitivity: if the pink ball were ±0.1 m deeper or shallower than the green one, the distance would be about 0.18 m. This depth assumption is the main uncertainty.
- Confidence: moderate.
