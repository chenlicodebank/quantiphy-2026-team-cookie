# q1500 – length of the bench seat (simulation_0016)

File fps 33.0044, question_fps 33.0 (difference negligible; 33.0 used).

View: nadir (top-down), static camera, floor parallel to image (uniform tile grid, scene/notes.md confirmed).
Benches run along image y, the same axis the person walks along, so one y-scale serves both.

Scale (from the prior, 1.3 m/s): footprint plateaus (scene record, re-checked: y = 99.4, 168.3, 235.3, 301.5,
368.3, 436.4; mid-stance spacing ~17 frames) give a floor-point speed of 3.952 px/frame = 130.4 px/s at 33 fps.
The pelvis moves horizontally with the same ground speed -> floor scale s_y = 1.3/130.4 = 0.00997 m/px.
Check: step 67.4 px = 0.67 m at a 0.51 s step period (realistic gait). Tiles 131 px = 1.31 m.

Bench (bench_profile.py, column intensity edges at frame 3): left bench cushions y 428 -> 662, right bench cushions
y 428 -> 662 (the dark band 404-428 above the right bench is its cast shadow, toward the upper right), so 234 px for both.
The cushion tops sit ~0.45-0.5 m above the floor. Camera height from depth_info: the plinth at the nadir is 9.97 m away;
benches are 10.63 / 10.59 m away with ~3.5-3.9 m horizontal offset -> vertical ~9.9-10.0 m, so H ~ 10 m. Magnification
of the seat top K = H/(H-0.47) ~ 1.047.
Length = 234 x 0.00997 / 1.047 = 2.23 m.  (If H = 8.1 m as the person-lean estimate suggests, 2.20 m: 1 pct effect.)

The person's own depth_info (9.24 -> 9.14 m) does not fit a pelvis walking at 1.3 m/s (it implies inconsistent camera
heights 8.4 vs 8.8 m), so it was not used (character origin stays near-static).

Second route: both benches give the same 234 px; the scale is consistent with the step length and with the bench depths.
Confidence: good (~3-5 pct), dominated by the seat-height/bounding-box assumption.
Answer: 2.23 m
