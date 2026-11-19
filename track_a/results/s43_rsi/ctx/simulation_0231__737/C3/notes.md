2D scene, one m/px scale from the prior: cat centroid track gives 211.5 px/s, so scale = 0.714/211.5 = 0.003376 m/px (checks: blackboard 4.48 m, chair seat height 0.47 m). SAM 3 mask of the orange chair at the right end of the blackboard spans x 1600-1798 (199 px horizontal extent, whole chair incl. legs), so width = 199 x 0.003376 = 0.672 m. Second route: chair height 289 px -> 0.98 m and seat height 0.47 m confirm the scale; local side-to-side width (~146 px = 0.49 m) is noted in notes.md, but the full rendered horizontal AABB extent is reported per the method card.

Final message:
**Answer: 0.672 m** (question 737)

Method summary:
- **Scale (2D, from prior):** cat centroid track linear fit = 211.5 px/s; prior 0.714 m/s → **0.003376 m/px**. Cross-checks: blackboard 1326 px → 4.48 m, teacher desk 660 px → 2.23 m, chair seat height ~140 px → 0.47 m — all realistic.
- **Object:** SAM 3 "orange chair" instance k=0 (score 0.92) is the light-wood/orange chair at the right end of the blackboard; mask verified to hold the whole chair (back panel, seat, legs) with no background.
- **Measurement:** mask horizontal extent 199 px (x 1600–1798) → 199 × 0.003376 = **0.672 m**; vertical extent 289 px → 0.98 m height, consistent.
- **Caveat noted in notes.md:** the chair is slightly rotated, so its local side-to-side width is ~146 px (0.49 m) while the full rendered horizontal AABB extent is 199 px (0.67 m); the AABB reading is reported per the method card.
