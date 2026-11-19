# q_722: paper airplane speed at t=1.25 s
- 2D render, 24 fps (file fps = question_fps), so t = 1.25 s is frame 30. Speed = |p30 - p29| x 24.
- Scale: chalkboard length = 5 m. Board outer edges (wooden frame included) are at x = 320 and 1692, so 1372 px; I checked the right edge at 1692 on row 600. That gives 3.644 mm/px. The green surface alone is 1327 px and would give a speed 3.4% higher (5.53 m/s); I used the full object, frame included.
- Plane centre: the record's nose-tail midpoint gives a step of 61.16 px from frame 29 to 30. My own background-difference bbox centre (measure.py) gives 61.35 px. Neighbouring steps are 62.8 / 61.4 / 59.2 px, a smooth trend. I used 61.2 px/frame.
- Speed = 61.2 x 24 x 5/1372 = 5.35 m/s.
- Check: two independent centre estimates (the record and mine) agree within 0.3%. The plane length (~140 px, about 0.51 m) stays constant, so the motion is planar.
- Confidence: high on pixels; the main uncertainty is whether the board length includes the frame (about 3%).
