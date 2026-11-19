# Q59 – width of the purple car (prior: white car length = 6 m)

2D top-down render. Static camera, one metres-per-pixel scale on the ground plane. The "white car" is the white van/minibus.

## Measurements (measure.py: mask = |pixel - road median| > thr, min-area rect)
- White van length (vertical extent), thr 25: 247 px at f0 (lower end has a shadow), 236–237 px at f36 and 242 px at f71.
  Zoomed crop at f36 (frames/van.png): body runs y≈616–852, so 236 px. scene/ record: 236 px. Adopted: 237 ± 3 px.
- Purple parked car width (vertical extent across a car parked horizontally): 73 px at thr 18 and 25 on f0, f36 and f71
  (rect 72 px). Zoomed crop (frames/purple.png): body y≈407–479, so about 72–73 px. thr 12 gives 87 px, but that includes the soft shadow halo.
- Scale = 6 / 237 = 0.02532 m/px.

## Answer
Width = 73 × 0.02532 ≈ 1.85 m. With 72 px it is 1.82 m. If the mirrors are included (~75 px), it is 1.90 m.

## Check
The purple car's length is 195–196 px, so 4.95 m, and its length/width ratio is 2.7. Both are plausible for a sedan next to a 6 m van.
The same masks on three frames give the same 72–73 px, which confirms the width is stable.
Confidence: good (±3%).
