# q_2096: initial distance between passer (P1, kicker) and receiver (P5, header), in m

File fps is 22.59, but question_fps is 30. All conversions here use 30 fps, as the convention requires.

Scale from the prior (g = 9.8 m/s^2):
- Fitting the raw ball y from scene/tracks/ball.csv (measured frames 3-38) with a quadratic gives a = 0.9266 px/frame^2.
- The median second difference is 0.945 and the camera-compensated value is 0.905, which agree.
- At 30 fps: 834 px/s^2, so the scale is 9.8 / 834 = 0.01175 m/px.
- Sanity check: P5's visible height of 148 px gives 1.74 m, which is realistic. At the file's 22.6 fps he would be about 3 m, which is not.

Distance at frame 0 (measure.py; frame 0 was viewed in frames/f0.png). Horizontal separation between P1 and P5:
- body centroid: 376 px, 4.42 m
- bbox centre: 373.5 px, 4.39 m
- head top: 391.5 px, 4.60 m

Answer: about 380 px, which is 4.45 m (a body-centre-weighted value).

Confidence: medium. The scale is solid (±2%). The main uncertainty is which reference point the annotators clicked on each person (±3%).
