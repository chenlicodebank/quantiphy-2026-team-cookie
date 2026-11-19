# q_267: length of the green toothbrush lying on the sink (m)

The camera is a static top-down view, and the scene is treated as 2D (one metres-per-pixel scale on the counter plane). The file is 24 fps, the same as question_fps.

## Scale from the prior: speed of the cup = 0.338 m/s
- The "cup" in the prior is the teal object that moves (scene/ calls it teal_box). It is the only object that moves.
- From scene/tracks/teal_box.csv (`speed.py`), it moves at 14.54 px/frame over frames 2–71. The mean of the per-frame steps is 14.540, and a linear fit gives 14.538. That is 348.9 px/s.
- Scale = 0.338 / 348.9 = 9.687e-4 m/px.
- No perspective is visible: the box's extents stay at 44 × 78 px from x = 412 to x = 1430, and no side faces appear. One scale is therefore used.

## Toothbrush (frame 0, static)
- `measure.py`: a yellow-green hue mask of the handle. The handle runs at an angle of 44.5° and is 87.7 px long, from (772, 424) to (834.6, 485.4).
- `profile.py`: an intensity profile along the same axis. The white head starts at s ≈ −69 px, around (754, 407), and the handle tip ends at s ≈ +43.5 px.
- Total length ≈ 112.5 px. This agrees with the scene record (about 116 px end to end, handle 89 px).
- Length = 112.5 × 9.687e-4 = **0.109 m**. The handle alone would be 0.085 m.

## Checks and caveats
- Other objects give plausible real sizes at this scale: the basin is 0.47 m wide, the drain 3.4 cm across, the drawer pull 0.32 m, and the cup's top face 4.3 × 7.6 cm. So the scale is consistent, although a toothbrush of 11 cm is short (full-size ones are about 17–19 cm).
- Ambiguity: the toothbrush lies at about 45°. A world axis-aligned bounding box would give about 0.08 m per horizontal axis. I answer with its length along the body.
- Confidence: moderate-high on the measurement (±3 px, so about ±3 pct). The bounding-box reading is the main risk.
