# q_1962: speed of the "red general chess" at t = 1 s (m/s)

## Identifying the object
- No red chess piece is visible in any frame. A full-frame difference check (findmov.py) shows only two moving
  objects: the black cat and the pink flamingo float. Nothing in the frame is saturated red.
- The cat is the prior's object, so the asked object is taken to be the other mover, the float (pink/red, rigid,
  slides without rotating). This is an assumption: the question's name doesn't match anything visible.

## Time base
fps = question_fps = 24, so t = 1 s is frame 24.

## Scale (2D convention, one m/px from the prior)
- The cat walks steadily. Linear fits of x against frame give 5.465 px/frame for the centroid, 5.463 for the bbox
  right edge and 5.439 for the left edge. I used 5.464 px/frame = 131.1 px/s.
- Scale = 1.041 / 131.1 = 0.00794 m/px.
- Sanity check: the float is 158 px wide, which gives 1.25 m, and the cat is about 106 px long including its tail,
  which gives 0.84 m. Both are plausible.

## Float speed at frame 24 (measure.py)
- One-frame backward difference 23→24 of the centroid: 13.5 px (dy is -0.1). The bbox edges give 14 px each, but
  they are integers.
- Per-frame speeds around the peak: 12.6, 13.2, 12.9, 13.5, 13.6, 12.8, 13.1 px/frame for frames 21–27. The mean
  speed over frames 21–26 is 13.2 px/frame. A local quadratic fit gives 12.8, but it flattens the peak.
- Adopted value: 13.4 px/frame = 321.6 px/s → 321.6 × 0.00794 = 2.55 m/s. Taking the raw 13.5 px/frame gives
  2.57 m/s; the window mean gives 2.52 m/s.

## Confidence
The measurement itself is good to about ±3%. The main risks are:
- the object identity (assumed to be the float);
- a possible depth difference between the cat and the float, which the 2D convention ignores.
