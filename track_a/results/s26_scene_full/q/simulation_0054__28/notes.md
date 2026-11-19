# Q28: width of the orange car (m)

The video is a 2D top-down render with a static camera, so one metres-per-pixel scale comes from the prior (a = -2.86 m/s²).
question_fps is 30.0 and the file is 30.003 fps. That difference is negligible (0.02 %).

## Scale (accel.py, using rows.npy from measure.py)
- Orange-car mask = background difference > 40, left half of the frame. I took the bbox centre per frame, which stays symmetric under motion blur.
- Quadratic fits of the centre y position against frame:
  - f16–90: -0.1811 px/f²
  - f16–50: -0.1767
  - f50–90: -0.1799
  - f30–90: -0.1815
- Second route, front-edge and rear-edge fits: -0.166 to -0.189 px/f². The speed falls linearly from 16 to 4.4 px/f, so the deceleration is constant.
- Adopted a = 0.180 px/f² = 162 px/s², giving a scale of 2.86/162 = 0.01765 m/px.
- Sanity check: the car length of 293 px comes out at 5.17 m.

## Width in pixels (width.py, width2.py; frames 45–90, slow and sharp)
- Body (wheel arches): x ≈ 292–404, which is 111–113 px → 1.97–2.00 m.
- Including the mirrors: x ≈ 285–407, which is about 123 px (the record's 124 includes mirrors) → 2.17 m.
- The mask's left side also picks up a faint shadow band at 281–291. I excluded it.

## Answer
The task's naming says a car's width is wheel to wheel, so I answer with the body width: 112.5 px × 0.01765 = **1.99 m**. The reading that includes the mirrors would be 2.17 m.

Confidence: moderate. The scale is good to about ±3 %. The main uncertainty is whether the mirrors count, about 9 % between the two readings.
