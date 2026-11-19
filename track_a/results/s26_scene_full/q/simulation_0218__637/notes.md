# Q637 – length of the big robot (m)

Prior: robot speed 5.924 m/s. At 24 fps (file rate equals question_fps) that is 0.24683 m per frame. The robot moves at constant speed, horizontally, and the camera is static.

## Method
- I took pixel tracks from `scene/tracks/robot.csv` and checked them on frame 21 with a grid: the rear of the tracks is at x≈643 and the drill tip at x≈1283, which matches the CSV value of 640.3 px.
- The scene shows perspective: different robot parts move at different pixel rates. The near-side rear corner moves 50.90 px/frame, the drill tip 54.02, and the far rear corner 45.80.
- For each point, the scale at that point's depth is 0.24683 m / (its pixel rate). The world x of a point is (u − 960) × scale.
- Length = X_tip − X_rear (`measure.py`).

## Results
- Per-depth route: 3.014–3.017 m on every frame from 9 to 27, even though the pixel length grows from 603 to 660 px over those frames. This holds the value steady across frames.
- Single-scale route: the frame-21 centred length is 640.3 px. Using the origin_est rate of 52.46 px/frame gives 3.013 m, which agrees.
- Frames 29–32 use the far-side rear corner and give about 2.97 m. The bounding box is the maximum extent, so I use the near-side value.

Answer: **3.015 m**. Confidence: high (about ±2%).
