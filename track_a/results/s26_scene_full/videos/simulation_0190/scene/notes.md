# simulation_0190 — measurement record

Video: 1920x1080, 120 fps, 401 frames (0..400, t = frame/120, 0 to 3.333 s). Source: simulation. inputs.json says 2D.
The camera is static and level and looks at the rear of a white box truck inside a grey warehouse.
**What moves:** the truck's white cargo body (with the yellow/black chevron bar under it) is lifted straight up
relative to the static black chassis. A brown cardboard box on top of the body also rises.
All motion is vertical. Horizontal drift is < 0.07 px.

## Files
- `scene.json`: inventory (moving and static objects, frame-0 pixel extents), events, camera.
- `tracks/cargo_body.csv`: one row per frame (0-400). Columns:
  - `cx, cy`: centre of the rear-face bounding box, used as the origin proxy.
  - `dx_from_f0, dy_from_f0`: sub-pixel template-match shift relative to frame 0.
  - `bbox_*`: the frame-0 bbox shifted by (dx, dy).
  - `roof_edge_y_measured`: the top edge, detected independently each frame.
  - `length_px`: horizontal width, 570 px. `height_px`: rear-face height, 520.4 px.
  - `match_score`, `occluded` (0).
- `tracks/cardboard_box.csv`: one row per frame. Columns:
  - `cx`, and `cy_top_based` = top edge + 87.8 px.
  - `dx/dy_from_f0`: template match on the upper part of the box only.
  - `top_edge_y`, `flap_tip_y`.
  - `bbox_x0/x1`, `bbox_y0` (top edge), `bbox_y1_visible` (= body roof edge).
  - `length_px`: width, 281.5 px. `visible_height_px`.
  - Occlusion flag: the bottom is always partly hidden behind the body's roof edge.
- `scripts/`:
  - `probe.py`: first look.
  - `track.py`: template tracking of body and box plus edge rows. Output: `raw_tracks.json`.
  - `track_box2.py`: box re-tracked with templates that avoid its occluded lower part. Output: `raw_box2.json`.
  - `finalize.py`: writes the CSVs and the overlay `frames/overlay.png`.
  - `steps.py`: per-10-frame step diagnostics.
  - `static.py`: static extents.

## Key numbers (pixels)
- **Cargo body rear face at frame 0:** x 658.5–1228.5, y 338.1–858.5.
  - Width 570 px, height 520.4 px, centre (943.5, 598.3).
  - At frame 400 it has risen 79.92 px: roof edge 258.5, centre y 518.4.
  - Its width stays constant, so its depth does not change.
  - The roof-edge detection agrees with the template shift to within about 0.5 px.
- **Cardboard box at frame 0:** x 806.0–1087.5 (width 281.5 px).
  - Top edge y 163.4; the open flap tip reaches y 147.6.
  - The visible bottom is at the body roof edge, y 338.1, so the visible height is 174.7 px (190.5 px including the flap).
  - The true box bottom is hidden, so its true height is at least 175 px.
  - At frame 400 it has risen 66.92 px (top 96.5). Three templates and the top-edge and flap-tip rows agree to within about 1 px.
- **Static chassis:** dark part x 672–1209 (about 537 px wide). It reaches from y ≈ 858 to the bumper at about 1025 and the reflectors at about 1040.
  - Tail lights: about (683–765, 918–945) and (1110–1205, 918–945).
- **Chevron bar:** frame 0 at x 802–1085, y 901–923. It moves with the body.
- **Background:** wall/floor line at y = 687.5. Dark window panel at the left, about x 0–192, y 16–683.

## Events
- **Body:** starts moving at frame ≈ 1 (t ≈ 0.01 s), very slowly at first.
  - Its per-frame upward step grows steadily: about 0.07 px/frame over frames 0–10 and about 0.30 px/frame over frames 390–400.
  - It is still speeding up when the clip ends.
- **Box:** stays still for about the first 12 frames, then starts rising (frame ≈ 12 ± 5, t ≈ 0.10 s).
  - It speeds up to about 0.22 px/frame, slower than the body after about frame 240.
  - It slows down from frame ≈ 385 and is stationary from frame ≈ 397 (t ≈ 3.308 s) to 400.
- **No contact or bounce events are visible:** no collisions, release or bounces. The box stays on top of the body, and the body's roof edge covers more of the box's bottom over time.

## Reliability and ambiguities
- **Accuracy:** the vertical shifts are good to about 0.1–0.2 px per frame (template match scores ≥ 0.97). Frame-0 extents are good to about ±1 px.
  - Per-frame steps are small (0.05–0.3 px), so one-frame differences are noisy.
  - Answering sessions that need speeds should difference over several frames or fit the shift curve.
- **Box versus body motion:** the box rises less than the body (ratio about 0.84–0.90 for most of the clip), and its visible height shrinks from 175 to 162 px.
  - Possible causes: the box sits farther back (deeper) than the rear face, it slides or settles, or it has its own simulated motion.
  - Treat the two as separate tracks and do not assume they move together.
  - The "2D" label means one scale applies within the rear-face plane. The box may be at a slightly different depth (it is the same 281.5 px wide all clip).
- **Origin proxy:** the body's reference point is the centre of the rear face, not the 3D centre of the body. In a 2D treatment its vertical motion is identical to the body's.
  - The box's `cy_top_based` is the top edge plus half the frame-0 visible height.
  - For motion, use `dy_from_f0`; it does not depend on which point you pick.
- **Box top-edge detector:** the raw per-frame top-edge detector in `track.py` sometimes locks onto a wall seam at y ≈ 128 (frames ~190–250). The CSV top edge therefore uses 163.4 + the template dy.
- **Other checks:** no motion blur or shadow confusion. The camera is static (background difference < 0.6 grey levels).
