# q_635 — length of the white sofa (m)

Prior: speed of the black cat = 0.94 m/s. 2D top-down render, static camera, fps 24 (file and question agree).

**Scale from the cat's speed.**
- Front edge (bbox_x1, scene/tracks/black_animal.csv) goes from 647 to 1185 over 49 frames, i.e. 10.98 px/frame.
  Split in halves: 11.0 for frames 0–24 and 10.96 for frames 24–49, so the speed is constant.
- Mask centroid: 563.9 → 1098.8, i.e. 10.92 px/frame.
- Taking 10.95 px/frame gives 262.8 px/s, so the scale is 0.94 / 262.8 = 0.003577 m/px.

**Sofa pixel length.**
- `measure_sofa.py` takes horizontal gradient edges on rows y = 620–780 in frames 0, 25 and 49 (the sofa does not move).
- Leftmost edge is about 565.5 px (y 700–740). Rightmost edge is about 1451.5 px.
- The extent is 886 px. The overlay `frames/sofa_mask.png` confirms both ends at about 565 and 1450.
- The scene record's visual bbox (567–1447, 880 px) agrees to within 1%.

**Answer.** 886 × 0.003577 = **3.17 m**. With the scene-record extent of 880 px it would be 3.15 m.

**Caveat.** The sofa's widest point is at arm height, and the cat's origin is lower. The view has slight perspective,
which the 2D single-scale convention ignores. Confidence: moderate to high (about ±5%).
