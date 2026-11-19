# captured_0039s — measurement record (pixels / seconds only)

**Video:** a real lab recording (Orbbec, 24 fps, 49 frames, 1280x720). The background was replaced with green by SAM2, and there is a watermark at the bottom right. The scene is 3D and the camera does not move. A small white ball sits still on a wooden table. Behind it are a pink bottle, a white cup, two leaning playing cards, a flat card, and a black card or phone with a yellow sticker. The ball starts rolling toward the camera and to the left (down-left in the image) at frame 18. It rolls off the front edge of the table after frame 40, falls with heavy blur in frames 41-44, and leaves through the bottom of the image from frame 45 on.

## Files
- `scene.json`: inventory, static-object pixel extents (frame 48, after the ball is gone), table corner points, camera info and events.
- `tracks/ball.csv`: the final ball track. Columns: frame, t, visible, ref_x/ref_y (the visible centre), bbox, diameter_px, mask ellipse major/minor, mask_height_px, occluded_or_cut, blur_level (0 = none, 1 = mild rolling blur, 2 = strong falling blur), method, phase.
- `tracks/ball_raw.csv`: raw per-frame mask stats: centroid, bbox, area, equivalent diameter, ellipse fit, circle fit.
- `camera_shift.json`: per-frame image shift against frame 0 (phase correlation on the static props). The maximum is 0.09 px, so the camera is static.
- `frame_diffs.json`: mean absolute difference between consecutive frames.
- `static_auto.json`, `table_auto.json`: automatic colour-mask extents. The bottle box there includes the pink card, so prefer the values in scene.json.
- `scripts/`: `track_ball.py` (ball mask and fits), `make_ball_csv.py` (picks the reference point), `camera_static.py`, `table_geom.py`, `frame_dups.py`.

## Method
- **Ball mask:** pixels that differ from frame 48 (no ball in it) by more than 25, and that are bright and unsaturated (V − 1.5·S > 100).
- **Frames 0-40:** the centre and diameter come from a least-squares circle fit to the mask contour. The shaded bottom of the ball is partly lost against the table, so the plain centroid sits about 0.2-0.5 px too high and the bbox is too short. The circle fit corrects for this, and overlays (frames/ov) confirm it hugs the ball outline.
- **Frames 41-43:** the centre is the middle of the blurred streak's bbox, i.e. the position at mid-exposure.
- **Frame 44:** the ball is cut off by the bottom of the image (y = 719), so the centre is estimated as bbox top + width/2. Treat it as unreliable.

## Reliability
- **Rest position:** (564.95, 437.95) ±0.1 px. Apparent diameter at rest is 20.7 px.
- **While rolling:** the apparent diameter grows steadily as the ball approaches the camera: 22.2 px at frame 19, 26.6 at 25, 31.2 at 30, 35.5 at 35, 42.3 at 40. This is the main depth cue: with f ≈ 763 px, depth ∝ 1/diameter. Per-frame circle diameters are good to about ±1 px. Horizontal blur of about 4 px/frame adds roughly 1-2 px, so smooth over several frames.
- **Centres while rolling:** about ±0.5 px.
- **Falling frames 41-44:** bbox widths of 49-51 px are inflated by blur and mask bleed, so do not use them as the diameter. Centres are ±3 px vertically.

## Events
| Event | Frame | t (s) |
|---|---|---|
| At rest | 0-17 | 0-0.708 |
| Motion starts (sub-pixel shift; first clear step of ~5 px at frame 19) | 18 | 0.75 |
| Last frame on the table top | 40 | 1.667 |
| Leaves the edge / starts falling | 41 | 1.708 |
| Out of view | 45 | 1.875 |

Nothing in view pushes the ball. It goes from rest to about 5 px/frame within one frame, so it was probably pushed from outside the mask, or by something removed with the background.

## Ambiguities
- **Frame 35→36:** the step is about 12 px, roughly twice its neighbours (≈5.9 px). This looks like a dropped capture frame. The frame indices are kept as they are; anyone differencing velocities across 35/36 should be aware of it.
- **Small frame-to-frame changes at frames 3-7 and 11-13:** these come from compression or exposure flicker. No object moves then.
- **The ball's shadow and reflection on the table** sit just below it and are excluded from the mask.
- **Static object extents:** read from grid crops, ±2 px. The table back-right corner is approximate (±5 px), and the horizon is not visible.
- **Real sizes:** no metric scale is assumed anywhere in this record.
