# q_457 — height of the box (m)

2D side view, 120 fps (file and question rates agree). Prior: box speed = 0.094 m/s (the box rises at constant speed).

## Measurements (measure.py)
- Box vertical shift found by matching the grey-level profile of the box interior against frame 0, every 20 frames:
  -3.2 px per 20 frames throughout (linear), -63.9 px by frame 400 -> 0.1598 px/frame = 19.17 px/s.
  This agrees with scene/ (19.2 px/s).
- Scale = 0.094 / 19.17 = 0.004903 m/px.
- Box body height from a brown-colour mask (x 570–890, which leaves out the flap): 186–190 px in frames 0–320, ~187.5 px
  on average (scene/ record: 187 px). After frame 340 the bottom is hidden behind the roof edge, so those frames are not used.
- An open top flap at the right sticks up about 17–20 px above the body top (flap top y≈143 vs body top y≈164 at
  frame 120). Body plus flap ≈ 205 px.

## Answer
- Body only: 187.5 px × 0.004903 = 0.919 m
- Including the flap (full AABB): ~205 px × 0.004903 ≈ 1.00 m
- Whether the reference AABB includes the flap is unclear. I answered 0.965 m, the midpoint, which is within about 5% of both readings.
- Second check: the scene/ record's independent template tracking gives the same speed and height, within 0.5%.
- Confidence: the scale is good (to about 1%). The flap reading is the main uncertainty (about ±5%).
