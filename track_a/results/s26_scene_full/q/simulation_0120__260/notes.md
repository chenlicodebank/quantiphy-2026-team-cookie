# q_260 — side length of the chessboard (m)

Prior: robot cleaner speed = 1 m/s. No depth_info. Top-down static-camera Blender render, treated as 2D (one m/px scale
from the prior object, per convention).

## Time base
File fps 24.007839, question_fps 24.0 — differ by 0.03 %, irrelevant (201.8 vs 201.7 px/s).

## Vacuum pixel speed (scene/tracks/robot_vacuum.csv, checked)
Straight horizontal motion along y≈811.5, constant speed. Linear fit of centre x over unoccluded frames 0–32:
8.401 px/frame; all frames 8.410; mean per-frame step 8.415 (all) / 8.407 (f1–32).
Speed = 8.405 px/frame × 24.0078 = 201.8 px/s ⇒ scale = 1/201.8 m/px = 4.955 mm/px.
Sanity: vacuum disc 68.8 px → 0.341 m (typical robot vacuum ~0.33–0.35 m), table 167 px → 0.83 m.

## Chessboard pixel side (measure_cb.py, measure2.py, frame 0)
It is a 10×10 board (the record's "8x8, 10.6 px squares" is wrong; the 85 px outer size is about right).
- Outer edges from max-profiles (white squares vs grey table): x 467.5→550.5 = 83.0 px; y 530.5→614.3 = 83.8 px.
- Second route: square period from dark-square edges: 8.30 px (x), 8.35 px (y) → 10 squares = 83.0 / 83.5 px.
Adopted side = 83.4 px.

## Answer
83.4 px / 201.8 px/s × 1 m/s = 0.413 m.
Caveat: the board lies on the table top, slightly nearer the camera than the floor-level vacuum, so a perspective-
corrected true size would be a few % smaller; the 2D one-scale convention is followed. Confidence: good (±3 % on
the pixel measurements).
