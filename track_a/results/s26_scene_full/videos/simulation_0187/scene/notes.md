# simulation_0187 – measurement notes

2D simulation (Blender), 1920x1080, 30 fps, 60 frames (t = frame/30). Static camera. One moving object: a white
airport catering truck (box body, cab on the right with a railed platform on top, tail lift at the rear/left) that
drives left -> right across a grey hangar wall/floor background, starting from rest at about frame 0 and accelerating.
No other moving objects, no people, no props.

## Files
- `scene.json` – inventory, sizes (px at frame 42), camera, events.
- `tracks/truck.csv` – one row per frame 0-59. Columns: `ref_x_px, ref_y_px` (reference = centre of the side-view
  bbox, tail-lift tip to front-most point; 946.5, 645.5 at frame 42), `offset_vs_f42_px` (horizontal displacement
  relative to frame 42), x of front_most / cab_nose / box_front / box_rear / tail_lift / front_wheel / rear_wheel
  (side-plane points; may be outside 0-1919 when the point is off-screen), `wheel_y_px`, bbox (clipped to the image),
  `side_length_px` 1507, `height_px` 587, `visible_length_px`, `silhouette_left/right_px` (raw mask edges, include
  the perspective front/rear face and are NOT side-plane points), `clipped`, `occluded` (never), `dx_from_prev_px`
  (per-frame displacement used to chain the track), `reliability`.
- `scripts/` – survey.py (first look), measure.py (mask + profile shift), edges2.py (mask edges by row band),
  track_side.py (main tracker), combine.py / build.py (track assembly -> truck.csv), wheels.py, tmatch.py
  (cross-checks), overlay.py (drawn checks), summary.py (camera check). Raw json outputs are kept there.

## Method
- Foreground = |frame − frame 59| > 18 (frame 59 is the empty background). The floor shadow (y > ~880) and parts
  of the white box that match the light wall are imperfect in the mask, so mask edges were only used for checks.
- Main track: four foreground-masked templates of side-plane features cut from frame 42 (cab side, box front,
  mid chassis, rear corner + tail lift), matched horizontally in every frame with partial-border overlap allowed,
  sub-pixel by parabola. Per-frame displacements are averaged over templates valid in both frames and chained
  from frame 42. All named points move with the same offset (rigid translation; y is constant: top 352 and tyre
  bottom 939 in every frame, so motion is purely horizontal).
- Sizes measured on zoomed crops of frame 42 (truck near image centre, least perspective) – about ±3 px for edges,
  ±5 px wheel centres, ±8 px tail-lift tip (thin, faint platform), tyre diameter ±8 px.
- Overlays (frames 8-57) confirm the wheel circles and edge lines sit on the truck.

## Reliability
- high (frames 36-50): several templates agree within ~1-3 px; displacement increments very regular.
- medium (14-35, 51-57): one or two templates (cab side early, rear late); smooth, ±2-4 px. Frames 55-57 use the
  partly off-screen rear template and may be a few px high (up to ~+4 px relative to a smooth curve at 57).
- low (3-13, 58): no side feature trackable; position = silhouette front (or rear) edge minus an extrapolated
  front-face (rear-face) width. These early values are probably too far left by up to ~30 px (frame 3) decreasing
  to ~5 px (frame 13) compared with a smooth continuation of frames 14-57. Frames 0-2: only a sliver, no position.
- Per-frame displacement (dx_from_prev_px) rises from ~30 px (frame 15) to ~118 px (frame 57) with a nearly
  constant increment of ~2.0-2.1 px/frame in the reliable range (frame-to-frame jitter ±0.5-1 px). Answering
  sessions should smooth/fit over several frames rather than difference single frames.

## Ambiguities
- Rig root location unknown (centre vs rear axle etc.); does not matter for speeds/accelerations in this 2D
  translation, but for a "position" question pick the point it names (wheel/box columns are given).
- "Length" of the truck: tail-lift tip to front-most (mirror/railing) 1507 px; box rear to cab bumper 1368 px; box
  alone 1078 px. A world-space AABB length would most likely correspond to the full 1507 px (incl. tail lift and
  mirrors) – note which is used when converting with a prior.
- Perspective: front face visible on the left, rear face on the right; silhouette widths vary by up to ~90 px,
  which is why side-plane template points were used.
- Shadow on the floor ahead of/below the truck; not part of the object.
