# Q152 — height of the plane (m); prior: car length = 5.67 m

2D render, 24 fps (question_fps equals file fps), static camera. One metres-per-pixel scale comes from the car.

Measurement (`measure.py`): I took the median background, made a |diff| > 12 mask, applied a 3x3 opening, and split objects at row 590.
- Car (Cybertruck) bbox length: 128 px at the image centre (frame 35, centre x≈938), and 129–134 px off-centre,
  where the end faces show in perspective. I used 128 px, the cleanest side-on value, so the scale is 5.67/128 = 0.04430 m/px.
- Plane bbox height (fin top to engine bottom): 255–256 px in every fully visible frame (12–35), so I used 255.5 px.
- Height = 255.5 × 0.04430 = 11.32 m.

Check: the same scale makes the plane 857 px × 0.0443 = 38.0 m long. That matches an A320-family airliner
(about 37.6 m long, about 11.8 m tall), so the scale is consistent. Using the car's off-centre length of 130 px instead
would give 11.14 m, about 1.6% lower.

Confidence: high (about ±3%).
