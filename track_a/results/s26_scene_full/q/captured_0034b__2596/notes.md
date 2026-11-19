# q_2596: total distance traveled by the left tennis ball (cm)

File fps = question_fps = 24, 49 frames, 1280x720, static camera.

## Method (lab method card)
- Track: scene/tracks/ball_left.csv (circle-fit centres). Checked on overlay crops (overlay.py -> frames/overlay.png)
  for frames 24-48, including the occluded frames behind the soccer ball (33-48) and the collision (38): the circles sit on the ball.
- Ball is held (jitter of about 1 px) for frames 0-24, released at about 24/25, rolls right behind the soccer ball, hits the right ball at frame 38, then drifts back left.
- 3D: f = 0.5959*1280 = 763 px, principal point (640, 360). Each centre is back-projected along its ray at the given
  distance 0.706 m (depth_info, t = 1.2 s). The ball's apparent size and image row stay almost constant, so the depth is taken as constant.
- Path length = sum of frame-to-frame 3D displacements (path.py).

## Results (path.py)
- raw, frames 0-48: 17.4 cm; raw, frames 24-48: 16.6 cm
- 5-frame moving average (segments split at release frame 24 and collision frame 38): 16.45 cm over 0-48, 15.5 cm over 24-48
- 3-frame: 16.8 / 16.0; 7-frame: 16.2 / 15.1
- second route, image-x motion only (24-48): 16.7 cm. Vertical noise adds little.
- Answer: **16.4 cm**.

## Caveat: the scale sources disagree
With f = 763 and Z = 0.706 m, the ball's 28.7 px diameter gives 2.7 cm, not the 6.7 cm in the prior. Likewise the soccer
ball (91 px at 0.894 m) would be 10.7 cm across. If the scale is taken from the prior instead (6.7 cm / 28.7 px), the
path is about 42.8 cm. I followed the stated reference convention (back-projection with depth_info and f = 763).
Confidence: moderate on the pixel path (±5%), low on which scale convention the reference used.
