# q_722: speed of the paper airplane at t = 1.25 s (m/s)

The prior is "length of the chalkboard = 5 m". The scene is 2D. The file rate and question_fps are both 24, so
t = 1.25 s is frame 30, and the speed is |p(30) - p(29)| x 24.

## Scale (chalkboard length)
- `edges.py` takes colour profiles across the board frame on frame 30, averaged over rows 325-420.
  - Outer wooden frame: left edge x ≈ 322.5, right edge x ≈ 1689.5.
  - The bars are about 19 px wide; the green surface runs from 341.5 to 1669.5.
  - Outer length = 1367 px.
- SAM 3 "chalkboard" mask on frame 30: box x 324.7-1690.1 (1365 px), horiz_px 1360. This agrees with my value within 0.2 pct.
- The scene record gave 1372 px (left edge 320). Frame 30 shows a dark shadow line at x = 320-322 just outside the
  wood, so I use 1367 px. The difference is 0.4 pct either way.
- Scale = 5 / 1367 = 3.658 mm/px.
- Other reading: if the prior means only the green surface (1328 px), the scale is 3.765 mm/px and the speed is
  5.48 m/s. I answer with the whole board including its frame, since the object's bounding box is the full board.

## Plane position
- `measure.py` builds a background (median of frames 0-5 and 44-49), takes a difference mask with threshold 20, and
  finds the principal-axis tips.
  - Frame 29 origin proxy (tip midpoint): (1417.7, 399.6). Frame 30: (1475.4, 418.5).
  - Step = 60.6 px/frame. The bbox centre gives 60.7 and the centroid 59.8.
  - Mask length is 140-141 px, which is consistent.
- SAM 3 "paper airplane" masks:
  - Frame 29 box centre: (1417.0, 400.2). Frame 30: (1474.7, 419.2).
  - Step = 60.8 px/frame, within 0.3 pct of my measurement.
  - SAM length is 141 px, and the overlays sit on the plane.
- Scene record `ref_*`: step from frame 29 to 30 = 60.9 px/frame.

## Second route
`fit.py` fits polynomials to the record's ref track (frames 14-35 cubic or quartic, frames 22-35, 25-35 and 26-34
quadratic). The fitted backward difference from frame 29 to 30 is 60.1-61.2 px/frame, and the derivative at frame 30 is
59.4-60.4. These are consistent with the raw 60.6-60.9.

## Answer
v = 60.6 px/frame x 24 fps x 3.658 mm/px = **5.32 m/s**.

Confidence: high. The pixel speed is good to about ±1 pct and the scale to about ±0.5 pct. The main risk is whether
the prior means the full board or only the green surface (+3 pct).
