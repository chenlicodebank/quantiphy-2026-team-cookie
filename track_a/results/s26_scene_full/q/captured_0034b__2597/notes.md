# q_2597: total distance traveled by the right tennis ball (cm)

File fps 24 = question_fps 24, 49 frames.

## Method (lab method card)
- Track: scene/tracks/ball_right.csv (circle-fit centres), checked visually in frames/montage.png (montage.py), frames 23-40.
  One correction: frame 26 has a ghost double image. The fit (811.5) sits between the real ball and its ghost, so I set the
  real ball's u to about 804. The circles at the collision (frame 38) and in all the other rolling frames sit on the ball.
- Back-projection with f = 0.5959*1280 = 762.8 px, principal point (640, 360), depth Z = 0.776 m (depth_info, t = 1.2 s, frame 29),
  held constant. Path length = sum of the frame-to-frame 3D displacements over frames 0-48 (measure.py).
- Results: raw 21.05 cm, Savitzky-Golay smoothed (5 frames, not smoothed across release or collision) 20.66 cm.
  By phase: held 0-24 about 0.5-0.8 cm, rolling 24-38 about 17.0 cm, after the collision 38-48 about 3.1 cm.
  Pixel path 207 px in total, 199 px after release.
- Answer: 20.9 cm.

## Depth model check
- A table-plane homography (vanishing line from the table corners) predicts that Z falls by about 7.5% from frame 29 to frame 48.
  With that, the total would be 24.1 cm. But the ball's apparent size grows only about 1% (mask area 711 -> 726 px), so I
  kept Z constant.
- The depth_info values do not match the image geometry. The soccer ball and pencil case are given as farther away than
  the tennis balls, yet in the image they are nearer. The left ball (0.706 m) shows no larger than the right one. So the
  depths cannot support a per-frame depth model. I used the single given depth for this ball.

## Scale inconsistency (important)
- With f = 763 and Z = 0.776 m, a 6.7 cm ball should look about 66 px wide. It actually looks about 29.3 px wide.
  The prior and depth_info disagree by a factor of about 2.25.
- Reading with the prior's scale instead (6.7 cm / 29.3 px, planar): about 45 cm.
- I answered with the method card's depth back-projection (20.9 cm), because the reference positions are described as
  back-projected with the measured depth.

Confidence: moderate on the depth-card reading (±5%). It is uncertain which scale convention the reference used.
