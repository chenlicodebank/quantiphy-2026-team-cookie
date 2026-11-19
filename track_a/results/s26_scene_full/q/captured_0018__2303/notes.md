# q_2303 — soccer ball velocity at 3.4 s (cm/s)

**Main problem:** the clip has 49 frames at 24 fps (0–2.04 s), and the file rate matches question_fps (24).
t = 3.4 s would be frame round(3.4 x 24) = 82, which is not in the video. Nothing in it shows the ball at that time,
so the answer can only be an estimate.

## What was measured (est.py, using scene/tracks/soccer_ball.csv, checked against the scene notes)
- Scale: f = 0.5959 x 1280 = 763 px. Ball depth is 2.80 m (depth_info), and the ball's apparent size stays about the
  same (~44 px), so its depth is taken as constant.
- Release at about frame 29 (centre y 265.5). Floor impact at frame 39 (centre y 541). Drop = 275.5 px x 2.8/763 = 1.01 m.
- Under gravity (9.8 m/s², the prior), the speed just before impact is sqrt(2 g h) = 4.45 m/s. The fall takes 10.9
  frames: about 11 frame intervals, which matches the dropped frame suspected between frames 35 and 36.
- Rebound speeds measured over frames 41–48: 2.4, 2.3, 1.7, 1.7, 1.3, 1.0, 0.8, 0.4 m/s. The ball reaches its apex
  around frame 49–50.

## Answer choice
Because t = 3.4 s is outside the clip, I assume the reference time comes from a longer original recording and falls
somewhere in the ball's moving phase. In the fall, speed rises evenly from 0 to 4.45 m/s; in the rebound it drops from
2.4 to 0.4 m/s. I picked the value that gives the best expected score over those possible speeds: about 1.75–2.75 m/s,
so the answer is **220 cm/s**.

Confidence: very low. The asked time is not in the video.
