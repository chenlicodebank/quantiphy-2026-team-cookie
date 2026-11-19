# q 2120 — distance between the two left umbrellas (m)

Prior: swimmer height = 1.8 m. Top-down 2D internet shot → one m/px scale from the prior (annotator convention).

- Swimmer, frame 0 (body flat at surface, frames/sw0.png): toes x≈578, top of head x≈783 → 205 px (matches scene record).
  Scale = 1.8/205 = 0.00878 m/px. (Toes→fingertips with arms forward = 252 px; not "height".)
- Left umbrellas, frame 0 (frames/umb.png): pole hubs (202,492) and (195,975) → 483 px;
  hexagon bbox centres (222,499) and (216,972) → 473 px. Mean 478 px.
- Distance = 478 × 0.00878 = **4.20 m** (hub route 4.24, bbox route 4.15).
- Camera is static (drift < 13 px), so the frame choice doesn't matter; time base not relevant.
- Sanity: pool water 1159 px → 10.2 m, lounger 246 px → 2.2 m: plausible.
- Alternative reading (arms-extended length as the 1.8 m) would give 3.41 m; not used.
Confidence: moderate-high (main uncertainty is which swimmer extent the annotators used).
