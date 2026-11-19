# q2485 – maximum height of ping pong ball (cm)

Asked quantity: how high the ball rises after the first bounce. The bounce is at t=1.1 s (frame 26, depth 1.557 m) and
the maximum height is at t=1.3 s (frame 31, depth 1.4115 m). The answer is the height of the ball centre at the apex
above its centre at contact with the table, which equals the height of the ball's bottom above the table.
question_fps = file fps = 24.

## Method (height.py, fit.py)
- I used the ball track from scene/tracks/ball.csv. The masks were checked; I also looked at frame 26 myself. In that
  frame the blurred blob spans y≈390–426, and the ball touches the table near y≈426.
- Back-projection with f = 0.5959·1280 = 763 px, cx,cy = 640,360. Each depth was used as the Euclidean distance
  along the ray.
- Bounce point: I took the f26 centroid (738,409); the contact centre (739,~416) is the alternative. Apex point: f31
  (748.1,304.3); f32 (750.2,301.3) is the true pixel apex.
- 3D displacement from bounce to apex = (0,-20.2,-14.7) cm, magnitude 25.0 cm. With the contact centre and f32 it is
  26.0–26.5 cm. The camera-y component alone is 20–22 cm.
- The camera is tilted down about 35°. Two independent checks show this:
  (a) the ratio dY/|d| = 0.81 (≈cos 36°);
  (b) the pixel acceleration of the arc, 7.67 px/frame² at 1.41 m, gives 8.2 m/s² in the image plane.
      That is 0.83·g, so the vertical is foreshortened by cos θ≈0.83.
  So the motion from bounce to apex is almost purely vertical in the world. The vertical height is therefore the
  full 3D magnitude, not the camera-y component.

## Second route (physics)
A parabola fitted to frames 27–35 puts the apex at frame 31.86 and the impact at frame 26.0–26.4. That is a rise
time of 0.221–0.227 s, so H = g t²/2 = 23.9–25.3 cm. The interval between bounces 1 and 2 (about 0.46 s) gives
H = gT²/8 ≈ 25.8 cm. Both agree with the 25–26.5 cm from back-projection.

Answer: 25.5 cm, the middle of the back-projection range 25.0–26.5. Confidence: moderate-to-good, roughly ±8%.
