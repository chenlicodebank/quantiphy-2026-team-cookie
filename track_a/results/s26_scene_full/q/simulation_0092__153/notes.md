# Q153: speed of the plane at t = 1.0 s (frame 24)

2D video, side view, static camera, fps = question_fps = 24, so no re-timing.
Script: `measure.py` (median background, |diff| > 12 mask, opening, components; plane rows 250-590, car rows 590-760).

- Plane bbox x0/x1, frames 22-26: 464/1320, 407/1263, 350/1206, 293/1149, 236/1092. Length is a constant 857 px,
  so both ends and the centre move exactly 57.0 px/frame. Backward difference at frame 24: 57 px, which is 1368 px/s.
- Scale from the prior (car length 5.67 m): the car's bbox length is 131 px at frame 24 and 128-132 px across
  frames 20-34 (perspective makes it longer near the image edges). I used L = 130 px, giving 0.04362 m/px.
- Speed = 1368 × 5.67 / 130 = **59.7 m/s**. Using L = 128-132 px gives 58.8-60.6 m/s (±1.5 %).
- Check: the plane's length is 857 × 0.04362 = 37.4 m. That matches a real A320 (37.6 m), so a single shared scale is
  plausible (the plane and car appear to be at the same scale). The record in scene/ agrees: nose step 57.0 px and
  car length 128-137 px.

Confidence: high (about ±3 %).
