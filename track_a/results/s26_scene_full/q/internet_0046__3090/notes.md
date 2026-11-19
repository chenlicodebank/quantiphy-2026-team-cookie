# q_3090 — velocity of the cup at 1.00 s

- fps 30 (file = question_fps). t = 1.00 s -> frame 30. Camera static (scene record; caps move <=3 px).
- Scale (one factor, internet convention): cup body height rim-to-base = 570 px (record median 568-570 near frame 30,
  checked by eye on frames/f30.png: rim ~295-300, base ~868). 0.105 m / 570 px = 1.842e-4 m/px.
- Motion: body centre x. Record: x30 = 540.3, x31 = 643.0 -> raw forward difference 102.7 px/frame.
  My own edge tracking (measure.py, background difference against empty frame 50, wall band rows 330-470) gives
  centres 544 -> 642 (98 px raw, noisier from motion blur).
  A quadratic fit over frames 27-35 gives v(30.5) = 103.7 px/frame (record) and 103.4 px/frame (mine) -> 103.5 px/frame
  = 3105 px/s.
- v = 3105 x 1.842e-4 = 0.572 m/s (raw record forward difference: 0.567 m/s).
- Confidence: the speed is good to about ±3 %. The height scale is good to about ±2 % (blurred rim, slight growth over the clip).
