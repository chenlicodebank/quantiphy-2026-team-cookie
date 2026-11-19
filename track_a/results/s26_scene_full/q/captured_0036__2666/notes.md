# q_2666 - ping pong ball velocity at 0.9 s (cm/s)

t=0.9 s -> frame round(0.9*24)=22 (question_fps = file fps = 24). Ball rolls on the table frames 13-35.

Method (vel.py): f = 0.5959*1280 = 763 px, principal point (640,360). Ball centres from scene/tracks/ball.csv
(white-mask edges + contact-shadow bottom, +-1.5 px). The 3D centres at frames 22 and 34 are fixed by back-projecting
with the given depths (1.010 m, 0.716 m). The ball rolls on a flat table in a straight line, so every other frame's
3D centre = point on the line P22-P34 closest to that frame's ray; ray-to-line gaps are < 1.2 mm on all frames 13-35,
confirming the straight path. Per-frame forward-difference speeds around frame 22: 87.4, 88.5, 86.5, 85.0, 89.9 cm/s
(frames 20..24); 5-frame smoothed = 87.4, 3-frame = 87.1, 7-frame = 86.7.

Checks: prior size reproduced: 31 px diam at frame 22 -> 1.01*31/763 = 4.1 cm; 45 px at frame 34 -> 4.2 cm (prior 4 cm).
Route 2 (vel2.py): depth from the apparent diameter (scaled to 1.01 m at frame 22) gives 75-92 cm/s depending on the
window (diameter noise, +-1 px = +-3% depth); depth linear in time between the two given depths gives 79 cm/s, but
that is biased low because the ball is slowing (speed falls from ~88 to ~77 cm/s by frame 34), so the depth rate is not
constant. The straight-line-on-table route is the best constrained.

Answer: 87 cm/s. Confidence: moderate-high (~+-6%).
