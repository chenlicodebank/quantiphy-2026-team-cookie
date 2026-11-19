# Q649: length of the wooden bench (m)

Prior: the vacuum is 0.438 m in diameter. Scene: a 2D top-down render with a static camera, 24 fps (file and question rates are the same). I used one m/px scale taken from the vacuum.

## Bench (the orange slatted bench at the top left, long axis along x)
- `edges.py`: I took column profiles of HSV saturation on frame 72, in three row bands (y 185-215, 215-250, 250-285), and found the half-level crossings.
  The left edge is at x ≈ 294.3 and the right edge at x ≈ 582.5 in every band, so the **length is 288 px**. The width is y 172.5-289, about 116.5 px.
- `measure_bench.py`: a mask gives the robust x extent 294-584 (290 px) and the same result on frames 0, 40, 72 and 79 (the bench is static).
  The scene record's 288 px (295-583) agrees.

## Vacuum scale
- The scene CSV's circle-fit diameter is 122.9 px near the dock (x≈1670) and 120.9 px at the end (x≈650), mean 121.4.
- `vac_check.py`: half-level profiles across the top surface give a vertical diameter of 120.0-120.2 px. Horizontally, the side away from the image centre shows the vacuum's side wall, which adds up to about 2.5 px at the dock.
- I used 121 px, the bbox-like diameter near the bench's side of the image: 0.438/121 = 3.62e-3 m/px.

## Answer
288 × 0.438 / 121 = **1.04 m**. The range over the possible diameter choices (120.1-122.9 px) is 1.026-1.050 m, about ±1.2%.
Second route: the scene record's own extents (288 px with the mean diameter of 121.4 px) give 1.039 m. Confidence: high (about 2%).
