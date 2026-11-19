# q_2337 — tennis ball diameter (cm)

Prior: g = 9.8 m/s^2. depth_info: soccer ball 2.80 m, near person 2.002 m, far person 3.13 m. No depth is given for the tennis ball,
so its depth has to be estimated. File fps = question_fps = 24. f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Pixel diameter (diam.py)
The ball is isolated on the white background at its rebound apex (frames 41-47, low speed). Binary extent: 20-22 px wide, 19-23 px
tall. The bottom edge is slightly cut at frames 44-46. Frame 0 includes hand pixels. Adopted D_px = 20.5 px (±1), which matches the scene record (20-21).

## Depth of the tennis ball (three routes)
1. Gravity from the free-fall pixel acceleration (accel.py, accel2.py, quadratic fits to cy). Fall frames 28/29-35: 5.30-5.46 px/frame^2,
   giving Z = g*f/(a*24^2) = 2.38-2.45 m. Sanity check on the soccer ball fall (frames 31-35): 4.86-5.5 px/fr^2, giving 2.36-2.67 m
   against the given 2.80. That is the right scale to about 10%, though noisy. The rebound arc (frames 37-48) gives 4.44, i.e. 2.92 m. This
   is suspect: the soccer ball rebound also gives a much lower acceleration (Z≈4 m, against the true 2.8). The rebound phases are probably affected by
   depth motion or timing irregularity (the record notes a dropped frame between 35 and 36), so I did not use them.
2. Floor-contact rows with a flat-floor pinhole model, converting the Euclidean depths to forward depths (near person feet y=719 ↔ 1.78 m forward;
   left person feet / soccer ball bottom y=577 ↔ 2.78-2.94 m forward). The tennis ball's floor contact is at y=616, which gives Z ≈ 2.41-2.50 m.
3. Pose check: the near person faces image-left and slightly away from the camera, with her arm outstretched. At Z=2.45 m the ball is about 0.85 m from her
   body centre, which is a full arm's reach. Z≈2.9 m would put it more than 1.1 m away, which is not physically possible.

Adopted Z = 2.45 m.

## Answer
D = 20.5 px * 2.45 m / 762.8 px = 0.0658 m ≈ 6.6 cm. The sensitivity is ±1 px → ±0.3 cm and ±0.1 m depth → ±0.27 cm.
A real tennis ball is 6.54-6.86 cm, which agrees. Confidence: moderate to good (about ±7%).
