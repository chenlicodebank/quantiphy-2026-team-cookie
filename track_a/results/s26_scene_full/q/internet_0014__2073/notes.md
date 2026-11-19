# q_2073: average velocity of the player with the ball, 8.0-9.0 s

- Scene: a static top-down drone view of a pitch. The camera drift is below about 2 px, and the stabilised tracks from scene/ are used.
- Player with the ball: the dark player B. They chase the rolling ball and reach it at frame about 262 (8.8 s), then dribble
  left. This was checked on frames 238 and 268 (frames/f8.png, frames/f9.png).
- Scale: centre circle radius. My own least-squares circle fit on frame 0 gives 116.55 px; scene/ gives 116.9 px.
  Scale = 9.15 / 116.6 ≈ 0.0785 m/px.
- B's displacement (measure.py):
  - question_fps 30 (frames 240-270): 37.8 px, which gives **2.97 m/s**. A 5-frame-smoothed endpoint gives 2.96, and a
    linear fit gives 2.98. The mean of the per-frame speeds is 3.10 (path, which includes jitter).
  - file fps 29.764 (frames 238-268): 3.07 m/s (smoothed 3.02).
- The two rates differ by under 1%, and both give plausible jogging speeds. The answer takes the middle of the two:
  **3.0 m/s**.
- Second route: the linear-fit velocity (2.98) and the smoothed endpoints (2.96-3.02) agree within about 2%.
- Confidence: good (about ±5%). The main uncertainty is the body-centroid reference point of the player.
