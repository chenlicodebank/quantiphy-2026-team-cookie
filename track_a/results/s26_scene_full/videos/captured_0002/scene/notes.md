# captured_0002 – measurement record

Lab recording (24 fps, 49 frames, 1280x720, 3D), background replaced by green. Static camera
(phase-correlation shift vs frame 0 <= 0.14 px). Pinhole per task convention: f = 763 px, principal point (640, 360).

## Scene
A wheeled over-bed table (wooden top, grey pedestal with casters) seen obliquely from the front and above.
A white board leans upright on the table near the back. A small orange/tan ball (~25.5 px diameter at rest)
sits on the board's top edge, rolls off at ~frame 27, falls in front of the board, hits the table top at
~frame 36 just in front of the board foot, moves toward the camera over the table, goes over the near table
edge between frames 40 and 41, then falls below the table, leaving the image bottom after frame 46.
The ball is the only moving object; there are no people or other props.

## Files
- `scene.json` – inventory (ball, white_board, table_top, table_stand), static pixel extents/corners (frame 48),
  camera, events with frames/times.
- `tracks/ball.csv` – per frame 0-46: time, bbox centre (cx, cy = reference point), mask centroid, bbox,
  mask length along main axis / width across (PCA of mask), area, occlusion flag, quality tag.
- `scripts/` – `diff.py` (frame differencing vs frame 48 + camera-shift check), `track_ball.py` (tracker,
  writes ball.csv and overlays), `static.py` (colour masks of static objects), `view.py` (crop viewer).

## Method and reliability
- Ball mask = |frame - frame 48| (ball absent in 47-48) > 40 (> 22 while over the white board, frames 29-40),
  in a window around the previous position. Overlays were inspected: masks sit on the ball in every frame.
- Frames 0-26 (at rest): centre ±0.5 px, diameter 25-26 px – the most reliable size of the ball.
  A slow drift of ~2 px down (281 -> 283.5) over 0-26 is small creep/noise, not real motion.
- Frames 29-35: ball is faint over the white board (low contrast + motion blur); mask holds only the bright core
  (16-20 px wide), so the centre is fine (±2 px) but sizes underestimate.
- Frames 36-40: ball over wood, faint/blurred; centre ±3 px; height is a blur streak.
- Frames 41-45: under the table, strong vertical motion blur (height 34-57 px = streak). Use the bbox centre
  as the position (mid-exposure) and the horizontal width (28-32 px) as apparent diameter: the ball appears
  ~1.15-1.25x larger than at rest, i.e. it is closer to the camera (it moved toward the camera over the table).
- Frame 46: ball cut by the image bottom edge; cy biased upward, size unreliable.
- Image-y step per frame (px): 30-36: ~17,17,19,24,28,30; 36-40: ~9,12,10,12; 40-46: 16,21,32,44,41,50.
  The drop at 36 marks the impact on the table.
- Static extents from colour masks at frame 48 (±2-3 px). Table far-left corner is ragged (segmentation).
  A small grey patch behind the board's left side (~528-559, 328-336) changes slightly up to frame 33
  (shading/segmentation artefact), not an object motion.

## Ambiguities
- Depth: no depth in this record; answering sessions should back-project with given depth_info and f = 763 px.
  The ball's 3D path is mostly vertical with a component toward the camera after the bounce.
- "Release" frame: 27 (first sub-pixel move) vs 28 (first clear move).
- Whether the ball touches the board while falling cannot be seen (it falls in front of it).
