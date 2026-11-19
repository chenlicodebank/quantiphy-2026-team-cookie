# q_1983: height of the rabbit (m)

The prior is the deer's speed, 1.277 m/s. The "deer" is the large ibex-like quadruped. The video is 2D, both animals stand on the same ground line (y ≈ 1551), and fps = question_fps = 30.

## Scale (measure.py, own segmentation: min(RGB)<247, opening, connected components)
- The ibex's centroid moves 6.535 px/frame net over frames 0-74. The mean of the per-frame centroid steps is 6.63 px/frame, which gait noise inflates. The torso-edge trunk_cx gives 6.45 px/frame.
- The root moves at a steady speed, so I used the net value: 196 px/s, which gives **0.00651 m/px**. The range across the three speed estimates is 0.00642-0.00660.

## Rabbit height (vertical bbox extent, frames 0-68, unclipped)
- Upright pose with ears up (frames 0, 38, 53): 72-73 px, which gives 0.47 m.
- Crouched or stretched mid-hop: 52 px, which gives 0.34 m. The median over the clip is 63 px, which gives 0.41 m.
- The reference size is probably the rest/upright pose, about 72 px → 0.47 m. Allowing some weight for a pose-averaged reading (0.41), I answer **0.46 m**.

## Check
- Scale route 2: using trunk_cx speed instead gives 72 px × 0.00660 = 0.475 m. Both routes agree to within about 2%.
- Sanity check: the rabbit stands about 17% of the ibex's height (421 px → 2.7 m in scene units). Rendered scenes are not at real scale, so this is only a rough check.

Confidence: moderate. The scale is solid; the main uncertainty is which pose the reference height uses.
