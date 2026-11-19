# q188 — speed of the shark at 1.0 s (m/s)

Prior: boat length = 10 m. 2D video, 24 fps file = question_fps 24 -> t = 1.0 s is frame 24.

## Scale (boat length)
- measure.py: background difference f57 vs f0, hull rows 380-640: x 663-1519 -> 857 px.
- SAM 3 segment "boat" f57: box x 669-1523, horiz_px 857 (overlay checked: whole hull, stern rudder to bow tip).
- scene record: 665-1523 -> 859 px. All agree within 0.3 pct; use 858 px -> 0.011655 m/px.

## Shark motion
- measure.py diff-mask centroids (vs f57): f21 1426.36, f22 1415.95, f23 1404.77, f24 1394.42, f25 1383.24,
  f26 1372.89, f40 1221.32 (y constant 905.2). Extents f24 x 1272-1549 (SAM f24 box 1274-1550: agree).
- SAM track shark_0.csv: f23 1397.0 -> f24 1386.8; span f2->f57 = -10.75 px/frame (frames 17-19 are SAM glitches,
  not used). Scene record fit -10.746 px/frame. My span f21->f40 = -10.79, f21->f26 = -10.69.
- Motion is uniform (constant velocity from frame 2), so the one-frame backward difference at frame 24 equals the
  constant velocity; single-frame differences (10.35 / 10.2 px) are centroid noise of ~0.4 px.
  SAM centroid sits ~8 px left of my diff centroid (constant offset, mine is unweighted mask incl. tail); no effect
  on speed.

## Answer
10.75 px/frame x 24 = 258 px/s x 10/858 m/px = 3.007 m/s -> 3.0 m/s.
Second route: SAM span speed 10.75 and scene fit 10.746 with SAM boat 857 px -> 3.01 m/s. Confidence high (~1 pct).
