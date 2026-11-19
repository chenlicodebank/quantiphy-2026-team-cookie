# q2121 – length of the earphone case (mm); prior: width = 45 mm

Object: white AirPods (1st/2nd gen style) case lying flat, static, right of the pencil, centre ~(2602,975) px,
rotated ~35 deg in the image. Lid seam near the upper-right edge, charging port on the lower-left edge, so the
length runs seam->port (perpendicular to the seam) and the width runs along the seam.

Method (scripts measure.py, edges.py, edges2.py, rot.py): crop 2400-2800 x 780-1180 on frames 0/15/29, mask by low
saturation (case S~6, slightly shaded port side S~10-27, wood S~55-65), rotate so the width axis is horizontal,
read subpixel extents per row/column, and fit min-area rectangles.

Key measurements (px):
- width: 187.3-188 (S<30), 190.3-191 (S<40); min-area rect short side 190.7-193.5
- length: 210-212 (S<30, upper face), 215.5-219 (S<40, includes the visible shaded port side); min-area rect long
  side 214-222; row/col maxima 217-221
- ratio length/width: 1.12 (strict face) .. 1.15 (full visible case, rect and S<40 maxima)
Same values on frames 0, 15 and 29 (static object).

Scale: one factor = 45 mm / width px (single planar scale, as the annotators did). Full visible outline
(~220/191 = 1.15) -> 51.8 mm; strict upper face only (210/187.5 = 1.12) -> 50.4 mm.
Sanity check: the real AirPods case is 53.5 x 44.3 mm (ratio 1.21). The top view shortens the length a little because
the ends are rounded. Answer: 52 mm.

Second route: the min-area rectangle of the mask (222.3 x 193.0 -> 51.8 mm) agrees with the per-line profile maxima
(219/191 -> 51.6 mm).
Confidence: moderate; the answer is within about +-4% for the outline the annotator chooses.
