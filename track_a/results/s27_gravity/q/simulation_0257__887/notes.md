# q_887 – width of the phone right of the plant

Video file is 24 fps, question_fps = 30; all timing uses 30 fps (frame index × 1/30 s). 2D scene, static camera.

## Scale (prior: plant falls with 9.8 m/s² before 0.5 s)
measure.py: quadratic fits to the pot's tracked bottom edge y1 (scene/tracks, frames 0–14, before impact at 15)
give a = 7.00 px/frame² (frames 2–14: 7.09; centroid 0–14: 6.93). Second differences are constant ~7 px/frame².
a = 7.0 × 30² = 6300 px/s² → 9.8 / 6300 = **0.00155 m/px** (range 0.00154–0.00157).

## Phone
phone_edges.py: half-level edge crossings per row on frame 0. The phone lies flat on the table, seen almost edge-on,
spanning x ≈ 1141.0 – 1191.3 at its widest rows (868–869) → 50 px; the front face rows give 45–48 px (a small
slanted end at the right suggests a slight yaw / visible corner). The full horizontal extent (≈ AABB x-extent) is
taken: ~49.5 ± 1 px.
Width = 49.5 × 0.00155 ≈ **0.077 m**.

## Checks
- The visible horizontal side must be the phone's short side: 0.077 m is a typical phone width, while as a
  length it would be far too small; the phone's long side runs into depth (top face strongly foreshortened).
- Same scale makes the LG outdoor AC unit 505 px → 0.78 m and pot ~0.07 m wide: realistic, confirming 30 fps
  timing (24 fps timing would give 1.2 m AC unit and 0.12 m phone width).
- Using the front-face extent (45 px) instead gives 0.070 m; answer 0.077 m.

Confidence: moderate-high (±5 %).
