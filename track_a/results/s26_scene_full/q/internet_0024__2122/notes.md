# q_2122 – length of the pencil (cm); prior: width of the earphone case = 45 mm

Overhead static view of a desk, frame 29 (no cup or hand). Pencil and AirPods case are both static, lying side by side
on the desk. I used the planar single-scale convention for internet videos.

## Earphone case width (prior object)
- The case lies on its back, lid seam toward the upper right, rotated about 35°. Width = its extent along the seam direction.
- measure2.py: convex hull of the low-saturation mask. Narrowest extent is 191.3 px (S<35) / 194.3 px (S<45) at 35-36°. The
  perpendicular (long) extent is 220-226 px, excluding the bottom face seen in perspective.
- measure3.py: half-contrast saturation edge crossings on 15 parallel lines along 34.5/35.5/36.5°. The maximum is 193.1 px
  (lines give 189-193). The long side is about 220 px, and the ratio 1.14 roughly fits the case's 44 x 54 mm face (domed top).
- Value used: **193 px = 45 mm → 0.2332 mm/px**.

## Pencil length
- I refined the pencil axis from saturation cross-section centres (axis 71.2°), then took grey and saturation profiles along it.
  The unsharpened end crosses at s ≈ -9 px (sharp edge). The graphite tip crosses half contrast (graphite 90 / desk 200) at
  s ≈ 751 px; a faint shadow beyond it is excluded.
- Length ≈ **760 px** (±5). The scene record gave 754 px, which agrees within 1 %.

## Result
760 × 45 / 193 = 177 mm = **17.7 cm**.
Spread: 754-765 px against 191-195 px gives 17.4-18.0 cm. A typical sharpened pencil is about 17-19 cm, so the value is plausible.
Check by a second route: the min-area rect width of 194.4 px with the record's 754 px gives 17.5 cm, which agrees within 1.5 %.
Confidence: good (about ±3 %). The case top sits about 2 cm above the desk, so it may look slightly enlarged by perspective; following the convention, this is not corrected.
