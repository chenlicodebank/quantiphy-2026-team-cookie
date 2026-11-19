# Q376: speed of the ball at t = 1 s (m/s)

- Time base: the file and the question both use 30 fps, so t = 1 s is frame 30. The moving ball is ball 13 (the orange stripe), rolling left.
- Scale (2D top-down view, orthographic): the ball diameter is 48.4 px.
  - The record gives a median ellipse major axis of 48.4 px.
  - My frame-difference masks (threshold 80) give an equivalent diameter of 47.9–48.6 px at frames 0, 29, 30, 31 and 39.
  - A zoomed crop of frame 30 shows the ball spanning about x 532–580 and y 479–527.
  - So 0.0757 / 48.4 = 1.564e-3 m/px.
- Per-frame step near frame 30:
  - The record's centroids give steps of 33.96, 32.51, 33.44, 33.87 and 33.43 px for frames 29–33.
  - My own centroids (measure.py) give 589.25 → 556.34 → 522.72, which is a step of 32.9 px into frame 30 and 33.6 px out of it.
  - The video has repeated and skipped frames, but none at frames 29–33. Around t = 1 the speed is nearly constant: about 31.5 px/frame at frame 21 and 34 at frame 37.
  - I take the local smooth value: 33.3 px/frame.
- Speed = 33.3 × 30 × 1.564e-3 = 1.56 m/s.
- Second route: the raw one-frame difference at frame 30 (32.5–32.9 px) gives 1.53–1.54 m/s, within about 2% of the answer.
- Confidence: good, about ±3%.
