# simulation_0029: measurement record

The clip is a 3D Blender render: 960x960 px, 25 fps, 75 frames (t = frame/25, 0 to 2.96 s). The camera is **static**. A red-and-white fishing
boat moves steadily **left**, and slightly toward the camera, across a calm rippled sea in front of sand dunes. A small dark
bird flies **left to right** above the dunes. The only static props are the shore posts, the beach, the dunes, the water and the sky. All values below are in pixels
(x right, y down) and frames. No metric scale was assumed.

## Files
- `scene.json`: inventory, per-object summary, camera and perspective cues, events.
- `tracks/boat.csv` (75 rows) has these columns:
  - `bbox_x0..y1`: box of the whole silhouette above the waterline, from the background difference. bbox_y0 is the
    antenna top; the faint mast pole is not included.
  - `hull_x0, hull_x1, hull_y0`: extents of the red hull. `hull_bbox_cx, hull_bbox_cy` is the centre of the box
    from hull_x0..hull_x1 and from hull_y0 to the waterline. **This is the recommended reference point.**
  - `hull_cx, hull_cy`: centroid of the red pixels.
  - `mask_cx, mask_cy`: centroid of the whole silhouette above the waterline.
  - `waterline_y`: first row below the dark keel band.
  - `mast_top_y`: raw pole-top detection. `mast_top_found` = 1 where it was reliable (44 frames).
    `mast_top_y_fit` is a linear fit, 490.5 - 0.095*frame, residual 0.7 px.
  - `height_px_fit` = waterline_y - mast_top_y_fit: the full height of the boat including the mast.
  - `hull_height_px`: from the hull top to the waterline.
  - `length_px_hull`: bow to stern along x. **Use this for length.**
  - `length_px_mask`: the same from the silhouette; noisier.
  - `antenna_top_y`: top of the short black antenna, about 27 px below the pole top.
  - `mast_x`, `mast_x_fit`: column of the antenna.
  - `area_px`, `occluded` (always 0), `note`.
- `tracks/bird.csv` (75 rows) has these columns:
  - `visible`
  - `cx, cy`: centroid of the dark silhouette.
  - `bbox_*`, `bbox_cx/cy`
  - `width_px, height_px`: the bbox. The width is roughly the projected wingspan.
  - `main_axis_len_px, across_px`: PCA extents.
  - `area_px`
  - `occluded`: 1 in frames 48-49, where the bird overlaps the antenna.
  - `cx_interp, cy_interp`: the centre, linearly interpolated in those two frames. Equal to cx, cy elsewhere.
- `summary_stats.json`, `static_raw.json`: summaries and static measurements.
- `scripts/`, in run order:
  - `explore.py`: first look.
  - `bg_diff.py`: background check.
  - `profile.py`, `mast_probe.py`: probes.
  - `track.py`: all tracks; also writes check overlays to ../frames/ov.
  - `postprocess.py`: mast fit and bird overlap flag.
  - `static.py`, `summary.py`, `cleanup.py`.
  - Run `track.py`, then `postprocess.py`, then `summary.py`.

## Methods
- **Camera:** the mean absolute frame-to-frame change in sky rows 0-400 is at most 0.5 grey levels, so the camera is static and needs no background correction.
- **Boat mask:**
  - The background is a composite: frame 0 for x < 452 and frame 74 for x >= 452. The boat's extents in those two
    frames (466-631 and 264-441) don't overlap, so this background is clean.
  - Mask = max-channel |diff| > 30 in rows 440 to the waterline, using the components that touch the red hull plus the
    cabin and rail parts (y >= 570) and the thin vertical antenna.
  - The x extents use only rows at least 4 px above the waterline, because water ripples at the bow leak into the mask.
- **Red hull:** r-g > 60 and r-b > 60, largest component above y = 690. The reflection lies below the waterline and is excluded.
- **Waterline:** the median, over the central hull columns, of the bottom of the dark keel band under the red. Reliable to about ±1 px.
- **Mast pole:** a thin, light-grey line that barely stands out from the white sky. It was detected by local contrast (< -8 grey levels) within ±4 px of
  the antenna column. It was found in 44 frames, always 25-29 px above the antenna top, and the fit is used.
- **Checks:** the overlays (frames/ov/ov*.png, every 6th frame) were inspected. The masks cover the hull, cabin, rails and
  antenna; the boxes and the waterline line sit on the boat.
- **Bird:** dark blob in (temporal median grey - grey) > 40, with y < 600, outside the dilated boat mask and the mast
  column band. Fragments within 6 px are merged. The overlay boxes hit the bird in all checked frames.

## Key numbers
- **Boat**
  - hull_bbox_cx goes 544.5 → 450.5 → 351.5 (frames 0 / 37 / 74), and hull_bbox_cy 646.5 → 649.
  - Steady step of about 2.63 px/frame (mask centroid 2.65 ± 0.27).
  - Length (hull) 158 → 176 px; the linear fit is 156.7 + 0.26·frame.
  - Height from waterline to mast top 188.5 → 200.5 px. Hull height 65 → 70 px.
  - The apparent size grows about 11% (length) or 6% (height), and the waterline moves down 679 → 684, so the boat is
    approaching the camera slightly. A 3D answer should use depth_info, not image x alone.
- **Bird**
  - cx goes 40 → 580 at about 7.3 px/frame; cy wavers between 518 and 538.
  - Width 13-28 px (median 19), height 4-20 px. The wings flap, so the silhouette size changes every few frames.
- **Static**
  - Shore posts: bbox x 112-139, y 646-659 (28 x 14 px).
  - Far shoreline at y ≈ 630-632.
  - Dune ridge at y 548-606, lowest behind the boat's area around x = 680.

## Reliability and ambiguities
- **Boat origin:** not visible. hull_bbox_cx/cy is the best guess for a hull-centred origin; mask_cx/cy is about 7 px
  higher. Their horizontal steps agree. Per-frame differences of hull_bbox_cx have ±0.7 px jitter from 1-px edge
  quantisation, so smooth them or use differences over several frames.
- **Boat length:** measured along image x, and the hull is turned slightly toward the camera, so it is slightly
  foreshortened. Width (beam) is not measurable.
- **Mast and antenna:** the raw mast_top_y is unreliable in about 30 frames; use mast_top_y_fit. In frames 48-49 the bird merged with
  the antenna in the diff, so the boat bbox_y0 there is the cabin top (576) and antenna_top_y is filled from a fit.
- **Bird:** small (26-205 px area) and motion-blurred in some wing poses, so its extents are ±2 px. Frames 48-49 are
  flagged and their centre is interpolated. Its depth is independent of the boat's.
- **Boat reflection:** the red reflection in the water is excluded from every boat measurement.
- **No events:** there are no release, bounce, impact or contact events. Both movers are in motion over the whole clip.
