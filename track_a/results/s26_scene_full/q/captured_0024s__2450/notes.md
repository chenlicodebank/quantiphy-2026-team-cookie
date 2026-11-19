# q 2450 - width of the slope (white ramp board), cm

The file and the question both run at 24 fps. Camera intrinsics: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Width means the board's extent across the slope (its short side, the top and bottom edges). The long side runs down the slope.

## Measurements
- `measure.py`: I masked the white board at frame 48 (bright, low saturation) and fitted lines to the 4 sides of the contour.
  The corners are TL (751.0, 360.0), TR (863.0, 361.6), BL (607.8, 467.5) and BR (706.3, 492.6). An overlay is in
  frames/board_fit.png and fits the board's edge well.
- Naive pixel x depth / f gives 18.3 cm for the top edge (112 px at 1.243 m) and 13.2 cm for the bottom edge (101.7 px at 0.99 m).
  These do not agree, because the width direction recedes strongly in depth. The bottom edge vanishes at about
  (186, 360), the same vanishing point as the table's left-front edge. The top edge lies on the horizon (y ~ cy), so
  it looks horizontal whatever its 3D direction is. The naive values are therefore foreshortened and too small.
- `shape_fit.py`: I fitted a perspective rectangle to the 4 corners, with the scale fixed so the centre depth is 1. The fit is
  unique, with 0.06 px rms. It gives W/Z = 0.217 and L/Z = 0.289 (W/L = 0.75). The width axis comes out horizontal
  (ex_y = 0.009) without being forced, which matches the table vanishing point. The board tilts about 30 deg. Adding 1 px of corner
  noise changes W by 3 % (`sensitivity.py`).
- Unit-scale depths: TL 1.17, TR 1.016, BL 1.036, BR 0.858, top-edge midpoint 1.09, bottom-edge midpoint 0.945.

## Metric scale (s, so that width = 0.217 x s)
- Book depth_info (`book_scale.py`): I intersected the book-centre ray with the board plane at frames 24 (1.0685 m) and 29
  (0.977 m), allowing a half-thickness of 0-1.5 cm. This gives s = 0.98-1.07, so W = 21.2-23.2 cm (full mask
  22.2-23.2 cm at h = 1.5 cm).
- Slope depths: taking far = 1.243 as the farthest corner TL gives s = 1.062 and W = 23.1 cm. Taking near = 0.99 as the
  bottom-edge midpoint gives s = 1.048 and W = 22.8 cm. Taking far as the top-edge midpoint gives 24.8 cm, but then near
  would be 1.08 instead of 0.99, so that reading is inconsistent. A fit forced to both edge midpoints gives
  19-20 cm with 3.3 px rms, a poor fit.
- The acceleration prior (2.8 m/s^2) would need s = 1.46, which contradicts every depth (the book would be at
  1.5 m instead of 1.07 m). The reference acceleration probably carries depth/back-projection noise, so I did not use it
  for scale.

## Answer
The routes cluster at 22-23 cm, so I answer **22.7 cm** (board about 22.7 x 30 cm).
Confidence: moderate. The main uncertainty is which surface points the slope depths refer to (about +-5 %).
