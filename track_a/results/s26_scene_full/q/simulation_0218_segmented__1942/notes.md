# q_1942 – outer diameter of the robot's tires (m)

Prior: speed of the big robot = 5.924 m/s. No depth_info. fps = question_fps = 24, no retiming.
2D treatment: one metres-per-pixel scale from the prior's pixel speed.

## Scale
- scene/ record: chassis tread band template-matched, ref_x = -188.87 + 50.789·frame px (residual ≤0.4 px),
  i.e. 50.79 px/frame = 1218.9 px/s, constant, horizontal.
- Independent check (fit.py): fitted road-wheel centre moved 422.7 → 1233.8 px from f12 to f28 = 50.69 px/frame (0.2 % off).
- Scale = 5.924 / 1218.9 = 0.004860 m/px.

## Tire diameter in pixels
- "Tires" = the 3 large spoked road wheels with grey rubber rims (enh.py contrast crop, frames/enh.png); the
  4th position (k=3 in fit.py) and the rear are spiked sprockets and were ignored (low ring score).
- fit.py: per wheel, grid search over centre and radius maximising the mean inside-minus-outside brightness across
  a circle (strut at the top excluded); frames 12, 16, 20, 24, 28 × 3 road wheels = 15 fits:
  radius 33.25–33.5 px in all, diameter 67.0 px (median; 66.5–67.0 range).
- Visual read on the 8x enhanced crop of f20: horizontal 794–862.5, vertical 812–879.5 → 67.5–68.5 px, which agrees.

## Answer
67.0 px × 0.004860 m/px = 0.326 m.

Second route: the visual edge read (≈68 px) gives 0.330 m, about 1 % off. The wheel's pixel size stays the same
from f12 to f28, so perspective has little effect along the path.
Main uncertainty: the near-side wheels sit a little closer to the camera than the robot origin, and the speed scale
belongs to the origin. With no depth data this cannot be corrected and is likely a few %. Confidence: moderate-high.
