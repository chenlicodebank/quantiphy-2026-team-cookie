# simulation_0177 — measurement record

Video: Blender render, 2D scene, 1920x1080, 24 fps, 60 frames (t = frame/24, 0 … 2.458 s).
Content: one elephant (side view, facing right, tusks, curled trunk, thin tail) walks left→right across a
grassy rolling-hill landscape under a cloudy sky. Camera static. No other moving objects.

## Files
- `scene.json` — inventory, camera, summary sizes/displacement, events.
- `tracks/elephant.csv` — one row per frame (0–59). Columns:
  - `ref_x, ref_y` — **recommended reference point** (body/torso centre ≈ rig root): frame-0 core centroid
    plus cumulative torso template shift. Smooth; use this for positions / speeds.
  - `core_*` — mask after a 25 px elliptical opening (body without tail, tusk, thin trunk): centroid and extents.
    `core_x0` = rump edge (reliable); `core_x1` jumps by ±20–30 px when the trunk merges/splits (unreliable);
    `core_y0` ≈ top of back/head (reliable ±2), `core_y1` ≈ feet (grass hides soles).
  - `cx, cy, bbox_*, length_px, height_px, area_px` — raw non-green mask (G−R<10, largest component). Leaks
    into dark grass on frames 0–9 (bbox_x0 = 161 is wrong; true rump ≈ 230–240) and has occasional spikes; use
    only as rough info.
  - `body_x0/x1/body_length_px` — columns where the mask is ≥60 % of the max column height (rough).
  - `torso_dx, torso_dy, torso_cum_x, torso_cum_y` — frame-to-frame NCC template shift of a 120x80 torso patch.
  - `bg_shift_x/y` — camera check (background phase correlation vs frame 0), all < 0.02 px.
  - `occluded` — 0 everywhere (feet only partly hidden by grass).
- `scripts/` — `seg3.py` (segmentation + template track + overlays), `finalize.py` (ref point, camera check),
  `check_shift.py` (independent silhouette-alignment check), `seg.py`/`seg2.py`/`probe*.py` (earlier attempts,
  superseded; seg2 background subtraction leaked because the elephant always covers x≈440–530).

## Key numbers (pixels)
- Motion: ref point (355.5, 740.3) at f0 → (563.6, 737.4) at f59: net 208.2 px, path 208.4 px, mean
  3.53 px/frame (≈84.7 px/s); per-frame steps 3.1–3.95. Purely horizontal (+x); vertical drift ≤5 px.
  Checks: rump edge moved 208.0 px; top-of-back silhouette alignment 214 px (integer-quantised).
  Template steps rise slightly from ~3.35 (f1–30) to ~3.8 (f40–59) px/frame, but the silhouette check shows a
  uniform ~3.6 px/frame and rump edge the opposite trend, so treat the walk as ~constant speed; the
  difference is gait deformation / measurement noise (±0.3 px/frame per frame).
- Sizes (manual on 2x zooms, f0/f30/f59, ±6 px):
  - body length rump → head/ear front, excluding trunk, tusks, tail: ≈ 240 px
  - rump → tusk tip: ≈ 281 px (this is the longest rigid-ish horizontal extent)
  - tail tip → tusk tip: 308 px (f30), 340 px (f59) — tail swings
  - height top of back/head (y≈655) → feet (y≈838–845): ≈ 184 px
  - Apparent size constant through the clip (motion parallel to the image plane), so one m/px scale applies.
- If a prior gives the elephant's (world bounding-box) length, the box likely spans tail-to-trunk/tusk at rest;
  the choice between ≈240 (body), ≈281 (with tusks) and ≈310–340 (with tail) is the main scale ambiguity
  (~±15–25 %). Height ≈184 px is less ambiguous.

## Static objects
- Grass ground / rolling hills (lower ~55 %), hill crest ≈ y 600 at left rising to ≈ y 470 near x 1500.
- Sky with clouds (top). No markings, props or other animals.

## Events
- Elephant walks during the whole clip (moving at frames 0 and 59); no start/stop, contact, bounce or turn.

## Reliability
- Camera static: certain. Horizontal displacement: ±3 px over the clip. Per-frame steps: ±0.3 px.
- Overlays (frames/ov3_*.png, outside the record) confirmed the mask covers the elephant; ear has an olive
  texture patch partly excluded by the colour mask, tusks excluded, tail sometimes partly excluded.
