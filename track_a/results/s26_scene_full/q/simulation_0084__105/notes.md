# Q105: width of the black and white car (m)

The scene is a top-down 2D render at 24 fps (file fps = question_fps). The black and white car is the dark_car in the lower lane, a Cybertruck-like truck with a white nose. The prior is the yellow car's speed, 5.07 m/s.

## Scale (measure.py, own segmentation)
- Yellow car, measured on every frame:
  - Front bumper, frames 1→71: −688/70 = −9.83 px/frame.
  - Rear bumper, frames 12→71 (once fully in view): −588/59 = −9.97 px/frame.
  - The two differ because the projected length shrinks slightly toward the image centre (perspective).
- The centre (origin) moves at about 9.90 px/frame, which matches the scene record. That is 237.6 px/s.
- Scale = 5.07 / 237.6 = 0.02134 m/px.

## Dark car width: per-column y extents of the mask, frames 24, 36 and 48 (all identical)
| Reading | Rows (y) | Pixels | Metres |
|---|---|---|---|
| Wheel to wheel (tyres, outer edges) | 588–685 | 98 | **2.09** |
| Cabin/body | 594–682 | 89 | 1.90 |
| Including mirrors | 581–695 | 115 | 2.45 |

The answer uses the wheel-to-wheel convention for car width: **2.09 m**.

## Check
- The dark car's length, about 268 px, gives 5.72 m. That is consistent with a Cybertruck: real length 5.68 m, width 2.03 m without mirrors. So the scale is plausible.
- The widths are stable across the three frames to within ±1 px.

## Confidence
- The scale is good to about 1.5%.
- The main uncertainty is the width convention. If the reference used the mirror-inclusive bounding box, it would be 2.45 m.
