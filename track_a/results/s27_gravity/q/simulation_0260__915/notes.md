# q_915: height of the mug (m)

The prior is free-fall acceleration of 9.8 m/s² before 0.5 s. The mug falls straight down at constant depth (x stays at 1241 px and the body width stays at 48 px), so one metres-per-pixel scale comes from its pixel acceleration. The file and question rates are both 30 fps.

## Scale (fit.py)
- I fitted parabolas to the scene track for frames 5-15 (free fall, before impact at frame 16), over several windows and reference points:
  - mid-silhouette ref_y: 6110-6270 px/s²
  - mask centroid: 6140-6180 px/s² (rms 0.2 px)
  - bottom edge: 6180-6250 px/s²
- Adopted value: a = 6150 px/s². Scale = 9.8/6150 = 1.593 mm/px.

## Height in pixels (hfit.py, edges.py, crops)
- The silhouette height at rest (frames 20-39) is 56 px, from rim y = 814 to base y = 869.
- The camera sits above the table: the table top is visible and the mug's bottom edge curves down by about 2-3 px at the centre. So the rest silhouette includes the projected ellipse (D·sinθ), on top of H·cosθ.
- The in-flight apparent height falls from 71 to a minimum of 53-54 px at frames 14-15, which is where the mug crosses the camera's eye level.
- Fitting the cylinder model h = H·cosθ + D·|sinθ| with θ = atan((y − y_h)/f) and D = 48 px gives:
  - H = 50.9 px, f ≈ 1246 px, eye level y_h ≈ 697.
  - Rest viewing angle about 6.6°, which matches the 2-3 px bottom bulge.
- Correcting the near-horizon frames (14: 54 px, 15: 53 px) for their small angles gives H ≈ 51.3-51.7 px.
- Adopted value: H ≈ 51.5 px.

## Answer
H = 51.5 px × 1.593 mm/px = **0.082 m**.

## Range
- Using the raw rest silhouette (56 px) would give 0.089 m.
- Using the minimum in-flight silhouette (53 px) would give 0.0845 m.
- I chose the perspective-corrected value. A mug about 8 cm tall is plausible.

Confidence: moderate. The scale is good to about 2%; the true pixel height is uncertain by about ±2 px (4%).
