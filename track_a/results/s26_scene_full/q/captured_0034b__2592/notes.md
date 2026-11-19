# q_2592: speed of the right tennis ball at t = 1.2 s (cm/s)

- t = 1.2 s -> frame round(1.2*24) = 29 (question_fps = file fps = 24).
- Track: scene/tracks/ball_right.csv. Circle fits checked by drawing them on frames 25-35 (crops.py ->
  frames/right_25_35.png). They sit on the ball for frames 28-35. Frame 27 is a bit blurred and frames 25-26 have a ghost/hand.
  The ball is released at frames 24-25 and slows slightly as it rolls left along the back of the table. The step at 35->36
  (a possible dropped frame) is outside the window.
- Lab method card: f = 0.5959*1280 = 762.8 px, principal point (640, 360), depth Z = 0.776 m (depth_info at t = 1.2 s),
  held constant over the short window (the apparent diameter stays at about 29 px, so the motion is lateral). Centres are back-projected
  to 3D, then velocity is taken from the 3D positions (velocity.py).
- Results (cm/s): linear fit over frames 27-31 = 29.2, 28-32 = 27.0, 27-33 = 27.8, 28-34 = 26.2, 29-33 = 25.8. Mean forward
  difference over 27..31 = 29.0. Normalising the ray (treating depth as Euclidean distance) lowers these by about 3%.
- **Answer: 27.0 cm/s** (middle of the 5-frame windows around frame 29; spread about ±2 cm/s).

## Scale inconsistency (important)
The prior (ball diameter 6.7 cm) does not agree with depth_info at f = 763 px. The ball is 29.2 px across, which at 0.776 m would make
it 2.95 cm. The same holds for the soccer ball (91 px at 0.894 m -> 10.7 cm). At f = 763 px, a 6.7 cm ball implies Z ≈ 1.75 m.
Using the prior as the scale instead (6.7 cm / 29.2 px) gives about 287 px/s * 0.229 = 66 cm/s, which is 2.4x higher. I followed the
stated reference convention (clicked centres back-projected with the measured depth and f = 0.5959*W), so the answer is 27 cm/s.
Confidence: moderate. The measurement under that convention is good to about 5-8%, but it is uncertain which scale the reference used.
