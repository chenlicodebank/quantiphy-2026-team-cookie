# Q605: width of the floor mirror (m)

Prior: speed of the black cat = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Objects
- The scene/ record calls the moving animal a "black dog". It is the black cat in the prior, and it is the only
  moving object. The view is top-down (2D), and the cat walks on the floor plane.
- Floor mirror: the "door_or_wall_panel_top_right" in scene.json. It is a framed light-green panel that leans
  against the top wall. Its bottom edge is on the floor at y ≈ 220 px, and its top rests on the wall at y ≈ 85 px.
  Because the top is closer to the camera, it looks larger and is shifted outward (perspective).

## Scale (crop.py, edges2.py)
- Cat x-slope from scene/tracks/dog.csv, linear fit over frames 0–49: nose 10.995, mask centroid 10.997,
  torso centroid 10.991 px/frame. That gives 263.9 px/s, so the scale is 0.94 / 263.9 = 0.003562 m/px.

## Mirror width
- I measured the mirror's bottom edge, which lies on the floor at the same scale as the cat. I fitted lines to the
  outer edges of the left and right frame rails (horizontal grey gradient, rows 170–218). The bottom edge row is at
  y ≈ 220 (vertical gradient). Fitted width at y = 216–222: 162–164 px. Reading the row profiles directly gives
  1386.5 → 1551 at row 219, i.e. 164–165 px. I used 164 ± 3 px.
- Width = 164 × 0.003562 = 0.584 m.
- Perspective: the top edge is about 200 px wide, which is 1.18× the bottom width. This ratio agrees with the
  lateral shift of the top corners from the principal point, so the camera is high, roughly 6.5× the height of the
  mirror's top. If the cat's origin is about 0.15 m above the floor, the floor scale is about 1.5 % larger than the
  cat-plane scale, which gives 0.593 m. Answer: 0.59 m.

## Second route
- Top edge: outer width ≈ 1460–1660 = 200 px. Dividing by the perspective factor 1.18 (taken from the corners'
  radial offsets from the image centre) gives ≈ 169 px floor-equivalent, i.e. 0.60 m. This agrees with the bottom
  edge within 3 %.

Confidence: moderate-high (±4 %). The mirror edges have low contrast against the carpet, and the cat origin's
height is unknown.
