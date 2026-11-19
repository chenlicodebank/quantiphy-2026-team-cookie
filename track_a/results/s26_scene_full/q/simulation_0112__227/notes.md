# q_227 — bridge thickness (m)

Prior: car speed 6.66 m/s. Time base: file fps 24.007 ≈ question fps 24.0, so the difference doesn't matter.

## Bridge pixel thickness (prof.py, frame 54 with no car, row-mean profiles over 4 column bands)
- Deck top edge: transition at y 539.5–540.5 (same in every band).
- The slab and girder boundary is at y≈557 (light slab 540–557, dark girder below).
- Girder bottom: transitions at y 613–617, edge ≈ 616.
- Total vertical extent ≈ 76 px. This is "thickness", read as the bridge's vertical (bbox z) extent.
  The deck slab alone is 17 px, about 0.16 m, which is the alternative reading.

## Scale
- Car near-side hub track: 28.227 px/frame → 677.6 px/s → 0.00983 m/px at the near-side depth.
- Parallax-corrected car centre plane: 27.0 px/frame → 0.01028 m/px at the origin depth.
  A check: silhouette length 423.5 px gives about 4.2–4.35 m, which matches a 911 (4.29 m), so the scene is close to
  real scale. A car width of about 1.77 m with the far/near depth ratio of 1.09 gives a centre depth of about 20.7 m.
- The camera sits at deck height (the deck top projects to the image centre row 540), so the deck surface is edge-on.
  The bridge's front face is nearer to the camera than the car's near side, but by an unknown amount.

## Result
- At the car-centre scale: 76 × 0.01028 = 0.78 m (upper bound).
- At the near-side scale: 76 × 0.00983 = 0.75 m.
- With the front face 1.5–2 m in front of the car centre (a 3–4 m wide deck): 0.71–0.73 m.
- Answer: **0.73 m**. Confidence is moderate, about ±6 %, mainly because the bridge face depth is unknown.
