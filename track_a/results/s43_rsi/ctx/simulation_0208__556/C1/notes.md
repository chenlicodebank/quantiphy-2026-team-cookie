# Q556: height of the typewriter (m)

Prior: free-fall acceleration before 0.45 s is 9.8 m/s^2. No depth_info. fps = question_fps = 24.

## Scale (fit.py)
I fitted a quadratic to the bbox / mask centre y for frames 0-6, which are above the horizon and lightly blurred:
6926-6981 px/s^2, giving 1.40e-3 m/px. With frames 0-9 the fit gives 7214-7295 px/s^2. Those later frames have
strong blur and the silhouette changes there, so I used the 0-6 value. The bbox top and bottom edges carry blur bias
(6775 vs 7186) but average to the centre value.

## Geometry: the scene is not flat
A perspective camera looks roughly level at the scene. The vanishing point of the mat's sides gives a horizon near
y ≈ 500-550.
- Frame 0, typewriter above the horizon: its dark underside shows as a band at y 292-318 (27 px, prof.py), and the
  band shrinks as it falls (27, 26, 25, 20 px). The silhouette runs from the carriage top (y = 192) to the
  bottom-back edge (y = 317): 125 px.
- At rest, below the horizon: the silhouette runs from the carriage top (848) to the bottom-front edge (1023):
  176 px.
- Neither pixel height is the true height. I built a pinhole model with depth ratios e = base depth / Z_front and
  c = carriage-top depth / Z_front:
  - frame 0: h/s_f = 125 + (v_h - 192)c - 27, where the 27 px band = (v_h - 317)e.
  - rest: h/s_f = 175 - (848 - v_h)c.
  - Solving gives c = 0.117, whatever v_h is, and h/s_f ≈ 137 px (134-140 for v_h = 500-550). e ≈ 0.13, so the
    carriage sits near the back, which is plausible.
- The fall track (silhouette top and bottom) moves with the scale of points about 12 % deeper than the front plane.
  So the front-plane scale is s_f = 1.404e-3 / 1.12 ≈ 1.25e-3 m/px.
- h = 137 × 1.25e-3 ≈ 0.172 m.

## Checks and other readings
- Plain 2D readings with the fall scale: the airborne pixel height gives 125 px × 1.40e-3 = 0.175 m, and the resting
  pixel height gives 176 px × 1.40e-3 = 0.247 m. The resting value includes the foreshortened top deck.
- The perspective model and the airborne reading agree within 2 %.
- The width is 292 px × s_f ≈ 0.37 m, so h/W ≈ 0.47, a plausible typewriter shape.

Confidence: moderate, roughly ±8 %.
