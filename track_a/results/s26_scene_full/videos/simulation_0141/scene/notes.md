# simulation_0141 — measurement record (pixels and seconds only)

Video: 1920x1080, 24 fps, 60 frames (t = frame/24, 0 … 2.4583 s). Blender render, 3D scene.
Content: one man (dark pinstriped shirt, dark trousers, seen from behind as a near-black silhouette)
walks AWAY from a static camera down a long white-arched corridor with a glossy tiled floor. He is the
only moving object. No other people, animals, vehicles or props.

## Files
- `scene.json` — inventory, camera/perspective, static-object positions, events, gait summary.
- `tracks/man.csv` — one row per frame (0–59), columns:
  - `frame`, `t` (s)
  - `ref_x, ref_y` — estimated pelvis (reference point for simulation humans). x = mean centre of the
    torso/hip run of the silhouette in the band 45–53 % of the way down from the head top (arms excluded);
    y = `sole_y − 0.53·height_px` (hip joint ≈ 0.53 of stature above the sole).
  - `bbox_x0, bbox_y0, bbox_x1, bbox_y1` — mask bounding box (includes swinging arms/hands, excludes the
    floor reflection).
  - `height_px` — head top to lowest sole point (vertical main axis = "length" of a standing human).
  - `width_px` — bbox width incl. arms; `shoulder_width_px` — widest row span in 14–24 % band (incl.
    upper arms).
  - `area_px`, `head_top_y`, `sole_y` (lowest mask row = planted foot), `sole_x` (x of lowest pixels),
    `head_cx` (head centre x), `occluded` (always 0).
- `scripts/` — `camcheck.py` (camera motion), `segment.py` (masks → `masks.npz`, small scratch),
  `track.py` (CSV), `overlay.py`/`overlay_track.py` (visual checks into ../frames), `vp.py` (vanishing
  point), `summarize.py`, `probe.py`.

## Method
- Camera: phase correlation of three background regions vs frame 0 → shift < 0.02 px in all frames:
  **static camera**.
- Segmentation: background = per-pixel 95th-percentile over all frames (man is always darker than what
  is behind him); mask = darkening > 35 and luminance < 110, morphological clean-up, largest component +
  attached parts. The glossy floor reflection under his feet is also darker than background but much
  lighter (lum ≥ ~40) than the silhouette (lum < 30): mask cut below the lowest very-dark row (shoe sole).
  Overlays at 13 frames checked by eye: masks cover head to shoes and both arms, reflection removed.
- A brighter striped region of the shirt sometimes leaves an open notch in the raw mask; bbox, height and
  sole are unaffected; the closed mask is used for ref_x and shoulder width.

## Perspective / camera (3D)
- Corridor vanishing point (floor-seam lines) = (959, 539) ≈ image centre → optical axis horizontal and
  along the corridor, principal point ≈ (960, 540). Horizon y ≈ 536 ± 4 (fit of head-top vs sole y on
  the man gives 533).
- Horizon crosses the man at ~0.745 of his head-to-sole height (upper chest): camera height ≈ 0.75 × the
  man's height.
- Apparent size: height_px 716 (f0) → 602 (f12) → 524 (f24) → 458 (f36) → 412 (f48) → 366 (f59), i.e.
  his distance roughly doubles over the clip. `height_px/(sole_y − 536)` stays 1.32–1.39 (oscillates with
  gait), confirming ground-plane consistency.
- Focal length is unknown. With a given depth d (camera centre → pelvis) at frame i and a known man
  height Hm: Z ≈ d / sqrt(1 + ((ref_x−960)² + (ref_y−540)²)/f²) and f ≈ height_px·Z/Hm (iterate; the
  pelvis is within ~170 px of the centre, so the correction is small unless f is small). With two given
  depths, f can also be solved from the change in ref pixel position. Back-projection:
  X = (x−960)·Z/f, Y = (y−540)·Z/f. Also the floor: Z = f·h_cam/(sole_y − 536) for the planted foot.
- Right colonnade pillar bases (frame 59, see scene.json) are equally spaced in depth (1/(base_y−539)
  steps by a constant); the man's sole reaches the nearest arch's base row (y≈838) around frame 46.

## Events
- Man walks during the entire clip (no start/stop). Foot contacts (lowest sole point stops rising in
  the image, new stance foot planted): frames 10, 22, 34, 46, 58 (t = 0.417, 0.917, 1.417, 1.917,
  2.417 s); step period 12 frames = 0.5 s; a contact before frame 0 holds sole_y = 1052 for frames 0–4.

## Reliability / ambiguities
- bbox / head_top / sole: ±2 px (sharp silhouette; slight softness at shoe tips next to the reflection).
- ref (pelvis) x: ±5 px (shifts with leg/hip sway); ref y: model-based (0.53·height) ±3 % of height_px
  (≈ ±10–20 px); head top bobs with gait and height_px shrinks a little in double support, so ref_y
  inherits a small gait oscillation. For smooth motion, fit over several frames or use sole_y plateaus.
- Image path of ref point ≈ 293 px over the clip, but most of his motion is along the line of sight —
  use depth/perspective for 3D distances, not image displacement.
- No occlusion. Reflection on the floor and reflections of the colonnade are not objects.
