# Q736 – height of the chalkboard (m); prior: black cat speed = 0.714 m/s

fps 24 (file and question agree). Static camera; the board is on the back wall, which faces the camera head-on.

## Scale from the cat
- Cat body x-track (scene/tracks/cat.csv, frames 1–49; frame 0 has a rendering ghost). I fitted lines to torso_cx,
  cx_dark, cx_mask, nose_x and the torso ends: 8.90–9.00 px/frame, mean ≈ 8.93 px/frame = 214.3 px/s (`speed.py`).
- At the cat's depth: 0.714 / 214.3 = 0.003332 m/px.

## Perspective correction (cat is on the desk, in front of the wall)
- Vanishing point from 29 Hough lines on the ceiling tiles: (960.3, 539.0), so the horizon is at y = 539 (`vp.py`).
- Wall–floor line y = 950 (`prof.py`). The desk's base meets the floor at y ≈ 1030 (`under.py`). On the desk top,
  the rear edge is at y ≈ 735 and the front edge at y ≈ 763; the right edge's slant agrees with the VP (ratio 0.88–0.90).
- Cat paw contacts y ≈ 736–741, centre line ≈ 738.
- Planes: Z ∝ 1/(y − 539). So Z_cat/Z_wall = (224/491)·411/(738−539) = 0.942. Plausible range 0.92–0.96,
  depending on the exact front floor line and paw line.
- Wall scale = 0.003332 / 0.942 = 0.003537 m/px.
- Sanity check with this scale: camera height ≈ 411 px × 0.00354 ≈ 1.45 m, desk height ≈ 0.80 m, the desk
  rear is ≈ 0.25 m from the wall, clock ≈ 0.39 m. All plausible.

## Board size (`board.py`, column profiles)
- Outer frame from y 296.5 to 737: 440.5 px (green surface only: 315–716 = 401 px).
- I took the chalkboard object as board plus frame, which is how its bounding box would be measured:
  440.5 × 0.003537 = **1.56 m**.
- Alternatives: green surface only would be 1.42 m; with no perspective correction (one 2D scale) it would be 1.47 m.

Confidence: moderate. The main uncertainties are the depth ratio (±2%) and whether the reference includes the frame.
