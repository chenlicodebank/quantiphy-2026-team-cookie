# q488: Ganymede orbital diameter (m)
2D scene (pole-on Jupiter, moons in plane facing camera), fps 30 = question_fps. Scale from prior: Callisto speed 0.627 m/s.
- Callisto pixel speed (uniform circular motion): R*omega = 60.97 px/s (scene tracks), 60.91 px/s (own re-detection from video:
  green excess over median bg, half-max centroid); mean per-frame speed 61.1 px/s (noisy). Use ~60.95 px/s -> 0.01029 m/px.
- Ganymede orbit radius of the moon origin: 267.35 px (common centre fit, scene) / 268.0-268.1 px (free circle fit, both routes).
  Drawn red line is 269.8 px but moon centres run inside it; used moon track.
- Diameter = 2 x ~267.7 px x 0.01029 = 5.51 m (routes: 5.513, 5.520; common-centre radius gives 5.50).
Confidence: high (~1%).
