# captured_0038x – measurement record

Lab video (real Orbbec camera, 1280x720, 24 fps, 49 frames, t = frame/24), background removed by
Segment Anything 2 (everything except table + objects is black; watermark bottom-right). Camera static.
Benchmark intrinsics: f = 0.5959*1280 = 763 px, principal point ~(640,360). No metric scale is assumed here.

## Files
- `scene.json` – inventory (all objects, pixel extents, positions), camera, events.
- `tracks/ball.csv` – the only moving object, every frame 0-48. Columns:
  `x, y` = reference point (visible centre; x from template matching, y = midpoint of top/bottom edge);
  `top_y, bottom_y, height_px` = vertical extent through the centre columns;
  `left_x, right_x, width_px_incl_blur` = horizontal extent (includes motion blur, ~16 px/frame while rolling);
  `mask_*` = bright-region mask (upper ~80 % of the ball only; its centroid is ~4 px above the true centre);
  `tm_score` = template-match correlation; `occluded` (never occluded); `edges_unreliable` = 1 for frames 30-35.
- `scripts/` – `track_ball.py` (median-difference + white-colour mask; run first), `final_track.py`
  (template matching + edge profiles, rewrites ball.csv; run second), `template_ball.py`, `full_mask.py`,
  `vprofile.py` (diagnostics), `static_objects.py` (static extents from the median frame), `pts.py`
  (timestamps / frame differences), `view_crops.py` (zoomed montages), `check_json.py`.

## Scene
White ball (ping-pong-like) rests at the left end of a square wooden table (x≈278, y≈488) for frames 0-11,
then rolls right across the near half of the table, passing in front of / over the lying playing cards
(frames 29-35), and is still rolling at x≈966, y≈512 at frame 48. Static props: pale-pink thermos bottle,
white tumbler cup, a playing card leaning on the bottle, playing cards lying flat in front of them, a dark navy
card with a yellow sticker near the front edge, the table top and its single dark pedestal leg.

## Events
- Rest: frames 0-11 (x jitter ≤3 px, segmentation noise).
- Motion start: between frame 11 and 12 (t≈0.46-0.50 s). Pixel steps: 48, 33, 28, 25, 19 px for frames 12-16,
  then a steady ~16 px/frame (frames 17-48). The large early steps coincide with heavy motion blur and a
  distorted segmentation; it may be a real push-and-slow-down, treat the first ~4 moving frames with care.
  No hand is visible (segmented out).
- Frames 35→36: a 32.7 px step (≈2x normal) with uniform container timestamps – most likely a dropped
  capture frame. Positions themselves are correct (checked visually).
- End: frame 48, ball still moving.

## Reliability
- Ball x: ±1 px (template match, score >0.95 for frames 16-46; 0.81-0.93 in blurred/over-card frames).
- Ball y: ±2 px. The underside is shaded and close to the table colour, so bottom edges/heights may be
  2-4 px short; best diameter estimate ≈38-41 px (vertical 33-38 measured, static width 40-42 with the left
  edge clipped by segmentation). Apparent size changes little across the run (ball depth roughly constant,
  slight approach to the camera as y increases).
- Frames 30-35: ball over white cards – y set to top edge + 17, widths blank.
- Static extents from the median frame: ±2 px; pink bottle bottom partly hidden by the standing card;
  table corners approximate (±5 px), leg cut off by image bottom.
- 3D answers need the question's depth_info: back-project (x, y) with f = 763 px and the given depth.
