# Q191: speed of the shark at t = 0.0 s (m/s)

Prior: shark acceleration = 1 m/s^2. This is a 2D scene, so one m/px scale comes from the shark's pixel acceleration.
fps = question_fps = 24.

## Method (fit.py)
- Used the shark tracks in scene/tracks/shark.csv (centroid, bbox centre, nose, tail). The motion is horizontal only.
- Frames 0 and 1 are identical, which looks like a duplicated start frame. Motion starts between frames 1 and 2.
- Fitted x(frame) with a quadratic over frames 1-72 and over frames 2-72.
  - Centroid: a = 0.1491 px/frame^2 = 85.9 px/s^2, rms 0.35 px. So the scale is 1/85.9 m/px.
  - Fitted velocity at frame 0 is 7.18 px/frame, i.e. 172.4 px/s = **2.01 m/s**.
  - At frame 1 the velocity is 2.05 m/s; the first frame step (frames 1 to 2) gives 2.07 m/s.

## Second route
Other reference points give the same answer within noise:
- bbox centre: 1.97-1.98 m/s
- tail: 1.99 m/s
- nose: 1.96-1.97 m/s

## Answer
The shark is uniformly accelerated with initial speed v0 ≈ 2.0 m/s (range 1.96-2.07, depending on whether the
simulation starts at frame 0 or frame 1). The literal backward difference at frame 0 is undefined, and frames 0 and 1
are identical, which is a render artefact. The answer is the simulation's initial speed: **2.0 m/s**.
Confidence: high (about ±3%).
