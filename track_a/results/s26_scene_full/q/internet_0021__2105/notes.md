# Q2105 – distance airplane ↔ roof top at t=0 (frame 0)

Scale (internet convention, one factor): plane nose-to-tail pixel length at frame 0 = 328 px (scene track bbox_w,
x 1594–1921; my own coarser mask gave 310 px, the track mask covers the stabiliser tip so 328 is used).
40 m / 328 px = 0.1220 m/px. Time: t=0 is frame 0 under either rate (fps 29.55 vs question_fps 25 irrelevant).

Plane reference point: bbox centre (1757.5, 865.5) at frame 0.
Roof top of the dark glass block directly below the plane (roof.py, per-column first dark pixel, frame 0):
rooftop box top ≈1405 (x 1625–1745), main roof/parapet line ≈1440–1445 (x 1775–1875); building roofline ≈1425–1430.
Vertical gap: to 1405 → 540 px (65.8 m); to 1430 → 565 px (68.9 m); to 1445 → 580 px (70.7 m).
Answer uses the roofline ≈1430 → 565 px × 0.1220 = 68.9 m ≈ 69 m.

Check: scene record's independent roof estimate for this block (≈1425 at frame 30, camera shift there ~2 px) gives
560 px → 68.3 m; consistent. Confidence moderate (which roof point the annotator chose: ±3 %, plane-length pixel ±3 %).
