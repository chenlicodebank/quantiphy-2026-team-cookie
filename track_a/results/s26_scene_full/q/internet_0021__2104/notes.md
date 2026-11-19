# q_2104 – average speed of the airplane (prior: length 40 m)

Method (internet convention, one scale): scale = 40 m / airplane pixel length nose-to-tail; average speed = mean of
per-frame displacements of a reference point (background-compensated for the slow camera pan) x scale x fps.
Script: speed.py (uses scene/tracks/airplane.csv, frames 0-88 while the plane is fully in frame).

Checks: zoomed frame 44 (f45.png) – stabiliser tip x~2420, nose x~2782 -> ~362 px, matching the record (364 px at f45).
Track fully covers the plane; frames 89-105 cut by right edge are excluded.

Key numbers: bbox centre (bg-compensated) 21.68 px/frame (raw 20.99). Pixel length grows 328 -> 406 px (plane
approaching); mid/mean length 364 px -> 0.1099 m/px. Frame-local scale (body lengths/frame) gives the same result.

Results (m/s)            fps 29.55   fps 25
bbox centre bg-comp        70.4        59.6
nose bg-comp               71.8        60.7
tail bg-comp               68.9        58.3
scale from frame 0 (328px) 78.1        66.1

Time base: file fps 29.554 vs question_fps 25. 29.55 fps gives ~70 m/s = 137 kt, a typical gear-down approach speed
for a B737-class airliner (40 m); 25 fps gives 59.6 m/s = 116 kt, below normal 737 approach speeds. Used the file fps.

Answer: 70.4 m/s. Second route (tail/nose points, frame-local scale) agrees within 2%. Main uncertainty: which
frame the annotators took the length on (328-406 px -> +-11%) and the fps choice.
