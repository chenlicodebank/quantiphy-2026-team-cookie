# simulation_0047 – measurement record (pixels, seconds)

Video: 1920x1072, 33 fps, 99 frames (0–98), t = frame/33. Blender render, **2D** scene: near-nadir top-down
view of a straight street running horizontally. **Camera static** (background phase-correlation shift < 0.01 px).
Low sun: every moving object casts a long shadow to the upper-left; shadows were excluded from all extents.

## Objects
Moving (only two):
- **cyclist** – rider in black on a white/silver bike with a ladder-like rear rack, on the asphalt road, riding
  right→left at y≈465–478. Hidden under the right tree's canopy at the start; front wheel tip appears ≈f6,
  fully out ≈f15, visible to the end (f98, ref x≈356).
- **pedestrian** – person in white top / dark trousers on the upper sidewalk, walking right→left at y≈317–320,
  visible and unoccluded in all 99 frames.

Static (positions in scene.json): utility box (light cabinet, upper-left sidewalk), manhole cover (road, left),
road with curbs, upper/lower sidewalks (tiles ~120 px), right tree (canopy x 1480–1910) and lower-middle tree,
pink parked bicycle with basket (lower sidewalk, x 1130–1256, y 806–882 – do not confuse with the moving
cyclist), building with two staircases at top, top-left buildings, flowering bushes, a small round item at (272,184).

## Files
- `scene.json` – inventory, size summaries, static-object extents, events, camera, relations.
- `tracks/cyclist.csv` (frames 6–98), `tracks/pedestrian.csv` (frames 0–98). Columns:
  `ref_x, ref_y` reference point (use this for positions/speeds); `tmpl_x, tmpl_y` raw template-match centre;
  `match_score`; `pos_source` (template or extrapolated); `x0..y1, bbox_w, bbox_h` object box;
  `mask_*` raw segmentation extents (noisy, see below); `occluded`; `extra_x, extra_y` (cyclist: rough rider
  pelvis/saddle estimate = ref + 16.5 px toward rear; pedestrian: same as ref).
- `tracks/*_raw.csv` – raw background-subtraction mask tracks (centroid, bbox, PCA length/width, area).
- `scripts/` – all code (run from scene_ws; the background image `scripts/bg_color.png` was deleted to save
  space – re-create it with `bg_color.py` before running the others): `bg_color.py` (median background), `track.py` (mask tracker with shadow rejection),
  `tmpl_track.py` (template matching, sub-pixel), `finalize.py` (merge + camera check), `static_measure.py`,
  `static_circles.py`, `relations.py`, viewers (`crops.py`, `overlay.py`, `maskviz.py`, `diffviz.py`).

## How measured / reliability
- Positions: grayscale template matching (TM_CCOEFF_NORMED, sub-pixel parabola) with a template from frame 50.
  **Cyclist**: extremely uniform — linear fit f14–98: x = 1619.23 − 12.849·f, y = 479.71 − 0.154·f, rms 0.26 px;
  i.e. 12.85 px/frame ≈ 424 px/s, constant (no acceleration visible). Frames 6–13 are partially under the
  canopy: positions there are **extrapolated** from that fit (pos_source says so); bbox x1 clipped at canopy edge.
  Match score drops to ~0.37 far from frame 50 (pedalling/lighting), but per-frame steps stay 12.6–13.1 px.
  **Pedestrian**: mean step 3.35 px/frame (≈110.5 px/s), oscillating 2.6–4.0 px/frame with the gait (speed
  peaks ≈f2, 20, 37, 55, 71, 88 → a step ≈17 frames). Path f0–98 328.3 px, net 326.7 px. Last ~6 frames have
  lower scores (0.56–0.65) and ±1 px y jitter.
- Reference points: cyclist ref = centre of bike+rider box (midway front-wheel tip ↔ rack end); the true
  rig root is unknown (could be the rider's pelvis ≈ extra_x). Pedestrian ref = head/torso centre from above,
  a proxy for the pelvis. Offsets do not affect displacements/speeds (both translate rigidly on average).
- Sizes (best values, from zoomed frame-50 crops): cyclist length 133 px (front tip x907 → rack end x1040),
  width 46 px (handlebar span, y448–494); rider body ≈45 px long. Pedestrian shoulder width 41–45 px (across
  motion), torso/head along motion ≈27–35 px, with swinging legs up to ~55–65 px. Heights are **not
  observable** (top-down). Cyclist `x0..y1` in the track are the frame-50 geometry moved with the template
  (consistent); pedestrian `x0..y1` come from the mask and often miss dark legs on shadowed ground (and
  sometimes include arm/shadow fragments) – treat as ±10 px along x; across-y extent (bbox_h, median 44) is reliable.
- Mask columns (`mask_*`) for the cyclist: thin front tip and parts of the rider are sometimes lost or shadow
  bits added; prefer the template-based box.
- Static extents: manhole centre (442.5, 554.5), outer ring diameter ≈94 px (radial profile, ±3), inner disc ≈78.
  Road: upper sidewalk edge y≈399, gutter to y≈413, lower curb y≈800–815 → curb-to-curb ≈402 px.
  Utility box top face 117×113 px (x346–462, y251–363); with visible side x346–503, y248–382 (perspective lean
  of a tall object: its roof is closer to the camera, so it appears slightly larger than ground scale).
  Parked bicycle diagonal length ≈136 px (rough, ±5).

## Events
f0 pedestrian already walking; cyclist under canopy. f6 cyclist tip appears. f15 cyclist fully visible.
f22 (t 0.667 s) cyclist passes the pedestrian's x (closest ref–ref distance 155.9 px; road vs sidewalk, no
contact). No starts, stops, turns, bounces or impacts; both keep moving left until the end (f98, t 2.970 s).

## Ambiguities
- Scale: no metric scale assumed. In this 2D top-down render a single px→m scale from a prior (e.g. a given
  cyclist/bike length, pedestrian speed, or cyclist speed) should apply to both movers (both at ground level;
  the cyclist/pedestrian tops are slightly closer to the camera, negligible).
- Long shadows (upper-left) are easy to mistake for the objects in diff images; two moving shadows are visible
  even when the cyclist is hidden at the start.
- Two bicycles: the moving one (road, white/black rider) vs the parked pink one (lower sidewalk, static).
