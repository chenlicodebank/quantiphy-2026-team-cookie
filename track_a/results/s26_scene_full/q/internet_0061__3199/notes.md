# q3199 – gap between the acorn's bottom and the chair surface at 1.80 s (cm)

## Geometry and time base
- The clip is rotated 90°, so gravity points toward the image's **+x (right)**. After the acorn bounces off the seat at frame 45, its
  x-motion is a clean parabola. The apex is at frame 52 (x≈732) and x accelerates by about 35 px/frame² back toward +x. Meanwhile y
  drifts at a nearly constant ~37 px/frame (horizontal motion). Free space can only reverse the motion like this under gravity.
  The grey mesh is the backrest. The tan region to the right is the seat ("chair surface"), with the seat/back rail at x≈1300-1340.
- fps 30.013 (file) vs 30 (question): a 0.04 % difference, which is negligible. t = 1.80 s → frame 54.

## Measurements (pixels)
- Acorn bottom (its rightmost edge, toward gravity) at frame 54: ≈937 px (scene bbox x1 = 933; zoomed crop `frames/e54.png`
  shows the dome edge at 935-940).
- Chair surface: the acorn next lands between frames 57 and 58. At frame 58 its rightmost edge is at x≈1320 (`frames/e58.png`,
  scene x1 = 1320), on the rail between the mesh end (≈1300) and the tan seat (≈1340). Surface line = 1320 ± 15.
- Gap = 1320 − 937 ≈ **383 px**.
- Gravity in pixels (`fitg.py`, quadratic fit of the x position during free flight):
  - fit over frames 47-57: 31,000 px/s²; over 48-56: 31,200; over 47-55: 33,300; over 49-57: 28,800
  - hull centroid (`track2.py`) and bbox edges give the same range
  - throw arc 39-45: 32,100 px/s²
  - adopted: a = 31,000 px/s²
- Scale = 9.8 / 31,000 = 3.16e-4 m/px. This gives an acorn ~220 px ≈ 7 cm across, which is plausible.

## Answer
383 px × 3.16e-4 m/px = 0.121 m → **12.1 cm**.

## Second-route check
Kinematics from frame 54 use v = 76 px/frame (central difference) and a = 34.5 px/frame². The time to cover 383 px is ~3.0 frames,
so landing would be at ~57. The observed contact is at 57-58, which is consistent. Spread of the result: a = 28,800–33,300 px/s²
gives 11.3–13.0 cm, and the surface line ±15 px adds ±0.5 cm. Confidence is moderate, about ±8 %.
