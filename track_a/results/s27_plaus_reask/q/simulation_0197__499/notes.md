# q_499 – vertical height of the "skynova" lettering (simulation_0197)

The scene/ record does not cover this text, so I measured it from scratch with `measure_text.py`. That script averages frames 0, 10, 20, 30 and 40, then masks the white, low-saturation lettering. The camera is static, and the file fps and question fps are both 30.

## Geometry
- The word "SKYNOVA" runs vertically up the left side of the bottle. It is rotated, so it reads bottom-to-top with A at the top. Only "NOVA" is in frame; "SKY" is below the bottom edge of the image.
- Measured glyph extents (px):
  - A: y 2036–2162
  - V: y 2172–2296
  - O: y 2312–2440
  - N: starts at y 2474 and is cut off at 2560
- The horizontal extent of the whole text is x 1106–1186, about 80 px.
- The bottle body spans x ≈ 1012–2150 (R ≈ 569 px). The text sits about 44–56° around the cylinder from the camera, so it is foreshortened horizontally. Its arc (cap height) is about 122 px, consistent with O's 128 px vertical width.

## Full word length (extrapolated)
I estimated the hidden letters from geometric-sans proportions calibrated on the visible O, A and V:
- Ink widths: N ≈ 100, Y ≈ 112, K ≈ 96, S ≈ 87 px.
- Gaps: about 22, 12 and 22 px.
- Result: the word runs from y 2036 to about 2925–2940, so it is about 905 px long (±30 px).

## Scale
- I took the prior (horizontal width = 0.00188 m) as the world horizontal (AABB) extent of the text, which is its projected horizontal extent of 80 px. That gives 2.35e-5 m/px.
- Real-scale check: this scale makes the bottle about 27 mm wide and the threaded neck about 18.6 mm. That matches a standard 18-410 dropper bottle, so the scene is at real scale.
- The alternative reading uses the 122 px cap-height arc for the 1.88 mm. It would make the neck about 12 mm, which is less plausible, and the answer about 0.014 m.
- I applied a small (~1.5%) correction for the camera looking down slightly, which shortens vertical lengths.

## Answer
Height = 1.88 mm × 905 / 80 × 1.015 ≈ 21.5 mm = **0.0215 m**.

Confidence is moderate. The main uncertainties are:
- Which pixel extent the prior's width refers to (projected 80 px vs arc 122 px).
- About ±4% from extrapolating the "SKY" letters that are out of frame.
