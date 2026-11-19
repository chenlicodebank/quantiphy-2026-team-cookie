# captured_0032s — measurement record (pixels and seconds only)

Lab video (Orbbec RGB, 24 fps, 1280x720, 49 frames, t = frame/24). The background was replaced with a SAM2
composite (bluish snowy backdrop, watermark "Modified with Segment Anything 2 Demo" bottom-right). Composited objects
show a thin bright halo/outline along their mask edges. 3D scene. Camera is **static**: phase correlation on the table
between consecutive frames is < 0.3 px for every frame.

## Scene
A wooden table top (brown wood grain) on one dark grey central leg, seen from the front, camera slightly above table
height. Two balls on the table top:
- **yellow_ball**: the larger yellow-green fuzzy ball (tennis-ball like). At rest at the back-right (centre ≈ (775.4, 410.2) px,
  diameter ≈ 32–33 px) for frames 0–21. Starts rolling at frame 22 (t = 0.917 s; first displacement between 21 and 22; no
  pusher visible because the background was replaced). Rolls left and toward the camera (image y increases, size grows),
  strikes the white ball at frames 29–30, continues left, rolls off the left side edge of the table top at frames 41–42
  (t ≈ 1.71–1.75 s), falls (motion-blurred streaks 42–47) and leaves through the bottom image edge after frame 47
  (truncated at 47, absent at 48).
- **white_ball**: small white/cream ball (ping-pong-ball like). At rest at back-left (centre ≈ (647, 415) px, diameter ≈ 17–18 px)
  for frames 0–28/29. Hit by the yellow ball: first displaced at frame 29→30 (x 646.3 → 647.8 → 652). Partly hidden behind the yellow ball
  at frames 30, 32, 33 and fully hidden at 31. Then rolls right and toward the camera, about 6 px/frame in x at the end, and is still
  rolling on the table at the last frame 48 (centre ≈ (791, 457), diameter ≈ 32–33 px).
- **table** (static), **table_leg** (static); extents in scene.json.

## Files
- `scene.json`: inventory, static extents, camera/perspective info, events.
- `tracks/yellow_ball.csv`, `tracks/white_ball.csv`: final per-frame tracks. Columns: frame, t, ref_x/ref_y (reference point = visible
  centre), bbox (x0,y0,x1,y1 inclusive, w,h), mask_len/mask_wid (PCA extents along/across main mask axis), axis_deg, diam_px (best
  apparent diameter), centroid_x/y (mask centroid), fit_cx/fit_cy/fit_d (least-squares circle fit to the upper 70 % of the mask contour),
  area_px, occluded, truncated, note.
- `tracks/*_raw.csv`: raw mask statistics from `scripts/track.py` (also min-enclosing circle, equal-area diameter).
- `scripts/`: `track.py` (colour segmentation + overlays), `finalize.py` (final tracks), `framediff.py` (camera-motion / frame-drop check),
  `static.py` (table geometry), `view.py`, `probe.py`, `probe2.py`, `check_overlay.py` (inspection helpers).

## Method
- yellow_ball mask: HSV H 23–40, S ≥ 70, V > 60 and R−B > 40 (excludes the yellowish reflection on the table, H ≈ 20); largest
  component. Reference point = mask centroid. diam_px: frames 0–21 bbox width (32 px; direct row/column profiles at f0 give ≈ 33–34 px
  wide x 32–33 px tall including the dark shaded rim, so true apparent diameter ≈ 33 ± 1 px); rolling 22–41: mask width across motion
  axis (horizontal motion blur widens bbox_w by up to ~10 px); falling 42–47: width across the blur streak (45–53 px). fit_* for
  yellow is inflated by blur — use centroid.
- white_ball mask: V > 158, S < 62, R−B > −6 (excludes bluish background and brown table), restricted to the table-top band,
  opened with a 7x7 disc to remove leaks along the bright table-edge/background boundary, holes filled. The shaded lower rim of
  the ball is missed, so ref point = circle model (cx = bbox centre, cy = bbox top + (w−1)/2, diam = bbox_w). fit_cx/fit_cy agree within
  ~1–2 px. Occluded frames 30, 32, 33: centroid of visible part (low accuracy); frame 31: no measurement.
- Overlays were drawn and inspected (frames/overlay.png, frames/check.png — scratch, not part of the record): masks sit on the right balls
  and cover their full extent except the white ball's shaded bottom rim.

## Apparent size vs time (depth cue)
- yellow: 32–33 px at rest (f0–21, image y ≈ 410) → 33 (f29) → 38 (f33) → 43 (f36) → 46 (f40–41, y ≈ 443) → ~48–53 while falling.
- white: 17–18 px at rest (y ≈ 415) → 29 (f36) → 30 (f42) → 32–33 (f46–48, y ≈ 457).
Both balls approach the camera after the collision. The diameter is the most direct per-frame depth cue (depth ∝ 1/diameter
for a fixed real ball size; with f = 763 px: Z ≈ 763·D_real/diam_px).

## Perspective
Table-top side edges converge to ≈ (720, 351) px → horizon y ≈ 351 (image centre 360), so the optical axis is close to level.
Back edge of the top: (576,425)–(851,428), 275 px long; front top edge: (463,483)–(965,495), 502 px long (ratio ≈ 1.83 = depth ratio
front/back if the edges are equal in length). Front slab thickness ≈ 22–25 px. Leg: x 714–748 (≈ 33 px wide), visible y 515–719.

## Reliability / ambiguities
- Centres: yellow on the table ±1 px; yellow falling ±2–3 px (blur streak; centroid = mid-exposure); f47 truncated by the bottom
  edge (centroid biased upward). White ±1–2 px (the static-phase ref_y jumps 414.5 → 416.5 at f6 with no real motion: mask-edge noise).
- Diameters: ±1–2 px (yellow) and ±2 px (white, slight under-estimate at rest).
- **Probable dropped frame between frames 35 and 36**: both balls move about twice their neighbouring per-frame displacement there
  (yellow Δx 14.7 → 31.4 → 17.1 px, white 7.7 → 16 → 4.6 px). Per-frame speeds across 35→36 are not consistent with 1/24 s.
- Exact collision frame: contact between frames 29 and 30 (white first moves 29→30; at 29 white x changes by only 1.6 px).
- Yellow leaves the table: on the table top through f41 (centre y increases ~2 px/frame), centre drops 7 px at f42 and 18 px at f43 → free fall
  begins ≈ f41–42.
- Reflection of the yellow ball on the glossy table and the SAM halo around objects are not part of the objects (excluded).
- No other moving objects, no people. Only one of each ball, so the names are unambiguous (yellow/large vs white/small).
