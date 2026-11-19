# Q2102 – average moving velocity of the picked bottle (cm/s)

Prior: the picked bottle is 11.7 cm tall (the tall clear perfume bottle with a metal neck). The convention is 2D with one scale.

## Scale
- In frame 0 the neck top is at y≈1183–1190. The base is hidden behind the pink bottle. A drift-compensated difference against frame 18 (`diff0.py`, `frames/diff0.png`) puts the base at about 1800–1820, so the height is about 625–637 px. Lifted frames 5, 7 and 8 in the record give 628, 635 and 638 px.
- I used 637 px: 11.7 / 637 = 0.01837 cm/px (±2%).

## Time base
The file is 19.59 fps and question_fps is 25. The odd rate 19.594595 (725/37) suggests the clip was re-timed when it was cut. I used 25 fps (the original footage). Both rates give a plausible hand speed, so this choice is the main risk: at 19.59 fps every answer below is ×0.784.

## Motion
The record's `tracks/bottle.csv` was read by eye. I spot-checked frames 0, 7 and 17 on zoomed crops and the base and neck positions agree within about 20 px. The lift starts at frame 2 and the bottle leaves the top of the frame by about frame 17. The camera drifts about 1% of the travel (a correction of about +1%).

Net displacement per frame, ×25 fps × scale:
- centre, frames 2→14: 1160 px / 12 frames → 44.4 cm/s
- neck top, frames 2→14: 1174 px / 12 frames → 44.9 cm/s
- base, frames 0→17: 1672 px / 17 frames → 45.2 cm/s
- base, frames 2→17: 1652 px / 15 frames → 50.6 cm/s (window running to the last partly visible frame)
- centre, frames 0→14: 38.6 cm/s

The speed rises through the lift, so the answer depends on the window. Over the moving, fully tracked phase, the routes give 44–45 cm/s, or about 45.4 cm/s after drift correction. The window that runs to the exit frame gives about 50.

**Answer: 46 cm/s.** Confidence is moderate: about ±10% from the window choice, plus the fps ambiguity.
