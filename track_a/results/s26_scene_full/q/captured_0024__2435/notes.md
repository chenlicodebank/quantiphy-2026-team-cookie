# q_2435 – book velocity at t = 1.2 s (frame 29), cm/s

- File fps = question_fps = 24, so t = 1.2 s is frame 29. f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Track: scene/tracks/blue_notebook.csv (full-mask centroid and cyan-cover centroid). I checked the overlays on
  frames 22–32 (frames/sheet.png, view.py) and they sit on the notebook. At frame 29 the notebook's front edge is
  just reaching the table at the foot of the ramp.
- 3D: P24 = back-projection with depth 1.0685 m, P29 = back-projection with depth 0.977 m. The 3D chord is 0.158 m
  over 5 frames, an average of 0.76 m/s over frames 24–29. For frames 20–29, each position is the point on the 3D
  ramp line (P24 to P29) closest to that frame's pixel ray (calc.py, calc2.py).
- Per-frame forward speeds (m/s): 26: 0.80–0.83, 27: 0.86, 28: 0.77–0.81. After the ramp foot (frames 29–31) the
  speed depends on the depth assumed on the table. It is 0.47–0.72 if the depth stays at 0.977 m, and 0.63–0.76 if
  the depth keeps falling at the ramp's rate.
- Smoothed velocity at frame 29 under the different assumptions:
  - 5-frame forward window: 0.67–0.79 m/s.
  - Central difference over frames 27–31: 0.65–0.77 m/s.
  - Quadratic fit on the ramp only (frames 20–29, no impact): 0.94 m/s at 1.2 s. The fitted acceleration is
    1.7 m/s², against the prior's 2.8.
- Answer: 76 cm/s, near the 3D average 0.76 m/s over frames 24–29 and the middle of the smoothed estimates.
- Confidence: moderate, about ±15 %. The main uncertainties are the depth after the book lands and how the
  reference smoothing window handles the deceleration on landing.
