# q_266: diameter of the blue rolling cup (2D top-down render)

- The object asked about is the moving teal object. scene/ calls it "teal_box", but it is really a cup lying on its side and rolling in +x. From above, a rolling cylinder looks like a rectangle. Its extent along the motion (x) is the diameter, about 44 px. Its extent across the motion (y) is the cup's height, 78 px.
- Scale comes from the prior, speed = 0.338 m/s. I re-measured the pixel speed with `measure.py`: the per-frame step over frames 2-71 is 14.537 ± 0.20 px/frame, and a linear fit gives 14.537 px/frame. At 24 fps that is 348.9 px/s, so the scale is 9.688e-4 m/px. The file fps and the question fps are both 24, so no re-timing was needed.
- Diameter in pixels:
  - Thresholded mask: the median row width is 44 px.
  - Sub-pixel coverage profile (`subpix.py`, frames 0/20/36/50/71): the width runs from about 41 px at the y-top end to about 43.5 px at the other end. The cup is slightly tapered or shaded, and the larger end gives the axis-aligned extent.
  - I used about 43.5 px, which agrees with the mask's 44 px.
- Diameter = 43.5 × 9.688e-4 ≈ 0.042 m. The range is 0.041-0.043 m depending on which end is read.
- Second route: frames 0, 20, 36, 50 and 71 each give the same width within ±1 px, and the mask and sub-pixel routes agree.
- Confidence: medium-high. The scale is solid; the uncertainty is about 3% from the taper and edge reading.
