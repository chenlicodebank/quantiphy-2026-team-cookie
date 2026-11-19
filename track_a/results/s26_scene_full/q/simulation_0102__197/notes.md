# Q197: speed of the boat at 1.0 s (m/s)

Prior: the shark's acceleration is 1 m/s². This is a 2D video, so I used one metres-per-pixel scale taken from the shark's pixel acceleration. fps = question_fps = 24.

## Shark pixel acceleration (fit.py, quadratic fits of x(frame))
- Mask centroid, frames 1–60: a = 0.1502 px/frame² (rms 0.54 px). Fits on 1–30 and 30–60 give 0.1448 and 0.1490, and the cubic term is about 0, so the acceleration is constant.
- Nose edge, frames 1–60: 0.1524. Tail edge, frames 1–72: 0.1506.
- I adopted a = 0.1505 px/frame², which is 0.1505 × 24² = 86.7 px/s². Scale = 1/86.7 m/px = 0.01153 m/px.

## Boat speed
- The boat moves at constant speed. The step from frame 23 to 24 is 17.96 px. The mean step over frames 2–72 is 17.887 px, and a linear fit gives 17.882 px/frame (jitter about 0.1 px).
- 17.89 × 24 = 429.3 px/s, times 0.01153 m/px, gives **4.95 m/s**. Using the nose-edge acceleration gives 4.89 m/s.
- Answer: 4.94 m/s.

## Checks
- The three shark reference points (centroid, nose, tail) agree within about 1.5% on the acceleration.
- At this scale the shark is 247.8 px = 2.86 m and the boat is 854 px = 9.85 m. Both sizes are plausible.
- Caveat: the two panels could have different scales, but nothing in the image shows perspective, so I used a single scale.
- Confidence: good (about ±3%).
