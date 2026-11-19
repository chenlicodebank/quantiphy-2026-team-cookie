# q_140: speed of big bird at 0.3 s
- 2D sim, static camera, 24 fps (file = question fps). t=0.3 s -> frame 7.
- Big bird (A) flies left at constant speed from frame 2 on. It is off-screen at frame 7, so I assume the constant velocity continues; the record shows no acceleration (quadratic-fit term is noise).
- My own measurement (measure.py: background-difference mask, column extents): A's tail edge sits at 787, 636.5, 486.5, 335, 185.5 px in frames 1-5, which is 150.4 px/frame. This matches the record's template-match value of 150.27 px/frame. I used 150.3 px/frame, i.e. 3607 px/s.
- Scale comes from the small bird's length (prior 0.94 m). Its x-extent measures 108-110 px depending on the threshold, and the record gives 107 (109 with antialiasing). I used 108.5 px, so the scale is 0.008664 m/px.
- Speed = 3607 x 0.008664 = 31.25 m/s. Using 107-110 px for the length gives 30.8-31.7 m/s.
- Second check: speed ratio A/B (1.636) times B's speed (91.87 px/frame x 24 x scale = 19.1 m/s) gives the same 31.25 m/s.
- Confidence: high, about ±2 %.
