# q_702 – width of pool tiles (horizontal side)

2D top-down render, 24 fps (file fps = question fps). Camera is static.

Script: `measure.py`.
- Prior object: the black cat walking right at constant speed. Centroid linear fit 5.457 px/frame, head-tip fit 5.466,
  mean per-frame step 5.477, net/49 frames 5.453. I used about 5.46 px/frame = 131.0 px/s.
- Scale = 1.041 / 131.0 = 0.00795 m/px.
- Tiles = the paving slabs next to the pool. Vertical grooves from column-profile minima on frame 0, in the slab row
  y 470–600: 430, 575, 719, 864, 1007, 1154, 1298, 1443, 1588, 1733, 1876. Pitch = (1876-430)/10 = 144.6 px. The same
  pitch shows in the coping strip and in the upper rows (144–145 px between grooves).
- Width = 144.6 x 0.00795 = 1.149 m. Using the mean per-frame step (5.477) gives 1.145 m instead.

Second check: grooves from the other rows give the same 144–145 px pitch, and the different speed estimates agree to
within 0.5%.
The slab's vertical side is about 263–266 px (about 2.1 m), but that is not what the question asks.
Answer: 1.15 m. Confidence: high (about 2%).
