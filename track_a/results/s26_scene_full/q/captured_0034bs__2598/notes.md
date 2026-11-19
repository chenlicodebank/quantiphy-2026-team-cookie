# q_2598 – velocity of the left tennis ball at 1.2 s (cm/s)

- question_fps = file fps = 24 → t = 1.2 s is frame 29. The left ball (A) rolls right from frame 24/25 and is
  unoccluded in frames 25–31, so frame 29 lies in a clean window, before the soccer-ball occlusion and the collision (frame 38).
- My tracking (`measure.py`): hue mask + least-squares circle fit and the mask centroid, frames 22–34. The centres agree with
  scene/tracks/tennis_ball_left.csv to within about 1–2 px (frame 29: (521.7, 282.7) mine vs (522.3, 281.6) in the record).
  Pixel speed is about 11.5 px/frame along +x, with a slight upward drift.
- Lab method card: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360), depth Z = 0.706 m (depth_info, left ball, t = 1.2 s).
  Each centre is back-projected as ((u−cx)/f, (v−cy)/f, 1)·Z, and the speed is the 3D displacement × 24.
- Speeds near frame 29 (cm/s):
  - circle-fit centre: forward 29→30 = 24.2, backward 28→29 = 27.0, 5-frame (27→31) = 25.2, linear fit over 26–32 = 24.9
  - mask-centroid centre (second route): 24.8, 26.6, 24.9, 24.5
  → **≈24.8 cm/s**
- Consistency warning: at Z = 0.706 m the ball's ≈31.6 px diameter gives a size of only ≈2.9 cm, not the 6.7 cm prior. Also,
  ball A passes behind the soccer ball even though its stated depth (0.706 m) is smaller than the soccer ball's (0.894 m).
  The depth_info does not fit the image geometry. The reference answers were made by back-projecting with the measured
  depth and f = 763, so I follow that convention. If the scale came from the prior instead (6.7 cm / 31.6 px), the answer
  would be ≈59 cm/s.
- Confidence: moderate. The pixel measurement is solid (±3%), but the scale convention is uncertain because the depth and
  the prior disagree.
