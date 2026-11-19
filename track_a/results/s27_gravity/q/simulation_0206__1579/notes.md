# q_1579 — speed of the typewriter at t = 0.125 s

question_fps = file fps = 24, so t = 0.125 s is frame 3. Speed = |p(3) - p(2)| x 24 (one-frame backward difference).

Prior: acceleration before 0.45 s = 9.8 m/s^2, so the typewriter is in free fall until it hits the desk (between frames 10 and 11).

## Release time (fit.py)
- I fitted quadratics to the pixel track over frames 0-9. The bottom edge from scene/ gives its vertex (zero velocity) at
  frame -0.10 (frames 0-9) or +0.004 (frames 2-9). I measured the bottom edge again myself by differencing against the
  last frame and got 107,114,132,162,203,254,316,387,469, which matches the record.
- The bbox-centre ref_y gives a vertex at about frame -0.24. That track is less reliable at the start because the top
  edge is cut off by the image in frames 0-1.
- x stays constant (about 1240 px), so it falls straight down. The depth change from 4.32 to 4.50 m fits a vertical
  drop seen by a camera looking down at the desk.
- Conclusion: it is released from rest at frame 0 (t = 0).

## Answer
In free fall from rest at frame 0: y(i) = 0.5 g (i/24)^2, so the backward-difference speed at frame 3 is
g (3^2 - 2^2) / (2 x 24) = 9.8 x 2.5 / 24 = 1.021 m/s.

## Second route
- The pixel acceleration of the bottom edge is about 11.3 px/frame^2. Matching that to 9.8 m/s^2 gives about 663 px/m
  for vertical motion near the start.
- The measured step from frame 2 to 3 is 30-31 px, which gives 1.08-1.12 m/s. The model step (2.5 x 11.3 = 28.3 px)
  gives 1.02 m/s.
- The extra few pixels are tracking noise and the slight rotation of the typewriter.

Confidence: high. If the release time were off by 0.2 frame, the answer would change by about 8 pct.
