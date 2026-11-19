# q2142 – length of the slope (cm)

Captured lab video, 24 fps (file fps = question fps), f = 0.5959*1280 = 763 px, principal point (640,360).

## Method
- Slope = white board leaning on the table; its raised top (far) edge and its bottom (near) edge on the table.
- Edge rows measured in code (`edges.py`, intensity gradient down columns x = 600..680, frame 48, ball gone):
  top edge y = 353.5 (sky -> board step), bottom edge y = 494.5-495 (board -> dark contact shadow).
- Which depth belongs to which end: edge widths 153 px (top) vs 198 px (bottom), ratio 0.773; given depths
  0.884/1.136 = 0.778 -> top edge = "far end" 1.136 m, bottom edge = "near" 0.884 m. Board width from both:
  153*1.136/763 = 22.8 cm, 198*0.884/763 = 22.9 cm (consistent).
- Back-projection at the edge midpoints (u = 640):
  P_far = (0, -0.0097, 1.1360) m, P_near = (0, 0.1540, 0.8705) m -> |P_far - P_near| = 0.312 m = **31.2 cm**.
  (Using u = 644/638 instead changes it by <0.1 cm; a ±1 px edge row changes it by ~±0.15 cm.)

## Checks
- Slope inclination ~31.7 deg. Ball at t=0 (u,v = 664,333, d = 1.1075) sits ~4 cm along the slope normal
  above the top-edge point (ball radius ~3.25 cm) – consistent within depth error.
- Timing: prior a = 3.0 m/s^2 from rest; 0.5*3*t^2 = 0.30 m (centre travel, slope minus ~1 ball radius)
  gives t ≈ 0.45 s ≈ 11 frames; record shows motion start at frame 28 and bottom at 38-39 -> consistent.
- (scene/ static extents were 353/496 for top/bottom, agree with my measurement.)

Confidence: good (±1 cm), dominated by which exact points the given depths refer to.
