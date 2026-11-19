# q_1883 notes
File fps = question_fps = 24. t=0.5 s -> frame 12.
Method: pelvis/centroid track from scene/ (pixels). Depth per frame taken as proportional to 1/bbox_h (polynomial-smoothed),
focal length f ~3130 px from bbox_h(f24)=380 px, height 2.2 m, distance 18.147 m at t=1 s (frame 24).
3D points = Z*((u-cx)/f,(v-cy)/f,1), rescaled so |P(f24)| = 18.147 m. Speed = one-frame difference x 24.
Acceleration: slope of speed around frame 12 (quadratic fit frames 4-27 and linear fit frames 6-20), for polynomial depth degrees 3-5 and pelvis/centroid:
values 5.6-7.0 (quadratic fit), 6.6-9.0 (linear fit), raw one-frame difference 4-11 (noisy).
Answer: 6.5 m/s^2. Confidence low-moderate (depth from bbox height assumption; pelvis heuristic is jittery).
