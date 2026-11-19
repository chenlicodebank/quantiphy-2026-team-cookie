# Q368 — length of the shark (m)

Prior: turtle acceleration = 2.639 m/s^2. 2D scene, static camera, fps 24 (file) = question_fps 24, so no re-timing.

## Scale from the turtle's pixel acceleration
- `track_turtle.py`: high-pass, contrast-normalised template matching of the carapace (x 1320-1560, y 495-555 at frame 34),
  with templates cut from frames 26, 30, 34, 38, 42 and 46, aligned to each other by their median offset. This gives clean x positions for frames 20-47
  (spread between templates < 1 px). The scene record's frames 20-30 were off by ~7 px because of a template-chaining offset;
  this track replaces them.
- Quadratic fit over frames 20-47: a = -538.8 px/s^2 (rms 0.48 px), v0 ≈ 5 px/s, so it starts at rest, which matches the record
  (steps of ~1 px/frame at frames 0-3). A fit with v0 fixed at 0 gives 535.2 px/s^2. Sub-windows give 526-579 px/s^2, and the record's frames 0-26 give 552 px/s^2.
  Value used: 538 px/s^2, so the scale is 2.639 / 538 = 0.004905 m/px.

## Shark length in pixels
- `shark_len.py`: background-difference mask (frame 47 as the background, with its left edge taken from frame 0). Bbox x-extent at threshold 6
  is 907-912 px in frames 26-38 (the faint snout is missed in frames 30-31). The record gives 911 px, using a snout at x 670 that was checked visually and the tail tip at 1579.
  Value used: 910 px.

## Answer
910 px × 0.004905 m/px = **4.46 m** (a plausible great white shark length).
Check: the free fit and the v0 = 0 fit agree within 0.7 %. Taking any acceleration from 526 to 552 px/s^2 gives 4.35-4.57 m.
Confidence: good (about ±3 %).
