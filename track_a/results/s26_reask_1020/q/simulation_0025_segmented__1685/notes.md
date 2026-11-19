# q_1685 — eagle wingspan (m)

File fps 25, question_fps 24 (t = frame/24 used for all times). 960x960, principal point (480,480).

## Scale / focal length
- Human depth is constant (114.83 m at t=1 and t=2) although the body visibly moves: the origin stays put, so the
  prior speed (1.3 m/s) cannot be used as a lateral speed. Lateral pixel speed is only 0.52 px/frame; using it as the
  full speed would give f ≈ 1150 px and a 5.5 m tall person, which is impossible. The person walks mostly toward the camera
  (feet move down 8–10 px, apparent height grows ~2 px).
- So f comes from the person's height (standard object): pixel height ≈ 56–57 px (measure.py, mask threshold 4,
  includes the faint white head; frame 0 = 57 px). Assuming a 1.75 m person at ≈114 m gives **f ≈ 3700 px** (HFOV ≈ 14.8°).
- Check against the prior: at f=3700 the lateral speed is 0.39 m/s, so the radial speed is 1.24 m/s, which means about 3.7 m closer over the
  clip and about +3.3% apparent size (≈ +1.8 px). Measured trend: about +2.4 px. Consistent.

## Eagle
- Bird span (bbox width, threshold 30) per flap cycle at wings-spread frames: 44 px (f14), 46 (f31), 48 (f42),
  49–53 (f56–62). Wings-raised V frames 0, 24, 49.
- 3D path (geom.py): the back-projected positions at t=1 (u=472,v=382, D=116.05) and t=2 (u=744,v=378, D=108.28)
  give the velocity V ≈ (7.9, 0.1, −8.05) m/s at f=3700. The bird flies level, about 45° toward the camera. The V-shaped views
  show the wings spread left/right, so the wing axis is taken horizontal and perpendicular to the heading: (0.71, 0, 0.70).
  This makes the image width a foreshortened projection (factor about 0.7).
- Naive span (no foreshortening) = px·Z/f ≈ 1.40–1.51 m. With the wing orientation it is 1.94 (f14), 2.02 (f31),
  2.11 (f42), 2.17–2.35 (f56–62).
- Cross-check: with no foreshortening, the raised-wing V height (32 px) would exceed the half-span implied by the
  flat width (≈25 px). With foreshortening factor 0.7 it is consistent (half-span ≈34 px, wing elevation ≈70°).
  A real eagle's wingspan is 1.8–2.3 m; the oriented value fits, while 1.45 m would be small.

## Answer
Wingspan ≈ **2.15 m** (mean of the per-cycle maxima with the orientation correction).
Confidence: moderate. f has about ±5% error (assumed human height, faint head). The heading-based foreshortening
assumes the bird faces its direction of travel. If it doesn't, the answer could fall as low as about 1.45 m.
