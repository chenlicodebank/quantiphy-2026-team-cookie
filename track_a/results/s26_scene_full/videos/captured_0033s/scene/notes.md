# captured_0033s — measurement record (pixels, seconds)

Lab video (real recording, 24 fps, 49 frames, 1280x720, 3D scene). The background has been replaced by a uniform blue sky
(watermark "Modified with Segment Anything 2 Demo", bottom right) and the person throwing the ball is removed. Visible: one
**ball** (small, white/pinkish, ping-pong-like) and a static **wooden table** on a dark grey central **pedestal**. No ground,
no horizon, no other objects. Lab convention: fx = fy = 763 px, principal point ~ (640, 360).

## Files
- `scene.json` — inventory, static object extents, camera, events.
- `tracks/ball.csv` — ball per frame 0–48: centre (mask centroid = visible centre), bbox, mask area, equivalent diameter,
  length along the main axis / width across it (PCA of mask), axis angle, motion-blur flag, state. Frames 38–48: not visible.
- `scripts/track_ball.py` (run with arg 95) → `_raw.json`; `overlay.py` (visual check, frames/ov_crops.png);
  `table.py` (table mask, per-frame stability, row profile `_table_rows.json`); `write_record.py` (writes csv + json).

## Method
Background = per-pixel median of every 2nd frame (ball moves, so it vanishes). Ball mask = |frame − bg| > 30 and min RGB > 95
(excludes its dark shadow on the table), open/close, largest blob nearest the previous position. Overlays checked for every
frame: box sits on the ball in all frames 0–37.

## Motion summary (ball)
- f0–2 held almost still at (624, 234) (removed hand); release/throw starts f3 (±1); rises, slight rightward drift.
- Apex 1 at f8 (cy 180.5). Falls, first bounce on the far part of the table top at f14 (cy 405; ball bottom at the far table
  edge y≈432; its shadow is visible).
- Apex 2 at f20 (cy 313). Second impact at f24–25 (cy max 434.6 at f25), small hop f26–27, then rolls/skips across the table
  toward the camera and left (f27–35, cx 583 → 457).
- Leaves the front-left table edge between f35 and f36, falls out of the bottom of the image after f37 (last visible).
- The ball moves strongly toward the camera: unblurred apparent diameter (width_across_px) ≈ 21 px (f0–3), 25 (f9–10),
  29.5 (f19–20), 33 (f26–28), 36 (f30–34), 45 (f35), ~60 (f36–37). With a known ball diameter D, depth ≈ 763·D/diameter_px;
  use depth_info when given (reference uses clicked centres back-projected with measured depth).

## Static objects (frame 0; camera static, table edges stable within 2–4 px all clip)
- Table top: far edge y≈431, x 452–765 (313 px); near upper edge from (304, 519) to (907, ~534) (603 px); front face thickness
  ≈27 px; overall bbox x 302–911, y 430–561. Strong foreshortening of the top (depth ~95 px in image). Near edge slopes ~15 px
  down to the right (slight roll). Corners ±3 px (soft segmentation edges).
- Pedestal: x 562–605 (44 px wide), from y 552 to the image bottom (continues out of frame).

## Reliability / ambiguities
- Centres ±1–2 px in clear frames. Heavy vertical motion blur f11–15 and f21–24 (fast fall/bounce) and diagonal blur f36–37:
  the centroid is the mid-exposure centre; len_main_axis is blur-stretched, so use width_across_px for size there.
- The shaded lower part of the ball (pink/brown on the table, f28–35) is partly excluded from the mask → cy may be 1–3 px
  high and bbox bottom a few px short in those frames.
- The ball's shadow on the table is excluded. Frames 36–37 the ball is in front of the table edge (no occlusion of the ball).
- Bounce frames are ±1 frame (24 fps sampling). No occlusion of the ball in any visible frame.
