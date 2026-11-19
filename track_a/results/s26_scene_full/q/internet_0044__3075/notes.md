# Q3075 – height of the kettle (cm); prior g = 9.8 m/s^2

Time base: file fps = question_fps = 30, so I used 30 fps.

Scale (from the prior): I fitted a quadratic in frame number to the ball's stabilised image y (scene/tracks/ball.csv,
cy_f0, measured flight frames only, with the arc-fill rows and the frames next to each bounce left out), one fit per arc
between bounces (measure.py):
the accelerations were 20.04, 19.80, 18.84, 19.44, 19.12 and 19.09 px/frame^2 (median 19.3, mean 19.4). The first two arcs,
in front of the kettle, give 19.8-20.0. I chose 19.5 px/frame^2.
g = 9.8 m/s^2 = 9.8/900 m/frame^2, so the scale is 0.01089/19.5 = 0.558 mm/px.

Kettle height: red HSV mask, largest component, checked on an overlay (frames/kmask0.png). The bbox height is 288 px at
frame 0 (y 524-812) and 288 px at frame 180, which agrees with the scene record (288 px).
Height = 288 x 0.558 mm = 16.1 cm.

Second check: the ball's diameter of about 76 px x 0.558 mm/px gives 4.2 cm. A table-tennis ball is 4.0 cm, so the scale is
plausible (the ball is a little nearer the camera than the kettle). The range of accelerations (19.1-20.0)
gives a height of 15.8-16.4 cm.
Confidence: moderate-high, about ±4%.
