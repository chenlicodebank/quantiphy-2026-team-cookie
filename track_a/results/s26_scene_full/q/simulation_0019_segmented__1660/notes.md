# q_1660 — width of the pedestal (square base) of the central sculpture

File fps = question_fps = 33. Static camera, 1080x1080, principal point assumed at (540,540).

## Focal length (from depth_info of the man)
- The man walks parallel to the image plane: his pixel height and feet row stay constant (bbox h 257-267, feet y ~785),
  so his camera-axis depth Z is constant. The Euclidean distance changes (6.84 -> 6.49 m) only because he moves toward the optical axis.
- Pelvis pixels (scene/tracks/man.csv, local linear fits): f0 u≈883-885, v≈647; f33 u≈689-692, v≈648.
- Solving D_i = Z*sqrt(1 + r_i^2/f^2) for both times gives f ≈ 907 px (±14 px from depth rounding), Z ≈ 6.36 m (solve.py).
- Check: predicted rest height 1.87*907/6.36 = 267 px vs walking bbox 257-267 px (median 261, ~98%, as expected for walking). OK.

## Pedestal pixel width (measure.py, frame 0, non-white mask)
- Lower dark block (widest part of the two-tier plinth): x 331-632 from y 780 to 890 -> 301 px; edges vertical (no visible pitch).
- Upper light tier is narrower (tapered, ≤ ~295 px), so the pedestal width = lower block width.

## Metric width
- Route 1 (depth to origin): Z_origin = 5.085/sqrt(1+r^2/f^2), front face at Z_origin - W/2, W = 301*(Z_origin - W/2)/f.
  Origin at centre of sculpture+pedestal (u 482, v 643): W = 1.435 m. Origin at plinth centre: 1.395; at bottom centre: 1.367.
- Route 2 (ground plane): camera height from man's feet = 245*6.36/907 = 1.72 m (panel base with its 11.042 m depth gives 1.74 m,
  so pitch ≈ 0). Pedestal bottom front edge at v=895 -> Z_front = 1.72*907/355 = 4.39 m -> W = 301*4.39/907 = 1.456 m.
  This rules out a low origin (bottom-centre origin would put the base at v≈918, not 895) and supports the high/centre origin.
- The two routes agree on 1.435-1.456 m (max allowed by the 5.085 m Euclidean constraint is ~1.444).

Answer: 1.44 m. Confidence: moderate-good (~±3%; dominated by focal-length uncertainty from the 0.01 m depth rounding).
