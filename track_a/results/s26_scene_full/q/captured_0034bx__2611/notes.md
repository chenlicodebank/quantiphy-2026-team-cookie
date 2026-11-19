# q_2611: total distance traveled by the right tennis ball (cm)

Clip is 24 fps (file fps = question_fps = 24), 49 frames, 1280x720, segmented lab capture.
Right tennis ball = scene record's `tennis_ball_B` (starts at far-right corner (820,256)). Checked on frames 15, 29, 33, 44, 48:
the track sits on the ball. Rest frames 0-23; the push starts at frame 24. It collides with the left ball at frame 38,
reverses, and drifts toward the camera until frame 48 (still moving at the end).

## Pixel path (final.py)
- Raw track path, frames 23-48: 193.7 px. Net 23->38 = 164.3 px; 38->48 = 28.4 px.
- Savitzky-Golay (w5) fitted separately on each side of the collision: 165.4 + 29.6 = 195.1 px. Value used: about 194.5 px (seg1 smoothed + seg2 raw).
- The frame 35->36 timing jitter (double step) does not change path length.

## Depth along the path
The ball's yellowness-threshold width (prof.py) is about 27 px at rest (frames 10/20) and still 26-28 px at frames 41-48.
That means no measurable size change, so the camera distance is roughly constant (within about 3%) along the path.
A tilted-table plane model (path.py) predicted 28->35 px growth, which is contradicted. That model was rejected, and the depth is taken as constant.

## Scale: conflict between the card and the prior
- Visual ball diameter (zoomed crops, crop.py) is about 31 px: frame 15 at rest, x 806-837; frames 29 and 33 vertical extent about 30-31 px.
- Card f = 763 px with depth 0.776 m would make the ball 3.1 cm, contradicting the exact 6.7 cm prior by about 2x.
  The clip appears to be rescaled relative to the main camera, so the card f cannot be applied to these pixels.
  Literal card result: 194.5 px x 0.714 m (z) / 763 = 18.2 cm. Rejected.
- Prior-based (main route): scale = 6.7 cm / 31 px = 0.216 cm/px at the ball's (constant) depth.
  -> 194.5 x 0.216 = 42.0 cm. With D = 32 px -> 40.7 cm; with D = 30 px -> 43.4 cm.
  Equivalent: f_eff = D·z/0.067 ≈ 330 px in z terms (z = 0.714 for Euclidean distance 0.776 at 23° off-axis).
- Second route: the soccer ball (96 px at 0.894 m), if it is size 5 (22 cm), gives f_eff ≈ 385, about 763/2. This hints at a
  2x-downscaled main-camera image and gives 194.5 x 0.714 / 381.5 = 36.4 cm. The left ball (≈31-33 px at 0.706 m) instead
  gives f_eff ≈ 310-330, agreeing with the right-ball prior route.

## Answer
41.0 cm: prior-based 42.0 cm, weighted slightly toward the larger visible diameter (the segmentation trims the pale rim)
and the soccer-ball route. Confidence: moderate. The main uncertainty is the scale (±5-10%), not the track.
