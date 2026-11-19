# q_2751 – white cup rim diameter (cm)

- Lab clip, 1280x720, 24 fps (file fps = question fps). f = 0.5959 x 1280 = 762.8 px.
- depth_info gives "distance_white_cup_camera = 8420m" – obviously a typo; read as 0.8420 m (consistent with the cup
  standing behind the card tent at 0.69 m and in front of the poker tower at 0.91 m... similar table depth).
- Cup is static. measure.py: median of frames 0,10,20,48, per-row white extent with sub-pixel half-level edges.
  Rim (top, y 380–393, full-width rows just below the rim ellipse top) = 73.9 px (739.5 → 813.4). Body tapers
  slightly to ~73 px lower down, so the rim is the widest part.
- Diameter = 0.842 m x 73.9 / 762.8 = 0.0816 m = **8.16 cm**.
- Alternative (Euclidean depth converted to optical-axis Z, off-axis angle ~11.8°): Z = 0.824 m -> 7.98 cm.
  Answer uses the method-card convention (depth_info distance directly).
- Scale check: credit card (flat on table, 0.69 m) expected 85.6 mm -> 94.6 px; on the frame its tilted outline
  spans ~90–105 px (x 511–617 incl. skew), consistent with f ≈ 763.
- Confidence: moderate-good (±3 %), main uncertainty the typo'd depth and the depth convention.
