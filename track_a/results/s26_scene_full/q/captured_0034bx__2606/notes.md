# q 2606: speed of the right tennis ball at 1.2 s (cm/s)

- The right tennis ball is ball B in scene/ (it starts at the far-right corner and rolls left after the push at frame 24).
  t = 1.2 s is frame round(1.2 x 24) = 29. The file rate and question_fps are both 24.
- Centres: I re-measured them in `measure.py` (HSV mask and a least-squares circle fit, frames 22–37). They agree with
  scene/tracks/tennis_ball_B.csv to within about 1–2 px; my y values are about 1–2 px lower. On a 4x crop of frame 29
  the ball's centre is at about (757, 264), which matches.
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Back-projection uses depth_info: right ball 0.776 m at t = 1.2 s.
- Depth at the other frames comes from two models: (a) constant depth 0.776 m; (b) the ball centre stays on a plane
  parallel to the table, with the table normal taken from the table-edge vanishing points. In (b) the depth goes from 0.784 to 0.770 m over frames 27–31.
- Velocity, smoothed over 5 frames around frame 29 (the reference smooths over at least 5 frames):
  | centres | depth model | mean forward diff, frames 27–31 | chord 27→31 | chord 26→32 |
  |---|---|---|---|---|
  | track | const | 27.8 | 28.3 | 29.5 |
  | track | plane | 29.7 | 30.1 | 31.8 |
  | own | const | 26.1 | 27.8 | 28.3 |
  | own | plane | 27.4 | 29.2 | 30.0 |
  Raw one-frame differences at frame 29 range from 22 to 35 cm/s, which is noisy. The ball is slowing down: about 43 cm/s at frame 26 and 24–28 cm/s at frames 30–34.
- Answer: **28.5 cm/s**, the centre of the smoothed estimates (spread ±2 cm/s).
- Caveat: at 0.776 m depth, a 6.7 cm ball should be about 66 px across, but it is only about 31 px in the image. So the
  depth_info scale and the size-prior scale disagree by about 2x. With the size prior instead (6.7 cm / 31 px), the speed would be about 55–60 cm/s.
  I followed the lab convention (back-projection with the given depth), as the reference does.
- Check with the left ball: the plane model, anchored on the right ball, predicts 0.752 m for the left ball against the given
  0.706 m. The given depths are not fully consistent with this geometry, which also makes the depth-change model uncertain.
- Confidence: moderate under the depth convention. The main risk is the scale inconsistency.
