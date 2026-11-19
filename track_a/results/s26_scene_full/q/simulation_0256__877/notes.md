# Q877 – speed of tennis ball at t = 0.5 s

- 2D simulation, 24 fps (file fps = question_fps = 24, no re-timing). t = 0.5 s -> frame 12.
- Camera static (scene record bg shift < 0.11 px). Ball moves horizontally left -> right with a slight steady deceleration.
- Script `measure.py`: Lab b* mask (b* > median + 8), largest component, b*-weighted centroid per frame 6-39.
  I checked the crop at frame 12 (`frames/f12b.png`): the ball spans roughly x 395-431, y 346-380.

## Scale (prior: diameter = 0.17 m)
- Pixel diameter: bbox width/height median = 36 px; equivalent-area diameter median = 36.35 px; the scene record says 36 ± 1.
  Used 36.2 px -> 0.17/36.2 = 0.004696 m/px.

## Speed
- Backward difference from frame 11 to frame 12: 59.48 px/frame (the scene record's centroids give 59.45).
- Second route: a quadratic fit of x over frames 6-39 gives a velocity of 59.25 px/frame at frame 11.5, which matches.
- Used 59.4 px/frame × 24 = 1425.6 px/s × 0.004696 = 6.69-6.73 m/s, depending on whether the diameter is 36.2 or 36 px.

Answer: 6.71 m/s. Confidence: high. The main uncertainty is the pixel diameter (±1 px, about ±3 %).
