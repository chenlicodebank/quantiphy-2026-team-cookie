# q2006 — height of the mug (m)

Prior: the mug's acceleration before 1 s is 9.8 m/s² (free fall). The video is 2D, 24 fps (file fps = question fps).

## Scale (measure.py)
- Fitted a quadratic to the vertical position over frames 0–18 (impact is between f18 and f19).
  - bbox centre: 8.847 px/frame²; mask centroid: 8.843; other windows (0–17, 2–18, 4–18): 8.81–8.87.
  - Top edge 8.77 and bottom edge 8.93. These differ because the perspective rim/base ellipses grow or shrink
    with image row, and their mean equals the centre's value.
- a = 8.84 px/frame² = 5092 px/s², so the scale is 9.8 / 5092 = 1.925e-3 m/px.

## Height in pixels
- The apparent height changes with image row (110 px at the top, 87 px at the image centre, 96 px at rest near
  the bottom), because the camera sees the base ellipse from below and the rim ellipse from above.
- Frame 14 (centre row ≈957, image centre 960): the top and bottom edges are flat across the whole body, so the
  mug is upright and seen side-on. Its height there is 87 px (frames 13–15: 89, 87, 88).
- The silhouette comes from the near rim. With the camera distance implied by the rest-frame perspective
  (f ≈ 3200–4700 px, so Z ≈ 6–9 m), this is about 1 % too large. Corrected value: H ≈ 86.3 px.
- H = 86.3 × 1.925e-3 ≈ 0.166 m (0.167 m without the correction).

## Check
- Rest frame: 96 px = H·cos α + D·sin α, with D = 77 px (body diameter). Taking H = 86 px gives α ≈ 8°, which
  matches the 662 px offset below the image centre for f ≈ 4700. The visible edge curvature at rest is
  consistent with that. If I trusted the edge curvature alone, H would be about 82 px (0.158 m).
- The diameter comes out at 0.148 m. Together the mug is large but plausible. The scale comes only from the
  gravity prior.

Confidence: about ±4 %.
