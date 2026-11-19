# q_724: clock diameter (m). Prior: chalkboard length = 5 m. 2D scene, static camera.

Method (measure.py, mean of frames 0/25/49 to reduce render noise):
- Clock (dark ring on the wall at the upper right). Half-depth edges from row/column profiles through the centre (1763, 292):
  vertical outer edges 236.3 to 348.9, so 112.6 px. Horizontal: left outer edge 1705.3, right inner edge 1812.6 plus the
  ring width (about 6 px), so about 1818.6 and about 113.3 px. The right outer edge blends into the clock's wall shadow.
  Threshold extents give 111–114 px, and the scene record says 112. Value used: **113 px**.
- Chalkboard length = whole object including its wooden frame. Outer frame edges are at x ≈ 319–322 and x ≈ 1690–1693,
  so about 1370 px (record: 1372). The green surface alone is 1328 px.
- Scale = 5 / 1372 m/px, so the diameter is 113 × 5 / 1372 = **0.412 m**.

Check: if the 5 m were the green surface only, the answer would be 0.425 m (3 % higher). Both the clock and the board are on
the same wall plane, so one scale applies. A diameter of about 0.4 m is plausible for a classroom clock next to a 5 m board.
Confidence: good (about ±3 %). The main uncertainty is which board extent the prior means.
