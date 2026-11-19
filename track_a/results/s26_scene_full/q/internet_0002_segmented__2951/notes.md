# Q2951 — width of the red car (m); prior: lane width = 3.66 m

Nadir aerial view, static camera; 2D planar scale from the lane width (one scale factor, annotator convention).
Time base irrelevant (static size question; fps 24 vs question_fps 30 does not matter).

## Lane width in pixels (measure.py)
Lines fitted through the dash centres of each dash row (scene.json, checked). The red car's lane lies between rows
y≈330 and y≈437: spacing 105.4 (x=200), 106.1 (x=400), 107.0 (x=640), 107.9 (x=900), 108.6 (x=1100) px; mean of all
five lanes ≈106 px. Car spends most of the clip at x 400–1000 -> lane width ≈ 107 px.
Scale = 3.66 / 107 = 0.0342 m/px.

## Car width in pixels (measure.py, edge.py)
Per-column vertical extent of the SAM mask (excluding the mirror columns, which reach 74–77 px):
f0 67, f12 66, f18 68, f24 67, f30 67 px (mask incl. a 4–6 px dark halo on the top side = road/shadow, values 60–100
vs body 120–180). Intensity profiles at f12 (x=450, 490, 560, 575): body proper ≈ 60–62 px; threshold 80 on the
mask -> median 62.5 px. Car tilt ≤ 0.05 rad, negligible (cos > 0.998).
Adopt body width ≈ 62 px (mirrors excluded, wheel-to-wheel/body reading).

## Answer
62 × 3.66 / 107 ≈ 2.12 m.
Alternatives: full mask 66–67 px -> 2.26–2.29 m; with mirrors 76 px -> 2.6 m (not the width convention).
Check: same ratio with mean lane spacing 106 px -> 2.14 m; a full-size pickup is ~2.0–2.1 m wide (plausible).
Confidence: moderate (±5 %, edge definition of soft SAM mask dominates).
