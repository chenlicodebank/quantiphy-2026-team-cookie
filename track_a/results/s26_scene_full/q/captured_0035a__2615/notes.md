# q_2615 – basketball displacement 0.5 s → 0.6 s (cm)

- question_fps = file fps = 24 → frames 12 and 14.
- Lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Centres (measure.py: HSV orange mask below y=400, filled contour, ellipse fit; overlays in frames/fit_*.png):
  frame 12 (771.1, 552.2), frame 14 (736.7, 534.5). These match scene/tracks/basketball.csv within about 1 px
  (771.6, 551.9) / (737.0, 533.3).
- Depth: depth_info gives 2.270 m for the basketball at t = 0.6 s. Check against the prior: 23.2 cm at 2.27 m should
  appear as 78.0 px; I measured 79.7 px (equivalent diameter, slight blur), which is consistent.
  No depth is given at 0.5 s. The pixel diameter shrinks by about 1–2.5% from frame 12 to frame 14, so Z12 ≈ 2.21–2.24 m.
- Displacement (disp.py), back-projecting ((u−cx)/f, (v−cy)/f, 1)·Z:
  - same depth at both frames: 11.5 cm
  - Z12 from the diameter ratio (2.21–2.24 m): 11.1–11.5 cm (z-depth) or 11.1–12.1 cm (Euclidean-depth reading)
  - record centres instead of mine: about 0.15 cm more
- Second route: record centres and record diameters give 11.4–11.9 cm. All routes fall between 10.8 and 12.2 cm.
- Answer: 11.5 cm. Confidence moderate (±5%): the depth change between 0.5 s and 0.6 s is uncertain.
- Note: the scene record suspects a dropped frame between frames 11 and 12. That does not affect this displacement.
