# captured_0034b: measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

## Scene
A static camera looks down at an angle on a wooden table. On the table are a black-and-white soccer ball (static, centre of the table),
a yellow pencil case (static, right of and in front of the soccer ball) and two yellow-green tennis balls.
Two seated people (blurred, faces masked) hold one tennis ball each at the table edges:
- **ball_left**: starts at the left edge of the table, at about (466, 281) px.
- **ball_right**: starts at the back-right corner, at about (821, 253) px.

Both people let go of their balls between frames 24 and 25. The balls roll toward each other.
- ball_left passes *behind* the soccer ball, on the far side from the camera. From frame 32 it is partly hidden.
- The two balls collide at frame 38 (t = 1.583 s).
- After the collision, ball_right rolls down-right in the image, toward the camera. ball_left drifts slowly back to the left, still partly hidden.
- Neither ball has stopped at the end of the video (frame 48).

Everything except the table area is blurred: the video was edited with Segment Anything 2 and has a watermark at the bottom right.

## Files
- `scene.json`: inventory of objects (how to tell them apart, visible frames, static sizes and positions), events, camera, table corners and perspective.
- `tracks/ball_left.csv`, `tracks/ball_right.csv`: one row per frame, frames 0–48. Columns:
  - `cx, cy`: fitted ball centre in pixels. This is the reference point.
  - `diam_px`: fitted diameter.
  - Mask bounding box (`bbox_*`), `mask_w`, `mask_h`, `mask_area`.
  - `visible_frac`: mask area divided by the area of the fitted circle.
  - `occluded`: 1 if the soccer ball hides part of the ball.
  - `merged_with_other`: 1 if the mask touches the hand or the other ball.
  - `method` and `fit_rms_px`.
- `static_measure.json`: soccer ball circle and pencil case oriented box, measured at frames 0 and 48 (they agree, so neither object moves).
- `scripts/`:
  - `track_balls.py`: tracking.
  - `static_objects.py`: static objects.
  - `framediff.py`: camera-motion and duplicate-frame check.
  - `crops.py`, `maskdbg.py`: overlay images used to check the tracks visually.
  - `table.py`: an automatic table outline. It failed because the mask leaked into the people; the corners were read by eye instead.
  - `write_scene.py`: builds `scene.json`.

## How the tracks were measured
- **Mask:** HSV colour mask for yellow-green (H 25–45, S ≥ 28, V ≥ 110). The low saturation limit keeps the pale highlight on top of each ball. The pencil case (H about 23) is cut out with a fixed box.
- **Fit:** a robust least-squares circle fitted to the outline of the mask.
- **Occluded frames:** outline points lying on the soccer-ball silhouette (centre (601.3, 315.0), r 45.6) are dropped. The diameter is fixed at the ball's median unoccluded diameter (29.0 px) and only the centre is fitted.
- **Checking:** the circles and boxes were drawn on every frame from 24 to 48 and looked at. They sit on the balls.

## Reliability
- **Frames 0–24 (balls held):** centres to about ±1 px. Diameters are inflated (32–36 px) because blurred fingers or hands are included in the mask. Use the rolling diameters instead.
- **Frames 25–27 (just after release):** motion blur, and for ball_right a ghost trail. Centres are good to about ±3 px. Diameters are not reliable.
- **Frames 28–48, ball_right:** never occluded. Centres about ±1 px, diameter 28.3–30.2 px (median 29.3).
- **Frames 28–31, ball_left:** clean. Diameter about 28.1–29.1 px (median 28.7).
- **Frames 32–48, ball_left (occluded):**
  - At 34–37 only a thin cap shows (visible fraction 0.24–0.44). Centres are about ±3–4 px.
  - At 38–48 about 55–70% is visible. Centres about ±2 px.
  - The vertical coordinate is the least certain.
- **Possible dropped frame:** between frames 35 and 36, both balls move about twice their usual step (left 587.7→609.0, right 697.2→678.4, against about 10–11 px per frame before). This is probably a dropped capture frame. Keep it in mind for speeds around t = 1.46–1.5 s.
- **Collision, frame 38:** the centres are 29.4 px apart, which is one diameter. The masks merge, so frame 38 is flagged `merged_with_other`. After it, ball_right's image-x motion reverses (656.5 → 662.6) and ball_left's does too (627.2 → 623.8).

## Camera and 3D
- **Camera motion:** none. The background shift is below 0.1 px over the whole clip, and no frames are exact duplicates.
- **Intrinsics:** benchmark lab intrinsics, fx = 763 px, principal point about (640, 360).
- **Distance from apparent size:** a tennis ball of known diameter D at depth Z appears about 763·D/Z px wide. For example, 29 px would correspond to Z ≈ 26.3·D. Use the depth_info given with the question when there is one. Pixel positions can be back-projected as X = (cx − 640)·Z/763 and Y = (cy − 360)·Z/763.
- **Table top corners (read by eye, ±5 px):**
  - back-left (500, 244)
  - back-right (803, 251)
  - front-right (851, 425)
  - front-left (436, 413)
- **Table perspective:** the back edge is 303 px and the front edge 415 px, so rows higher in the image are farther away.
- **Apparent ball size over time:**
  - ball_right stays at about 28–30 px. Its motion is mostly sideways, then toward the camera after the collision (diameter about 29.7 px at the end).
  - ball_left is about 28.7 px before it is hidden.
  - Size changes are within the fit noise (about ±1 px), so depth changes are small (≲ 5%).
- **Static objects at frame 0:**
  - Soccer ball: centre (601.3, 315.0), diameter 91.3 px, bbox [556, 270, 649, 359].
  - Pencil case: centre (695.8, 347.0), length 98 px along its axis (tilted about 25–28° up to the right), width 33 px, bbox [648, 320, 739, 381]. The ends are slightly rounded or blurred, so allow ±3 px.
- **Not measured:** the people's sizes, because they are blurred.
