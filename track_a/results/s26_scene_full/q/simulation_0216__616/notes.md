# q_616: height of the vase (m). Prior: black cat speed = 0.94 m/s. No depth_info.

Time base: fps = question_fps = 24, so no re-timing is involved.

## Scale from the cat
- Cat speed in px: the record's matched upper-body track gives a mean step of 17.73 px/frame (std 1.1). The torso
  centroid gives 17.61 (net) and 17.75 (path). The manual nose readings give 529 -> 1237 over frames 0-40, which is
  17.7 px/frame. `speed.py` checks this; its template-match attempt failed because the background dominated, so I
  ignored it.
- 17.73 x 24 = 425.6 px/s, so the scale at the cat's depth is 0.94 / 425.6 = 0.002209 m/px.

## Vase pixel height (`vase.py`, `vase2.py`, frames 0 and 49, same result)
- The top of the lip is at y ≈ 573.5. The bottom of the base (front of the base ellipse) is at y ≈ 790.3, so the
  visible extent is about 217 px (the record says 219).
- The base outline is a shallow ellipse with a sagitta of about 2.5 px, so the base centre sits at y ≈ 788. The lip
  ellipse is negligible because the lip is close to the horizon. The vertical height at the vase's depth is therefore
  about 214.5 ± 2 px.

## Perspective: the vase is farther away than the cat (`vp.py`, `stand.py`)
- The bench-top slat gaps run front to back. I fitted 14 lines; they meet at a vanishing point of (930, 546). Its x
  is close to the image centre, so the horizon is at y_h ≈ 546.
- TV stand at x = 1000: the top surface spans y 776 (back) to 794 (front), and the floor rail is at 988.
  - The ratio (Hc - h_stand) / Hc = (794 - 546) / (988 - 546) = 0.559.
  - Check: this puts the back of the stand's floor line at y = 958, which matches the wall/floor junction
    (950-968). So the horizon is consistent.
- Depth ratios:
  - Vase base centre at y 788 on the stand top. Its floor-equivalent y is 546 + 242 / 0.559 = 979.
  - The cat's paws touch at y ≈ 1018-1020 on the near side and ≈ 1003-1006 on the far side, so the body's
    mid-depth is at y ≈ 1012.
  - Z_vase / Z_cat = (1012 - 546) / (979 - 546) = 1.076.
  - Varying the horizon from 500 to 600 and the cat's ground y from 1005 to 1020 gives a ratio of 1.06-1.10.

## Answer
H = 214.5 px x 0.002209 m/px x 1.076 = 0.51 m.

Second route: the flat 2D convention (one scale, record's 219 px) gives 0.484 m. That is 5 % lower, and the gap is
the depth offset, because the vase stands on a console behind the cat. I give the perspective-corrected value.
Sanity check: the cat at this scale is 0.54 m nose to rump, and the vase is a bit shorter than the cat is long,
which looks right in the frames. Confidence: moderate; the estimate is ±4 %.
