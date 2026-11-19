# q_597 — width of the white sofa (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing issue.
The camera looks straight down at the room. The corner edges of the walls point radially to the image centre, so the nadir is at the centre. The camera is static.

## Scale (black cat)
- My own segmentation (`cat_check.py`, dark blob with gray < 60, frames 0, 7, …, 49): the head front edge and the centroid both move 10.98 px/frame. Fitting the scene/ track (`cat_speed.py`) gives bbox_x1 10.978 px/frame and body_cx 10.94 px/frame. Speed is constant and y drift is about 0.
- 10.98 x 24 = 263.5 px/s, so the scale is 0.94 / 263.5 = 0.003567 m/px on the cats' plane.
- Sanity check: black cat body ~0.56 m, width ~0.15 m, room floor ~5.6 m wide, round rug ~1.7 m. All plausible.

## Sofa extents (frame 10, `sofa_edges.py`, `sofa_profile.py`)
- Top edge: tips of the two arms, a sharp step at y ≈ 519 px (x ≈ 670 and x ≈ 1340).
- Bottom edge: the convex back, y ≈ 996 px (x ≈ 960–1060).
- So the y extent is 477 px. That is the shorter horizontal extent (front-to-back depth), which is the "width" here.
- The x extent is about 562–1451 px, so 889 px. That is the length, ≈ 3.17 m.
- The scene/ record gives 885 x 470 px (its mask top of 535 misses the soft outline, as the record itself says). The visual outline was 518–1000. Both agree within a few px.

## Result
- Width = 477 px x 0.003567 = 1.70 m, assuming the sofa outline is on the same scale as the cats.
- Perspective: the sofa's widest outline is roughly 0.4–0.7 m above the floor. The cat origin is ~0.0–0.25 m. The camera height can't be pinned down: the picture frame and the walls suggest H ≈ 6–15 m, which makes the outline look 2–6 % too big.
- I applied a moderate ~2 % correction. **Answer 1.67 m** (range 1.60–1.70).

## Second route
- Scene record extents (470–482 px) x the same scale give 1.68–1.72 m, consistent.
- The scale from the cat's centroid instead of its head edge differs by less than 0.4 %.

Confidence: moderate. The main uncertainty is the unknown camera height (perspective of the raised sofa outline), worth ±4 %.
