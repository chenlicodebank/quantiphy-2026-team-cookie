# captured_0001 – measurement record

Lab recording (24 fps, 1280x720, 49 frames, t = frame/24), background replaced by SAM2 (watermark bottom right).
Scene: a yellow ball rests on the raised top edge of a white board leaning as a ramp on a brown table (single dark leg).
At ~frame 28 the ball rolls down the ramp toward the camera, onto the table (~38-39), across the table, off its
front edge (~43-44) and falls out of the bottom of the frame (gone from 47). Camera is static (<0.3 px shift).

## Files
- `scene.json` – inventory (ball, ramp_board, table, table_leg), static pixel extents, events, camera notes.
- `tracks/ball.csv` – per frame: `cx,cy` = mask centroid (visible centre, the reference point), `bbox_cx/cy`,
  bbox `x0..y1`, `bbox_w/h`, `area_px`, `equiv_diam` (2*sqrt(area/pi)), `length_main_axis`/`width_across` (PCA
  extents of the mask), `main_axis_angle_deg`, `touches_border`/`occluded` (1 = cut by image border).
- `scripts/track_ball.py` (HSV yellow threshold, largest component), `scripts/overlay.py` (check sheet),
  `scripts/static_and_camera.py` (frame diffs, phase-correlation camera shift; its automatic board/table masks were
  poor, so static extents in scene.json were read manually from zoomed grid frames).

## Reliability
- Ball centre: ~±0.5 px for frames 0-35 (sharp). Frames 36-43: motion blur, centre ±2 px. Frames 44-45: strong
  blur and smeared mask (45 cut by bottom border) – centroid ±5-10 px, sizes unreliable. 46: sliver only.
- Ball diameter: 44.7 px at rest (frame 0, depth largest). Apparent size grows as it approaches the camera
  (≈52 at 36, 60 at 38, 66 at 40, 73 at 41, 78 at 42-43). Use `width_across` (perpendicular to blur) as diameter
  during motion; `bbox_h` is blur-inflated (e.g. 54 vs 45 at 33-34). Apparent diameter ∝ 1/depth (f = 763 px), so
  a depth at one time plus diameter ratios gives depth at other times.
- Static extents: ±2-3 px (edges hand-read). Board top edge 568-721 @ y353, bottom 539-737 @ y496.
  Table back edge 480-833 @ y445, front edge 304-1027 @ y~552-562, front face ~30-35 px thick; leg x 660-709.
- Timing irregularities: frames 17-19 appear duplicated (identical tracks); step 35→36 is unusually large
  (40 px vs 16 and 26 px around it) – possible dropped frame. The cy dip at 39 (469.6→465.8) is at the
  ramp→table transition (small hop or mask noise).
- Motion start: tiny drift (<1.3 px) frames 23-27, first clear vertical motion at 28, unambiguous by 30.
- Ambiguity: only one ball; no people or other props. Shadow of the ball on the board/table is grey, not in mask.
