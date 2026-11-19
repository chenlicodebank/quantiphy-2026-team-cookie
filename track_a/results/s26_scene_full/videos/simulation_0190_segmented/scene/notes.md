# simulation_0190_segmented — measurement record

2D segmentation video (Blender render, white background), 1920x1080, 120 fps, 401 frames (t = frame/120).
All values are pixels / seconds. Image y points down: rising = decreasing y.

## Scene
Straight-on rear view of a truck. The **container** (white rear box body with yellow border, chevrons,
"DOLL" labels and a roller door) rises vertically, carrying a brown **cardboard_box** (open dark lid flap)
on its top and the yellow/black **hazard_bar** beneath it. The **truck_lower_chassis** (black frame,
bumper, tail lamps) stays still. Camera static (bumper/lamp templates move < 0.1 px). No ground or background.

## Files
- `scene.json` — inventory, extents, positions at f0/f400, events, camera.
- `tracks/container.csv` — every frame: centre of rear-face mask bbox (ref_x, ref_y), bbox, width/height.
- `tracks/cardboard_box.csv` — every frame: centre of the box-body bbox (lid flap excluded), bbox,
  width/height, top including lid flap, and gap to container top.
- `tracks/hazard_bar.csv` — frame-0 bbox moved by the template-match offset (subpixel).
- `tracks/truck_lower_chassis_check.csv` — static-check offsets of the left tail lamp.
- `scripts/tm_offsets.csv` — subpixel template-match (dx, dy, score) for box, container, hazard bar, lamps,
  bumper. **Best motion signal: `container_dy`** (score > 0.996, ±0.1 px).
- `scripts/` — track_tm.py (template matching), measure.py (masks to tracks), events.py, static.py, overlay.py.

## Measurements
- Container: about 567.5 x 510.5 px (w x h), the same within ±1 px all clip. Centre (944, 594.5) at f0 and (944.5, 514.5) at f400.
  Net rise 79.95 px (template). Horizontal drift < 0.2 px.
- Cardboard box: width about 279 px. Body height 168 px at f0, shrinking steadily to 150 px at f400. Width stays the same, so this
  is probably a perspective/tilt change of the top face. With the lid flap the f0 height is 190 px. Its bottom sits 3–7 px above the container top
  edge in every frame (it moves with the container): bottom edge −82 px vs container −80 px.
  The box template score falls to 0.88 because the texture's shading changes, so use the mask track or
  container_dy for the box's motion, not `cardboard_box_dy` in tm_offsets (it lags by about 7 px at the end).
- Hazard bar: 285 x 31 px, moves exactly with the container (difference ≤ 0.18 px).
- Static chassis: bumper width about 543 px (row 1020), 548 px at row 930; bbox below y=900 is [669,900,1217,1044].
  Tail lamps are at roughly x 683–763 and 1125–1200, y 918–945.
- Roller-door opening (moves with container): about 245 x 426 px at f0, bbox [821,404,1066,830] (estimated by eye, ±3 px).
- Whole silhouette height (lid-flap top to wheel bottom): 901 px at f0, 965 px at f400. Width about 571 px.

## Events
- Frames 0–4: still (offsets ≤ 0.06 px). The rise starts at about frame 5 (t ≈ 0.042 s). Offset passes −0.35 px at frame 6.
  Shortly after the start the rise is already about 10 px/s.
- The rise keeps going and speeds up until the last frame (400). There is no stop, bounce or reversal. A quadratic fits
  container_dy with 0.23–0.26 px rms. This is descriptive only, not a model.

## Reliability / ambiguity
- Mask edges ±1 px and subpixel template offsets ±0.1 px. Mask ref points step in 0.5 px.
  For per-frame speeds, use `container_dy` in tm_offsets.csv (the same offset applies to box and hazard bar).
- 2D scene: a single scale from the prior object. Container width or height, box width, or bumper width are all usable.
  The box's apparent height changes, so prefer the box width (or its f0 height) for box-size priors.
- "Truck" could mean the whole vehicle (static chassis plus the rising body) or the moving body. In this clip
  only the body (container + box + hazard bar + part of the frame) moves.
