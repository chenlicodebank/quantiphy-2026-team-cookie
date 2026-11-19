# Q374: pocket diameter (m)

Prior: ball diameter = 0.0757 m. This is a 2D top-down render with one px→m scale (the camera is static and the view orthographic).
fps = question_fps = 30. Time does not matter for this question.

## Scale (ball)
- `ball.py` takes a half-level colour-distance edge on a radial profile for 9 static balls at frame 39.
  The median is 47.6 px; the spread of 44–50 comes from shading and shadow.
- The scene record gives 48 x 48 bounding boxes and a moving-ball ellipse of 48.4 px.
- I take **48 px** as the ball diameter, so the scale is 0.0757/48 = 1.577e-3 m/px.

## Pocket
- The pocket pieces have three grey levels: the hole is about 0, the liner about 14 and the black frame about 35 (`pocket.py` profiles).
- The scene record's "pocket dark region" sizes (130 / 118 px) are the whole black pocket piece, not the hole.
  Its pocket centres are also off; for example the top-middle hole is centred at y = 136.5, not 122.6.
- `hole.py` thresholds the hole at 7, applies a morphological opening, takes the component at the centre, then fits a circle and computes an area-equivalent diameter.
  The overlay is `frames/hole_ov3.png`; the circles fit well.
  - Middle pockets: 77.2–77.5 px from the fit and 78.1–78.3 px from the area (bounding box 77 x 80).
  - Corner pockets: 80–82.8 px from the fit and 80.4–81.6 px from the area. These are slightly inflated where the hole merges with the dark shadow on the inner side.
  - The thresholds 4, 7 and 10 agree to about ±1 px, except where the hole leaked into the liner.
- Chosen hole diameter: **78.5 px**, which gives 78.5 × 0.0757/48 = **0.124 m**.

## Check
- The middle pockets alone give 77.5 px → 0.122 m; all six together give 79.9 px → 0.126 m.
- The ratio pocket/ball is 1.64, which is plausible: real pockets are about 1.8–2 ball diameters.
- Confidence: moderate-high, about ±3 %.
