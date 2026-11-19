# q_1838 — average speed of the grey/red (silver, red-striped) car

2D top-down video, 24 fps (file and question rates match). Prior: black car speed = 26.085 m/s.
Both cars move at a near-constant pixel step (dark ~27.16 px/frame, silver ~22.29 px/frame), so one m/px
scale from the black car gives the silver car's speed: v_silver = 26.085 x (silver step / dark step).

## Route 1 (ratio.py, scene/ template-fit ref points)
Mean per-frame step over frames 2–48 (skipping the duplicated frame 0→1 and the poor exit slivers):
dark 27.161, silver 22.288 px/frame -> ratio 0.8206 -> 21.40 m/s.
Other windows: 5–45 -> 21.43; 2–30 -> 21.44; 30–48 -> 21.37.

## Route 2 (check.py, plain mask centroids, my own segmentation)
Frames 6–44 without the tree-occluded frames 31–35: dark 27.10, silver 22.30 px/frame -> ratio 0.823 -> 21.47 m/s.

## Answer
21.42 m/s (≈ 0.821 x 26.085). The frame 0→1 near-zero step (duplicated first render frame) is left out; if it were
counted in a mean over every frame, both cars would drop by the same ~2 %, and the ratio would stay the same as long
as the prior is defined the same way. Confidence: high (routes agree within 0.3 %).
