# q_699: width of the pool tiles (horizontal side)

Prior: the black cat's speed is 1.041 m/s. depth_info is null. The file fps (24) is the same as question_fps (24).

## Scale from the cat's speed
- The camera is static (scene record). The cat walks at constant speed along +x on the deck. Its feet are at y ≈ 920 (median feet_y), just behind the deck's front edge at y ≈ 925.
- Pixel speed from scene/tracks/cat.csv (centroid cx_mask):
  - linear-fit slope 5.455 px/frame;
  - mean per-frame dx 5.49 px/frame;
  - net change over frames 0 to 48: 5.47 px/frame.
- I used 5.47 px/frame = 131.3 px/s, so the scale at the cat's depth is 1.041 / 131.3 = 0.00793 m/px.

## Tile width in pixels (joints.py, deckfit.py, scale.py, lattice_left.py)
- **Deck paving slabs:** I located the joints from dips in the row intensity profile, at frame 49.
  - They form a regular lattice. Along the deck front edge (y 924–928) the spacing is 148.8 px (10 joints, residuals ≤ 2 px).
  - The joint lines converge with perspective, so the spacing shrinks with height on the deck: 149 px at y 926, about 146–147 px at y 918–920, and 144.5 px at y 914.
  - At the cat's walking line (y ≈ 916–920) the spacing is about 146 ± 1.5 px.
- **Pool-edge coping blocks (curb face, y 945–972):** the spacing is 149.9 px (11 joints).
  - This lattice is offset from the deck lattice by half a tile. The face is slightly closer to the camera than the deck edge, which explains the slightly larger spacing. It looks like the same world width as the slabs.

## Answer
- Width = 146 px × 0.00793 m/px = **1.16 m**.
- Readings and sensitivity:
  - At the deck front edge (148.8 px), the width would be 1.18 m.
  - For the coping blocks, after correcting to the cat's depth, it is the same, about 1.16–1.19 m.
  - Using the fit slope of 5.455 px/frame instead gives 1.161 m.
- Second-route check: two separate tiled structures (the deck slabs and the coping blocks), measured at several heights, agree to within about 2%.
- As a sanity check, the cat is about 105 px long, which is 0.83 m. That is large for a cat, so the scene is not at real-world scale, as the paper warns. Only the prior sets the scale.
- Confidence: moderate to high, about ±3%. The main uncertainty is which depth line the reference used.
