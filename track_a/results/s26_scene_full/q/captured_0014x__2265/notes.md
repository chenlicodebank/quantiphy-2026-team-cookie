# q2265 – displacement of the ball, 0 s to 0.6 s (cm)

File fps = question_fps = 24 → frames 0 and round(0.6*24)=14.

Method (lab card): f = 0.5959*1280 = 762.8 px, principal point (640,360). Positions = unit ray x depth_info
(Euclidean camera distance): 1.8180 m at t=0, 1.7288 m at t=0.6.

Ball centre (own measurement, measure.py / circfit.py, background = median of frames 32-48):
- Frame 0 (at rest, lower part hidden by the board's top edge): circle fit to upper outline → (545.2, 295.5),
  r ≈ 13.5 px (consistent with r 14.3 px at frame 14 scaled by depth ratio → 13.6). The scene record's 297.5
  centroid is biased down by board-edge pixels.
- Frame 14: mask bbox y 338-371 (5 px vertical motion blur), x 533-561; centre (547.5, 353.5)
  (circle fit upper arc 351.8, centroid 354.0).

Displacement = |P14 - P0| = 16.06 cm. Sensitivity: v14 ±1.5 px → 15.8-16.3; scene-record centres → 15.7;
treating depth as z instead of range → 16.6.

Check: prior a = 4.6 m/s² from start ≈ frame 8-8.5 gives 0.5·4.6·(0.23-0.25 s)² ≈ 12.5-14.4 cm along the
slope; plus the ball's motion is consistent order-of-magnitude (depth change 8.9 cm + transverse 13.4 cm → 16 cm).
Confidence: moderate-high (±5%).

Answer: 16.0 cm
