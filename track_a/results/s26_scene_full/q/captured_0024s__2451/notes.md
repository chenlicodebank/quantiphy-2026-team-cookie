# Q2451 - length of the table (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px, c = (640, 360).
Camera is static. The table is a square wooden top on a single post, seen corner-on.

## Measurements (frame 48; scripts measure.py, check.py, plane.py)
- Table mask (non-blue pixels): left top corner (413, 471); right corner tip (1133-1137, 503-504).
- Edge lines from the silhouette (rms 0.6-1.3 px): back-left, back-right, front-left (bottom), front-right (bottom).
  Vanishing points (1968, 342) and (157, 345). The f implied by orthogonal VPs is 801 px (close to 763). With
  f = 763 the two edge directions are 87.5 deg apart, so the top is close to a rectangle. The plane normal comes from these VPs.
- Naive route: back-project L (depth 1.035) and R (depth 0.573) and take |L-R| = 0.787 m. But that pair is NOT
  consistent with a horizontal table plane. On the plane through R, L would be at 0.63 m, not 1.035. On the plane
  through L, R would be at 0.94 m, not 0.573.
- Cross-check against the other given depths, using the table plane:
  - Anchored on L = 1.035: the ramp's near (bottom) edge comes out at 0.933 m (given 0.990), and the book at
    frame 29 (t = 1.2, at the ramp foot) at 0.998 m (given 0.977). These are consistent.
  - Anchored on R = 0.573: they come out at 0.57 and 0.61 m. This is inconsistent, so the right-corner depth is the
    outlier, probably a depth reading at the dark, blurred segmentation edge of the far-right tip.
- Rectangle reconstruction anchored on L = 1.035 (corners from the plane plus the edge directions): the sides are
  |LF| = 0.574, |FR| = 0.564, |LB| = 0.564, |BR| = 0.574 m, so the table is square, about 0.569 m.
  The predicted front corner lands at pixel (662, 594), against the observed top front corner at about (643, 586). This is OK.
- Scale check against the ramp and book depths: the ratios are 1.061 and 0.979, plus 1.0 for L, with a mean of 1.013.
  That gives 0.569 x 1.013 = 0.577 m.

## Answer
Length (side of the square top) is about 57.5 cm.
Alternative reading: the 3D distance between the "left" and "right" points from the given depths is 78.7 cm. That
is about the diagonal, and it relies on the inconsistent right-corner depth. I did not use it.
Confidence: moderate. The plane geometry is solid, and the absolute scale rests on L and the ramp/book depths, which agree within about 4%.
