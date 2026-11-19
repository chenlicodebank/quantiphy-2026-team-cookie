# Q2679 — width of the table (m)

Lab video, 24 fps (file and question_fps agree), 1280x720. f = 0.5959*1280 = 762.8 px, principal point (640,360).
Prior: ball diameter 4 cm. depth_info: ball centre at 1.010 m at t=0.9 (frame 22) and 0.716 m at t=1.4 (frame 34).

## Method (table.py, geom.py)
1. Table outline from the clean frame 48 (non-white mask): left/right side edges fitted on rows 456-580, back edge
   from the top boundary (x 430-740), front top edge from the wood->dark-band transition per column (y≈587.5-592.5).
   Corners: BL (415,439), BR (758,446), FL (186,586), FR (998,592). Side-edge vanishing point (577,336).
2. Table-plane normal = (side-edge 3D direction) x (front/back-edge 3D direction), using K^-1 on vanishing points.
3. Plane offset from the ball: ball centre P = depth * unit ray at frames 22 and 34 (track centres (569.6,453.2) and
   (836.5,513.2), ball still on the table top at both), surface 2 cm (ball radius) below the centre along the normal.
   Using the back-edge direction: h = 0.1740 m (frame 22) and 0.1737 m (frame 34) — the two given depths agree to 0.2 %.
4. Corners back-projected onto the plane: front edge 0.558 m, back edge 0.560 m, sides 0.73 / 0.71 m.
   So the shorter horizontal extent (width) = left-right extent ≈ 0.56 m; length (front-to-back) ≈ 0.72 m.

## Checks
- Using the front-edge direction or an exactly level horizontal direction instead: widths 0.558-0.573 m (spread ±1.5 %).
- Method-card route: front edge 812 px at depth ≈0.52 m -> 812*0.52/762.8 = 0.553 m.
- Ball apparent size at frame 22 is ~27-28 px vs 30.2 px expected at 1.01 m (blur/segmentation of the underside),
  roughly consistent.

Answer: 0.56 m (confidence: good, ~±3 %). The length reading (long side, front-to-back) would be ≈0.72 m.
