# Q727: length of the teacher's table (m). Prior: chalkboard length = 5 m. No depth_info.

Answer: **2.29 m**

## Time base
fps = question_fps = 24. The table is static, so the time base does not matter.

## Objects
- Teacher's table: the long light-wood desk under the left half of the board. The cat walks on it.
- Chalkboard: framed green board. Its outer frame runs x 320.1 → 1693.4, which is **1373.4 px**.
  The green surface alone is 1328.9 px.
- Both are static. Measured on frame 49 with sub-pixel Sobel edges (`final.py`).

## Pixel measurements (`final.py`, `enh*.py`, `floor.py`)
- Front edge of the table-top slab: x 71.6 → 772.1, which is **700.5 px**. The front panel below the slab is 93.5 → 751.9 (658 px).
- Front edge of the table top: y = 762.1. Back edge of the table top: y ≈ 742–745.
- The front panel meets the floor at y = 999.6 (checked on a raw crop: wood floor below it).
- The wall–floor line is at y = 951.8 (right side, x 1780–1880).

## Perspective (the scene is not a flat 2D plane)
The camera is level, with its principal point near the image centre. Two separate checks agree:
- Top surface: (742−540)/(762−540) gives Zfront/Zback ≈ 0.91.
- The right-side corners converge toward x = 960: (960−787)/(960−772) ≈ 0.92.

Floor contacts give the relative depths of the board and the table:
- The wall (the board's plane) meets the floor at y = 951.8.
- The table's front panel meets the floor at y = 999.6.
- So Z_tablefront / Z_wall = (951.8−540)/(999.6−540) = **0.896**. The table front is about 10% closer to the camera than the board.

## Result
- Scale at the board: 5 / 1373.4 = 0.003641 m/px. The outer frame is taken as the board's bounding box.
- L = 700.5 px × 0.896 × 0.003641 = **2.285 m**.

## Cross-checks and sensitivity
- Back edge: about 647 px at Z_back ≈ 0.97 Z_wall gives ≈ 2.29 m, consistent.
- A naive 2D scale that ignores perspective would give 2.55 m. This was rejected: the table clearly stands in front of the wall.
- If the 5 m referred to the green surface only, the answer would be 2.36 m.
- Using the front panel only (without the slab overhang) would give 2.15 m.
- Confidence: moderate, about ±5%. The main uncertainties are which board extent the 5 m refers to and the floor-line rows (±2 px, about 0.6%).
