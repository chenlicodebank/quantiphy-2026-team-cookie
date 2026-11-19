# simulation_0097 – measurement record (pixels, frames; no metric scale)

Video: 1920x1080, 24 fps, 41 frames (t = frame/24, 0 – 1.667 s). Simulation, **2D** scene.
Pixel coords: x right, y down, full resolution.

## Scene
- Flat uniform grey background (RGB ~132,126,135, noise ≤1 grey level). No ground, horizon, markings,
  shadows or other static objects. Camera static (nothing to shift against, object sizes constant).
- Two moving objects, both seen exactly side-on, both moving purely horizontally:
  1. **airplane** – white Air China jet (red phoenix on tail fin), upper half, nose to the RIGHT, flies right (+x)
     at a constant pixel rate (~53.4 px/frame).
  2. **car** – white/silver Cybertruck-like pickup, lower right (y≈587–627), front to the LEFT; at rest at frame
     0–1, then speeds up to the left (−x), roughly uniformly (~0.37 px/frame², reaching ~15 px/frame at frame 40).
- No contacts, collisions, bounces or direction changes. The objects never overlap.

## Files
- `scene.json` – inventory, extents, events, camera notes.
- `tracks/airplane.csv`, `tracks/car.csv` – one row per frame where visible. Columns:
  frame, time, cx_bbox/cy_bbox (visible-mask bbox centre), cx_centroid/cy_centroid (mask centroid),
  x0,y0,x1,y1 (visible bbox, inclusive), length_px (x1−x0+1), height_px, area_px,
  cut_by_left_edge/cut_by_right_edge, **cx_est/cy_est (recommended reference point: full-object bbox centre)**,
  est_from (full_bbox / right_edge / left_edge), occluded (=cut by frame edge).
- `scripts/track.py` (segmentation + tracks + overlays), `scripts/thr_check.py` (threshold sensitivity),
  `scripts/check.py` (per-frame displacements, sub-extents).

## Method
Foreground = pixels whose max channel difference from the frame's median colour > 6, 3x3 opening, components
≥15 px; rows <545 → airplane, ≥545 → car. Overlays (frames/ov_*.png) checked: masks cover the whole plane
(incl. faint grey tail-cone tip at x≈360 in frame 24, which a higher threshold drops → 793–794 px) and the
whole car incl. wheels.

## Key numbers
- **Airplane** full-view extents (frames 18–38): length 800 px (799–801), height 239 px (tail-fin top y=269 to
  engine bottom y=507). Fuselage alone: rows ~394–480 (~86 px), centre line y≈437. Engine nacelle x 816–906 at f24.
  Visible frames 3–40; partially cut by the left edge 3–17 (cx_est = nose x1 − 399.5) and by the right edge 39–40
  (cx_est = tail x0 + 399.5). Nose x1 = 53.41·frame − 122.4 (resid 0.3 px). Per-frame Δcx 52.5–54.5 px (pixel
  rounding of the bbox; use a fit/longer baselines for precision). cy constant (bbox centre 388; mask centroid ~422).
- **Car** extents: length 121 px (120–123 frame to frame from anti-aliasing), height 41 px (y 587–627). Always
  fully visible (frames 0–40). Centroid x 1473.96 (f0) → 1163.77 (f40) (net −310.2 px; path length same since
  motion is monotonic & straight). Δx frame 0→1 = 0.0; then grows ~linearly. cx_centroid is smoother than cx_bbox
  (bbox ±0.5–1 px jitter); centroid sits ~1.5 px right of the bbox centre (constant offset, irrelevant for motion).
  Sanity quadratic fit of centroid: x ≈ 1474.7 − 0.349 f − 0.1857 f² (resid 0.2 px).

## Events
- f0 (0 s): car at rest; plane off-screen (extrapolated centre x ≈ −522).
- f1 (0.042 s): car starts moving left.
- f3 (0.125 s): plane nose appears at left edge (extrapolated entry f≈2.3).
- f18 (0.75 s): plane fully visible (tail tip crosses x=0 at f≈17.2).
- f39 (1.625 s): plane nose reaches right edge (f≈38.2); plane partly out f39–40.
- f40: end; car still accelerating.

## Reliability / ambiguities
- Positions: ±0.5 px (car centroid ±0.2 px); plane cx_est in edge-cut frames relies on rigid length 800 px (±1 px).
- Origin vs bbox centre: the Blender origin of the airplane may sit on the fuselage axis (y≈437) rather than the
  bbox centre (y=388, raised by the tail fin); the car's root may be at ground/wheel-bottom level (y≈627) rather
  than the bbox centre (607). Horizontal positions/speeds are unaffected; vertical offsets matter only for
  plane–car distance questions (plane–car vertical separation: bbox centres 219 px, fuselage axis to car centre
  ~170 px, fuselage axis to car bottom ~190 px).
- Depth: 2D convention says one scale for both, but the pixel length ratio plane/car = 800/121 = 6.6 while a real
  airliner (~37 m) / Cybertruck (~5.7 m) ratio is ~6.5 – consistent, so a common scale looks plausible.
- No motion blur visible; car's light-grey roof edge is close to background colour (height possibly 1–2 px low).
