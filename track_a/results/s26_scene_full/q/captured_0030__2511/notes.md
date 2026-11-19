# q2511 — velocity of the red ball at 0.8 s (cm/s)

The file runs at 24 fps and question_fps is 24, so t = 0.8 s is frame round(19.2) = 19. The given depths fall at frames 5, 10, 14 and 19.
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). The camera is static (per the record).

## Situation at frame 19
The ball (swung on a stick by the person) has just crossed the far side of its loop moving right (about 40 px/frame
at about 1.32 m depth, roughly 170 cm/s laterally). Starting at frame 19 it turns towards the camera, and its depth falls from
1.32 m (f19) to about 0.95 m (f22). The speed is therefore changing quickly at frame 19: forward steps are about 170 cm/s
(18→19) and about 340–400 cm/s (19→21).

## Route 1: ball moving in a plane (main route)
I back-projected the 4 given depths at the ball centroids and fitted a plane. The residuals are ≤6 mm, and the plane is
nearly parallel to the table (its horizon falls at y≈343 against the table's y≈328). Intersecting each frame's centroid ray with this
plane gives a 3D position for every frame. Taking the forward 3D differences ×24 and averaging the 5 forward
steps centred on frame 19 (17→18 … 21→22) gives:
record centroids 284, re-measured centroids (remeasure.py) 279, bbox-mid 312, plane forced parallel to the table 265/267 cm/s.

## Route 2: depth from the ball's pixel size (check)
I took depth = k / (vertical pixel extent of the ball), with k anchored at the given depth at frame 19. The resulting depths for
f17–23 (1.31, 1.32, 1.315, 1.12, 0.99, 0.87, 0.80) agree with the plane route (1.26, 1.36, 1.34, 1.21, 1.04, 0.98, 0.85).
The mean of the 5 centred forward steps is 291 cm/s. Size-based depth on its own scatters by ±10% against the given depths
(blur), so I used this route only as a check.

## Answer
About 285 cm/s: the 5-frame-smoothed forward-difference speed at frame 19.
Other conventions would give different values. The raw forward difference at f19 alone is about 340 cm/s. A centred
derivative of smoothed positions (Savitzky–Golay) is about 150–240 cm/s, because frame 19 sits right where the ball
speeds up into the turn. Confidence is moderate, because the speed is changing quickly at this time.
