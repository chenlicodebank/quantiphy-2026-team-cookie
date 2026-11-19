# q716: chalkboard height (prior: chalkboard length = 5 m)

Static frontal 2D view. The board is roughly parallel to the image plane, so I used one scale: 5 m / the board's pixel width.

Measurements (`edges.py`, frame 47, intensity profiles at 4 columns and 3 rows):
- Outer wooden frame: left ≈ 320, right ≈ 1691, so width ≈ 1371 px. Top ≈ 296, bottom ≈ 736, so height ≈ 440 px.
  These agree with scene.json (1372 × 443) to within about 3 px.
- Green surface only: ≈ 1327.5 × 400 px.

The object's bounding box should include the frame, so height = 5 × 440 / 1371 = **1.605 m**.
Check: the record's outer extents give 5 × 443 / 1372 = 1.614 m. If only the green surface counted, the answer would
be 1.507 m (about 6 % lower).
Confidence: good, provided the frame is part of the board object.
