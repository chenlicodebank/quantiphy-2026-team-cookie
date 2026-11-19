# q_2419 — width of the book (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 763 px, principal point (640,360).
"Width" = the book's shorter horizontal side (book lies flat; its long side, ~19 cm, runs left-right across the image,
so the width runs front-to-back, foreshortened). Horizontal image extent of the book (175 px on the table, 125 px
on the ramp) is the LENGTH (~19 cm), not the width.

## Measurements (scripts: profile.py, edges.py, vp.py, solve.py, routeA.py, routeA2.py, routeB.py, check_ramp.py)
- Camera pitch from the table side edges' vanishing point (line fits, residual 1-2 px): VP (599, 350) -> horizon y=350,
  camera pitched down ~0.75 deg (halves: 346/352).
- Book at rest on the table (mean of f40-48), per column x=560..630, sub-pixel edges of the cover top face:
  back edge ~480.5 (at x=565), front-top edge ~495.4, bottom contact ~511. Edges slope -0.043 px/px and the ends of the
  top face lean left going back -> book yawed ~10-13 deg (right end farther).
- Book at rest on the ramp (mean f5-14): cover face rows 350.4 -> 379.5 (29.2-29.6 px) at all columns.

## Route A (table, depth 0.851 m at t=1.6)
Level-frame rays; front face vertical, top face on a horizontal plane; column chord x cos(yaw).
- depth read as distance to the visible surface at the book's image centre (565,496.5) (= front-top edge): chord 9.84 cm
  -> W 9.6-9.7 cm (pitch 0.45-1.05 deg: 9.3-10.0). This reading also reproduces the book length: 174 px front edge at
  Z~0.82-0.84 with 10 deg yaw -> L ~0.19 m = length measured on the ramp (125 px at ~1.16 m).
- depth read as 3D centre of the book: W ~8.8-9.1 cm (but then length on the table ~0.178 m, inconsistent with 0.19).
## Route B (ramp, pitch-independent)
Ramp plane from the given slope distances (top edge centre (589,358) at 1.201 m, bottom edge centre (583.5,480) at
0.9555 m): slope 30.5 deg in camera frame; check: book on the plane at t=1.2 (f29) -> 1.017 m vs given 1.02 m.
Cover plane = ramp plane + T (1.25-1.6 cm). Cover face rows -> W = 8.65-8.8 cm (median 8.7).
B is very sensitive to the ramp angle (W ~ projected 4.45 cm / sin(angle)); using the table W/T ratio with the ramp
cover/front-face pixel ratio gives a slope ~28.4 deg, which would raise B to ~9.2 cm.

## Answer
Routes: A 9.6 (9.3-10.0), B 8.7 (up to 9.2). Combined estimate 9.3 cm. Confidence moderate (±8%).
