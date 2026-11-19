# q_733 — black cat length including tail (prior: chalkboard length = 5 m)

fps 24 = question_fps, so the timing is consistent. The time base doesn't matter here because the question asks for a size.

## Scale (chalkboard)
- `board.py` averages 10 frames and finds the board edges from intensity gradients. The outer wooden frame runs
  x 320.5 → ~1690, about **1370 px** wide (y 296–736). The green surface is 342 → 1670.5, 1328 px.
  The board is fronto-parallel: its top and bottom edges sit at the same y from x=400 to x=1600.
- I took the chalkboard object as board plus frame, so 5 m / 1370 px = 3.650e-3 m/px on the wall plane.

## Cat pixel length
- The cat appears grey because it is seen through haze and sunbeams. I built a median background over all 50 frames
  (`catmask.py`) and segmented the cat from the difference (`catext.py`). The views in `catview.py` check that the
  ends are the tail tip and the front of the head.
- In frames 12–19 the tail tip (raised tail, rearmost point) and the head are both clearly visible. The horizontal
  extent from tail tip to nose is 195, 198, 199, 201, (206), 201, 202, 198 px at threshold 6, and 192–200 px at
  threshold 10. By eye on frames 15 and 18: 296→496 and 322→522, both 200 px. I used **198 px**.
  - Frames 0–10 are cut at the front by the sunbeam or board-frame edge (x≈376), which gives 190 px or less.
  - Frames 20 and later: the tail is washed out.

## Depth correction (2D clip, but the cat is in front of the wall)
- The cat walks on the desk top, paws at y≈744. The desk top spans y 765 (front edge, right corner x=773) to y 737
  (back edge, right corner x=792).
- With the principal point at cx=960, the depth ratio is Z_back/Z_front = 187/168 = 1.113. Interpolating 1/Z
  linearly in y, the paws are at 0.9725 × Z_back.
- I assumed the desk is against the wall, so the cat's scale is 0.9725 × the wall scale.

## Result
198 px × 3.650e-3 m/px × 0.9725 = 0.703 m (0.723 m without the depth correction; 0.725 or 0.745 m if the scale
comes from the green surface only). Answer: **0.71 m**, which sits within about 5 % of all these variants and is
also a plausible length for a real cat including its tail.

Confidence: moderate. The two main uncertainties are whether the board's 5 m includes the frame (±3 %) and the
depth offset (0–4 %). The cat's pixel length is good to about ±2 %.
