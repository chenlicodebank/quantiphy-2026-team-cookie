# Q759: width of the chair (m)

Prior: the black cat's speed is 0.714 m/s. No depth_info. fps is 24 in both the file and the question, so the time base is 24 fps.

## Scene
- Straight top-down Blender view. The cat walks +x on a table top. A tablet-arm student chair stands on the floor at the right.
- The chair is clearly lower than the table top, and its tablet, seat rails and floor feet are each at a different height. So one image-wide m/px scale is not valid. I used pinhole geometry with z-depths relative to the floor depth (D_f = 1) and the principal point at the image centre.

## Measurements (`measure.py`, readings from zoomed crops in frames/)
- **Cat pixel speed:** 13.44 px/frame. This is the average of the head-front and mask-centroid slopes over frames 22-44, where the cat is fully visible and before the grey-head artifact. That gives 0.714 / (13.44 × 24) = 0.002213 m/px at the depth of the cat's body/head.
- **Table top vs floor:** the table's leg feet show beyond the top's edge, at (738, 405) and (738, 794). Fitting a radial perspective model to the top edges (x = 714, y = 366 and 848) gives D_t/D_f = 0.857, with residuals of 2 px or less and a leg inset of 14 px. So the table height is 0.143 D_f.
- **Chair legs:** the legs run radially from the side rail to the feet: (1587,540)→(1537,540) and (1582,711)→(1545,706). That puts the rail depth at 0.93 D_f, so the seat is at about 0.49 × table height (≈0.37-0.40 m if the table is 0.75 m). This is plausible.
- **Chair pixel extents:**
  - Seat: x 1585-1767, y 550-715.
  - Tablet: x 1597-1836, y 499-535.
  - Left feet: x 1537 and 1545; rear foot at y 706.
- **Cat height correction:** the cat's tracked points are about 0.15-0.22 m above the table. This assumes a real-scale scene with a 0.75 m table; the cat is then 0.73 m long including its tail, and the table is 1.1 m wide, which are sanity checks.
- **Tablet height:** not directly observable. I scanned 0.47-0.75 m.

## Result (world extents)
| case | side-to-side (x) | front-to-back (y) |
|---|---|---|
| no cat-height correction | 0.53-0.57 | 0.52 |
| head at 0.15-0.22 m | 0.55-0.60 | 0.537-0.552 |

The shorter horizontal extent is front-to-back, from the tablet's front edge to the rear feet. It is stable at 0.52-0.55 m whatever the tablet height. The side-to-side extent, including the tablet overhang, is 0.55-0.60 m.

- **Width = shorter horizontal extent ≈ 0.54 m** (the benchmark's convention).
- Alternative reading, width as side to side: about 0.56 m.

## Checks and confidence
- The two readings agree to within 4 %. The tablet height changes the front-to-back value by only about 1 %.
- The main uncertainty is the absolute depth scale, i.e. the cat-height correction of 0-5 %. Overall confidence is moderate, about ±6 %.
