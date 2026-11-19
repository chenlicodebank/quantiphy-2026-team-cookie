# Q205: length of the shark (m). Prior: shark acceleration = 1 m/s^2

This is a 2D side-view render at 24 fps (the same rate as question_fps). The camera is static. The shark swims left along a horizontal line (cy ≈ 904). The scale comes from the shark itself, so the same depth applies to both measurements.

## Pixel acceleration (fit.py, seg.py, vel.py)
I fitted a quadratic x(t) over frames 1–53 (motion starts after frame 1):
- record centroid cx: −87.3 px/s²
- my own centroid (threshold-25 mask): −86.3
- my own tail tip: −85.0
- record tail edge x1: −86.1
- my own nose tip: −84.0 (this edge is noisier)

As a cross-check, I fitted a line to the per-frame backward-difference speed over frames 2–53: 85.2 to 86.3 px/s². The fits by window vary between about 80 and 89 because of tail-swing noise.

**Adopted value: 86 px/s² ± 1.5.** That gives a scale of 1/86 m/px.

## Pixel length (length.py, zoomed frames/nose.png and frames/tail.png)
The record's mask (bbox_w = 260 px) misses the pale, blue-tinted snout. At frame 24 its x0 is 1334, but the snout tip is visibly at about 1313.

My own measurement takes the leftmost differing column in the snout rows and the rightmost column of the tail tip. The median over all 54 frames is **282 px** (interquartile range 280–282). At frame 24 the zoomed frames confirm about 1313 to 1595.

## Answer
282 / 86 = **3.28 m**. The range is 3.23 (using 87.3 px/s²) to 3.36 (using 84 px/s²).

If you used the record's 260 px it would give 3.02 m, but that undercounts the snout.

Confidence: moderate-high, within about 4%.
