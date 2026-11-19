# q_2934 – width of the blue shopping bag (cm)

- File fps 24 = question_fps 24. Frame at t=1.4 s = 34. The bag is static: the record's centroid std is <0.5 px.
- The bag (scene.json "tote_bag") is navy and lies flat on the floor, right of centre. Its handle loop comes out of
  the edge from (822,295) to (894,347), so that edge is the opening. "Width" = extent across the face along the
  opening = the long side of the body (~90 px). The perpendicular side (~55 px in the image) is the bag's height.
- Segmentation (`bagseg.py`, frame 34): navy mask, holes filled, handle removed by morphological opening, convex-hull
  quad. Corners: (772,314), (822,295), (894,347), (843,371). Overlay: frames/bagmask.png.
  Edge lengths: opening edge 88.8 px; opposite (bottom) edge 91.0 px; sides 53.5 and 56.4 px.
- Lab method card: f = 763 px, d = 3.307 m. Width = 3.307 x 89.9 / 763 = 0.390 m. Adding ~1-2 px for soft edges
  gives ~0.395 m.
- Second route (`plane.py`, `rect3d.py`, `normals.py`): a floor plane from the depth_info centres, the board-rectangle
  reconstruction, and the bag quad as a rectangle. The plane normal is poorly constrained, so the width ranges from
  0.39 to 0.55 m. Normals that make the bag's corner close to 90 deg give 0.39-0.43 m. This is consistent with the
  card, but it suggests some foreshortening the card may miss.
- Answer: 40 cm (card value, nudged slightly toward the perspective estimates). Confidence: moderate, about ±10%.
