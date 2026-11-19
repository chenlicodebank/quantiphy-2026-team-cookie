# simulation_0085 — measurement record (pixels, frames; t = frame/24)

Scene: 2D simulation, top-down view of a flat uniform grey ground (RGB 140). Camera static (no background
features, nothing shifts). No perspective: both objects keep constant pixel size over the clip, so one
metres-per-pixel scale from the prior object applies to everything. No static objects or markings.

## Objects
- **cyclist**: rider in dark clothes on a teal bicycle, upper lane, image y ≈ 381, heading and moving left (-x).
  Visible frames 0–71 (fully in frame 4–67; enters from the right edge, front leaves left edge at 68).
  Whole rider+bike extent: length 213 px along x (211–217), width 61 px across (handlebars/arms).
  Bike-only (teal pixels): length 208 px, width 50 px. Speed essentially constant ≈ 26.6 px/frame
  (per-frame dx alternates 26/27 from integer edges); frame 0 and 1 have the same position.
- **car**: Cybertruck-like pickup (white/silver body, black roof glass, dark rear bed, side mirrors), lower lane,
  image y ≈ 727.5, front to the left, moving left. Visible frames 0–71 (front visible from x=1839 at f0;
  fully in frame 40–63; front edge leaves at 64). Length bumper-to-bumper 726–728 px (range 722–734),
  width 316 px including mirrors, ~268 px body without mirrors (frames 0–17 when mirrors still off-screen).
  Starts from rest at frame ~1–2 and accelerates roughly uniformly, per-frame front-edge displacement
  rising ~1.5 px/frame each frame to ~62 px/frame around frame 67, then about constant to the end.

## Files
- `scene.json` — inventory, extents, events, camera.
- `tracks/cyclist.csv`, `tracks/car.csv` — every frame: ref_x/ref_y = bbox centre of the visible mask
  (use only when cut_by_frame_edge=0), centroid of mask, bbox, length_px (x extent), width_px (y extent),
  height_px blank (top view, not measurable), area, cut_by_frame_edge, occluded (always 0: no overlap).
  `centre_x_full` = best origin estimate every frame: bbox centre when fully visible, otherwise leading
  (front, x0) edge + (L-1)/2 or trailing edge − (L-1)/2 with L = median full length (cyclist 213, car 726);
  `centre_x_src` says which. y of the origin is constant (cyclist 381–382.5, car 727.5).
- `tracks/cyclist_parts.csv` — teal bike-only bbox/centroid; "rider_*" columns are all dark pixels
  (g<80), which include the tyres, so their extents equal the whole cyclist; rider_cx is biased toward
  the torso (~10 px behind (+x) the bbox centre). Pelvis is hidden under the torso from above; the
  bike/bbox centre is the recommended origin (pelvis ≈ bbox centre +0…10 px in x).
- `scripts/` — probe.py (pixel levels), track.py (segmentation: |grey−140|>45 or RGB saturation>35,
  close + hole fill; components split by y<520 → cyclist, else car), edges.py (edge-based centres),
  parts_summary.py, overlay.py (bbox/ref drawn on frames, checked visually at frames 0 and 45: boxes hit
  the full cyclist and the full car incl. mirrors, shadows excluded).

## Reliability / ambiguity
- Edges ±1 px; per-frame displacements ±1 px (integer edges). Car length varies 722–734 px across frames
  (motion blur / anti-aliasing at higher speed); for car motion, front edge x0 (frames 0–63) and rear edge
  x1 (frames 40–71) are the cleanest signals, and both give the same per-frame dx. The switch between
  estimators in centre_x_full produces small jumps at frames 40 (−3 px) and 64; prefer edge differences.
- Soft shadows (grey down to ~100) surround both objects and are excluded by the threshold.
- Car origin assumed at bbox centre (vehicle root in top view); a rear-axle root would shift it by a
  constant, irrelevant for speeds. Distances between the two origins: x from centre_x_full, y gap 346 px.
- Events: overtake (car front passes cyclist front) ≈ frame 60.7; car centre passes cyclist centre ≈ frame 68.
