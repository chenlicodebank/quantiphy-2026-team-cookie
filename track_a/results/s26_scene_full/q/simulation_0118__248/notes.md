# q_248 — diameter of the disc (m)

Prior: toy car speed = 0.05 m/s. 2D top-down scene, static camera, near-orthographic view, so a single m/px scale applies.

## Scale (car speed)
- The car moves uniformly to the right (+x).
- Own template-matching track (car_speed.py), frames 10–120: slope 2.6153 px/frame, residual 0.10 px. The net displacement / 110 frames is 2.6137 px/frame.
- The scene record's mask-centroid track gives 2.609 px/frame, which agrees.
- Using 2.615 px/frame × 24.003 fps = 62.77 px/s, the scale is 0.05 / 62.77 = 7.966e-4 m/px.
- fps 24.003 vs question_fps 24 makes a 0.01% difference, so it is ignored.

## Disc
- "The disc" is taken to be the small black round disc (puck-like) lying on the marble tray, centre (622.8, 443.9) px. It is static in all frames.
- Measured in measure.py:
  - Dark-pixel area-equivalent diameter: 20.3–21.0 px across thresholds and frames.
  - Sub-pixel half-max profile widths along rows and columns: mean 20.71 px.
  - The two methods agree, giving 20.7 px.
- Diameter = 20.7 × 7.966e-4 = **0.0165 m**.
- The disc sits on the tray, a few mm above the car's plane. The camera is far away (near-orthographic), so this is negligible.

## Alternative reading
If "disc" meant the round marble tray: Hough diameter 254.8 px (scene record 259 px), which gives about 0.203–0.206 m. I did not use this reading: the tray reads as a tray, while the black object is a plain disc that looks added to the scene.

Confidence: high in the measurement (~2%); moderate in which object is meant.
