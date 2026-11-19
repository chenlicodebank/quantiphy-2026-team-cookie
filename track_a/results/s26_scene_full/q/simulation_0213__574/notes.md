# q_574: height of the wooden bench (m)

The prior is the black cat's speed, 0.94 m/s. There is no depth_info. The file fps and question_fps are both 24, so no re-timing is involved.
The "wooden bench" is the slatted wooden table at the right. In scene/ it is recorded as `side_table`.

## Scale from the cat (measure.py)
- The cat walks at a steady pace. A linear fit to its nose (bbox_x1) gives 17.76 px/frame (rms 0.7 px). The centroid gives 17.81 and the torso 17.86.
  The two windows, frames 0-22 and 44-49, agree. I used 17.78 px/frame, which is 426.7 px/s.
- This gives s_cat = 0.94 / 426.7 = 0.002203 m/px in the cat's lane. The cat's paw bottoms are at y = 1020 (edge at 1020.5).

## Bench pixels (prof.py, legs.py, frame 48, bench unoccluded)
- The top surface is seen slightly from above. Its back edge is at y ≈ 782 and its front edge at y ≈ 805.5. The front face and apron run from 806 to 831.
- The front feet end at y = 995.5 (x ≈ 1540 and x ≈ 1870). The back-left foot ends at y ≈ 967.5.
- The full image extent is 782 → 995.5, which is 213 px. Part of that is the foreshortened top surface, not height.

## Perspective
- The bench stands behind the cat's lane: its feet are at y 967-995, the cat's paws at 1020.
- The camera is level. The lamp base's centre line is vertical to within 0.002-0.007 px/px at 555 px off-centre (vert.py), so the pitch is under about 1°.
  That puts the horizon near the image centre. The sag of the lamp-shade rim (≈2-3 px) suggests y_h ≈ 540-580; I used 555.
- Camera height = (1020.5 - y_h) × s_cat ≈ 1.025 m.
- Height of a horizontal surface: H = Hc × (1 - (y_top - y_h) / (y_floor - y_h)), using a top edge and a foot at the same depth.
  - Front pair (805.5 / 995.5): 0.442 m.
  - Back pair (782 / 967.5): 0.460 m.
  - Midpoints (793.75 / 981.5), which cancel a symmetric top overhang or leg splay: **0.451 m**.
- Changing y_h between 540 and 580 moves the result by less than 1%.

## Checks
- The front and back pairs bracket the answer at 0.442-0.460 m (±2%). The implied top overhang is about 1.5% of the depth on each side, which is self-consistent.
- A naive single 2D scale with no perspective (213 px × s_cat) would give 0.47 m. That figure counts the foreshortened top surface and ignores that the bench is farther away, so I rejected it.
- A plausible real-world bench or table height is 0.45 m.

**Answer: 0.451 m.** Confidence: moderate-high (about ±3%).
