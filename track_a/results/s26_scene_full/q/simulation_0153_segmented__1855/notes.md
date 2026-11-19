# q_1855 — acceleration of the blue car at t = 1 s

Time base: fps = question_fps = 24, so t = 1 s is frame 24. Acceleration = (speed(24) - speed(23)) x fps, using backward-difference speeds.
The scene is a 2D side view with one px→m scale taken from the tyre prior (0.369 m).

## Scale
`tire.py` measures the dark tyre pixels of the front tyre, which is clearly visible:
- horizontal extent through the hub row: 111–113 px (frames 30, 36, 41)
- vertical extent: 110 px (837→946)

Motion blur is negligible because the width is 113 px at 49.5 px/frame and 111 px at 43 px/frame.
I used D = 111 px, so the scale is 0.369 / 111 = 0.003324 m/px. The rear tyre merges with the dark wheel well, so I did not use it.

## Acceleration (px/frame²)
Single backward differences at frame 24 are noisy: marker 0.67, front hub 1.04, rear hub 0.36.
The acceleration decreases smoothly over these frames (≈1.3 at frame 19 → ≈0.4 at frame 28), so I fitted local polynomials to the positions.
I then evaluated x(24) - 2x(23) + x(22) on each fit (`fit.py`), using the scene's template tracks:
- marker: 0.745 (fits over frames 17–31 and 16–34, cubic or quartic)
- front hub: 0.74
- wheel midpoint: 0.785–0.79
- quadratic fit over frames 20–28: 0.63–0.67

Second route (`check.py`): I matched my own sill + front-wheel template (from frame 26) with sub-pixel NCC. Its fits give 0.69 (frames 18–30, cubic) and 0.745 (frames 16–34, quartic).

Adopted value: 0.74 px/frame², which gives 0.74 x 576 x 0.003324 = **1.42 m/s²**.
The plausible range is about 1.3–1.5 m/s², depending on the fit window.

Confidence: moderate. The local acceleration changes from frame to frame, and the scale assumes the tyre and the origin are at the same depth (planar).
