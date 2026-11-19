# Q100 — speed of yellow car at 1.0 s (simulation_0083, 2D top-down, 24 fps)

- fps = question_fps = 24 → t = 1.0 s is frame 24.
- Scale: prior length 5.67 m. Yellow car x-extent measured in my own code (measure.py, yellow chroma R−B>30 mask)
  = 270 px at frames 0–28, matching the scene record → 0.021 m/px.
- Motion: bbox centre moves exactly −10 px/frame (frames 23→24: 10.0; 16→24 and 20→28 means: 10.0; 24→32: 10.1,
  slight edge perspective growth). Scene record tracks agree (constant 10 px/frame from frame 2).
- Speed = 10 px × 24 fps × 5.67/270 = **5.04 m/s**.
- Second route: multi-frame windows on both sides of frame 24 and the record's tracks give the same value.
- Confidence: high (constant velocity, clean mask, near-orthographic view).
