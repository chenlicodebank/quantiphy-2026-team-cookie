# q_2649 — basketball velocity at t = 0.9 s (cm/s)

- t = 0.9 s -> frame round(0.9*24) = 22 (file fps = question fps = 24).
- Lab camera: f = 0.5959*1280 = 763 px, principal point (640, 360).
- depth_info: basketball 2.7777 m at 0.9 s. The two t=1.4 s entries are both labelled "soccer_ball"; one must be the
  basketball. Apparent size picks 2.602 m: the basketball's diameter grows 61.2 -> 65.2 px from frame 22 to 34
  (depth ratio 0.94 -> 2.61 m), and the measured/predicted size ratio is the same 0.96 at both frames with 2.602 m
  (2.373 m would predict 74.6 px vs 65 measured). So basketball depth = 2.7777 m @ frame 22, 2.602 m @ frame 34.
- Centres: scene/tracks/basketball.csv, re-checked with my own HSV mask centroid + enclosing circle (measure.py):
  same to <=1 px at frames 15-24 (circle overlay frames/f22.png fits the ball).
- 3D centre = depth * unit ray((u-cx)/f, (v-cy)/f, 1). Depth linearly interpolated between the given values (model A).
- Velocity = linear-fit slope of the 3D centre over a 5-frame window 20-24 (centred on 22) -> 125.5 cm/s
  (v = [-99, +68, -35] cm/s). The 7- and 9-frame windows give 124.9 and 125.8. The mean forward speed over 20-24 is 125.8.
- Second route (model B: depth from 1/diameter fitted over the free flight, scaled to 2.7777 m at frame 22): 130 cm/s.
  This is a bit higher because the size-based depth rate is steeper. I used the given-depth model.
- The collision with the soccer ball is near frame 25, after the window. The forward-only window 22-26 gives 120.6.
- Answer: 125.5 cm/s. Confidence: good (about ±5%).
