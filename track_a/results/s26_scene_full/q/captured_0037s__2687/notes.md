# q_2687 – height of the white cup (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 763 px, principal point ~(640,360).
Depth of the white cup at t=1.0 s: 0.845 m. Camera is static, so the cup is the same in every frame; I measured it on frame 24.

## Measurement (measure_cup.py, frame 24)
I masked the white cup (low saturation, high value) and read intensity profiles down column 775:
- top: the back of the rim is a bright line at y≈377 and the front of the rim is at y≈380 (the rim shows as a ~3 px ellipse)
- bottom: the front bottom edge is at y≈503 (the mask ends at 502/503; dark shadow at 504)
- the bounding-box height is 376.5→503.5 = 127 px; the front-silhouette height (front of rim to front of bottom) is about 124 px
- the cup is about 71 px wide at the top and about 55 px at the bottom (it tapers)

## Scale check with the prior
The ball (4 cm) at 1.055 m should appear 4*763/105.5 = 28.9 px wide. The record gives about 27.7 px for frames 21–27 (-4 %), so f = 763 px and the depths are consistent.

## Results
- Lab-card convention (centre depth × pixel extent / f): 127 px → 14.06 cm; 124 px → 13.73 cm.
- Geometric check (second route): the front silhouette sits closer than the cup's centre. The front of the rim is at about 0.845-0.039 m and the front of the bottom at about 0.845-0.030 m. Back-projecting y=380 and y=503 with a level camera gives H ≈ 13.2 cm. The camera is pitched slightly downward (the rim ellipse is 3 px against 1.8 px predicted for a level camera), which changes this only a little.
- The reference height was measured with a ruler, so the true value is probably about 13.2–13.7 cm. The plain convention gives up to 14.1 cm.

Answer: 13.5 cm, which is within about 4 % of every route above. Confidence: moderate-high.
