# q_3107: ball velocity at 1.50 s (internet_0048)

- **Time base:** fps = question_fps = 30, so t = 1.50 s is frame 45. That is the apex of the arc (y min 304.8 px).
  I checked the frame at 2x zoom: the ball centre is at about (793, 305), which matches the record in scene/tracks/ball.csv.
- **Scale from the prior (g = 9.8 m/s²):** I fitted a parabola to the ball's y over the clean free-flight frames 36–60
  (release at about 35, bounce at 61). The fitted acceleration is 4.14 px/frame² (raw coordinates) and 4.13
  (camera-compensated). The mean raw second difference is 4.21. That gives a scale of 9.8 / (4.13 × 900) ≈ 2.63 mm/px.
- **Velocity at frame 45:** the horizontal velocity is about 64.4–64.9 px/frame and the vertical velocity is about 0.5
  px/frame (apex). The raw forward difference is 64.46 px/frame (64.77 camera-compensated).
  - Speed = 64.5 × 30 × 2.63e-3 ≈ 5.09 m/s.
  - Camera-compensated: 5.14 m/s.
- **Second-route check:** fits over the windows 38–58, 36–47 and 44–60, and both coordinate sets, all give
  5.06–5.15 m/s. Forward, backward and central differences agree to within 0.1 %.
- **Answer:** 5.1 m/s. Confidence: high (about ±2 %).
