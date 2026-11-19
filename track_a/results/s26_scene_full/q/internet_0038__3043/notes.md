# q3043 – width of the MacBook (cm)

Prior: the Magic Mouse is 5.71 cm wide. This is Apple's spec naming: width = left-right, depth = 11.35 cm.
The view is top-down and the camera is static. The mouse's long axis runs vertically in the image.

Measurements (measure.py, frames 8 and 14, half-max threshold, subpixel edges):
- Mouse width: max per-row white extent = 68.8 px. Mouse length = 134 px; the ratio 1.95 matches the real 11.35/5.71 = 1.99.
- Scale: 5.71 / 68.8 = 0.0830 cm/px.
- Laptop base, left-right extent: 424-426 px over many rows clear of the hands (x 436-861).
- Laptop base, front-to-back extent: about 300 px.

Readings:
- Width as left-right extent (Apple spec naming, the same naming the prior uses): 425 × 0.0830 = **35.3 cm** (ANSWER).
- Width as the shorter front-back depth: 300 × 0.0830 ≈ 24.9 cm.
- The lid edge line (466 px → 38.7 cm) is not used. The lid is closer to the camera and seen edge-on, so it looks larger.

Sanity check: a 15/16" MacBook Pro is 35.6-35.9 × 24.7-24.8 cm, which matches both pixel extents. The pixel aspect ratio 425/300 = 1.42 also matches the real 1.43.
Confidence: good for the left-right reading (about ±2%). The main risk is how "width" is defined.
