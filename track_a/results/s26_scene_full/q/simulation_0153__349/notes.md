# q_349 — speed of the blue car at t = 1 s

2D side-on motion at constant depth (contact line y≈947). fps = question_fps = 24, so t = 1 s → frame 24, and the
speed comes from the backward difference over frames 23→24.

## Scale (prior: tyre diameter = 0.369 m)
wheel.py / wheel2.py: dark-run analysis of the rear tyre against the bright floor (frames 30–36). At hub height (rows
891–897) the tyre ring spans x 822/823 → 929, so the diameter is about 107 px. Both sides of the ring are equally thick
(16–17 px), which means nothing is occluding it. The hub centre is at y≈893.5, and 893.5 + 53.5 = 947, which matches
the ground contact. The width is the same in frames 30–36.
Scale = 0.369 / 107 = 3.449e-3 m/px.

## Pixel displacement 23→24
- scene record panel template (lower body between the wheels): 382.68 − 334.66 = 48.0 px
- disp.py NCC, rear-light patch (score 0.99): 47.99 px; canopy rear pillar (score 0.98): 47.0 px; front body patch
  (score 0.70, partly background, so biased low): 45.2 px
I used ≈47.6 px/frame. The points low on the body, near the root, read 48.0; the pillar reads 47.0.

Speed = 47.6 × 24 × 3.449e-3 ≈ 3.94 m/s (3.97 if I use 48.0). Answer: 3.95 m/s.
Second route: a separate template track (the rear lights) agrees with the record's panel track to within 0.05 px.
Confidence: about ±3 % (from the tyre-edge threshold of ±1 px and the 1 px spread between points).
