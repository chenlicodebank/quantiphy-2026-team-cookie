# q1533 – width of the 'B1' lettering on the back wall (simulation_0150)

Prior: tyre diameter = 0.764 m. depth_info at t = 0.5 s (frame 12, 24 fps; file and question rates agree):
left-front tyre 11.38 m, B1 sign 23.44 m (Euclidean distance from the camera centre).
Camera is static and level, principal point taken as (960, 540) (the vanishing point of the aisle).

## Measurements (scripts in this folder)
- **B1 lettering** (`answer.py`, frame 41 with the car gone, cross-checked on frame 12): mask of yellow pixels (r−b);
  column profile edges at the half level → x 879.8 … 1061.2 → **width 181.4 px** (rows 430–597, height 168 px).
  scene.json gives 183 px by eye, so the two agree.
- **Tyre diameter in pixels** (`tirewidth.py`, `rays*.py`, overlays `frames/z_front26.png`, `z_rear26.png`): the dark
  region around the rim also includes the shadowed yellow body and the wheel-well shadow, which inflates
  the radius to about 100 px. Rubber is neutral grey (r−b < 20), shadowed body is not. Measured that way, the
  horizontal extent through the rim centre on the outer, silhouette side is R ≈ 87–90 px for both wheels in all
  side-on frames 16–27. The full horizontal width is 175–180 px (180 px near the image centre at f20–21, where the
  tread and perspective effects are smallest). The bottom contact is at y ≈ 882 and the rim centre at y ≈ 791, so R ≈ 91 px including
  the contact shadow. **Adopted D = 178 ± 3 px.** In frame 12 the wheel centre is at (1656.7, 791.4): the same
  image height as the side-on frames (791.2), so the car is at the same depth Z and the side-on size applies.
- Rim (white) diameter is about 123 px. scene/notes.md gave the tyre as about 175 px (approximate), which is consistent.

## Geometry
Iterate f = D_px · Z_tyre / 0.764 with Z_tyre = 11.38 / sqrt(1 + r²/f²) (r = offset of the wheel from the
principal point). This gives f = 2546 px (HFOV 41°) and Z_tyre = 10.93 m. The B1 sign is almost on the axis: Z_B1 = 23.44 m.
B1 width = 181.4 · 23.44 / 2546 = **1.670 m**.
Sensitivity to the tyre diameter: D = 175 → 1.701 m, D = 180 → 1.650 m.

## Check
With this f, the car comes out at length 4.95 m, height 1.52 m and wheelbase 3.05 m. That is about 1.2× a real
RX-7 (4.3 / 1.23 / 2.43 m), the same factor as the prior tyre against a real RX-7 tyre (0.764 / 0.63 ≈ 1.21), so the
scale is internally consistent.
The answer is inversely proportional to the tyre's pixel diameter. That diameter is the main uncertainty (about ±2 %).

Confidence: moderate to high (estimated error about 3 %).
