# simulation_0204 – measurement record

Video: 2124x1080 px, 24 fps, 30 frames (t = frame/24, frame 0 = 0 s). Blender simulation, labelled 2D. Static camera.

Scene: a magnifying glass falls straight down from the top-centre (x≈1030-1060) onto a desk mat on a
table, bounces/pivots on its rim once and settles. Static props: a typewriter (left), a paper card with
scissors and a dark block (right of centre), the desk mat, a teal wall.

## Files
- `scene.json` – inventory (all objects, pixel extents, positions), camera, events.
- `tracks/magnifier.csv` – per frame 0-29: bbox-centre reference point (`ref_x_bboxcentre`, `ref_y_bboxcentre`),
  mask centroid, bbox, bbox width/height, min-area-rectangle length/width/angle, mask area, occlusion flag
  (always 0), phase label.
- `scripts/track.py` (run as `track.py 18 0.03 --dbg`): background = per-pixel median of frames 0, 8, 29 (the
  magnifier is at distinct places in them); mask = max-channel difference >18, shadow pixels (uniformly darker
  with unchanged chromaticity) removed, close 15x15, holes filled, open 9x9, rows y≥1047 cut (mat front-edge
  strip shows only reflections), largest component. `scripts/export.py` writes the CSV. `scripts/profile.py`
  column profiles used to split lens vs handle. `scripts/strip.py` montage of frames 9-24 for events.

## Key measurements (pixels)
- Magnifier in flight: total length (lens rim to handle tip) 162 px horizontal (bbox 979-1141 at f0), lens
  diameter ≈103 px (x 979-1082), handle incl. ferrule ≈59 px, lens centre x≈1030.5. Nearly edge-on, apparent
  height 42 px (f0) → 20 px (f7) → 40 px (f10), small tilt; horizontal length constant 161-162 px.
- Fall is purely vertical: x of bbox centre stays 1057.5-1060 for frames 0-11; y of bbox centre goes
  200.5 (f0) → 993.5 (f11). Per-frame drops grow steadily (7.3, 20, 33, 46, 59, 72, 85, 98, 111, 123, 135 px by
  centroid), i.e. released from rest at frame 0.
- At rest (f24-29): bbox 974-1124 x 991-1046 (151x56 px); handle points toward the camera so it looks shorter.
- Typewriter bbox 486-798 x 861-1033 (312x172 px). Card 1192-1387 x 983-1002; scissors 1215-1308 x 969-992;
  dark block 1321-1365 x 990-1017. Mat back edge y≈948.

## Events
release f0 (0 s); last airborne frame f11 (0.458 s); first impact between f11 and f12 (≈f11.2, ≈0.467 s;
f12 = 0.5 s shows contact); pivot/bounce on the left rim with handle raised f13-16 (handle tip highest at f15);
second (flat) landing f18 (0.75 s); wobble f19-23; at rest from f24 (1.0 s).

## Reliability / ambiguities
- Flight frames 0-11: mask is clean against the plain wall, ±1 px on edges, positions ±0.5 px. Use these for
  any scale (prior size → magnifier 162 px length / 103 px lens diameter) and fall measurements.
- Origin: the Blender origin is not visible. Bbox centre (x≈1059) and mask centroid (x≈1049, weighted to the
  lens) are both given; lens centre is x≈1030. For the vertical drop all give the same y-differences (±1 px)
  while the object doesn't rotate; after impact (f12+) the object rotates, so the reference choice matters
  by up to ~20 px.
- Frames 12-23 on the mat: lens is transparent and the mat is textured; shadows/reflections partly removed;
  bbox edges ±3-5 px, the bottom edge clipped at y=1046. Width/height there reflect rotation, not size.
- No occlusion, no camera motion; mild motion blur only in the fastest flight frames (f9-11, ~1-2 px).
- Static-prop extents were read off zoomed frames: ±5 px.
