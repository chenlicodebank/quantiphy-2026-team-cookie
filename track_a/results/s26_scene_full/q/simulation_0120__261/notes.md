# q261 — length of the square tray (with two sculptures) next to the chessboard

The video is a 2D top-down view with a static camera. The tray is the dark grey square on the coffee table, above and to the right of the chessboard.

Scale comes from the prior (robot cleaner speed = 1 m/s). In scene/tracks/robot_vacuum.csv the vacuum moves in a straight line at a constant speed:
- mean per-frame step over the unoccluded frames 0–32: 8.407 px
- linear fit: 8.401 px/frame
- net distance / 48 frames: 8.413 px/frame

8.407 px/frame × 24.008 fps = 201.9 px/s, so the scale is 201.9 px per metre. The file fps (24.008) and question_fps (24.0) differ by only 0.03 %, which doesn't matter here.

Tray size (measure.py, intensity profiles on frame 0, edges taken at half the step between levels):
- horizontal: x 513.0 → 574.6, so 61.6 px
- vertical: y 463.5 → 526.6, so 63.1 px (the bottom edge may include a little of the tray's side or shadow)
- I used 62.5 px as the side length.

Length = 62.5 / 201.9 = 0.310 m (the range is 0.305–0.313 m depending on which edge set is used).

Second check: the visual read of the 3× gridded zoom gives about 61 × 65 px, which agrees.

Caveat: the tray sits on the table, so it is somewhat nearer the camera than the floor-level vacuum, and its true size is probably a few percent smaller. Following the 2D convention, I used a single scale from the prior.

Confidence: moderate to high, within about ±5 % under that convention.
