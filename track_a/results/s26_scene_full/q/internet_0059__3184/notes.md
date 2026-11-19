# q_3184 – left edge of left poster to right edge of right poster (cm)

Prior: g = 9.8 m/s^2. Treated as 2D (the wall faces the camera), with one scale from the ball's vertical pixel acceleration. fps is 30 (file and question agree).

## Scale (fit.py)
- I fitted a quadratic to the ball centre y over frames 66-97, leaving out the frames where the ball is cut by the image edge:
  - image cy: a = 4930 px/s^2;
  - background-compensated cy_bg: a = 4956 px/s^2;
  - mask centroid: a = 4931 px/s^2.
- The rising part alone gives about 5330 px/s^2 and the falling part alone about 4750 px/s^2. This fits air drag (or slight depth motion). The whole-arc value matches the mean of the annotators' second differences, so I use a ≈ 4945 px/s^2.
- Scale = 9.8 / 4945 = 0.001982 m/px.
- Sanity check: the ball's diameter of 121 px × 0.198 cm/px gives 24.0 cm, which is a regulation basketball. This agrees very well.

## Pixel distance (edges.py)
- Dark frame edges, from the dark-pixel column profile: frame 0 gives 438 to 1412 (974 px), and frames 40, 70 and 81 give 970-971 px.
- A thin clear acrylic border adds about 2-4 px on each side. The scene record's outer boxes give 433 to 1415 (982 px).
- I use 980 px. Camera drift is only a translation; there is no zoom.

## Answer
980 px × 0.1982 cm/px ≈ 194 cm.

Sensitivity:
- Using only the rising-arc acceleration gives about 180 cm.
- Using only the falling arc gives about 202 cm.
- Using 974 px gives 193 cm.

Confidence: moderate-good (±5%).
