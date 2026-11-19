# Q1597 — height of the table-lamp shade (m) → **0.245**

File fps 24 = question_fps 24; static camera; principal point assumed (960,540).

## Focal length (cat prior: 0.94 m/s, depths 4.199 m @f0, 4.481 m @f24)
Back-projected the cat reference point at f0 and f24 with the given depths and solved |P24−P0| = 0.94 m
(solve_f.py, refine_f.py): torso centroid 2080–2099 px, mask centroid 2103–2151, bbox centre 2121–2145.
Independent: the vanishing points of the back-wall and right-wall floor lines (orthogonal) give, for a
level camera, f = 2136; conversely for f≈2100 they put the horizon at y≈541 → camera is level (pitch≈0).
Used f = 2100 (±1.5%).

## Floor / table model (geom.py, table_edges.py)
Mirror bottom centre (1523,813) at 6.407 m → camera height ≈0.80 m. Front-left (closest) bench-leg foot
(1407,840) on that floor is at 5.77 m; leg centre pixel (1416,767) at the given 5.69 m → Z≈5.53, consistent.
Cat origin height comes out 0.22 m at both times (consistent).
Table top (in code, luminance columns): back edge row ≈655.7, front edge row ≈663.9 (top of front-face
notches), at the lamp x. Lamp base front contact row ≈662 → lamp sits near the front.
Front edge Z_f ≈ 5.52–5.60 → lamp contact Z = Z_f·123.9/122, + base radius (22 px) → lamp axis Z ≈ 5.67–5.75.

## Shade (measure_shade.py, mask overlay frames/shade_mask.png)
White-shade mask (thr 164–166): rows 399.5–491.5, width 192 px at the bottom, 62 px at the top.
Naive height 92 px × Z/f = 0.248–0.252. Perspective-corrected (camera 0.13 m below the bottom rim):
top = front point of top rim (Z − r_top), bottom = rim sides (Z) or back rim seen through the opening
(row ≈494.5, at Z+R) → 0.243–0.248 (f = 2100), range 0.239–0.250 over f 2087–2136 and Z_f 5.52–5.60.

## Answer
0.245 m. Second route check: naive pixel-height × depth / f gives 0.248–0.250, i.e. within 2%.
Confidence: moderate-good (~±3%); main uncertainties are f (cat origin proxy) and the lamp's depth on the table.
