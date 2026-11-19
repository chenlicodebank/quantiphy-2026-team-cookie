# q_1936 — TV height (m)

Prior: black cat speed = 0.94 m/s. The scene is 2D (side-on view, static camera), 24 fps. The file rate and the question rate are both 24, so no re-timing.

## Measurements (measure.py)
- Cat speed in pixels: a linear fit of x against frame over all 50 frames gives 17.65 px/frame for the mask centroid cx and 17.80 for the dark-fur centroid. The mean 2D step is 17.86. The walk is steady. I used 17.72 px/frame = 425.3 px/s.
- Scale = 0.94 / 425.3 = 0.002210 m/px.
- TV height in pixels, measured on the per-pixel-max image so the cat drops out: the dark screen spans y 530 to 756/757 (227–228 px). The record's bbox gives 230 px (529–758), which includes the edge pixels. I used 229 ± 2 px.
- TV height = 229 × 0.002210 = **0.506 m**. The range from the extreme choices of pixel height is 0.502–0.508 m.

## Check
Different cat reference points (cx, dark_cx, bbox_x0, torso_cx) give speeds within ±0.8 % of each other. A TV height of 0.51 m and a width of about 0.88 m (397 px) fit a 40-inch-class TV, so the scale is plausible.

## Caveat
The furniture stands slightly behind the cat's walking line: its feet are at y ≈ 990, the cat's paws at about 1021. A perspective correction would make the TV a few percent larger. Following the convention for 2D scenes, I used one scale with no correction. Confidence: moderate to high (about ±5 %).
