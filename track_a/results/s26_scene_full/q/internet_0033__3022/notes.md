# Q3022 – speed of the plate (bowl) of tomatoes, 0 s to 0.52 s (m/s)

Prior: fork = 20.3 cm. Internet footage, so I used one planar scale from the prior's pixel length, as the annotators did.

## Scale (fork)
- The scene record does not cover any fork. The cleanest fork is the one lying flat on the table by the pink-blazer
  diner's plate, with the tines on the plate rim (frame 0).
- `fork_tip.py` reads intensity profiles along the fork axis from (1725,296) to (1832,209). The tine tip is at
  s ≈ -1 px, where the tines first darken the white plate, and the handle end is at s ≈ 139.5 px (sharp drop to
  table brown). That gives a length of **140 px** (±3), and scale = 0.203/140 = 1.450e-3 m/px.
- Check: the fork in a diner's hand at the bottom of the table shows ≥132 px of metal with part of the handle
  under the palm, so about 150 px. The ~7 % difference matches the perspective seen in the plate sizes (top
  plates 224-238 px, bottom plates 249-256 px). The bowl travels at mid-table, so the top fork's scale may be about
  3 % small. I left that uncorrected, following the single-scale convention.

## Time base
The file runs at 19.29 fps and the question at 25 fps. I used **25 fps**, assuming the clip was re-timed from
25 fps stock footage (that is what the convention says the reference follows). So t = 0.52 s is frame 13.
Both rates give plausible hand speeds (0.78 vs 0.59 m/s), so the scene alone cannot tell them apart. That is the
main uncertainty. Under 19.29 fps (frame 10) the answer would be 0.588 m/s.

## Motion
- The bowl is already moving at frame 0, nearly straight +x and speeding up (15 → 23 px/frame).
- The camera drifts about 1 px/frame upward. I used the record's background-compensated rim centres
  (`cx_bgcomp_f0`).
- Second route (`track_check.py`): my own template tracker on the bowl, with the background shift taken from static
  table patches. It gives frame 0 (1520.0,856.0) → frame 13 (1799.1,833.4) background-compensated, which matches
  the record (1520.4,855.9) → (1798.7,838.0) to within 0.5 %.
- Results (`speed.py`): mean of the per-frame speeds over frames 0-13 = 0.784 m/s (rim, background-compensated),
  0.782 m/s (raw rim), 0.786 m/s (tomato centroid). Displacement over time = 0.778 m/s.

## Answer
**0.78 m/s.** Confidence: medium-high if the 25 fps reading is correct (scale ±3-5 %). It would be about 25 %
lower under the file's 19.29 fps.
