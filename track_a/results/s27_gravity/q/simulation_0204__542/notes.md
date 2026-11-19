# Q542 – length of the letter under the gun (simulation_0204)

File fps = question fps = 24. Object: the beige paper card ("letter") lying on the desk mat under the dark revolver,
right of centre (x 1192-1389, y 984-1001 at frame 29). No depth_info; scale from the prior (g = 9.8 m/s^2).

## Scale
- accel.py: quadratic fit to the magnifier's vertical position, frames 0-11 (free fall, before impact at about f11.2):
  a = 7445 px/s^2 (bbox centre), 7431-7445 (centroid) -> s_mag = 1.316e-3 m/px at the magnifier's depth.
  Sanity check: magnifier length 162 px -> 0.21 m and lens 103 px -> 0.136 m, both plausible.
- Perspective (table.py): the table's side edges meet at (1065, 542), so the horizon is y = 542 and the camera is level
  and centred. On the table plane, scale ∝ 1/(v - 542). The magnifier keeps the same lens width in flight and at rest
  (103 vs 104 px), so its fall depth = its resting depth. Its ground contact under the lens centre is v ≈ 1020 ± 5.
- Card edges, measured in code at half-level crossings (cardedge.py): back edge v = 983.8, x 1192.0-1379.3;
  front edge v = 1000.5, x 1197.5-1388.0.
  s(1000.5) = 1.316e-3·478/458.5 = 1.372e-3; s(983.8) = 1.424e-3 m/px.
  Front edge 190.5 px -> 0.261 m; back edge 187.5 px -> 0.267 m; world X extent of the corners (AABB) -> 0.267 m.
  Answer: mean 0.264 m.

## Which side is the length
Focal length from the resting lens ring's ellipse (lensprof.py): minor/major = 17/103.5 = 0.164, which gives
f ≈ 458/0.166 ≈ 2750 px (HFOV about 42°). Camera height above the table = 0.63 m. Front-to-back depth of the card =
0.629·f·(1/441.8 - 1/458.5) ≈ 0.14 m, so the horizontal x-extent (0.264 m) is the longer side, i.e. the length.
The depth side would only exceed 0.264 m if f > 5100 px, which the lens ellipse rules out. The card is about
0.26 x 0.14 m, a plausible letter or envelope.

## Checks and confidence
Front and back edges agree to within ±1 % after the perspective correction. The result is insensitive to the
horizon position (±5 px -> <0.1 %) and the magnifier contact row (±5 px -> ±1 %). The g fit is stable to 0.3 %.
Expected error is about 3 %.
