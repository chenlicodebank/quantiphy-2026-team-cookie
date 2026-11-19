# q_2776: distance from the yoga ball to the person at 1.5 s

The file's frame rate and question_fps are both 24, so t = 1.5 s is frame 36. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
The depth_info line for t = 1.5 s says "soccer_ball", but the only ball in the video is the yoga ball, so I read it as the yoga ball at 1.4972 m. Its apparent size agrees with that (see the checks below).

## Measurements (script: measure.py)
- Ball centre at frame 36, from the scene record, checked on the frame image: free circle fit (360.9, 668.8), fixed-radius fit (361.9, 675.5). The bottom of the ball is cut off by the image edge. I used the midpoint, (361.4, 672).
- Person centre: centroid of the person mask, (588, 445), steady across frames 30–39. This is also the middle of the person's vertical extent (head top at y 349, shoes at about 540).
- Each centre was back-projected along its unit ray to the given Euclidean distance: 1.4972 m for the ball and 3.83 m for the person.
- Result: the 3D distance is **2.497 m**. The two ball fits give 2.496 and 2.499. Moving the person centre by ±15 px gives 2.486 to 2.509.

## Checks
- Ball radius from frame 24 (diameter about 154 px at 2.4985 m): R = 0.251 m. At 1.4972 m that radius should look 259 px wide, and the measured diameter trend at frame 36 is 257 px. Going the other way, the size implies a depth of 1.508 m at frame 36, against 1.4972 given.
- Ball speed from size-based depth plus image position over frames 21–28: mean 2.13 m/s, and 2.13 at frame 24. The prior is 2.1464 m/s, about 1% away.

Confidence: high, within about ±2%. The main uncertainty is where the annotator clicked the person's centre.
