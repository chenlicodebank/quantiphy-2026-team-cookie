# Q58 – width of the turning yellow car (m)

Prior: the white car (the white van, which drives straight up) is 6 m long. 2D near-top-down static camera, so one
metres-per-pixel scale on the ground plane.

Scripts: `measure.py` (masks from the difference between f0 and f71 at several thresholds; each object is away from its
own position in the other frame), `profile.py` (edge profiles averaged across the body).

## Measurements (px)
- White van length:
  - f0: white roof 811.5–1046 = 234.5 px. Including the dark front face seen in perspective (it starts at about 800): 246 px.
  - f71: white roof 82–311.5 = 229.5 px. Including the rear face (down to about 318): 236 px.
  - The record (scene/vehicle_sizes.json, body at threshold 25) gives 236 px at f0 and at f71. The masks at threshold 40 give 235 and 241 px.
  - Best estimate: about 236–241 px. I used about 238 px.
- Yellow (tan) car width, across its axis:
  - f0: rows 880–920 span x 951.5 to about 1030.5 (≈79–80 px). Including the mirrors (rows 830–850) it is ≈80 px.
  - f71 (after the turn, horizontal): y 595.5–676.5 ≈ 81 px.
  - The record gives 81.8 and 83 px. The masks at threshold 40 give 80 and 81 px.
  - Best estimate: ≈81 px.
- Shadows inflate the masks at lower thresholds (up to +17 px in width), so I did not use those values.

## Result
- Scale: 6 / 238 = 0.0252 m/px. Width = 81 × 0.0252 ≈ 2.04 m.
- Over the range of readings: 6 × 80/241 = 1.99 m to 6 × 82/234.5 = 2.10 m.
- Answer: **2.05 m**.

## Second-route check
The yellow car's width measured independently on the f0 frame (vertical) and the f71 frame (horizontal) agrees (80 vs
81 px). The van's length agrees across f0 and f71 and across both mask thresholds to within ±3%. The yellow car's
length (219 px ≈ 5.6 m) against its width of 2.05 m gives a plausible car aspect ratio.

Confidence: moderate-high. The main uncertainty (±3%) is whether the van's perspective-visible end faces belong in
its length.
