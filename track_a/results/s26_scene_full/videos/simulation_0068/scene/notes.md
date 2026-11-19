# simulation_0068 – measurement record (pixels, seconds)

Video: Blender simulation, **2D** scene, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s), 2160x1080.
Straight top-down view of a 4-way street intersection. Pixel coords: x right, y down. Image up = "north".
**Camera static** (background shift < 0.01 px over the clip, phase correlation of sidewalk patches).
No visible perspective: identical props (lamps, planters) have the same pixel size anywhere in the frame,
so one metres-per-pixel scale applies to the whole frame.

## Files
- `scene.json` – inventory, static objects (pixel positions/extents), events, camera, median vehicle sizes.
- `tracks/van.csv`, `tracks/sedan.csv` – one row per frame 0-71 (both vehicles visible and unoccluded in every frame).
  Columns:
  - `frame, t`
  - **`ccx, ccy` – recommended reference point** (centre of min-area rectangle of the body colour mask, ≈ the vehicle's
    geometric centre in top view), `clength, cwidth` (rect extents along / across the vehicle axis), `caxis_deg`
    (orientation of the long axis in the image, 0 = horizontal, 90 = vertical, mod 180), `cbbox_*` (axis-aligned bbox of the colour mask).
  - `cx, cy, length, width, axis_deg, bbox_*`, `mx, my`, `area` – same from the background-difference mask (convex hull);
    includes a little soft shadow / mirrors, so slightly larger (±3-10 px in length on some frames).
  - `edge_touch` (0 always), `occluded` (0 always). No height in a top view (top-down camera: height not observable).
- `bg.jpg` – half-size median background (vehicles removed; faint van ghost near (823,882) from its slow start).
- `static_raw.json` – raw component list of static props from the background.
- `scripts/` – track.py (diff mask tracks) → colour_mask.py (colour masks, adds c* columns) → events.py (per-frame steps),
  check.py (camera shift), static.py (static props), build_scene.py (scene.json), draw_paths.py (overlay check).

## Moving objects
- **van** – white van/minibus in the west (left) lane of the N-S road, drives straight north (up), x = 831 ± 0.5 throughout.
  Body 234 x 84 px (white paint; diff mask 234 x 87-88). Centre y 927 (frames 0-1) → 199 (frame 71).
  Starts from rest at frame ~2 and speeds up steadily all clip: per-frame step ≈1-2 px early, ~10 px at frame 35, ~20 px at frame 71.
  Front (top) edge y 808 → 81. Centre positions are quantised to ~0.5 px (axis-aligned box), so single-frame
  differences are noisy by ±1 px; fit/smooth over several frames for speed/acceleration.
- **sedan** – tan/beige car, starts in the east (right) lane of the N-S road beside the van (centre 990,850.5),
  turns right and ends driving east (centre 1372.5,636.5 at frame 71). Body 219 x 81 px.
  Frames 0 and 1 identical; from frame 2 it moves ~6.9 px/frame (per-frame steps 6.0-7.9, noise ±0.5 px) for the rest of the clip,
  i.e. near-constant pixel speed through the turn. Heading north (axis 90°) → east (axis 0/180°): rotation starts
  frame ~3, axis 135° at frame ~29, essentially complete at frame ~61.

## Events (frame / t)
- 0-1 (0-0.042 s): neither vehicle moves (frame 1 identical to frame 0 for both).
- 2 (0.083 s): sedan starts moving at full ~6.9 px/frame; van starts creeping (accelerating from rest).
- 3 (0.125 s): sedan starts turning right; ~29 (1.21 s) half-way; ~61 (2.54 s) heading due east.
- 20 (0.833 s): van front crosses the south sidewalk line (y≈755) into the intersection box.
- No contact, collision, bounce or stop. Centre-to-centre distance van–sedan: 176.4 px at frame 0 (minimum), 695.8 px at frame 71.

## Static objects (see scene.json for all coordinates)
Road N-S x 615-1081 (≈466 px wide); road E-W y 287-755 (≈468 px wide); four beige sidewalk corner blocks; no lane markings.
White ball on the E-W road at (2028.7, 432.5), diameter ≈20 px; grey rock pile at (2065, 622), ≈69 x 44 px;
8 three-headed street lamps (≈57-75 x 57 px), 4 hydrant-like dark props at the corners, 3 brown planter squares (≈82 x 80 px),
1 dark grate square on the NE sidewalk (≈88 x 91 px, centre 1278,72), a small teal round object (≈24 px) on the SE sidewalk.
None of them move.

## Reliability / ambiguities
- Vehicle centres: ±0.5-1 px per frame; sizes ±2-3 px (soft edges, blurry rendering, dark windshields).
  The van's grey front bumper and a soft ambient-occlusion shadow surround the body; colour-mask sizes exclude them.
- The simulation "origin" of a vehicle may be its root (possibly not exactly the geometric centre, e.g. near the rear axle).
  For the straight-driving van this does not change displacements. For the turning sedan the mask centre path differs slightly
  from a rear-axle path (shorter arc for a rear point); the centre is the best estimate available.
- Pixel step of the van is quantised (0.5 px); use multi-frame fits for speed/acceleration questions.
- 2D scene: questions should use one scale from the given prior (e.g. van or sedan pixel length 234 / 219 px, or a pixel speed).
