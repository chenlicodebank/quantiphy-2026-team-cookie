# q_3076 – height of the white cylinder (cm)

Prior: g = 9.8 m/s^2 (the bouncing ping-pong ball). Internet video, single planar scale. fps = question_fps = 30, so no re-timing.

## Scale from gravity (fit_g.py)
Quadratic fits of the ball centre's image y (stabilised `cy_f0` from scene/tracks/ball.csv, measured blob centroids only,
no arc-fill rows, no edge-truncated rows) for each arc between bounces:
20.05/20.39, 19.83/19.70, 18.84/18.61, 19.50/19.32, 19.67/19.12, 19.60/19.01, 20.15, 19.94 px/frame^2
(all points / dropping the frame next to each bounce). One short arc near the bowl (124-131, 25.0) is an outlier and was dropped.
Adopted a = 19.5 px/frame^2 (range 19.0-20.0) = 17550 px/s^2 → scale = 9.8 / 17550 = 5.58e-4 m/px.

## Cylinder height (cyl.py)
Vertical intensity-gradient edges (top rim to bottom edge) on 5 columns, frames 0, 180, 216: 193-198 px, centre columns 198;
white-pixel mask extent 197-201 px. Scene record: 196 px. Adopted 197 px.

Height = 197 × 0.0558 cm = 11.0 cm (range 10.7-11.3 cm over the spread of fitted accelerations).

## Check
Ball apparent diameter ~76 px × 0.0558 = 4.2 cm vs a real 40 mm table-tennis ball; the ball is slightly in front of
the objects, so it looks a little larger. The scale is consistent. A ~11 cm cup/vase looks right next to the kettle and bottles.
Confidence: good (about ±4%).
