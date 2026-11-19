# Q512: droplet speed at t = 0.05 s

- This is a 2D simulation at 60 fps (question_fps is also 60, so no re-timing). t = 0.05 s is frame 3. The speed is the backward difference between frames 2 and 3, times 60.
- Scale comes from the prior. A quadratic fit of the drop's mask centroid (scene/tracks/drop.csv, using render indices; frame 7 is a duplicate and render step 8 is missing, but neither affects frames 0–6) gives a = 31.67–31.70 px/frame². The residuals are under 0.4 px. So m/px = 9.7 / (31.69 × 3600) = 8.50e-5.
- The raw step from frame 2 to 3 is (−1.45, 80.86) px, which is 80.87 px. That gives a speed of 80.87 × 60 × 8.50e-5 = **0.4125 m/s**.
- Second route: the step from the fitted parabola gives 0.4113–0.4117 m/s. The same answer holds whether the fit uses frames 0–6, 1–6 or 0–10. Bounding-box top/bottom edges step 80–81 px between frames 2 and 3 with second differences of about 32 px, which also agrees. If the drop started exactly from rest at frame 0, the speed would be 2.5 × 9.7 / 60 = 0.404 m/s. The fit puts release a little before frame 0, which explains the 0.412.
- My own background-difference mask (measure.py, threshold 18) broke the drop into fragments, so I relied on the record's hole-filled centroids instead. Their area stays steady at about 3850 px.
- Answer: 0.412 m/s. Confidence is high (about ±2%).
