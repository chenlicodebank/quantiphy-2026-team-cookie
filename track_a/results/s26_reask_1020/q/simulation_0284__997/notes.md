# Q997: length of the plane (m)

2D top-down render. The camera is static and the aircraft flies straight to the left (nose pointing left) at a
constant speed. Prior: plane speed = 22.16 m/s. The question's rate is question_fps = 25. The file's rate is
24 fps, but every time conversion uses 25, as the rules require.

## Speed (pixels)
- Scene record, template-matching track over frames 2–60: dx = −34.1 … −34.6 px/frame, mean ≈ 34.25 px/frame.
  The one outlier (−35.2) was ignored.
- My own check (measure.py) correlates the column gradient profiles of frames 10 and 40. The best shift is
  1029 px over 30 frames, which is 34.3 px/frame. This agrees with the record.
- Speed = 34.25 px/frame × 25 fps = 856.3 px/s.

## Scale
22.16 / 856.3 = 0.02588 m/px.

## Length (pixels)
- Length runs along the body and the direction of travel (x). It goes from the forward tips of the under-wing
  pods (the front-most point) to the fuselage tail tip.
- Scene record: 566 px, from a shadow-free median stack.
- My check: frame 24 differenced against frame 60. The pod tips are at x ≈ 1134–1136. The tail tip is at
  x ≈ 1700–1701, where the difference along the y = 729 row drops at the tail edge (the shadow continues past
  it). That gives ≈ 566 px, which confirms the record.

## Answer
566 × 0.02588 = **14.65 m**.

## Plausibility and confidence
- 14.65 m is a realistic fighter-jet length.
- The wingspan would be 725 px × 0.02588 = 18.8 m.
- Using the file's 24 fps instead would give 15.26 m. Not used.
- Confidence: high, about ±2 %.
