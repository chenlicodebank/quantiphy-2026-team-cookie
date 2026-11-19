# q 2551 — length of the table (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). Camera f = 0.5959*1280 = 762.75 px, principal point (640,360).

## Method
1. `edges.py` (frame 0): table mask (non-black component) -> line fits of the top surface edges:
   back edge (mask top), left/right side edges (mask sides, rows 432-479, residual < 0.6 px), front top edge
   (max vertical luminance gradient between top surface and front face). Corners: BL (573.6,424.9), BR (850.8,428.3),
   FL (463.1,482.8), FR (963.0,494.7). Side edges vanish at (717.7,349.5); front/back edges vanish at (-4596,362).
2. `geom.py`: table-plane normal = cross of the two vanishing directions (they are 87.5 deg apart, near-rectangular).
   Plane offset from the depth_info at t=1.5 s (frame 36): tennis ball centre (582.5,437.5) at 1.183 m, ping-pong
   centre (722,434) at 1.353 m, each lowered by its radius (3.35 cm, 2.0 cm) along the normal. The two balls give the
   same plane offset to 0.05 mm (camera 16.84 cm above the table top) — strong check of the depth_info and f.
   Alternative plane (route B: contains the side-edge direction and both ball contact points) differs by 0.01 deg.
3. Back-projecting the 4 corners onto the plane: front edge 60.4 cm, back edge 60.4 cm, left side 74.6 cm,
   right side 74.6 cm (corner angle 92.5 deg). Front edge at Z~0.93 m, back edge at Z~1.67 m.
   Length = longer horizontal extent = front-to-back side = 74.6 cm; width = 60.4 cm.

## Checks
- `check.py`: the yellow ball's plane-based distance vs its apparent-size distance (f*6.7cm/diam): frame 40 1.111 vs
  1.111 m, frame 42 1.036 vs 1.022 m, at rest 1.633 vs 1.597 m -> consistent within 1-2 %.
- Sensitivity: the length depends mostly on the back edge (grazing view): 1 px -> ~2.2 cm. The mask's back edge is a
  hard SAM2 cut; a half-maximum sub-pixel fit (`profile.py`) puts it ~0.5 px higher -> 75.8 cm. Front edge ±2 px -> ±1.4 cm.
- Range of estimates 74.6-75.8 cm; answer 75 cm. Width reading (shorter side) would be 60.4 cm.

Confidence: moderate-good (±3 %).
