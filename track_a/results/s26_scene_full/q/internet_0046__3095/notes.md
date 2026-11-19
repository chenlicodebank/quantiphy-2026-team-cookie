# q3095: acceleration of the cup at 1.10 s

- Time base: the file and the question are both 30 fps, so t = 1.10 s is frame 33. The camera is static (scene record, caps move ≤3 px).
- Scale (internet convention, one factor): cup body height rim to base = 570 px (frame 33: top 305, bottom 875; median 569.5 over
  frames 27-34; checked on frame 33 with a grid). 10.5 cm / 570 px = 1.842e-4 m/px.
- Motion: the mug is pulled to the right and speeds up the whole time it is in view (frames 27-39 fully visible). There is no bounce or impact.

## Measurements (px/frame²)
- Body centre (record `ref_x`, re-checked with my own band profile in `edges.py`, slope 3.53). Local quadratic fits centred on frame 33:
  windows 31-35: 3.79, 30-36: 4.02, 29-37: 3.95, 28-38: 3.90, 27-39: 3.77. The raw 2nd differences at 33 are 3.5 (central) and 4.4 (forward).
- Left (trailing) edge, sharp step, own subpixel measure (`leftedge.py`) and strip template (`strips.py`): 2.9.
- Right edge strip, handle template, and interior texture: 4.4-5.1.
- The left/right disagreement is symmetric about the image centre: apparent width shrinks to its minimum near x≈960 and grows toward both
  edges (record widths 499 → 465 → 495). That points to lens/perspective stretch, so the left and right edge accelerations are biased in
  opposite directions and the centre cancels the bias. The interior texture is the privacy blur, which may not stay fixed to the mug.
- Adopted: centre ≈ 3.85 px/frame² × 900 = 3465 px/s² × 1.842e-4 = **0.64 m/s²**.

## Check
The left and right edge means average to (2.9 + 4.5)/2 ≈ 3.7 px/f², or 0.61 m/s², which matches the centre fits (0.63-0.67).
Confidence is moderate: the per-frame noise of the 2nd difference is large (±1 px/f², about 25 %), and the result depends on which
reference point the annotators clicked (left edge alone would give 0.48 m/s², handle 0.73 m/s²).
