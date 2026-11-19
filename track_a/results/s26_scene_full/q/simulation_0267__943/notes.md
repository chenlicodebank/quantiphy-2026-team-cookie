# Q943: spacecraft speed at 0.5 s (prior: acceleration at 1.0 s = 4 m/s^2)

- The video is 2D at 24 fps (question_fps is also 24). The spacecraft (a flying car) translates horizontally to the left at constant acceleration. The camera is static.
- I fitted a quadratic to x(t) from scene/tracks/flying_car_final.csv using `fit.py`. I ran it for three reference points (the nose-tail midpoint ref_x, the nose x0 and the tail x1) and several frame windows (2-24, 2-30, 10-40, 14-34, 2-52).
  - Acceleration: 650-685 px/s^2. The ref_x fits give 662-671 px/s^2.
  - The fitted start time t0 is about 0.00 s: the car accelerates from rest at t = 0.
  - Backward-difference speed at frame 12: 310-323 px/s.
- The answer does not need a metres-per-pixel scale, only the ratio v(0.5)/a, which comes out at 0.472-0.482 s. Times 4 m/s^2 that gives 1.89-1.93 m/s.
- Second route (analytic): uniform acceleration from rest at t = 0 gives the backward difference at frame 12 = a*(12^2-11^2)/(2*24^2)*24 = 4*23/48 = 1.917 m/s. The instantaneous value a*t would be 2.0 m/s.
- Answer: 1.92 m/s. It agrees with the measured 1.89-1.93 m/s and is within about 4 % of 2.0 m/s. Confidence: high.
