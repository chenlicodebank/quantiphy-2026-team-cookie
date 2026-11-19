# Q1803: boat length (m); prior: shark acceleration = 1 m/s^2

2D side-view clip at 24 fps (the file's fps and question_fps agree). The camera is static. One metres-per-pixel scale comes from the shark's pixel acceleration.

## Shark pixel acceleration (fit.py)
I fitted a quadratic to x(t) over frames 2-58, the frames where the shark is fully in view. It starts moving at frame 2 with v0 ≈ 178 px/s.
- template_dx: 85.2 px/s^2
- bbox centre: 86.2 px/s^2
- nose x0: 86.7 px/s^2
- tail x1: 85.6 px/s^2
- Split windows: 2-30 gives 86-91; 30-58 gives 84-85.

Adopted value: 85.8 px/s^2, so the scale is 1/85.8 m/px.

## Boat length (px)
- The record gives a median x extent of 858.5 px.
- My own re-measurement (boatlen.py; mask min(RGB) < 250 in rows 0-739, counting columns with at least 3 mask pixels) gives 863, 859, 862, 865 and 858 px at frames 0, 10, 20, 30 and 40.
- Adopted value: 860 px.

## Answer
860 / 85.8 = 10.02 m, giving **10.0 m**.

The spread of the inputs (acceleration 85.2-86.7 px/s^2, length 858-865 px) gives 9.9-10.15 m. A 10 m fishing boat is a plausible size. Confidence: high.
