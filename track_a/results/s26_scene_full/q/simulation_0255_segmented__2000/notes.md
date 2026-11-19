# Q2000 — speed of the tennis ball at t = 0.5 s (m/s)

2D segmentation video, 24 fps (file fps = question_fps, no re-timing). t = 0.5 s -> frame 12.
Speed = backward difference between frames 11 and 12 x fps.

Script: `measure.py` (I re-tracked the video myself: dark-pixel mask, weighted centroid, area-equivalent diameter, vertical half-max extent).

- Ball diameter in px: area-equivalent diameter median 24.99 (mean 25.12); vertical mask extent median 25; vertical half-max profile 24.7–24.9. I used **25.0 px**.
  Scale = 0.17 m / 25 px = 0.0068 m/px.
- Step from frame 11 to 12: 41.04 px (the scene record gives 41.07).
  Check: a global quadratic fit over all 41 frames (residual 0.19 px) gives 41.11 px/frame at 11.5, and a local fit over frames 6–17 gives 41.09.
  I used 41.1 px/frame, which is 986 px/s.
- Speed = 986 x 0.0068 = **6.71 m/s**.

The ball moves horizontally (y std 0.09 px) and slows down steadily. It has no bounces.
Confidence: high. The main uncertainty is the diameter (±0.3 px, about 1–2%).
