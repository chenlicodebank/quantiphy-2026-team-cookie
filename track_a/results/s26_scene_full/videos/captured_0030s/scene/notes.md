# captured_0030s — measurement record (pixels, seconds)

Lab video, 3D, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s), 1280×720. The background was replaced
(the "Modified with Segment Anything 2 Demo" watermark is at the bottom right, x 1030-1280, y 690-720), so the only real
content is a **red ball on a grey string** and a **brown table**. Camera: Orbbec Femto Mega, f ≈ 763 px, principal
point ≈ (640, 360) (from the benchmark conventions, not measured here).

## Files
- `scene.json`: inventory, camera, table geometry, events, perspective summary.
- `tracks/red_ball.csv`: one row per frame (0-48, the ball is visible in every frame). Columns:
  `cx, cy` = centre of a least-squares circle fitted to the ball's colour-mask contour (the visible centre, which is the
  reference point); `cy_corr` = the y-centre to use (equal to cy except in occluded frames 12-17, see below);
  `centroid_x/y` = mask centroid; `bbox_*` = mask bounding box (inclusive pixel coordinates; w/h = x1-x0+1);
  `circle_diam_px` = fitted circle diameter; `equiv_diam_px` = 2·sqrt(area/π); `mask_len_main_px / mask_wid_px` =
  minimum-area-rectangle sides; `motion_blur` = 1 if the centre moved ≥45 px to or from a neighbouring frame;
  `pale_render` = 1 for frames 47-48; `occluded`; `diam_interp_px` = diameter interpolated for occluded frames.
- `static_table.json`: table outline per frame (camera check) and row extents at frame 16.
- `scripts/`: `track_ball.py` (the track), `static_table.py`, `write_scene.py` (events, scene.json),
  `draw_path.py`, `zoom_ov.py`, `montage.py`, `dump_frames.py`, `probe*.py` (colour probes used to pick thresholds).

## Objects
- **red_ball** (moving, frames 0-48): a glossy red sphere with a thin grey string/cord trailing from it toward the back.
  It moves continuously on a closed, roughly elliptical loop low over the tabletop, like a pendulum swinging in a
  circle. Seen from above, it goes clockwise (front → left → back → right). It starts near the front centre (f0) and moves left, reaches
  the leftmost point at f8, the far side at f12-19 (just beyond the table's back edge), the rightmost point at f23, the
  nearest point at f27-28 (in front of and over the table's front edge), the leftmost point again at f33, then the far
  side at f36-46, and it is on the right going toward the front at f48. One loop takes about 25 frames (leftmost points
  at f8 and f33, 1.04 s apart). The second far pass (f36-46, y≈427, D≈40-45) does not go behind the back edge.
  There is only one ball, so it cannot be confused with another object.
- **grey_string**: a thin grey cord attached to the ball, visible as a short grey streak about 100-150 px long going
  back and up from the ball. The segmentation cut it off, so its pivot or top is never visible. Not tracked.
- **table** (static): a brown wooden rectangular top on one dark central pedestal. Image geometry (stable to ±2 px over
  all frames):
  - top surface: back edge y≈442 (x ≈378-810, corners approximate), front edge y≈530 (x 203-975, 772 px long);
  - front face (thickness of the top): rows 530-559, 29 px;
  - top's extent toward the back in the image: 88 px;
  - pedestal: x 572-620 (48 px wide), from y 559 to the bottom of the frame (cut off); the floor is not visible.
- **background, watermark**: synthetic, not physical.

## Ball apparent size (depth cue)
The ball's apparent diameter changes about 2× around the loop. Real ball diameter / pixel diameter × 763 gives its depth.

| frames | where | diameter |
|---|---|---|
| 0-3 | near | ≈67 px |
| 8 | left | 51 |
| 11, 18-19 | far | ≈41-45 |
| 23 | right | 58 |
| 25-29 | nearest | 70-80 (blurred; bbox_h 66-77) |
| 33 | left | 54 |
| 40-46 | far, 2nd pass | ≈40-44 |
| 48 | right | 46 |

The cleanest (sharp, unoccluded) diameters are at frames 7-10, 19-24, 31-46. For blurred frames, use bbox_h (the blur is
mostly horizontal) or circle_diam_px, not bbox_w.

## Events
- The ball is already moving at f0 and still moving at f48: no start or stop, release, bounce or impact is visible.
- Leftmost x: f8 (x 415) and f33 (x 398). Rightmost x: f23 (x 861).
- Highest in the image (farthest): f18 (y 418) and f39 (y 426). Lowest (nearest): f28 (y 514).
- f12-17: partly hidden behind the table's back edge. f25-29: the ball's bottom extends below the front edge line
  (y>530). The extremum at f1 is noise (y 493.8 vs 493.5); so is the one at f14, which falls in the occluded frames.

## Reliability and ambiguities
- **Segmentation.** The colour mask is float hue ≤17.5° (or ≥340°) with saturation >0.33. This excludes the ball's red
  reflection on the table (hue 18-26°), and zoomed overlays (frames/z*.png) confirm it covers the full ball. Centres
  are good to about ±1-2 px when the ball is sharp.
- **Motion blur** (f0-4, f11-12, f25-30) smears the ball horizontally by up to about 20 px. The centre is still good to
  ±2-3 px, but bbox_w and mask_len are inflated.
- **Occlusion** (f12-17): the ball's bottom is cut off flat by the table's back edge, so mask cy is biased up by 3-8 px.
  cy_corr = bbox_y0 + D_interp/2, with D_interp interpolated between f11 and f18 (≈±2 px).
- **f47-48**: the ball appears pale pink/white (a compositing artefact). It is tracked with a separate pale-colour mask
  and its size continues the trend.
- **Camera**: static. The table outline moves ≤2 px across all frames, so no background-shift correction is needed.
- No depth_info is known here. Do not assume a metric scale.
