# internet_0053: measurement record

The video is real footage at 30 fps: 81 frames (0-80), 1920x1080. Time is t = frame/30.
All values are in image pixels (x to the right, y downward) and seconds. No metric scale was guessed.

## Scene
- The camera is static and shows a side view of a path in front of a tennis-court fence with green screening.
- One person rides a black two-wheel electric kick scooter from left to right. The face is greyed out by anonymisation. They wear a white long-sleeve top, a light cap and khaki cargo trousers.
- The rider stands on the deck with both feet for the whole clip. I saw no kicking in the frames checked (0, 24, 40, 56 and 72, plus the sheet every ~5 frames).
- The rider is fully visible in frames 0-73. The front wheel touches the right image edge at frame 74 and is out of the frame from 75. The front part of the rider and scooter is cut off by the edge from frame 75 to the end. The rear wheel is still visible at frame 80.
- No other moving objects. Leaves flicker slightly in the wind.

## Files
- `scene.json`: inventory (the moving unit and the static objects with pixel bboxes and sizes), camera, perspective cues and events.
- `tracks/rider_scooter.csv`: one row per frame (0-80). Columns:
  - `rear_wheel_cx`, `front_wheel_cx`: wheel centre x. Each is the centre of the wheel's dark run in rows 700-712.
  - `rear_run_*`, `front_run_*`: the raw runs. These are chords of the lower wheel half, not the full wheel width.
  - `wheelbase_px`: front centre minus rear centre. Measured in frames 0-73. In frames 74-80 it comes from a linear trend, which is about +1.5 px too high compared with frames 70-73.
  - `wheel_diam_px` = 0.267 x wheelbase.
  - `scooter_length_px` = 1.267 x wheelbase. This is the outer length, back of the rear wheel to front of the front wheel. Both ratios come from full wheel extents read by hand at frames 0, 40 and 72.
  - `scooter_cx`: midpoint of the wheel centres. This is the recommended horizontal reference point. `scooter_cy` is the wheel-axle height.
  - `bbox_*`: x from the back of the rear wheel to the front of the front wheel, clipped at 1919. y from the cap top to the wheel bottom.
  - `bbox_cx`, `bbox_cy`: centre of that box.
  - `height_px`: cap top to ground contact.
  - `head_top_replaced`: 1 where a leaf outlier was replaced by the 9-frame median (frames 52-55, 24).
  - `upper_body_x/y`: an independent chained template track of the rider's body. x is anchored to 1335 at frame 45.
  - `cam_dx`, `cam_dy`: background drift.
  - `occluded`: 1 when the scooter is cut by the image edge (frames 74-80).
- `scripts/` contains, in run order:
  - `camera_and_bg.py`: camera drift and median background. It writes `bg_band.npy`; rerun it before the other scripts because `finalize.py` deletes that file to save space.
  - `chain_track.py`: the upper-body track.
  - `wheels.py` and `wheels2.py`: exploration scripts.
  - `build_track.py`: writes the final CSV and the check overlays in `../frames/check`.
  - `zoom_ruler.py`: zoomed crops with pixel rulers, used for the hand readings.
  - `track.py` and `template_track.py`: first attempts that failed.
  - `finalize.py`: validates scene.json and removes large files.

## How it was measured and how reliable it is
- **Camera:** phase correlation of the ground strip against frame 0. The drift is at most about 2 px in x and 3.6 px in y, which is negligible next to motion of 15-20 px per frame. It is not subtracted from the track columns. If needed, subtract `cam_dx` from the x values.
- **Wheel centres:** this is the most reliable part of the record, about ±1 px. Overlays confirm the centres at frames 0-80 every 8. The hand-read centres at frames 0, 40 and 72 agree within 1 px. In frames 79-80 the rear wheel was found with a stricter threshold (it touches the hydrant base), so its centre there is about ±2 px.
- **Scooter length:** the hand readings are 207.0 px (frame 0), 192.5 px (frame 40) and 180.5 px (frame 72), each ±2 px. A question giving the scooter's real length should take its pixel length at the frame(s) it uses, or at a mid-clip frame (about 192 px).
- **Head top:** from colour background subtraction, ±1-2 px, and checked against the zooms. The cap top is at 379 in frame 0 and stays at 384-386 from about frame 14 on.
- **Rider standing height** (cap top to shoe sole): about 315 px at frame 0 and about 304 px at frame 40, ±3 px. Rider plus scooter height, from cap top to ground: 341 px at frame 0, 327 px at frame 40 and 323 px at frame 72.
- **Static objects:** hand readings from ruler zooms, ±2-3 px.

## Ambiguities
- **Perspective:** the video is labelled 2D, but the path is slightly oblique. Moving right, the scooter shrinks by about 12% (wheelbase 161.5 → 142.5 px) and the ground contact rises from y 719.5 to 707.5. Pixel sizes therefore depend on the frame. The benchmark's convention uses one scale factor; when converting, pick the prior's pixel size at a stated frame, or at mid-clip if no frame is stated.
- **Slowing down:** the wheel step falls from about 19.5 px per frame (frames 0-10) to about 15 px per frame (frames 70-80). Part of this is the perspective shrink of about 12%; the rest is a real slow-down.
- **Partial visibility:** from frame 74 the bbox is clipped at the image edge, so `bbox_cx` moves less than the scooter does. Use `rear_wheel_cx` or `scooter_cx` there (scooter_cx in frames 74-80 = rear + trend wheelbase/2).
- **Contrast and lighting:** the scooter is black on a dark background, so it is hard to separate. Wheels were measured only where they overlap the grey asphalt. Frames 18-32 have a bright, sunlit background at the gate; the wheel track is fine there.
- **Occlusion:** the rider passes in front of the lamp post (frames 0-4), the bench (about 45-66) and the hydrant (about 74-80). None of these hide the rider.
