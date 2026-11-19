# q_2628 — soccer ball velocity at 1.6 s (cm/s)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px, pp (640,360).
t = 1.6 s -> frame 38. At that point the soccer ball is rolling back (up-left in the image, away from the camera)
after the collision with the basketball at frames 19/20.

depth_info: the 4th line is labelled "soccer_ball" but 2.412 m is the basketball at 1.6 s (basketball pixel
diameter 69.4 px gives 2.55 m by size, the same 0.95 ratio as at 0.6 s: 74.2 px -> 2.39 vs given 2.27).
Soccer ball: 2.758 m at frame 14, 3.052 m at frame 38.

## Measurements (measure.py)
Own re-measurement of the soccer ball, frames 26-46: median-background difference mask, circle fit to the
contour. Centres agree with scene/tracks/soccer_ball.csv to 0.1-0.3 px. Frame 38: (498.8, 351.6), d = 44.4 px.
Overlay checked in frames_f38.png. Pixel step around frame 38: about 4.3 px/frame (35->36 is doubled because of a
dropped frame, so it is excluded).

## 3D speed (velocity.py, diamtrend.py)
Positions = back-projection of the centre with the camera distance at each frame.
- Route A (main): distance per frame from the ball's pixel diameter (Z ∝ 1/d, linear trend over frames 28-46,
  scaled to 3.052 m at frame 38). Five diameter estimators give a radial rate of 30-42 cm/s (median about 36).
  Lateral rate about 41 cm/s (4.3 px/frame * 3.052/763 m/px * 24).
  Speeds: forward diff 38->39 51; mean of steps 36-40 54.5; chord 36->43 54.8; mean of steps 33-43 without the
  dropped-frame step 55.4 cm/s.
- Route B (check): ball centres on a plane through the four given 3D points (soccer and basketball at 0.6 s and
  1.6 s), plane residuals up to 2.3 cm. This gives a steeper depth rate (radial about 56 cm/s) and a speed of
  65-67 cm/s. The plane's tilt is sensitive to those 2 cm residuals, and the frame-14 soccer point may be slightly
  airborne after the kick. The diameter trend contradicts B's depth rate. The diameters follow the given depths
  well (basketball diameter ratio 1.069 vs given distance ratio 1.063), so I trust Route A.
- If the reference's smoothing window spans the dropped frame 35->36, the value would be about 60-62.

Answer: 55.5 cm/s. Confidence: moderate (about ±10%, driven by the depth-rate component).
