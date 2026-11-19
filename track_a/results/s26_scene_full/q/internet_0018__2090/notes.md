# q_2090 — distance between the benches and the court (m)

Prior: singles court width = 8.23 m. Top-down drone view, near-orthographic, so one planar scale (annotator convention).

## Scale
Singles width at the net = 924.7 px between line centres (scene record). Re-checked in `measure.py` at x=2010: top singles
sideline y=587.5, bottom singles fit 1512.2 -> 924.7 px. Scale = 8.23 / 924.7 = 0.008900 m/px (112.4 px/m).
Cross-check: doubles width 1235.5 px / 112.4 = 10.99 m (the standard is 10.97 m), so the scale is consistent.

## Distance
- The benches sit at the top edge of the frame (x 1930-2500), facing the top doubles sideline. "The court" is read as the court boundary, i.e. the outer (doubles) sideline.
- Top doubles sideline (white-pixel profile, frame 0): y = 432.0 at x=2010 and 430.5 at x=2390.
- Bench front edge (white-pixel row profile): left bench seat at 85 and legs at 98; right bench seat at 72 and legs at 87.
- Gaps: left bench 347 (seat) / 334 (legs) px; right bench 358.5 (seat) / 343.5 (legs) px. Mean ≈ 346 px.
- 346 px × 0.00890 = **3.08 m**. The range across the two benches and the two edge choices is 2.97-3.19 m.
- Other readings: to the singles sideline it would be ≈ 4.46 m (+155 px); from the bench centre (y≈55) it would be ≈ 3.35 m.

Second route: the scale from the doubles width (10.97 m / 1235.5 px) gives 346 × 0.008879 = 3.07 m, which agrees.
The camera drift (<15 px over the clip) is irrelevant here because the bench and the line are measured in the same frame.

Confidence: moderate, about ±5 %. The main uncertainty is which bench edge the annotator used.
