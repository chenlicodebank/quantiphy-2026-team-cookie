# Q3240: velocity of the acorn at 0.17 s (m/s)

The object called "cup" in scene/ is the acorn: a black cap over a white body, pulled from left to right by a cord. The camera is static (the background drifts 3 px or less).
Time base: the file and the question are both 30 fps. t = 0.17 s maps to frame round(5.1) = 5.

## Measurements (measure.py: background = median of frames 9–11, difference mask, half-max column extent of the dark cap)
- Cap centre x (full-res px): f3 695, f4 1233, f5 1966, f6 2842. The scene record gives 703, 1240, 1962, 2833, which agrees within about 10 px.
- Acorn height (top of the cap to the bottom of the body): 626 px at f5, 626 at f4, 650/648 at f3/f6 (blur). The scene record gives 604–644. I used 620 px, so the scale is 0.08/620 = 1.29e-4 m/px.

## Velocity
- Forward difference at frame 5 (the internet-video annotation convention): p6 − p5 = 876 px (record: 871) → about 873.5 px × 30 = 26,200 px/s → **3.38 m/s**.
- Cross-checks: the backward difference (p5 − p4 = 733 px) gives 2.84 m/s, and the central difference gives 3.11 m/s. The acorn is accelerating, so these readings differ. I answer with the forward difference, which is the stated convention.
- With a height of 626 px instead of 620, the answer is 3.35 m/s. Height uncertainty is about ±3%.

Confidence: moderate. The main risk is whether the annotators used the forward or a central difference.
