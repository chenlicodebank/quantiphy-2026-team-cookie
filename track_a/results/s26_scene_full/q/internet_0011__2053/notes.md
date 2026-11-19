# q_2053: displacement of the player in white (m)

**Scale.** The prior is "court width = 4.88 m", which is 16 ft, the standard lane (key) width. I take it as the width of the narrow key rectangle under the hoop.
- `lane.py` measures the lane lines on frame 0, at rows y=700 to 1150:
  - line centre to line centre: 1077 px;
  - outer edge to outer edge: 1089 px;
  - inner edge to inner edge: 1066 px.
- I use about 1083 px, which gives 4.506 mm/px.
- Sanity check: the sidelines are 3334 px apart, which gives 15.0 m (the FIBA court width). The ball is 53 px, which gives 0.24 m. Both are consistent, so this reading of the prior is right. (If the 4.88 m were the full court width, the ball would come out at 8 cm, which is impossible.)

**Displacement.** This is a straight line from frame 0 to frame 106. The frame rate doesn't affect it.
- Mask centroid from the scene track:
  - raw: (1543.7, 577.1) → (2082.2, 1927.1), 1453 px;
  - camera-compensated: 1449 px.
- Second route: I read the head and shirt centres by eye on gridded crops (frames/f0.png, frames/f106.png):
  - head: (1572, 612) → (2112, 1968), about 1460 px;
  - shirt: about 1453 px.
- Adopted value: 1455 px × 4.88 / 1083 = **6.56 m**. The range is 6.5 to 6.6 m, depending on the lane-width convention (±1%) and the reference point.

**Answer: 6.57 m.** Confidence: good. The main uncertainty is whether the prior means the lane width (I believe it does).
