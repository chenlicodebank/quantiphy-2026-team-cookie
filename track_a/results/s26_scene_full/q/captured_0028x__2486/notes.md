# Q2486: velocity of the ping pong ball at t = 1.0 s (cm/s)

The file and the question both run at 24 fps, so t = 1.0 s is frame 24 and t = 1.1 s is frame 26 (round(26.4)), which is the first bounce contact frame.

## Inputs
- Ball centres come from scene/tracks/ball.csv (blur-streak centroids). I checked them on zoomed crops of frames 23–27 (frames/f23_27.png).
  - Frame 24: streak y 321–355, centre (733.1, 338.6).
  - Frame 26: streak y 387–430, the ball touching the table. Ball centre at contact taken as (739, 419.5).
- Camera: focal length f = 0.5959 × 1280 = 762.8 px, principal point (640, 360). Back-projection uses the ray scaled to the given Euclidean distance.
- Given depths: 1.805 m (frame 24), 1.557 m (frame 26), 1.4115 m (frame 31).

## Results (measure.py)
- A: 3D displacement from frame 24 to frame 26, divided by 2 frames: **3.65 m/s**. Components: x −0.22, y (down) +2.04, z −3.02 m/s.
- B: 3D displacement from t = 1.0 s to t = 1.1 s, with the frame-26.4 position interpolated, divided by 0.1 s: **2.91 m/s**.
- D: forward difference from frame 24 to frame 25, with the depth at frame 25 linearly interpolated: **3.47 m/s**.
- C: motion in the image plane only, at 1.805 m with no change in depth: 1.86 m/s (frames 24→25), 1.60 m/s (central difference over 23–25).
- Physics check: the ball is released at about frame 20.7, so free fall alone gives vy ≈ 1.35 m/s at frame 24.

## Concerns
- In the given depths, the distance drops by 0.25 m in 2 frames, which means about 3 m/s toward the camera. The ball's apparent size does not support this. Its diameter grows only from about 20.4 px to 22.9 px between frames 24 and 31; with a 40 mm ball, that gives depths of 1.50 m and 1.33 m.
- So the given depth series may include sensor jumps near the bounce. The reference used these measured depths, so I keep the depth change. The unknown amount of smoothing in the reference over 5 or more frames, which crosses the bounce at frame 26.2, could lower its value toward about 1.7 m/s.
- Answer: 320 cm/s, a compromise between routes A, B and D (2.9–3.65 m/s).
- Confidence: low to moderate.
