# Q2124 – longest side of the laptop (cm); prior: earphone-case width = 45 mm

Static overhead shot (camera static, see scene/). Both objects are static, so I measured on frame 29 (cup gone) and
checked on frame 0. I used one planar scale from the prior, following the internet-video convention.

## Scale reference: AirPods case (white, right of the pencil, centred near (2602, 970) px)
This is an original AirPods case lying on its back, with the Lightning port on its lower-left edge. "Width" is the
shorter face dimension, which runs parallel to the port edge (image direction about 35° below +x). The real case
measures 44.3 x 53.5 mm, which is consistent with 45 mm.
- `measure_case.py` / `measure_case2.py`: low-saturation mask, then minAreaRect or extent along the port-edge
  direction. Width is 191–195 px across thresholds; the perpendicular dimension is 220–225 px. Mask overlays are in
  frames/case_mask*.png.
- `case_profile.py` (second route): half-max saturation edge profiles on 25 parallel lines. Width is 186–189 px on both
  frame 0 and frame 29; length is 207–218 px.
- The record's rough value of 205 px was read by eye and is too large.
- Adopted width: 192 px (range 188–196). Scale = 45 / 192 = 0.234 mm/px.

## Laptop (MacBook Air, upper left)
The longest side is the front edge of the base; the screen is cut off by the top of the frame. In
`measure_laptop.py` / `laptop_lines.py` I fitted lines to the front edge (both sides of the notch agree), the left
side and the right side. Corner to corner at the virtual corners is 1424 px, and the extent of the rounded outline
along the edge is 1420 px (overlay in frames/laptop_lines.png). Adopted length: 1420 px.

## Answer
1420 px x 0.234 mm/px = 333 mm. The range from case-width uncertainty (188–196 px) is 32.6–34.0 cm. As a sanity
check, a real 13" MacBook Air is 32.5 cm wide. Answer: **33.0 cm**.
Confidence: moderate-good (±3 %). The main uncertainty is the case pixel width, because its edges are soft. The case
top is also about 2 cm above the desk, but I applied no perspective correction, per the convention.
