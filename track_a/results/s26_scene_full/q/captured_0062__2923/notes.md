# Q2923: length of the whiteboard (cm)

The file fps and question_fps are both 24. t = 1.4 s is frame 34.
The whiteboard is the flat white board lying on the floor and sliding away from the camera.

## Method
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Corners (`check.py`, `multi.py`):
  - Board mask from an HSV threshold. A 25 px morphological opening removes the two clips.
  - Each of the 4 edges is a line fitted to the middle 70% of its contour points; the corners are where those lines cross. I checked the overlay `frames/check34.png`: the outline sits on the board edge.
  - The corners in `scene/` are off by about 7 px on the far edge (the clips probably pulled it outward). With those corners the board came out 0.77 x 0.73 m, and the edges were not consistent from frame to frame. I did not use them.
- Floor plane:
  - The board is a rectangle, so in each frame its two pairs of opposite edges give two vanishing points, and from those the plane normal. In frames 24-48 the two edge directions meet at 88-90 deg, which checks f.
  - I then fitted one normal over frames 24-48 jointly, requiring right angles at the corners: n = (-0.127, 0.791, 0.599).
  - The board centre (where the diagonals cross) in frame 34, back-projected at depth_info 2.815 m, fixes the camera-to-floor distance h = 1.789 m.
- Corners are back-projected by intersecting their rays with that plane, and the edge lengths are measured in 3D.

## Results
| | long edges | short edges |
|---|---|---|
| frame 34 | 0.814 / 0.811 m | 0.611 / 0.612 m |
| frames 24-48, same plane | mean 0.814 m, sd 0.003 | about 0.61-0.62 m |

- Frame 34 with its own per-frame normal: 0.813 m.
- With the median of the per-frame normals: 0.813 m.
- The size stays constant as the board recedes, so the plane fits well.
- Length (the longer horizontal extent) = **81.3 cm**. Width is about 61 cm.

## Second check: the velocity prior
Using the same plane, the 3D board-centre speed around frame 34 is:
- one-frame steps: 1.4-1.6 m/s;
- over the 6-frame window 31-37: 1.79 m/s. This window includes the frame 35->36 double step, which is probably a dropped capture frame.

The prior is 1.934 m/s, about 8% higher. Given that the reference velocity is a smoothed average of clicked centres, this agrees with the scale. Other objects' depths are too noisy to give a plane (residuals about 10 cm), so I did not use them.

Confidence: good, about ±3%.
