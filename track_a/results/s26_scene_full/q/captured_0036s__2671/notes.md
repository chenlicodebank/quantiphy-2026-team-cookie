# q_2671 — ping pong ball velocity at t = 0.9 s (cm/s)

Lab video, 24 fps (file and question_fps both 24), 1280x720. f = 0.5959*1280 = 762.8 px, principal point (640,360).
t = 0.9 s -> frame round(21.6) = 22. depth_info: dist 1.010 m at frame 22, 0.716 m at t=1.4 s -> frame 34.

## Track
scene/tracks/ball.csv centroids checked against zoomed crops (frames/crops.png) and my own mask (track.py,
mytrack.json): u agrees within ~1 px. v is within 1-3 px; the top of the ball sits on the table back edge
around frames 20-24, and the shaded underside merges with the contact shadow. The v errors hardly matter (tested ±3 px).
The image path for frames 14-34 is a straight line (v = 333.1 + 0.2155 u, rms residual 1.4 px), so the ball rolls
in a straight line in 3D.

## Route A (used): straight 3D path through the two given points (velocity.py)
P22 = 1.010 * unit ray(frame 22) and P34 = 0.716 * unit ray(frame 34). Each frame's 3D centre = the point on the
line P22-P34 that the frame's viewing ray meets. Distances: f20 1.072, f21 1.040, f22 1.010, f23 0.978, f24 0.952,
f25 0.924 m.
Speeds near frame 22 (cm/s): 21->22 88.8, 22->23 94.4. Smoothed over 5 frames: (P25-P20)/5 = 88.8,
mean forward 21..25 = 87.5, (P25-P19)/6 = 87.6. Raw v and v shifted by ±3 px give 87.3-89.4.
-> answer 88.5 cm/s. Speeds in frames 25-35 are a smooth 87 -> 76 cm/s (slow rolling deceleration).

## Route B check: apparent size
The mask height (from the halo above the ball to the halo below it) times the Route-A distance is about constant over
frames 26-35 (about 30-32 px*m). The Route-A depth rate is therefore consistent with the ball's growth in the image.
At rest (frame 5, H = 24 px), Route A's extrapolated distance of 1.41 m is about 7 % more than size implies (about
1.33 m). That is the badly conditioned far end of the line, away from frame 22.

## Route C check: table-top plane (plane.py)
The plane normal comes from the table's vanishing points, and the plane is placed through P22. It predicts 0.749 m at
frame 34, against the given 0.716 m, and the camera grazes the plane at about 2.4 deg, so per-frame depths are noisy.
The 5-frame speed is about 81-83 cm/s. This route contradicts the given depth at frame 34. Forcing it through both
given points reduces it to Route A, so Route A is preferred.

Confidence: moderate. The answer is likely within ~5-8 %. The main uncertainty is the depth rate near frame 22.
