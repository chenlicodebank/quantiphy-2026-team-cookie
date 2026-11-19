# simulation_0083 — measurement record (2D, simulation, 24 fps, 72 frames, 1920x1080)

## Scene
Top-down (near-orthographic) render of a uniform light-grey ground plane with two cars on parallel horizontal
lanes, driving apart in opposite directions. Static camera (0.00 px background shift in every frame). No ground
markings or other props. Times: t = frame/24.

- **yellow_car** — yellow/gold car, upper lane (centre y ≈ 415.5), nose left, drives **left**.
- **black_car** — black rear half / white-silver front half, lower lane (centre y ≈ 539.5), nose right, drives **right**.

## Files
- `scene.json` — inventory, sizes, lane positions, relations, events, camera.
- `tracks/yellow_car.csv`, `tracks/black_car.csv` — one row per frame (0–71): `frame,time,ref_x,ref_y`
  (bbox centre = origin proxy), `bbox_x0,bbox_y0,bbox_x1,bbox_y1`, `length_px` (x extent, along motion),
  `width_px` (y extent incl. mirrors), `height_px` (empty: not visible top-down), `front_edge_x`, `rear_edge_x`
  (in travel direction), `mask_cx,mask_cy,area_px` (mask centroid — less reliable, see below), `occluded` (always 0),
  `near_other_car` (1 = cars overlap in x, frames 0–15), `touches_frame_edge` (always 0).
- `scripts/explore.py` (median background), `track.py` (segmentation + tracks + overlays), `check_ext.py`
  (length stability), `checks.py` (static start, camera, body width), `profiles.py` (pixel profiles used to set thresholds),
  `cleanup.py`. The background cache `bg.npy` was deleted to keep the record small: run `explore.py` first to
  rebuild it (`track.py` does this itself).

## Method
Background = per-pixel median of every 6th frame. Car pixels = yellow chroma (R−B > 30) OR darker than background
by > 34 OR brighter by > 12; the soft blob shadows are at most ~30 levels darker and are excluded. 5×5 closing,
components ≥ 30 px, union split at row 479 between the lanes. Overlays (frames/mask_*.png, checked visually at
frames 0, 8, 36, 71) show the masks covering each car including mirrors, nose and tail, without shadow.

## Key measurements (px)
- Rest lengths (x, along motion): yellow 270, black ≈ 269 (268–270 near image centre). Widths incl. mirrors: 116
  both; body without mirrors ≈ 94 (yellow) / 93 (black) median, ≤ 100 at wheel arches. Height not observable.
- Lane separation (centre y): 124 px. Frame 0 centre offset (yellow − black): dx = +78, dy = −124 (dist 146.5).
- Motion: frames 0 and 1 are identical (both cars still). From frame 2 both move at constant per-frame
  displacement with no ramp: yellow exactly −10 px/frame in x; black +13.96 px/frame mean (12–15 frame to frame
  through 1-px quantisation). y constant. No direction change, contact, bounce or occlusion. Both fully visible
  in all 72 frames (yellow ends at x 24–300, black at x 1621–1901).

## Reliability / ambiguities
- Positions: ±0.5–1 px per frame (integer bbox edges). The bbox centre is used as the origin; a vehicle root may
  sit off-centre along the car's length, which shifts absolute positions/inter-car distances by a constant but
  not displacements.
- Mild perspective at the image edges: the apparent length grows to 277 (yellow, x < 350) and 281 (black, x > 1550),
  because the car sides become visible. This moves the bbox centre by ≤ ~3 px; using the rear edge (yellow:
  `rear_edge_x` = right edge) or bbox centre gives the same per-frame displacement to within ~0.1 px/frame on average.
  For a size prior, use the near-centre lengths (270 / 269).
- Frames 0–15 (`near_other_car`=1): the cars are side by side, ~6 px apart in y; the shadow gap between them is
  absorbed into the masks, so `width_px` reads 119–121 and ref_y is ~1–2.5 px off. x values are unaffected.
  Use width 116 and lane y 415.5 / 539.5.
- `mask_cx` for the yellow car drifts from bbox centre (by up to ~11 px) late in the clip because its windshield
  turns grey under the lighting and drops out of the mask — use `ref_x`, not `mask_cx`.
- 1-px rounding produces occasional 1–2 px jumps in single frames (e.g. yellow frame 7, 12–13; black frames 11–14);
  differences over several frames are more reliable than single-frame differences.
