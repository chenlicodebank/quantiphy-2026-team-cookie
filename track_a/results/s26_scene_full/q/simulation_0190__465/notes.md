# q465: speed of the box at t = 2 s (frame 240)
- "The box" is the brown cardboard box on top of the truck. The prior gives its width as 1.33 m. Its horizontal extent on screen is 281 px (my gradient edges: 806.4 to 1087.2; the record says 281.5). The scene is 2D, so the scale is 1.33/281 = 0.004733 m/px.
- The box moves straight up. I tracked it with sub-pixel template matching (reference frame 240) over frames 200-280, using three regions of the box.
  - Slope at frame 240: 0.2067, 0.2070 and 0.2052 px/frame from a quadratic fit; 0.198 to 0.208 from a linear fit over +-10 frames.
  - The acceleration is nearly zero.
- Second route: the dy track in scene/tracks/cardboard_box.csv gives 0.2115 px/frame over frames 230-250. That is about 2% higher.
- I used 0.207 px/frame: 0.207 x 120 fps x 0.004733 = 0.1176 m/s.
- fps is 120 for both the file and the question.
- Confidence: good, within about 3%. The main remaining uncertainty is whether the 1.33 m width is the box's horizontal extent as seen on screen (that is the assumption here).
