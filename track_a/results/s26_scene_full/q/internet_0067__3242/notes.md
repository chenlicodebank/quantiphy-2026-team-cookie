# Q3242 — width of the acorn (cm); prior: height = 8 cm

The object in this clip is an acorn-shaped toy with a black cap and a white body. The scene record calls it a "cup", but it is the same object. It is dragged from left to right across the floor and is fully visible only in frames 3–6. The clip is 2D, the camera is static, and fps = 30. One scale applies: 8 cm divided by the acorn's pixel height. Width is taken as the horizontal extent across the face of the acorn, which is also the direction of motion.

## Measurements (measure.py, measure2.py)
- The background is the median of frames 9–11. I computed the colour difference between each frame and that background.
- Height: I took the median difference over the central 160 columns and found the half-max edges at the top of the cap and at the bottom of the body.
  - Frame 3: about 995 to 1630, so about 635 px.
  - Frame 4: 1003 to 1647, about 644 px.
  - Frame 5: 1018 to 1670, about 652 px.
  - Frame 6: 1030 to 1700, about 670 px. The acorn gets closer to the camera over time, so it looks taller.
- Width: I used the half-max horizontal extent of the black cap, which is the widest part. Half-max cancels the motion blur. Rows 1120–1240 give:
  - Frame 3: about 550 px.
  - Frame 4: 521–541 px, mean about 535.
  - Frame 5: about 515 px.
  - Frame 6: about 565 px.
- Width-to-height ratio per frame: 0.87, 0.83, 0.79, 0.84, for a mean of about 0.83. That gives 8 × 0.83 ≈ 6.65 cm.
- Second route, from the scene record: half-max width of about 545 px over a bbox height of about 620 px gives 7.0 cm. Using the blurred bbox width (about 600 px) would give about 7.7 cm, but that width is inflated by motion blur.

## Answer
6.8 cm. This sits between my half-max measurement (6.65) and the record's value (7.0). Confidence is moderate: the strong motion blur makes the horizontal edges uncertain by about ±20 px.
