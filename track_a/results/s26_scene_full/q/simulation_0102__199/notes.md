# Q199: length of the shark (m). Prior: shark acceleration = 1 m/s^2

This is a 2D scene. The shark swims left in the underwater panel at a constant apparent size, with no perspective. The video and the question both use 24 fps, so no re-timing was needed. I used one metres-per-pixel scale, taken from the shark's own pixel acceleration.

## Pixel acceleration (scale)
- `track2.py`: I template-matched the shark's front half (score > 0.95, sub-pixel peak) in frames 1–58, then fitted a quadratic to x(t). This gives **87.0 px/s²** (87.1, 86.8 and 87.0 over the windows 1–58, 1–30 and 30–58; rms 0.08 px). A linear fit of the per-frame speeds (the benchmark's speed-difference convention) gives 87.2 px/s².
- Second route (`check.py`, edges from `len2.py`): the nose edge gives 86.6, the tail edge 87.7 and the midpoint 87.4 px/s². The record's centroid ref_x gives 86.4.
- Result: 87.1 px/s² ≈ 1 m/s², so the scale is 0.01148 m/px. The shark starts with a non-zero speed (~7.5 px/frame), and its acceleration is constant.

## Pixel length
- `len2.py`: I took the background difference against scene/scripts/bg.png (empty-water noise p99 = 2). I used the column profile of the max difference, found the sub-pixel nose and tail-tip crossings, and repeated this over frames 2–56.
  The median length is 282.0 px at threshold 10 and 280.5 px at threshold 15. The tail beat changes it by only ±1 px.
- **Correction to the record**: scene/ gives a length of 247.8 px. That value misses the snout. The snout is rendered as a pale, semi-transparent ellipse (diff only 15–27), and the record's threshold of 60 plus a 5×5 opening cut it off. I checked this on the zoomed frame 20 (frames/clean.png): the outline runs to x ≈ 506, and the tail tip is at x ≈ 787.
- I used L = 280.5 px. The tail edge has high contrast, so a half-contrast edge would trim about 1 px.

## Answer
L = 280.5 / 87.1 = **3.22 m**. The range across thresholds and acceleration estimates is 3.19–3.25 m.
If I had used the record's 247.8 px, the answer would be 2.85 m. I rejected that value because it excludes the visible snout.
Confidence: good on the scale (all routes agree within 1%). The length depends a little on how the faint snout edge is defined (±1%).
