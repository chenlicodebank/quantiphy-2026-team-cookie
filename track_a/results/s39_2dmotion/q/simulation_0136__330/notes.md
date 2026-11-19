# q_330 – speed of the cup at t = 2.25 s (simulation_0136, 2D)

File fps = question_fps = 24, so t = 2.25 s -> frame 54. Speed = |p(54) - p(53)| x 24.
Camera is static and looks straight down: the blue tapered cup lies on its side and moves left to right.
At frames 52-57 the cup is cut off by the right image border (at frame 54 about 80 of its 122 px width is visible),
so the centre cannot be read off directly as a bbox centre. The scene/ record's cx_est for frames 52-57 is only a
linear extrapolation (24.6 px/frame), and its x0 column there differs from my masks by about 25-30 px, so I did not use it.

## Scale (prior: cup diameter = 0.087 m)
- Diameter = width at the mouth (widest horizontal extent of the lying cup's silhouette) on upright, fully visible frames.
  My HSV mask, frame 26: bbox width 122 px (frames 7-28: 120-124). SAM 3, frame 26: horiz 124 px (box 125.4).
  They differ by 1.6 %, under 3 %; SAM outlines are usually about 1 px wider on each side. Used 122.5 px -> 7.10e-4 m/px.

## Displacement of the cup from frame 53 to frame 54 (scripts in this folder)
1. Left edge at mid-height (edges.py, integer HSV mask, mean of rows 620/650/680): 1821.7 -> 1844.0 = 22.3 px.
   Sub-pixel version (subpix_edge.py, rows 600-700): 22.6 px. Frames 44-52 with the same measure: 24.3-25.3 px/frame,
   which matches the full-silhouette centre (25.0 px/frame), so the edge follows the centre while the cup is fully visible.
   The bottom-left corner moves 24 px and the top-left corner 15 px, because the cup's tilt is easing.
2. SAM 3 masks on frames 53 and 54 (sam_edges.py): mean left edge over rows 600-700 is 1820.65 -> 1843.69 = 23.0 px.
   This is within 3 % of route 1. The overlay (frames/seg_02_f54.jpg) covers the visible cup correctly.
3. Template pose fit (fit_pose.py / fit_pose_fixcy.py): the upright silhouette from frame 26 is rotated and shifted
   to match the visible part of the mask. Result 53 -> 54: dx = 20.9 px (cy free: 20.93 px including dy).
   The fit has a systematic problem: the tilted cup is not just a rotated template (the tilt is partly out of plane,
   with IoU 0.93-0.95), and with cy free it drifts 5 px even though the mask's top and bottom stay at y = 518/779.
   On frames 51-53 it also reads 1-1.5 px below the edge routes. So it is a lower bound rather than the best value,
   but the cup's apparent width may shrink as the cup straightens, which would make the true centre slightly slower
   than the edge.
- Frame 55 is unreliable because the mask picks up a blue reflection in the cooktop trim (checked on a zoomed strip,
  frames/strip.png). Physically the centre leaves the smooth cooktop for the counter at about frame 52-53, and the
  cup slows from the steady 24.6-25 px/frame it had on the cooktop. That fits 21-23 px/frame at frame 54.

## Answer
Used 22.0 px/frame, weighted toward the edge routes (22.3-23.0) with the pose fit (20.9) as a lower bound:
v = 22.0 x 24 x 0.087 / 122.5 = 0.375 m/s (the range of the routes is 0.356-0.392 m/s).
Confidence: moderate, roughly ±5 %. The main uncertainty is where the centre is on the partly visible, tilting cup.
