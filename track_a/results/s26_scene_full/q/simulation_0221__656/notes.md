# q_656: diameter of the white fur carpet

The scene is a 2D top-down render at 24 fps (file fps and question_fps are the same, so no re-timing issue). The camera is static. Size questions do not depend on time.

## Scale (from the prior: vacuum diameter = 0.438 m)
- Vacuum outer-rim circle fit from scene/tracks/robot_vacuum.csv: 120.8 px at its resting place (650, 500), which is the position closest to the rug. I checked this on a 5x overlay at frame 77 (vac2.py): the green 120.8 px circle sits on the outer rim. A strongest-gradient fit (vac.py) lands slightly inside the rim at 118.6 px. Row and column profiles give an outer edge of about 121 px.
- Scale = 0.438 / 120.8 = 0.003626 m/px.
- Perspective: the vacuum's apparent size changes by only about 1.7% across the frame, which gives camera-height effects of about 0.5%. These are negligible.

## Rug
The rug is a round white fur rug at the bottom left. Its right part is hidden under the sofa and the bottom of the frame cuts it off. I fitted circles to the visible rim (left, top and bottom arcs, ray angles 100-306 deg) at frame 77:
- strongest gradient (rug2.py): D = 481.4-484.9 px, centre (438, 835), rms 2.9 px. Frames 0 and 40 give the same result (481-486 px).
- threshold crossings (rug3.py) at 25% / 50% / 75% of the edge contrast: 485.0 / 480.4 / 474.4 px.
- The overlays (frames/ov.png, frames/ov3.png) follow the rim all round the visible part. The record's box (~445 px) was a loose eye estimate, and I corrected it here.
- Value used: 482 px (outer fur edge, matched to the vacuum's outer-rim measurement).

## Answer
482 x 0.003626 = 1.748 m, which I give as **1.75 m**.
Second route: the threshold-based fit gives 480-485 px, which is 1.74-1.76 m. The uncertainty is about ±2%, mostly from the fuzzy fur edge. Confidence is fairly high.
