# q_577 — height of the table lamp (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Measurements (measure.py, shade.py, legs.py)
- Cat pixel speed: a linear fit of the nose (bbox_x1) over the visible frames gives 17.76 px/frame (rms 0.7 px). The centroid gives 17.81 and the mean per-frame step is 17.78. That is 426.3 px/s, so the scale at the cat's lane is 0.94/426.3 = 0.002205 m/px.
- Lamp pixel height (frame 48, column profiles): the finial/shade top is at y≈499-503 and the base's contact with the table top is at y≈789-790. Height = 290 px (the scene record says 289).
- Plain 2D scale: 290 × 0.002205 = 0.640 m.

## Depth correction
The lamp stands on the table, which is behind the cat's lane:
- The cat's paws touch the floor at y≈1020.
- The table's front legs reach y≈993 and its back leg y≈965, so the floor point under the table centre is at y≈979.

Horizon row:
- The lamp shade's bottom rim (r = 108 px) is almost edge-on. Its centre sits only ~3 px lower than its ends, so the camera is about level with y≈605, looking slightly down (~1.6°).
- With any plausible focal length (1500-2700 px), the horizon falls at y≈530-560.

Depth ratio, cat lane to table: (1020-545)/(979-545) = 1.094. It stays between 1.09 and 1.10 for horizons from 520 to 570. So the lamp height is 0.640 × 1.094 = 0.70 m.

## Checks / confidence
- The cat-speed routes (nose fit, centroid fit, mean step) agree within 0.3%. The lamp height from the scene record (289 px) and from my profiles (290 px) agree.
- The main uncertainty is whether to apply the depth correction (+9%). I applied it because the table is clearly behind the cat's lane.
- Answer: 0.70 m. Likely range 0.64-0.71 m.
