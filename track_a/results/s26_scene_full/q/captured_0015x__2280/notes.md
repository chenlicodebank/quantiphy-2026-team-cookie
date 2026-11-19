# q_2280 — velocity of the toy (teddy bear) at 2.6 s, cm/s

- File fps = question_fps = 24, so t = 2.6 s is frame round(62.4) = 62. At frame 62 the bear has just been caught
  (catch at frame 59) and the hands are pulling it down to the hip, so it is still moving fast downward.
- Scale (2D clip, no depth_info): from the gravity prior. A parabola fitted to the free-flight bear positions
  (frames 17-22 and 53-58; `fit_g.py`) gives a pixel acceleration of 2720-3090 px/s^2 depending on the reference
  point (bbox centre 2973 and 2931). I used 2920 px/s^2, so the scale is 9.8/2920 = 3.356 mm/px. Sanity check: the bear
  is 95 px = 32 cm and the person is 508 px = 1.70 m, both plausible.
- Bear centre y in frames 59-65, read from 2x zoom crops with a 10 px grid (`crops2.py`, frames/zoom59_65.png),
  matching the scene track: 199, 252, 278, 310, 326, 342, ~352. x drifts by only a few px, so it is ignored.
- Velocity at frame 62 (`velocity.py`), using three routes:
  - forward differences averaged over 5 frames, (p65-p60)/5: 480 px/s = 161 cm/s
  - 5-point linear-fit slope: 547 px/s = 184 cm/s
  - central difference (p63-p61)/2: 576 px/s = 193 cm/s
- The routes disagree because the bear is slowing down (per-frame steps 53, 26, 32, 16, 16, 8 px). Answer:
  **175 cm/s**, between the routes.
- Confidence: moderate, about ±10%. The bear is held, partly hidden and rotating in these frames, so its centre is
  uncertain by about 5 px.
