# Q1502 – height of each window frame (prior: width = 1.48 m)

File fps = question_fps = 24. The windows are part of the static backdrop (a flat photo of a facade), so the
answer is a ratio: H = 1.48 m x (pixel height / pixel width) of the same window. depth_info (bird, neon sign) is
not needed, because both extents lie on the same plane at the same depth.

## Measurements (frame 40, central facade, 5 columns x 4 rows of windows)
Scripts: measure.py, profile.py, prof2.py, opening.py, lintel.py. Crops: frames/c3.png, c4.png, c5.png.
- Height: very consistent across all windows and rows, 164-166 px from the top of the opening (dark
  lintel-shadow band) to the lit sill. Row-to-row variation is under 2 px, so the photo's upward perspective has
  negligible effect.
  - The frame proper starts below the lintel-shadow band (frame head bar at y≈65 in the top row), which gives
    ≈155 px.
- Width:
  - Opening read on the lintel band and by eye: ≈118-124 px, median about 121.
  - Including the visible side reveal: ≈127-130 px.
  - Outer edges of the frame proper: ≈120 px.

## Readings
| reading | H px | W px | H/W | height |
|---|---|---|---|---|
| dark outer rectangle incl. reveal | 165 | 128 | 1.29 | 1.91 m |
| opening (lintel shadow to sill) | 164 | 121 | 1.355 | 2.01 m |
| frame proper (head bar to sill) | 155 | 120 | 1.29 | 1.91 m |

Check: the lit window at the bottom has the same width as its neighbours (661-786 px vs 659-785 px); its
173 px height includes glow.

## Answer
1.93 m, a compromise between the 1.91 and 2.01 m readings. Confidence: moderate, because it is not clear which
edges count as the "window frame". The spread of the readings is about ±4 %.
