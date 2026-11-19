# q1709 – average speed of the eagle (m/s)

File is 25 fps; question_fps = 24, so t=1 s → frame 24 and t=2 s → frame 48 (scene/ frame column used, not its seconds).

## Method (measure.py)
- Eagle = "bird" track in scene/tracks/bird.csv (dark flapping bird, visible f0–f58, clipped at the edge from f54).
- Radial component: given eagle distances 139.757 m (t=1) → 130.247 m (t=2), so it comes 9.51 m closer in 1 s.
- Focal length: taken from the adult human (~140 m away, both distances given). Their bbox height is 73 px median and
  77–78 px at the top of the gait, for a 1.75–1.80 m person → f ≈ 5840–6210 px (hfov ≈ 9°). Principal point taken
  at the image centre (480, 480).
- Back-projected the eagle centroid at f24 and f48 with the given distances: 3D displacement 11.5–11.8 m over 1 s.
  The across-image part is ≈ 6.6–7.0 m and the depth part is 9.51 m.
- Its image velocity speeds up smoothly (10.5 px/frame for f0–24, 12.0 for f24–48), which matches a constant 3D
  velocity seen as it gets closer, so the t=1–2 s value is the clip average.

## Checks
- Prior: the human's image-plane speed is ≈ 0.74 m/s with this f. To reach 1.3 m/s they must also move ≈ 1.07 m/s
  toward or away from the camera. Their given distance barely changes (an animated character's origin can stay put),
  and their pixel height changes by less than 2% over the clip. Feet move down 47 px, which fits walking toward a
  camera that looks down. So the prior is consistent with this f. Using the prior alone as purely sideways motion would
  give f ≈ 3600 px and a 2.8 m tall person, which is impossible, so that reading was rejected.
- Eagle wingspan check: max 76 px at ~134 m → 1.64–1.74 m, a realistic eagle.
- Smoothing the centroid over one flap cycle (±6 frames) instead of raw centroids changes the result by under 1%.
- f uncertainty of ±10% changes the answer by about ±2%, because the given depth change dominates.

Answer: 11.6 m/s. Confidence: fairly high (±5%).
