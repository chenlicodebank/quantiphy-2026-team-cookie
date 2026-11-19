# Q1096: walking speed of the person at t = 1.0 s (m/s)

Answer: **0.43 m/s**

Frame rates: the question uses 30 fps and the file runs at 29.9966 fps, so t = 1.0 s is frame 30.

## Method
- **Camera:** static, as recorded in scene/ (wall phase correlation).
- **Motion:** the man walks left to right, parallel to the image plane. His head-top row stays at 649-654 and his body
  height at about 218 px for the whole clip, so his depth Z is constant and the speed is the lateral pixel speed
  times Z/f.
- **Pixel speed** (`track_head.py`): I subtracted a median background and took the centroid x of the head and neck
  band (rows 648-690). The props do not cover this band for frames 0-50.
  - Linear and quadratic fits over windows centred on frame 30 (15-45, 16-44, 20-40, 23-37, 10-50) give
    1.65-1.71 px/frame. I used about 1.67 px/frame.
  - The one-frame steps around frame 30 vary between 1.44 and 2.1 px because of the gait.
- **Scale** (`speed.py`): the person is 1.87 m tall and about 218-222 px from head top to sole, so k = Z/f ≈
  0.0085 m/px.
  - Combining k with the given distance at t = 0 (13.882 m) and the pelvis pixel at frame 0 gives Z = 13.18 m and
    f ≈ 1540 px.
  - That geometry predicts a distance of 13.763 m at t = 1 s; the given value is 13.768 m. The height scale and
    the given distances agree.
- **Speed** = 1.67 × 30 × 0.0085 ≈ 0.43 m/s.

## Second route (distances only)
The camera distance falls by 0.114 m between t = 0 and t = 1 s while the man is about 3.7 m left of the optical
axis. With constant Z, this gives a mean lateral speed of (d0 − d1) · d / |X| = 0.427 m/s. The pixel track over the
same second gives 0.434 m/s.

## Plausibility
0.43 m/s is slow for a walk; the usual floor is 0.9 m/s. Two independent routes still agree on it: the height scale
and the change in the given distances. A faster speed would need motion in depth, but the apparent size does not
change.

The pace is not constant. Late in the clip (frames 74-88) the head moves about 2.5 px/frame (≈0.64 m/s), but around
t = 1 s it moves about 1.67 px/frame.

**Confidence:** moderate to good, about ±5 %. The main uncertainty is gait oscillation in the one-frame reference
value.
