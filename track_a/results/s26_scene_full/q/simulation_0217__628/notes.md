# Q628: lampshade diameter (m)

The video is a top-down 2D Blender render at 24 fps (the file fps and question_fps agree). The camera is static.
The prior is the speed of the black cat, 0.94 m/s. I used one metres-per-pixel scale for the whole image.

## Cat pixel speed (measure.py)
- Mask: max(BGR) < 60, largest component. The cat walks along a straight line (+x).
- Centroid per-frame step: mean 10.93 px/frame, median 10.94.
- Linear-fit slope: 10.94 px/frame. Net centroid motion: 10.92 px/frame.
- Front edge: 10.98 px/frame. First half 11.02, second half 10.82, so the speed is effectively constant.
- Speed: 10.94 x 24 = 262.6 px/s, so the scale is 0.94 / 262.6 = 0.003580 m/px.

## Lampshade (lamp2.py)
- Mask: the white pleated shade, V > 110/130/150 and S < 60, with the largest outer contour filled. I checked
  frames 0, 24 and 49.
- Bounding box: x 1116–1265 (150 px). y 150–299 (150 px) at frames 24 and 49. At frame 0 a sun patch above the shade
  makes the top edge ambiguous.
- Other routes agree: minimum enclosing circle 150–151 px, equal-area diameter 147–149 px (the pleat tips make this
  smaller), centre (1191, 224.5).
- The record in scene/ (148 px, from a stricter threshold) agrees within 1.5 %.
- I used a diameter of 150 px (axis-aligned extent, tip to tip).

## Answer
150 px x 0.003580 m/px = **0.536 m**.

The second route, the equal-area diameter (148.5 px), gives 0.532 m.
The shade sits above the floor, so it is a little closer to the camera than the cat. Under the 2D single-scale
convention this is ignored. Confidence: good, within about 3 % under that convention.
