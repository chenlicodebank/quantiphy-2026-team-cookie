# q1761 — width of the orange car (m)

2D top-down clip, fps = question_fps = 30. Prior: car acceleration = -2.86 m/s² (car decelerates uniformly).

## Scale from the prior (measure.py)
Quadratic fit y(t) of car over frames 17–90 (fully visible):
- mask centroid: a = -162.4 px/s² (rms 0.26 px); halves 17–50: -159.1, 50–90: -160.7
- bbox centre: -163.8; front edge: -155.9; rear edge: -168.5 (edge noise averages out in the centre)
Adopted a = -162.4 px/s² → scale = 2.86 / 162.4 = 0.01761 m/px.

## Width in pixels
Per-row mask width profile on frames 50, 70, 85, 90: body width 113–115 px over the middle of the car
(median ~112, p90 114). A thin protrusion on the left side only (not mirrored on the right, so a shadow/edge
artifact rather than mirrors) raises bbox width to 120 px in later frames. Adopted body width 114 px.

## Answer
width = 114 × 0.01761 = **2.01 m** (with the left protrusion: 2.11 m). Check: length 289 px → 5.09 m,
length/width ≈ 2.5 — a plausible large sports car. Acceleration fit spread (±2%) gives 1.97–2.04 m.
Confidence: moderate-high.
