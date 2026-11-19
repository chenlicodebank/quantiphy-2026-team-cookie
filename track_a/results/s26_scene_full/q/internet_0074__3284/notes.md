# Q3284: ball velocity at 1.00 s (m/s)

**Time base:** the file is 23.976 fps, but it was made from 30 fps footage by dropping every 5th frame: every 4th step in the
ball track is about twice as long as the others. The question gives 30 fps. A file frame k is original frame k + floor(k/4).
t = 1.00 s is original frame 30, which is file frame 24 (the file's own time for frame 24 is 1.001 s, so the two time bases agree).

**Scale:** court width (sideline to sideline) at frame 24 is 904.4 px between line centres and about 913 px between outer
edges. I used 908.6 px, halfway between the two, which gives 6.1 m / 908.6 px = 0.006713 m/px. The camera is a near-overhead
drone and is close to static (slow zoom of about 1.6% over the whole clip), so I used one planar scale.

**Ball:** I used the colour-blob centroids from scene/tracks/ball.csv (±1–2 px). The ball is in the serve's flight, between
contact at frame 14/15 and the net at about frame 34. measure.py works out the speeds using the true original-frame gaps:
- forward difference 24→25 (original frames 30→31): 1236 px/s, **8.30 m/s**
- neighbouring single steps: 8.70, 8.97, 8.36 m/s (noisy, ±2 px per step)
- 10-original-frame windows: 20–30: 8.25; 25–35: 8.56; 30–40: 8.39; 25–40: 8.44 m/s

**Answer:** 8.4 m/s, a lightly smoothed forward speed. The pixel speed is close to constant over these windows, so a second
route (any multi-frame window) agrees within about 2%.
**Confidence:** fairly high. The remaining uncertainty is how the annotators measured the court width (±0.5%) and the
per-frame noise of the forward difference (±4%).
