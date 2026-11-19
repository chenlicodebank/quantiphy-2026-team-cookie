# q 2242 — width of the slope (cm)

The slope is the white board lying tilted on the table, which the ball rolls down. File fps = question fps = 24.

Method (lab method card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- I segmented the board in code (`measure.py`: HSV V>200 and S<40 inside an ROI, largest blob, approxPolyDP). Frames 0, 40 and 45 match
  to 1 px. Corners: TL (501,312), TR (592,303), BR (609,408), BL (509,422). The mask's row widths run from 96 px (top) to 103 px (bottom).
- `geom.py`: the top (far) corners are back-projected with depth_info slope_far = 1.854 m and the bottom (near) corners with
  slope_near = 1.701 m.
  - Top edge = 22.1 cm, bottom edge = 22.4 cm (the edges across the slope, perpendicular to the ball's path).
  - Sides along the slope = 29.4 / 29.1 cm.
- Width = the shorter horizontal extent across the board, i.e. the edge across the slope ≈ **22.2 cm**. The length along the slope is
  ≈ 29.3 cm, the other reading of the name.

Second-route check: the two edges, measured independently at two different depths, agree (22.1 vs 22.4 cm). Using the mean depth
for both instead gives 21.6 / 23.8 cm, averaging 22.7 cm. Sanity check: ball diameter 26 px at 1.818 m = 6.2 cm, which is plausible.
The acceleration prior is not needed for a size.
Confidence: good, about ±3 %. The main uncertainty is the rounded corners and which points the depths refer to.
