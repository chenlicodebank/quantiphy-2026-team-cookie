# q_3272: velocity of the credit card at 0.50 s (cm/s)

- Scale: prior card length 8.56 cm. The card's long side is 432.9 px (median minAreaRect length over the sharp rest frames 33–38, checked on frame 36: x ≈ 929–1362). This gives 0.01977 cm/px, one planar scale.
- Camera: static (the spotlight disc does not move), so image displacement is card displacement.
- Track: scene/tracks/card.csv mask centroid. I checked it on frames 13, 15 and 16 (frames/f15.png): the box fits the blurred card. As a second reference point I used the top-left corner of the bounding box.
- Time base: the file runs at 26.85 fps and the question states 30 fps. A hand motion can't show which rate is right. I used question_fps = 30 (the original-footage convention), so t = 0.5 s is frame 15.
- measure.py results:
  - 30 fps, frame 15: the forward difference is 45.6 px/frame (centroid) and 45.8 px/frame (corner), i.e. 27.0 and 27.2 cm/s. A light quadratic smoothing over frames 12–19 gives 49.0 and 47.5 px/frame, i.e. 29.1 and 28.2 cm/s.
  - Check at 26.85 fps, frame 13: forward 32.2–33.9 cm/s, smoothed 29.1–29.5 cm/s.
- Answer: **28.5 cm/s**, the lightly smoothed value. It falls between the raw forward differences and agrees under both time bases.
- Confidence: moderate, about ±10%. The main uncertainties are the fps choice, the per-frame jitter and the length used for the scale. The apparent length at t = 0.5 s is about 400 px; using it would raise the answer by about 8%.
