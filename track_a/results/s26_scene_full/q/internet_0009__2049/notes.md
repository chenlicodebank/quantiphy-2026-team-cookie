# q_2049 — total displacement of the right player (m)

Static top-down drone view (camera shift <= 0.7 px), so I measured in image pixels with a single planar scale (the annotators' convention).
Displacement here means the straight-line distance from the first frame (0) to the last frame (110). The time base does not matter for this question.

## Scale
I re-measured the singles court width (prior 8.23 m) in code (`measure.py`) on frame 60, using white-line centres between the singles sidelines:
1341.5 px at y=950, 1339 at y=1100, 1343 at y=1300 and 1344 at y=1500. That gives about 1342 px, so the scale is 0.006133 m/px.
Check: the baseline-to-service-line distance of 893.5 px converts to 5.48 m (real value 5.485 m).

## Player position
- Core centroid from scene/tracks/right_player.csv (black clothing plus hair): (1486, 973.5) at frame 0 and (1450, 1435) at frame 110. Displacement 463 px, or 459 px when the first and last 3 frames are averaged. That is **2.84 m**.
- Full-mask centroid: 486 px, or **2.98 m**.
- Head position read by eye from crops (frames/f0.png, frames/f110.png): about (1510, 940) to (1480, 1440), roughly 500 px, or 3.07 m.

## Answer
2.88 m. This is a body-centre estimate weighted toward the torso core and checked against the mask centroid.
The spread between reference points (about ±4 %) is the main uncertainty.
