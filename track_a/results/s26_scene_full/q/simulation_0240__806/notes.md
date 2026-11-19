# Q806 – height of the horse in the front (m)

Prior: speed of the horse at the back = 0.874 m/s. fps 24 (file and question agree).

Objects: "back" horse = chestnut (trailing, and slightly farther: hooves y≈1048); "front" horse = pale/cream
horse (leading, nearer: hooves y≈1055). Both readings of front/back give the same pair.

Measurements (scene/ tracks, checked on frames 12 and 24):
- Chestnut centroid x 234.1 (f0) -> 385.5 (f48): 3.154 px/frame = 75.7 px/s (bbox edges give 2.96-3.29, mean ~3.13).
  Frame 49 is an animation-loop reset, excluded.
- Scale at chestnut depth: 0.874 / 75.7 = 0.01155 m/px.
- Pale horse vertical extent (hoof to ear top): median 177.5 px (range 168-188 with head bob).

Perspective: house verticals are vertical (brick wall 580 px wide top and bottom), so the camera is ~level and the
horizon is near the image centre y≈960. Ground-contact rows 1048 (chestnut) vs 1055 (pale) give a depth ratio
pale/chestnut ≈ 88/95 = 0.926.
- Perspective-corrected: 177.5 × 0.01155 × 0.926 = 1.90 m.
- Single 2D scale (no correction): 177.5 × 0.01155 = 2.05 m.
Check: chestnut height 166 px × 0.01155 = 1.92 m, ≈ the corrected pale height, which suggests two horses
of the same size at slightly different depths. So the corrected value is more plausible.

Answer 1.95 m. I chose a value between the two routes, nearer the corrected one. It is about 2.5% from 1.90
and 5% from 2.05.
Confidence: moderate. The main uncertainties are the hoof rows (grass hides them, ±3 px, which is ±4% in the
depth ratio) and which frame or pose the reference bounding box uses (pixel height varies by ±5%).
