# q_1181 — height of the first step in front of the door of the nearer house

Answer: **0.130 m** (spread over routes and parameters: 0.125–0.135; confidence moderate, about ±8 %).

## Object
The nearer house is the stone house on the right with the arched wooden door at x≈1650–1730. Its stoop runs between two
stone newel posts (balls at about (1350,300) and (1505,300)). The stone railings rise to the right, toward the door.
The bottom (first) step sits between the posts at x≈1367–1450, y≈576–630. Its riser faces the road, and its edges run
toward the street vanishing point. The camera is static. File fps = question fps = 33.

## Riser in pixels (step_edges.py, edges_auto.py)
I averaged the image along lines through the street VP (588,205), which run parallel to the step edges, at columns
1380–1418 in frames 60 and 97:
- top edge: where the tread meets the bright nosing
- bottom edge: the dark contact line with the sidewalk

Result: Δv ≈ 30 ± 1.5 px. At x=1395 the riser runs from row 588.5 to 618.5. Measuring the bottom at the start of the
face→shadow gradient instead gives about 28.4 px.

## Camera (model.py)
- Principal point at the image centre (960,383). The camera is pitched down: building verticals converge downward,
  with the vertical vanishing point about 20–27k px below. The street VP is at y≈195–214. It is taken as the horizon,
  because the near road and sidewalk look level.
- Focal length comes from the near manhole cover, a circle on the road (manhole2.py). Column and row edge reading puts
  the inner disc at y≈707–764 with a half-width of about 110 px. The outer ring is about 700–770 by 570–835. Both give a
  ratio of 0.26 ± 0.01. Since sin(depression angle) = ratio and depression = atan((735.5−383)/f) + pitch, this gives
  f ≈ 2000 px (1967–2040 over horizon rows 214–195).
- My first automatic ellipse fit (manhole.py, ratio 0.24) was biased and has been discarded. It would have given f≈2180
  and a step of 0.120 m.

## Metric scale: camera height H above the road, three routes (final.py)
- **A, speed prior.** I back-projected the cyclist's rear-wheel ground contact onto the road plane at frames 33 and 66.
  Setting the chord equal to 4.87 m gives H ≈ 1.89 m.
- **B, given bike depths.** I used 12.1238 and 16.9027 m with the origin offset along the path fitted so that both
  times give the same H. That needs an offset of about 1.5 m and gives H ≈ 1.88 m.
- **C, image scale.** The rig's image scale ratio Z(66)/Z(33) is 1.45–1.47 (from heights, track distances to the VP,
  and template matching). Combined with the path's Z advance per second (4.87 × u_z), this gives Z(t=1) ≈ 10.4 m and
  H ≈ 1.81–1.89 m.
- Curb height from the curb face at x=1070 (rows 656–681.7) is about 0.10 m. The step base is on the sidewalk plane at
  X≈1.9 m, Z≈9 m.
- Step height = the vertical extent of the riser line above its sidewalk point.

Results (ratio 0.26, horizon rows 195/205/214): route A gives 0.135/0.132/0.129, B gives 0.135/0.131/0.128, and C
gives 0.125–0.134. Median 0.130.

## Inconsistencies (flagged)
- The given bike depth ratio is 1.394, but the image size ratio of the cyclist between t=1 and t=2 is about 1.46. So the
  bike origin cannot be the visible rig at Z≈d: it appears to sit about 1.5 m ahead of the rear-wheel contact. If the
  origin were at the rig, H would be about 2.0 m and the step about 0.139 m.
- The human depths (17.2 and 18.4 m) contradict the ground geometry: the pedestrian's feet are lower in the image than
  the bike's wheel at 12 m. I did not use them.
- The cyclist's image shows Z speed rising from about 4.4 to 5.3 m/s over the clip. That could be acceleration or the
  road rising toward the crest. Routes A and C use only the t=1→2 interval, where the depths imply about 4.8 m/s.
- Sanity check: with f≈2000 the pedestrian is about 1.65 m tall and the camera about 1.85 m high, both plausible. A
  13 cm riser is plausible for a stoop step.

## Uncertainty
- Riser ±1.5 px: ±5 %
- Manhole ratio ±0.01: about ±4 %
- Horizon row ±10 px: ±2 %
- Choice of route: ±4 %
