# q 2462 — width of the table (cm)

File fps = question_fps = 24; table is static (frame 48 used). f = 0.5959*1280 = 762.8 px, c = (640,360).

## Corners (code: mask.py, edges.py, geom2.py)
Table-top outline from a non-black mask + the top/front-face gradient edge, with lines fitted:
- left corner L = (413.6, 467.1), front corner F = (642.2, 575.1),
  right corner R ~ (1143, 490) (faded by segmentation), back corner B ~ (780, 440) (hidden by ramp/books).

## Which points the depth_info names
- distance_table_left = 1.035 -> L. distance_table_right = 0.573 m cannot be the far right corner R
  (a plane through L, R@0.573 and the ramp foot passes through the camera — impossible). Ground-plane
  geometry puts F at ~0.52–0.57 m and R at ~1.0–1.3 m, so "table_right" = the near/front corner F.
  The two depth points are therefore the two ends of the short front-left edge L–F = the table width.

## Measurement
Back-projection with the given depths: |P(L,1.035) - P(F,0.573)| = 0.5224 m -> **52.2 cm**.
Click position on the edge thickness (top surface vs mid-face) changes this by < 0.2 cm.

## Checks
- Plane through P(L), P(F) and the ramp foot (660,478) @ distance_slope_near 0.99 m: angle L-F-R = 88.5 deg
  (85.8–89.9 for +-5 px on the ramp foot) -> the depths give a consistent rectangular top; other side
  F–R ~ 0.80–0.85 m (so 52 cm is the short side = width; length ~ 80–85 cm).
- Vanishing-point plane (uses the occluded back edge, weak) gave LF 0.57–0.63 m depending on which depth
  sets the scale; those two depths are mutually inconsistent with that plane (camera height 0.142 vs 0.159),
  so that route is less reliable than the direct back-projection.
Confidence: moderate (±5–8 %).
