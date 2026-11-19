# Q763 – height of the green (teal) wall section, prior: ball diameter 0.282 m

## Measurements (measure.py, measure2.py, measure3.py)
- Teal band, from colour/saturation row profiles in 4 column strips that avoid the ball and the reflections:
  top edge at y = 679.5 (grey→teal step between rows 679 and 680) and bottom edge (wall/floor junction) at y = 980.0.
  **Height 300.5 px**, the same in every strip.
- Ball diameter: 75.0 px (circle fit 74.75, area-equivalent 75.7, from scene record; frame 24 mask is 76 px tall).
- Ball at its lowest point (frame 24): centre y = 1004.2, bottom y ≈ 1042. That is 62 px **below** the wall base, so the ball
  is clearly in front of the wall (nearer the camera). One shared scale would therefore be wrong.
- Camera is level: the backboard's left and right edges are perfectly vertical (x 795/1152 in every row).
  The two outer court lines meet at a vanishing point (962, 538.4), so the principal point is at the image centre and the horizon is at y = 538.4.

## Perspective correction (level pinhole camera, camera height h)
- Ball plane: f/d = 75/0.282 = 265.96 px/m. Floor under the ball: f·h/d = (1004.24 − 538.4) + 265.96·0.141 = 503.3 px
  (the bottom edge alone gives 1042 − 538.4 = 503.6, which agrees).
- Wall plane: f·h/D = 980 − 538.4 = 441.6 px, so D/d = 1.140.
- Wall scale = 265.96/1.140 = 233.3 px/m, so the band is 300.5/233.3 = **1.288 m**.
- Second route: the bottom-edge ratio 503.6/441.6 = 1.1404 gives 1.288 m as well. Camera height h = 503.3/265.96 = 1.89 m, which is plausible.
- For reference, a single planar scale (ignoring the depth difference) would give 300.5·0.282/75 = 1.13 m. I rejected it
  because the ball touches the floor well in front of the wall.

## Answer
1.29 m. Confidence: moderate-high. The main uncertainty is whether the reference uses the perspective-correct value (the true world size) or a single scale.
