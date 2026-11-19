# q_2928: width of the white box (cm)

- The object is the "white box": the small white/red drink carton lying on the floor at about (516,496) px. In scene/ it is called `milk_carton`. It is static throughout the clip. Its depth at t=1.4 s (frame 34) is 2.082 m.
- The file fps and question_fps are both 24.
- The carton lies flat with its long axis diagonal in the image (about -58 deg). The parts visible are:
  - the top face, white with text;
  - its right side face (grey, about 6 px wide);
  - the red near end.
- Width = the shorter horizontal extent, which is the top face measured across the long axis.

## Measurement (width.py)
- I rotated the crop so the long axis is vertical. On 36 rows I found the half-max edge crossings.
- Top-face width = 22.9 px (IQR 22.5-23.3). The same value comes out in frames 24, 34, 44 and 48.
- Side face ≈ 6 px. The outer extent including the side face is 28.5 px (about 7.8 cm). This is not the width: the side face is a vertical face.

## Results
| Route | Method | Width |
|---|---|---|
| Method card | 2.082 m × 22.9 / 762.75 | **6.25 cm** |
| Perspective-corrected 1 | Back-project both long edges onto the floor plane through the carton centre (plane.py). Floor normal from the board's vanishing points. | 6.45-6.59 cm |
| Perspective-corrected 2 | Same, but with a plane fitted to the 4 depth points | 6.08-6.20 cm |

- The perspective-corrected values vary with the assumed top-face height.
- The given depths do not lie on a single plane very well (about 10 cm residuals; check.py). The two plane estimates bracket the method-card value.

**Answer: 6.3 cm.** Confidence: moderate-high (about ±5%). The main uncertainty is the edge blur (±0.5 px, about 2%) and the foreshortening.
