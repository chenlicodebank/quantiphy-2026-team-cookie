# q_2933: length of the blue shopping bag (cm)

The file and the question both run at 24 fps. t = 1.4 s is frame 34. The bag is the `tote_bag` in scene/; it does not move.

## Pixel measurement (seg.py, frame 34)
- I made a navy mask (low V or blue hue), filled the holes, and removed the handle loop with a 9x9 opening. Overlay: frames/bagseg_34.png.
- The bag body is a parallelogram with corners L (774.5,315), T (826,296), R (891,347) and B (839,369.5).
  - Sides L-B and T-R (the opening/handle edge, which the "MARINE" text runs along) are about 80 px.
  - Sides L-T and B-R are about 55 px.
  - The whole mask including the handle has a min-area rectangle of 125 x 75 px.

## Scale
f = 763 px, and the bag's distance is 3.307 m.
- **Method card, no foreshortening correction:** the 80 px side gives 3.307*80/763 = 36.6 cm. The 55 px side gives about 24 cm.
- **Foreshortening-corrected (boardplane.py, bagsize.py):**
  - I fitted the floor orientation by requiring the board's 4-corner outline (frames 24-48) to back-project to a rectangle of constant size. The fitted normal is (-0.155, 0.784, 0.601). The board comes out at 80 x 64 cm, with an angle rms of 3.4 deg.
  - Check against the prior: the board's speed on this plane, averaged over frames 32-37, is 1.85 m/s against 1.934 m/s in the prior (4% off).
  - Projecting the bag corners onto a parallel plane through the bag centre gives sides of 39.5 / 40.3 cm (opening edge) and 34.4 / 33.9 cm.
  - Moving that plane by ±5 cm changes the sides by ±1.2 cm.
- A plane fitted only to the depth_info object centres is inconsistent (residuals up to 10 cm), so I did not use it.

## Answer
The length is the longer side, which is the opening edge: about 40 cm when corrected and 36.6 cm uncorrected. I answer **39 cm**, leaning towards the corrected value.
- With the handle included, the full extent would be about 54 cm uncorrected; I did not use this reading.
- Confidence is moderate (about ±10%).
