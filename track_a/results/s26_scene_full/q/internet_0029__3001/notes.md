# q3001 — distance of the ball from the desk at t = 0.30 s

- **Time base:** 50 fps (file rate = question rate). t = 0.30 s is frame 15.
- **Camera:** static (from the scene record). The clip is 2D: the ball falls vertically in front of a door.
- **Track:** `scene/tracks/ball.csv` (mask centroids). I checked frame 15 visually; the centre is at (548.5, 330.4).
- **Desk:** the grey box/tray top edge is at y ≈ 974 px, read on a zoomed frame 24 (`frames/f24.png`). The ball lands on it.
- **Scale from g = 9.8 m/s²** (`fit.py`):
  - The ball's steps double every 5th frame (7, 12, 17, 22, 24). This looks like a 60→50 fps conversion that drops one source frame in every six.
  - Treating those as two 1/60 s intervals, a quadratic fit of y over frames 8–23 gives 8887 px/s². The max residual is 1.1 px.
  - Sub-windows agree: 8698–9299 px/s². I used 8890 px/s².
  - The total duration is the same either way (15 output frames = 18 source frames = 0.30 s). So a naive 50 fps fit over frames 8–23 gives a similar 9473 px/s², but with residuals of 26 px.
  - Scale = 9.8 / 8890 = 1.102 mm/px.
  - Sanity check: the ball's 76 px diameter comes to 8.4 cm, and the door knob's 64 px to 7 cm. Both are plausible.
- **Distance:** the gap from the ball's bottom (330.4 + 38 = 368.4) to the desk top (974) is 605.6 px, which is **0.668 m**.
  - Alternative reading, ball centre to desk: 643.6 px = 0.709 m.
  - With the naive 50 fps scale, the gap would be 0.627 m.
- **Confidence:** moderate. The main uncertainties are the convention (ball bottom vs. centre) and how the annotators handled the dropped frames.
