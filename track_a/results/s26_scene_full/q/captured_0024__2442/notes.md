# q_2442: width of the table (cm). captured_0024, lab, 24 fps (file fps = question fps)

Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Table geometry (frame 48, scripts edges.py / geom.py / geom2.py / width.py)
- I fitted the table-top edges with sub-pixel vertical-gradient tracking and line fits (rms 0.1-0.25 px):
  - back-left edge L-B: y = -0.0739x + 496.9
  - left-front edge L-F: y = 0.4732x + 271.3
  - front-right edge F-R: y = -0.1704x + 684.5
- Corners: L = (412.5, 466.5) and F = (642.1, 575.1). The right end R is blurred or occluded (person's arm). Wood is
  visible up to x≈1097, and the dark edge band runs to x≈1140.
- Vanishing point of L-B ∥ F-R is (1944, 353). With the orthogonality constraint and known f, the table plane is
  level in the camera frame (pitch 0.04°, roll -0.3°). So the camera is level and slightly above the table top.
- Check: the apparent thickness of the edge band, converted with the plane-model depths, is a near-constant
  2.3-2.5 cm (×scale) along both edges (thick.py). So the plane's depth ratios are consistent.

## Scale: which depth_info points are the table points
- Story A: table_right = front corner F (0.573) and table_left = right corner R (1.035), so the given points are the
  two ends of the F-R edge.
  - F = 0.573 sets the plane scale (camera 15.5 cm above the table top).
  - On the F-R line, |R| = 1.035 then falls at x ≈ 1117, inside the visible right-end range (1097-1140).
  - slope_near 0.99 at the ramp foot on the table needs a scale 1.127, within 2% of this one.
  - The book path between t = 1.0 and 1.2 (given depths) is 24.5°, and the ramp from slope near to slope far is
    23.9°, consistent with each other.
  - The book is 3.5 cm above the table at t = 1.2, which is plausible.
- Story B: table_left = left corner L (1.035).
  - This scale is 15% smaller, and the plane then puts F at 0.498, not 0.573.
  - slope_near comes out as 0.88, not 0.99.
  - 0.573 would only fit a random point on the front edge (x≈800).
- Story B is less consistent, so I used Story A. Note that the names left/right are swapped relative to the image
  under Story A.

## Result
- The direct back-projection of F (depth 0.573) and R (depth 1.035) gives a 3D distance of **0.627 m**. This is
  robust to where R sits: it ranges 0.617-0.637 for R anywhere between x 1097 and 1138.
- Second route: the plane model at the F-scale with R on the plane at |R| = 1.035 gives F-R = 0.627 m (the same).
- The other side, L-F, is 0.671 m at this scale. Width is the shorter horizontal side, so width = F-R = 62.7 cm.
- Alternatives:
  - Story B scale: L-F = 58.4 cm.
  - Square-corner R at x = 1138: F-R = 67 cm.
- Confidence: moderate, roughly ±8%.
