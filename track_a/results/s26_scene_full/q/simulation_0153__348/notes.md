# Q348 — length of the blue car including the extending wire

Prior: tire diameter = 0.369 m. No depth_info. The file and the question both use 24 fps (time is not used here).
The car is a light-blue cart driving side-on at a constant depth (the ground contact stays at y≈947), so I used one
planar m/px scale taken from the tire.

## Tire diameter in pixels (circle.py, edges.py, blur.py)
- The edges are sharp (dark-to-floor transition over about 2 px), so there is no motion blur inflating horizontal extents.
- Rear tire, circle fitted to its outer edge at half-level: D = 108.1 / 108.2 / 108.2 px (frames 37/38/39).
  Frame 38 row 894: left edge 914.9, right edge about 1022 → about 107.5 px.
- Front tire: its left side merges with the fender shadow. The right edge at 1357.1 and the hub centre at about 1303.5
  (from the symmetric hub rings) give a radius of 53.6 → D ≈ 107.2 px.
- Adopted D = 107.8 px (±0.5). Scale = 0.369 / 107.8 = 3.423 mm/px.

## Length in pixels (extent.py)
- I took a background-difference mask (bg = frame 41 for x<930, frame 0 elsewhere) and checked it visually
  (frames/mask38.png). The "extending wire" is the thin rod that sticks up and back from the rear of the canopy. It is
  the left-most point of the car. The front-most point is the front tire.
- Frame 38: wire-tip half-level edge ≈ 805.5, front tire edge 1357.1 → 551.6 px. Frames 34/36: bbox 550/551 px
  (inclusive counts). The record's scene/cart.csv agrees (547–553 px over frames 31–41).
- Adopted L = 551.5 px.

## Result
L = 551.5 × 0.003423 = 1.888 m → **1.89 m**.

Second route: frames 34/36 (550/551 px) with the frame 37/39 tire fits (108.2 px) give 1.875–1.88 m. Using the front-tire
diameter alone (107.2 px) gives 1.90 m. Sanity check: height 483 px → 1.65 m and wheelbase 337 px → 1.15 m, which
are plausible for a utility cart.
Confidence: good (about ±2%). The main uncertainty is the tire's pixel diameter and whether the wire leans in depth
(a planar assumption is used).
