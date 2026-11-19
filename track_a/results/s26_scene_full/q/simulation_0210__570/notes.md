# Q570 – width of the floor mirror (m)

Prior: the black cat's speed is 0.94 m/s. depth_info: none. fps = question_fps = 24, so no re-timing.

## Scale from the cat
- scene/tracks/cat.csv, cx_mask (the mask centroid, used as the origin proxy): a linear fit over all 50 frames
  gives 427.7 px/s. Three sub-windows give 429.6, 430.5 and 423.4 px/s. The mean of the per-frame speeds is
  432 px/s, but that includes the gait wobble. y is constant, so the cat walks parallel to the image plane.
- Scale at the cat's depth: 0.94 / 428 = 0.002196 m/px.

## Mirror pixel width (mirror.py, feet.py; frame 0; the mirror is static)
- Outer wood frame, measured by colour difference in each row: 242–245 px at the top (y 405–480, x ≈1630–1874),
  245 at y 600, 247 at y 760, and 246–250 at y 880–910. It widens towards the bottom because the mirror leans
  against the wall, so its bottom is nearer the camera. Bottom edge at the floor: y ≈ 978, width ≈ 250 px.
  Wall/floor line: y ≈ 955.

## Depth correction (the mirror is behind the cat)
This is a 3D render. The floor is visible, the table top is seen from above, and the cat's paws (y ≈ 1030) are
lower in the image than the mirror's base (978). The mirror is therefore farther away than the cat.
- For floor points with a pitched pinhole camera, image scale is proportional to (y_floor − y_horizon).
- Horizon estimates, all rough:
  - Table-slat vanishing point (slats2.py): ≈ 292.
  - Mirror width growth 243 → 250 px between the wall top and the floor base: ≈ 160–255.
  - Mirror lean, combined with edge convergence and the gap between its base and the wall line: ≈ 105.
  - Lamp-shade rim sag of only ~4 px over 215 px (≈ 2° look-down) means a narrow field of view.
  - Working value: y_h ≈ 200–260.
- The cat's midline floor row is ≈ 1029.
  - Bottom route: 250 px × (1029 − y_h) / (978 − y_h) = 250 × 1.066–1.070 ≈ 267 cat-depth px.
  - Top route (the top rests on the wall, floor row 955): 243 × (1029 − y_h) / (955 − y_h) = 243 × 1.098–1.105
    ≈ 267–269 px.
  - The two routes agree. Over the extreme horizon choices (105 to 540) the factor stays within 1.054–1.11.
- Width = 268 px × 0.002196 m/px ≈ 0.589 m.

## Answer
0.59 m (the mirror's horizontal extent across its face).
- Without a depth correction (one flat 2D scale) it would be 245 × 0.0022 ≈ 0.54 m.
- Confidence: moderate. The speed scale is good to about ±1.5 %; the depth factor is uncertain by about ±3 %.
