# Q902 — width of the iPhone right of the plant (simulation_0259, 2D)

File fps = question_fps = 30.

## Scale from the prior (cup free fall, g = 9.8 m/s^2)
`measure.py`: quadratic fits to the cup track (scene/tracks/cup.csv) over free-fall frames 0–14 (the impact is at frame 15, so it is not fitted):
- top_y (lid edge, the cleanest point): a = 6322–6329 px/s^2, rms 0.2 px, the same in every window (0–14, 1–14, 3–14, 0–10)
- centroid / bbox centre: 6250–6310 px/s^2 (slightly affected by the underside ellipse shrinking, a perspective effect)
- Adopted a = 6300 px/s^2, which gives 9.8/6300 = 1.556 mm/px (±0.5 %).

## Phone
Black phone lying flat at x 1142–1192, y 865–876 (frame 0, static). Dark-pixel mask row extents: 51, 51, 50, 50, 50 px on the top rows,
so its horizontal extent is 50.5 ± 0.5 px. Its long axis points into the depth: the face is foreshortened to about 10 px vertically.
Width = 50.5 × 1.556e-3 = 0.0786 m.

## Checks
- An iPhone is about 7.1–7.8 cm wide, so 7.9 cm fits. Its length (≥14.7 cm) would need about 95 px, which is not what we see, so the horizontal extent is the width.
- Other objects at this scale: mug body 45 px = 7.0 cm, plant pot 47 px = 7.3 cm, bag 225 px = 35 cm, cup rim 42.5 px = 6.6 cm, visible table 1020 px = 1.59 m. All are plausible.
- Depth: the phone's contact line (y≈875) is within about 4 px of the cup's rest contact line (y 871), so the two are at about the same depth (<~1–2 % scale difference).

Confidence: good (about ±3 %).
