# q1645 — maximum height of the cart above the ground (m)

The file runs at 22 fps and the question at 24 fps. Times are taken at 24 fps; for example, t = 1 s is frame 24. The cart does not move, so its maximum height is just the vertical extent of its bounding box.

## Scale (focal length from the bird prior)
- Prior: the bird is 1.19 m long (beak to tail, along its flight direction). It flies almost parallel to the image plane: the depth drop between t = 0 and t = 1 s is only about 4° of its path.
- Depth Z of the bird from depth_info, after the off-axis correction: 34.18 m at f0 and 33.94 m at f24.
- Bird pixel length from bbox_w on frames where the wings are edge-on (scene/tracks/bird.csv, checked on crops w1, w19, w36, w44):
  - f1: 139 px, giving f ≈ 3991 px
  - f9: 145 px, giving f ≈ 4150 px
  - f18–19: 142.5 px, giving f ≈ 4071 px
  - f27: 146 px, giving f ≈ 4159 px
- Focal length used: **f ≈ 4090 px**, which is a horizontal field of view of about 26°.

## Cart pixel height (cartmask.py, frame 0, white background)
- The non-white mask's bbox is y 1013 to 1268 at thresholds of 30, 60 and 100.
- Top: tips of the rear posts at y 1013–1014 (x ≈ 1760 and 1860). Bottom: the near wheel's ground contact at y 1267–1268.
- That gives Δv ≈ 254.5 px. The near wheel's vertical diameter is 205 px, so the cart is 1.24 wheel diameters tall.

## Depth at the cart
- Cart origin distance is 30.374 m, which gives Z ≈ 29.95 m after the off-axis correction.
- The near wheel and near side board are about 0.4 m closer than the bbox centre. This estimate uses the axle's angle of about 20° to the line of sight (from the wheel ellipse, 192/205) and a track width of about 1.6 m (from the far wheel's image offset). The near side is therefore at Z ≈ 29.6 m.
- The camera is nearly level, and the top and ground points are at almost the same depth. Pitch therefore hardly changes the result: modelling a 3.7° downward pitch changed it by less than 1%.

## Result
- Height = 254.5 × 29.6 / 4090 = **1.84 m**.
- The plausible range is 1.80–1.87 m. The two sources of spread are the bird's pixel length (about ±3%) and whether the cart's depth is taken at its centre (1.86 m) or at the near side (1.84 m).
- Second check: the ground-to-top estimate made under a level-camera model, using the ground point under the rear corner at its own depth, gives 1.81 m (with f = 4120). The direct Δv·Z/f estimate gives 1.82–1.86 m.
- Confidence: moderate, about ±5%. The main assumption is that "bird length" means the beak-to-tail body length rather than the wingspan.
