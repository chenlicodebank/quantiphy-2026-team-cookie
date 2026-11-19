# Q2022 – pizza diameter (cm); prior: Monopoly money width = 7.5 cm (internet video, depth_info none)

Static sizes only, so time base is irrelevant (file 18.31 fps, question 24 fps). Near top-down view, one planar
scale (internet convention): cm/px = 7.5 / (bill "width" in px); pizza = its pixel diameter x that scale.

## Where the candidates part ways
C1 (47.0) took the bill's "width" as its SHORT side (~150-174 px) -> 43.8-50.8 cm, averaged.
C2 (24.0) took it as the LONG side (~315 px) -> 24 cm.
Pizza pixel size is the same for both (~1006-1015 px). The whole disagreement is which bill side is 7.5 cm.

## Decision: long side
- A banknote's "width" is conventionally its long horizontal dimension (banknote sizes are quoted width x height,
  e.g. 156 x 66 mm), and the bills here lie with their long side horizontal.
- Standard-object check (the deciding test). At frame 22: helper's finger ~55 px wide, thumb ~70 px, pepperoni
  ~90 px, wine-glass foot ~218 px (it stands on the table).
  * Long-side scale (7.5/308 = 0.0244 cm/px): finger 1.3 cm, thumb 1.7 cm, pepperoni 2.2 cm, glass foot 5.3 cm.
    These are all about 15-25 % small but plausible.
  * Short-side scale (7.5/150-176 = 0.043-0.050 cm/px): finger 2.4-2.75 cm, thumb 3.0-3.5 cm, glass foot
    9.4-10.9 cm. The fingers are more than 40 % too large, so this reading is rejected.
  (The scene's true scale looks like ~0.03 cm/px, so the real bills are ~9.5 x 4.6 cm and the pizza ~30 cm. 7.5 cm is
  closer to the real long side (-21 %) than to the short side (+63 %), which also supports the long-side reading.)

## Measurements (my code)
- billfit.py, frame 22 (index 22 of the file): line fits to the bill edges, refined by gradient.
  * "1" bill (isolated, clean fit, resid <0.3 px): long sides 306.7 / 304.7 px, short 173 / 179.
  * top tilted "500" bill: long sides 304.3 / 313.9 px (short 126/159, the left edge is unreliable because of the
    overlap and curl).
  * Long side: about 305-310 px; I use 308 px.
- rowext.py, frame 22: per-row outer rim transitions. The right rim maxes at x=1854 (rows 740-800), the left rim is
  at 830-840. Horizontal diameter is ~1017-1020 px (same-row 1019 at y=800). The ellipse fit (pizzafit.py) gives a
  horizontal extent of 1018-1020 at frames 22 and 29 (the pizza is not perfectly round; vertical ~965-990 px). The scene
  record gives 1015 (f29).
- Pizza diameter used: 1017 px (horizontal, matching the bills' horizontal long-side convention).

## Result
7.5 x 1017 / 308 = 24.8 cm. Alternatives: mean diameter ~995 px gives 24.2 cm, and bill 305-314 px gives
24.3-25.0 cm. Answer **24.7 cm**.
I agree with C2 (24.0). The ~3 % difference comes from my slightly shorter bill (308 vs 315 px) and wider pizza
(1017 vs 1006 px).
Second route: the "1" bill alone (305.7 px) gives 25.0 cm and the top 500 bill alone (309 px) gives 24.7 cm.
Confidence: moderate-high on the reading (long side), and ±3 % on the pixel ratio.
