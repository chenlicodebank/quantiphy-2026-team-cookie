# Q1027: butterfly displacement from 0.5 s to 1.0 s

- Prior: speed = 0.32 m/s. The video is a 2D side view, 24 fps (the file and the question use the same rate), so the window is frames 12 to 24.
- Track (scene/tracks/butterfly.csv, body_x): the flight is horizontal (leg tips stay at y≈717–719) and the speed is constant. Per-frame steps are 29.4–32.4 px with a mean of 30.88 px/frame; a linear fit over frames 2–71 gives 30.88 px/frame.
- Scale: 0.32 m/s ÷ 24 = 0.01333 m per frame, which equals 30.88 px, so 4.318e-4 m/px.
- Displacement in frames 12–24: body_x goes from 1970.9 to 1601.8, which is 369.1 px, or 0.1594 m.
- Second route: uniform straight-line motion gives 0.32 × 0.5 = 0.160 m. The front-edge track (x0, 360 px over the window; slope 31.76 px/frame) gives 0.151 m, but its wing-beat effects make it less reliable.
- Answer: 0.16 m. Confidence is high, with an error of about 1%.
