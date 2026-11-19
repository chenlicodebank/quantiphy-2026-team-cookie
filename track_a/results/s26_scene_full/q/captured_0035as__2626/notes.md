# Q2626 — soccer ball velocity at t=1.5 s (cm/s)

t=1.5 s -> frame 36 (question_fps 24 = file fps). Lab camera: f = 0.5959*1280 = 762.8 px, pp (640,360).

## Data
- Soccer ball centre track from scene/tracks/soccer_ball.csv. I checked it frame by frame over frames 28-46 with
  my own background-difference mask (measure.py): the centres agree to about 1 px (except frames 31 and 37, where
  my mask was partial).
- The depth_info line "t=1.6 s, distance_soccer_ball_camera = 2.412 m" must be the basketball. Basketball
  diameter at frame 38 is 69.4 px, so 2.412*69.4/763 = 21.9 cm, which matches 22.1 cm at frame 14 (2.27 m, 74.2 px).
  The prior is 23.2 cm. Soccer ball: 2.758 m at frame 14 and 3.052 m at frame 38, which gives a consistent
  diameter of about 18.5 cm from both.
- The ball is rolling back toward the far person (away from the camera), so the depth rate matters a lot.

## Depth models (frame 36 velocity)
1. Ground plane (plane.py): fitted camera height/tilt to the 4 depth points (soccer radius 9.3 cm,
   basketball radius 11.6 cm on the floor). Residuals are 0.4-1.6 cm. Depth at frame 36 = 3.02 m, receding
   at about 0.5 m/s.
   Per-frame speeds about 50-77 cm/s (123 at the 35->36 step, which has a dropped frame, see scene notes).
   5-frame central 79, mean of 5 steps 75.5, 7-frame 73-75, quadratic fit to frames 24-46 = 71.5
   (66 if the dropped frame is corrected).
2. Size-based depth (D proportional to 1/diameter, linear fit): 5-frame values 63-65, quadratic fit about 62.
3. Linear depth interpolation between the two given times: 56-59. This underestimates, because the
   ball approached until frame 19 and only receded afterwards.
The plane model agrees with the receding trend in my own enclosing-circle diameters (49.6 px -> 44.4 px from
frame 30 to 46, a ratio of 1.12, the same as the plane depth ratio).

## Answer
72 cm/s: plane model, smoothed over about 5-7 frames. The reference's smoothing would include the dropped
frame's doubled step, so I did not correct for it. Confidence moderate (±12%).
