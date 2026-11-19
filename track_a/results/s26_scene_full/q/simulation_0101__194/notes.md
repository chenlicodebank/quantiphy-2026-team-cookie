# q194: length of the shark (m). Prior: shark acceleration = 1 m/s^2

2D side-view sim, 24 fps (file fps = question_fps). One m/px scale from the shark's own pixel acceleration.

## Acceleration (measure_shark.py, own background-subtraction mask, shark_track.csv)
Quadratic fit of x(t), frames 1-72 (shark at rest frames 0-1, then moving left):
- centroid: 85.8 px/s^2 (rms 0.37 px); halves of the window give 85.2 and 86.8
- bbox centre: 86.6, nose (xmin): 86.8, tail (xmax): 86.4
-> a ≈ 86.2 px/s^2 => scale = 1/86.2 m/px.
(Per-frame steps grow steadily from 7.6 to ~18 px/frame: 0.15 px/frame^2 ≈ 86 px/s^2, consistent.)

## Length
Mask length 266 px median (264-272). The snout tip is semi-transparent and missed by the mask: on a 5x zoom of
frame 40 the faint snout reaches x≈1130 vs mask x_min 1138; tail tip 1403. Nose-to-tail ≈ 274 px.
Length = 274 / 86.2 = 3.18 m (mask-only 266 px gives 3.09 m).

## Check
Independent reference points (centroid, nose, tail, bbox) and two time windows all give a within ±1.5%.
Confidence: moderate-high; main uncertainty is the snout edge (±3%).
