# q_3040: width of the swimming pool (m)

The prior is "height of the swimming woman = 1.63 m". The video is a top-down drone shot that I treat as planar, with one scale factor (internet convention). No times are involved, so the difference between fps 22.52 and question_fps 24 does not affect the answer.

## Pool width (px)
The pool is the strip between the top deck edge and the bottom deck edge. The swimmer swims along it in x; the long axis runs out of frame. The width is the vertical extent of the water.

`edges.py` finds, column by column, the step in the (G−R) "teal-ness" profile in 480-px column bands, for frames 0, 40, 80, 120 and 163:
- Top water edge: about 176–192 px. The edge tilts slightly, from about 176 at the left to about 191 at the right.
- Bottom water edge (where the water meets the grey bottom coping): about 2063–2071 px.
- Bands without glints and splash give a width of 1876–1888 px. Zoomed crops (frames/top.png, frames/bot2.png) confirm about 185 and about 2067 at x ≈ 1000–1500.
- The dark band from y ≈ 1850 to 2060 is wall shadow on the water, not deck.

**Width = 1880 ± 8 px.**

## Woman's height (px)
I used head-to-toe length in stretched glide frames, read from zoomed gridded crops:
- f123: toes at x ≈ 1715, top of head (hair) at x ≈ 2440, about 725 px. The body is almost horizontal (Δy ≈ 40, which is negligible).
- f162: toes at x ≈ 2000, top of head at x ≈ 2690, about 692 px.
- f82: feet at about 1415, head at about 2100 (partly blurred), about 690 px.
- The scene record's glide-frame head_to_toe values are 690–730 px, which agrees.

**Height = 710 px**, taken as the middle of these readings.

## Result
- Scale = 1.63 / 710 = 0.002296 m/px.
- Width = 1880 × 0.002296 = **4.32 m**.
- Sensitivity: using a height of 690 px gives 4.44 m; 730 px gives 4.20 m.

Second route: the scene record states an edge-to-edge distance of about 1900 px and glide lengths of 690–730 px, which give 4.2–4.5 m. This is consistent with my measurement.

Confidence: moderate. Most of the uncertainty is in the swimmer's pixel height, about ±3%.
