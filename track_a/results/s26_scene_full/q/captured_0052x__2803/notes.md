# q_2803: basketball diameter (cm)

File fps = question fps = 24. The basketball doesn't move. Its bottom is cut by the frame edge (y = 720), so the size comes from the visible outline.

## Method (`measure.py`)
- Masked the non-green pixels in the crop x 720-900, y 590-720 and kept the largest blob (the basketball).
- Took its outer contour without the points on the bottom edge, and fitted a least-squares circle in every frame (0-48).
- Results were stable in every frame:
  - centre (801.5, 671.1)
  - fitted diameter 94.1 px; the contour follows pixel centres, so this is about 1 px generous
  - horizontal mask width 92 px
  - vertical: top 624 to centre 671 gives a radius of 47 px, so a diameter of about 94 px
- Overlay in `frames/fit.png`: the circle sits on the ball's outline. The sides look slightly flatter than a circle.
- I used about 93 px for the diameter.

## Scale
Lab method card: f = 0.5959 x 1280 = 762.8 px, depth of the basketball = 1.9365 m.
D = 1.9365 x 93 / 762.8 = 0.236 m.

## Checks
- Width route (92 px): 23.4 cm. Circle-fit route (94 px): 23.9 cm.
- If I use the axial Z instead of the ray depth (the ball is about 25 deg off-axis), I get 21.2-21.7 cm. I didn't use this, because the card says size = depth x pixels / f.
- A real size-7 basketball is about 24 cm across, which agrees.

Answer: 23.6 cm. Confidence: good, within about 3%.
