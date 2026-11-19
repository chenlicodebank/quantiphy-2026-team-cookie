# q_2936: width of the white box (cm)

The file rate and question_fps are both 24 fps. The "white box" is the small white drink carton that the scene record
calls `carton`. It sits still at about (517, 496) px for the whole clip, and its depth_info distance is 2.082 m at t=1.4 s.
The moving white board is the prior's object. The answer does not depend on it.

## Method
- The carton is static, so I averaged all 49 frames to reduce noise (`box_zoom.py`, `frames/box_zoom.png`). Its mask
  (`box_measure.py`, `frames/box_mask.png`) is identical in frames 10-48.
- The video is effectively 640x360 upscaled 2x: pixel rows and columns come in identical pairs. Edge precision is
  therefore about ±1 px.
- The carton lies on its side with its long axis running diagonally up-right. Three faces are visible: the white top
  face, the brown front end face and a thin grey right side face. Width is the shorter horizontal extent, which is the
  short edge of the top face (`edges.py`):
  - front edge (brown/white boundary): (491.5, 508) to (514, 513) = 23.0 px
  - back edge (top contour): (522, 464) to (543.5, 470.5) = 22.5 px
  - front bottom edge (rows 520-521, partly shadowed): about 22.2 px
  - mean is about 22.7 px
- Method card: width = d x px / f = 2.082 x 22.7 / 763 = 6.19 cm.

## Second route / checks
- Strict pinhole: the depth along the optical axis is Z = 2.082 / 1.029 = 2.023 m, which gives 6.02 cm for an edge
  parallel to the image plane.
- In the image the edge is tilted 5 px per 22.5 px, so it probably has a small depth component. Correcting for that
  foreshortening would give about 6.3 cm.
- Range: 6.0 to 6.3 cm. Answer: 6.2 cm, which matches the method-card value.
- Sanity check: a drink carton about 6 cm wide fits a 200-250 ml carton. Its length and height are heavily
  foreshortened in this view.
- I tried a floor-plane fit to the given depths, but the depths do not lie on one plane (residuals up to 11 cm, and the
  bin is 58 cm off the plane), so I did not use it.

Confidence: moderate. The ±1 px edge uncertainty is about ±4%.
