# q1241 – height of the walking pedestrian (simulation_0058)

File fps = question_fps = 24. t=0.58 s -> frame 14, t=1.58 s -> frame 38. At frame 38 the pedestrian is mostly
outside the image, so the height is measured at frame 14 (depth 18.7297 m given).

## Focal length (focal.py, vanacc.py)
Pinhole camera, principal point (1080,540). Ground orientation comes from the horizon row 422.5 and the main-road
vanishing point (1253.1, 422.5) from the scene record. The white car (van) is placed in 3D at frames 14 and 38 from its
given depths. Every frame's van position is then projected onto that 3D line, and a quadratic is fitted
(frames 2–71; frame 1 is a duplicate of frame 0).
- Acceleration = 4 m/s² (the prior) gives f ≈ 2208 (rear-edge track), 2235 (centre track) and 2240 (frames 2–46 only).
- Second route: the van moves perpendicular to the main road between frames 14 and 38 when f ≈ 2220. The same test on
  the cyclist gives f ≈ 2005. The vertical-motion constraint is too weak to use (1 px ≈ 1.4 cm at 30 m).
- Sanity checks at f = 2220: van length ≈ 6.2 m, taxi side length ≈ 5.6 m, bike length ≈ 1.68 m and rider + bike
  height ≈ 1.71 m. All are plausible. With f = 2000 these come out 10% larger, which is too large.
- Adopted f = 2220 ± 40 px (hFOV ≈ 52°).

## Pedestrian pixel height (prof.py)
Absolute difference from the scene's background_final.png at frame 14, with half-contrast edges: head (hair) top at
row 548.5 and shoe bottom at 788.5, giving 240 px. The record has 549–788. The height is 237–241 px over frames 4–18
because of the gait.

## Conversion (height.py)
Pelvis = depth 18.7297 × the unit ray through (92, ~676). Along the world-vertical line through it, I find where the
projection reaches the head row and the feet row. The pedestrian is far off-axis (|ray| ≈ 1.097), so
H < D·h_px/f. Result: H = 1.863 at f = 2210, 1.842 at f = 2240, 1.944 at f = 2100. The choice of pelvis row has
almost no effect (±0.001).

Answer: 1.86 m. Confidence is moderate. The main error source is f: ±2% from the van acceleration and perpendicularity
routes, up to −8% if the cyclist route (f = 2005) were right. A gait-height versus rest-height difference adds about ±2%.
