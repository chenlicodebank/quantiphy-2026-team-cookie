# Q2423 — width of the table (cm)

Lab clip, 24 fps (file and question_fps agree), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).

## Which dimension
Rough perspective: camera ~0.145 m above the table top, axis about horizontal. The front edge (y≈530) is at z≈0.64 m
and the back edge (y≈442) at z≈1.35 m, so the table is about 0.7 m front-to-back and about 0.6 m left-to-right.
The shorter horizontal extent is therefore left-right, and depth_info gives the table's left/right distances, so both
readings point to the left-right extent. (Front-to-back reading: about 70 cm, rough estimate.)

## Measurement (measure.py)
Table mask = brown/dark HSV pixels (checked visually in frames/mask48.png). Row extents of the front face
(rows 538–552) are x = 280…924 → 645 px, the same in frames 0/12/24/36/48 (static camera). The top-surface front edge
(row 534) is 641 px.

## Scale
Method card: size = depth × pixel extent / f, with depth = mean(0.704, 0.725) = 0.7145 m
→ 0.7145 × 645 / 763 = 0.604 m.
Second route: back-project the two ends as ((u-cx)/f, (v-cy)/f, 1) × depth (left end at 0.704, right end at 0.725)
→ |ΔX| = 0.602, ΔZ = 0.021 → 0.602 m. Same answer.
(If the given depths are treated as Euclidean ray lengths instead, the result would be about 0.54 m; the card
convention is the one used here.)

Answer: 60.4 cm (a standard 60 cm table width fits). Confidence: moderate-high. The main uncertainty is the
depth convention (±10%).
