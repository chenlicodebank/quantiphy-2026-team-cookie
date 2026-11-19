# q_533 – height of the typewriter (m)

The file and the question both run at 24 fps.

## Scale from the prior (gravity)
- `measure.py`: a quadratic fit to the magnifying glass's bbox-centre y over frames 0-10 (free fall, before the impact at frame 11)
  gives a = 7444 px/s² (7421 px/s² when fitting from frame 2). Using a = 7430 px/s² gives k = 758 px/m, i.e. 1.319 mm/px, in the
  glass's fall plane. Checks: the glass is 162 px long, so 0.21 m (realistic). Using perspective, the twin-bell alarm clock comes out about 0.20 m tall.

## Perspective (the desk is seen from slightly above)
- The desk's side edges (left from (300,945) to (65,1050); right from (1745,945) to (2010,1070)) meet at the
  depth vanishing point, which puts the horizon at y≈614.
- The camera height above the desk is h = (y_contact − y_h)/k, using the glass's landing footprint y≈1010, so h ≈ 0.52 m. This does not depend on f.
- f ≈ 1560 px comes from ellipse ratios (ashtray ≈0.24, lens ring ≈0.25-0.3; tanα = (y−y_h)/f). It is consistent with a desk depth of 0.62 m.
- Typewriter at frame 29, from column profiles: top of the carriage at y≈858 and front-bottom of the base at y≈1038
  (180 px). The paper sheet, which reaches y≈780, is treated as a separate prop and left out.
- The formula is H = h·(1 − (y_top−y_h)/(y_bot−y_h)) − (y_top−y_h)·D/f, where D ≈ 0.25 m is how far the carriage top sits behind
  the front edge of the base.
  This gives 0.222 − 0.039 = **0.183 m**. With the horizon at 594 instead it gives 0.180. With D in 0.18-0.32 and f in 1300-1800 it ranges from 0.17 to 0.20.

## Second route / bounds
- A naive planar reading (180 px × 1.319 mm) gives 0.237 m. That is an upper bound, because it ignores both the carriage sitting behind the front edge and the
  typewriter being nearer the camera than the fall plane.
- If the paper sheet were counted as part of the typewriter, the height would be about 0.30 m (not used).

Answer: 0.18 m. Confidence: moderate (about ±12%).
