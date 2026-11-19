# q_491: diameter of the Callisto model (m)

2D render, 30 fps (the file rate and question_fps agree). It shows a static planet (Jupiter) and a single small grey moon orbiting it. That moon is Callisto, "the outermost", and it is both the prior's object and the asked object.

## Scale from the prior (speed 0.627 m/s)
- measure.py re-tracks the moon with an intensity-weighted centroid. The mean per-frame step is 2.035 px/frame. A second route, arc speed = fitted angular rate 0.004927 rad/frame × radius 412.74 px, gives 2.034 px/frame. The motion is uniform circular, so the speed is 61.0 px/s.
- Scale = 0.627 / 61.0 = 0.010277 m/px.

## Moon pixel diameter
The edge is soft: limb shading plus about 1 px of blur. Results by method:
- Equal-area diameter at half the plateau (extent.py): 10.95 px. The flux / plateau method gives 10.99 px.
- Bounding box at the half-plateau level: 11.8 px wide × 10.7 px high.
- Equal-area diameter at 0.3 of the plateau: 11.96 px. The record's threshold (12 grey levels above the background) gives 12.6 px, which includes the blur halo.
- Fit of a shaded, blurred disk model (fitdisk.py, 12 frames): 11.80 ± 0.65 px. Flat-disk fits give about 11.1-11.4 px and shaded fits 11.8-12.8 px.

On a shaded sphere the true limb lies further out than the half-max contour, so I take 11.7 ± 0.6 px.

## Answer
11.7 px × 0.010277 m/px = **0.120 m** (range 0.113-0.129 m across the methods).
Confidence: moderate. The scale is solid (to within 0.5%), but the moon is only about 12 px across, so its size is uncertain by about ±5%.
