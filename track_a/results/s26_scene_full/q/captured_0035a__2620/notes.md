# q_2620 – basketball speed at t = 1.6 s (cm/s)

- The file and question_fps are both 24, so t = 1.6 s is frame 38. Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360). The camera is static.
- depth_info: the second "t=1.6s, distance_soccer_ball_camera = 2.4120 m" must be the basketball. It is the nearer of
  the two balls at 1.6 s and it is consistent with the prior: diameter 71.5 px at frame 38 x 2.412 / f (ray-corrected) = 22.2 cm, against the prior's 23.2 cm.
- Track: scene/tracks/basketball.csv (RANSAC circle centre). After the collision (frame 20) the ball rolls upper-left at about 5 px/frame.
  There is a dropped-frame jump between frames 35 and 36, so I kept every window at frames 36 and later.
- 3D positions: back-projected with range R(i) = 2.412 + k*(i-38). k = 0.0016 m/frame comes from a linear fit of the
  diameter-implied range over frames 21–48. Setting k to 0 or 0.006 changes the result by less than ±1.5 cm/s.
- Results (measure.py): forward difference at frame 38 = 37.5, mean of the per-frame speeds over 36–40 = 35.9, linear fit over 36–44 = 34.3,
  linear fit over 36–48 = 33.4 cm/s.
- Second route (check_centroid.py): I re-measured the orange-mask centroid from the video myself. Forward difference at 38 = 35.9, mean over 36–41 = 35.7,
  linear fit over 36–44 = 34.5 cm/s. The two routes agree.
- Answer: 35.5 cm/s. Confidence: good, about ±5%.
