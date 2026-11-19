# q_2715 – white cup rim diameter (cm)

File fps = question fps = 24. t = 1.4 s -> frame 34. Cup is static (identical extents in frames 10, 30, 34, 40).

Method (lab method card): f = 0.5959 x 1280 = 763 px; depth to white cup = 0.8740 m.
- `measure_cup.py`: white/low-saturation mask rows and row-wise brightness-gradient edges in the cup crop.
  Rim top at y ~ 376-378; width just below the rim (y 380-398): mask 71 px, gradient edges 722.5-795.5 = 72-73 px.
  Used 72 px. (scene/ record had top width 71 px, consistent.)
- Size = 0.874 x 72 / 763 = 8.25 cm (card convention, Euclidean distance).
  With the off-axis correction (cup centre ~(758,434) px; z = 0.874/1.0124 = 0.863 m): 8.14 cm.
- Answer 8.2 cm (midpoint).

Second route: credit card prior. The dark card near the front edge (depth 0.6867 m) spans ~102 px horizontally
-> 9.2 cm vs 8.56 cm true; ~7 % high, consistent given the card's oblique orientation / bbox including its
edge. Supports the f / depth scale to within a few percent.

Confidence: good (±4 %). Main uncertainty: rim edge pixel location (±1 px = 1.4 %).
