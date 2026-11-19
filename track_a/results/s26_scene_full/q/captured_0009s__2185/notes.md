# q_2185: basketball's distance from the camera at 1.8 s

- The question's depth_info states this directly: at t = 1.8 s, distance_ball_camera = 1.5835 m. That is frame 43 at 24 fps; the file and the question both run at 24 fps.
- Second route (check.py): I took the scene track's fitted ball diameter and scaled it so the t = 0 depth comes out at 1.321 m (136 px, which gives a ball diameter of 0.225 m). Range is inversely proportional to pixel diameter, so:
  - frame 43 (107 px) gives R ≈ 1.65 m;
  - frame 46, the apex (110 px), gives R ≈ 1.60 m, against 1.5795 m given.
  The ball is affected by motion and the hand-cut notch at t = 0, so this route can be off by a few percent. It agrees within about 4%.
- Answer: 1.5835 m, the measured depth given with the question. High confidence.
