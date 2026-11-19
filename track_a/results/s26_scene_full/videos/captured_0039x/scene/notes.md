# captured_0039x — measurement record (pixels, seconds)

Lab video (Orbbec camera, 24 fps, 49 frames, 1280x720, 3D scene). The background has been blacked out by
segmentation; only the table, its contents and the ball remain (there's a watermark at the bottom right:
"Modified with Segment Anything 2 Demo"). Time t = frame/24. Per the task conventions, focal ≈ 0.5959·1280 = 762.8 px
and the principal point is ≈ (640, 360). No metric scale is assumed anywhere in this record.

## Scene
A small grey/off-white **ball** (the only moving object) rests at the back edge of a wooden **table** top, left of a
**pink bottle**, during frames 0–17. It starts rolling at frame 18 (t = 0.75 s) toward the camera and to the
left. It crosses the table top diagonally (image path (565,440) → (479,523)), reaches the front edge around
frame 40 (t ≈ 1.667 s), then falls over the front edge just left of the **dark blue card**. It falls through frames
41–44 and has left the image at frame 45 (t = 1.875 s). Static props: a white cup, a leaning playing card plus a
flat stack of cards, the blue card with a yellow sticker, and the black table pedestal. Image extents, corners and
sizes for all of them are in scene.json.

## Files
- `scene.json`: inventory (description, how to tell each object apart, visibility, pixel extents), events, camera
  and perspective cues.
- `tracks/ball.csv`: one row per frame (0–48). Columns: `cx, cy` = visible ball centre; bbox; `diam_px` = apparent
  diameter; `width_px` / `height_px` = mask extents (horizontal / vertical); `occluded`; `method`; `note`.
- `camera_shift.json`: per-frame (frame, dx, dy) of a ball-free region relative to frame 0, from phase correlation.
- `track_overlay.png`: every tracked circle drawn on frame 0. Green = fitted, orange = manual (falling frames).
- `scripts/`:
  - `track_ball.py`: background difference against the median of frames 45–48.
  - `track_mask.py`: intensity plus chroma mask.
  - `refine.py`: row-width estimate.
  - `edgefit.py`: RANSAC circle fit to Canny edges, excluding the lower 100° sector (shadow).
  - `fall_crops.py` / `static_crops.py`: gridded crops used for the manual readings.
  - `table_geom.py`: table outline.
  - `build_record.py`: assembles the CSV and overlay and computes the camera shift.

## Methods and reliability
- **Frames 0–18 (at rest)**: the ball's top half sits against the black background, so the background-difference blob
  is clean. Centre is (565.0, 440.4) ± 0.3 px and the diameter is 24.7 ± 0.5 px (bbox 25×24).
- **Frames 19–40 (rolling)**: the ball is grey on a beige table, so plain differencing fails, and the dark contact
  shadow under the ball gets into the masks. I used a circle fit to the outline edges, ignoring the bottom sector. I
  checked the overlays visually (they sit on the ball outline). Centres are good to about ±1 px. The diameter jitters
  by ±1.5 px from frame to frame (e.g. 34: 43.0, 35: 42.5), so smooth it, e.g. fit 1/D linearly in time, before using
  it for depth.
  - Apparent diameter grows from 24.7 px (rest) to 29 (f19), 32 (f24), 37.4 (f30), 42.5 (f35) and 50.9 (f40). The
    ball approaches the camera: depth at f40 is about half the depth at rest (Z ∝ 1/D).
- **Frames 38–40**: a faint second copy of the ball appears offset down-left (frame blending / compression ghost).
  The circle was fitted to the sharper copy, so the centre is uncertain by ±2–3 px along the motion direction.
- **Frames 41–44 (falling over the edge)**: strong vertical motion blur. I read the left, right, top and bottom
  extents by eye from 2× crops (±2 px). `cx, cy` is the middle of the blur streak (≈ the mid-exposure position).
  - `width_px` (52–57) is the horizontal ball size. It is slightly inflated by blur edges, so prefer the rolling-frame
    diameters for size.
  - `height_px` is the blur streak length, not the ball size.
  - Frame 44 is cut by the image bottom (y = 719), so its `cy` is an estimate (flagged occluded). Low reliability.
- **Camera**: static. The shift is at most 0.07 px in x and 0.12 px in y, so no compensation is needed.
- **Static extents** (scene.json) were read from gridded crops of frame 48 (±2 px); table corners come from the
  mask polygon (±3 px).
  - The pink bottle's base is partly hidden by the leaning card. Its height of 146 px runs to the visible base at the
    left side.
  - The cup is tapered: 72 px wide at the top, 53 px at the bottom, 123 px tall.

## Ambiguities
- The motion start is clear at 18→19 (≈5 px). Between 17 and 18 the ball moves less than 1 px, so the start is at
  frame 18 ± 1. No pusher is visible (the background is removed).
- "Leaves the table" is frame 40 ± 1: the ball bottom reaches the front edge line (y ≈ 549 at x ≈ 478).
- The shadow under the rolling ball is excluded from the ball's extent.
- The ball's colour (grey) is close to the table colour, so the automatic masks are unreliable. Use the
  edge-fit centres.
- Only one ball exists, so there are no look-alike objects. The leaning card and the flat cards share the same
  back pattern.
