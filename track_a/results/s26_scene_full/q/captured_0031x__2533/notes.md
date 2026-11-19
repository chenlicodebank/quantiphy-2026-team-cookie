# q_2533 — width of the table (cm)

File fps = question_fps = 24, so t=1.6 s is frame 38. Lab camera: f = 0.5959*1280 = 763 px, c = (640, 360).

## Method
- `edges.py`, `geom.py`: on frame 48 (the yellow ball is gone), the table-top silhouette was fitted with sub-pixel lines:
  left/right side edges (rms 0.14/0.19 px), back edge (0.5 px), and the front top edge (the top/front-face luminance step, 0.26 px).
  Corners: BL (574,424.3), BR (849.8,428.0), FL (463,482.6), FR (962.6,494.9).
- Vanishing point of the side edges (front-back direction) = (717, 349). The left-right direction comes from the front/back edges
  under the constraint that it is orthogonal to that VP direction. Together these give the table-plane normal. Back-projecting the
  corners onto the plane at camera height h gives a rectangle: front edge 3.569h, back edge 3.571h (the two agree, so the model is
  self-consistent); left side 4.41h, right side 4.52h (mean 4.47h).
- Scale h (`scale.py`): for each on-table frame 0-42, the tennis ball's distance from its pixel diameter (D = 6.7 cm) was matched to
  the ray/plane model with the ball centre r = 3.35 cm above the top. Result: h = 0.168 (median at rest), 0.1658 (median while
  rolling), 0.1675 (median of all frames). The per-frame values agree from 1.70 m down to 0.95 m.
- Check against depth_info at frame 38: with the labels as given (tennis 1.19 m, white 0.994 m), the implied h is 0.192 from the
  tennis ball and 0.143 from the white ball, which contradict each other. With the labels swapped (tennis 0.994 m, white 1.19 m),
  h is 0.1659 and 0.1673, which agree with each other and with the diameter route. Image geometry backs the swap: at frame 38 the
  yellow ball's contact point is lower in the image (closer) than the white ball's. Its diameter also gives 0.95-1.0 m, not 1.19 m,
  and a white ball at 1.19 m would be 3.9 cm (a ping-pong ball), against 3.3 cm at 0.994 m. So the depth labels seem swapped.
  Either way, h is about 0.167 m.

## Result
- h = 0.167 m → left-right extent = 3.570 x 0.167 = 0.596 m; front-back extent = 4.47 x 0.167 = 0.746 m.
- Width = the shorter horizontal extent = **59.6 cm** (left-right, across the front). Under the other reading (front-back depth
  as "width") it would be about 74.6 cm.
- Second route (method card): the back edge is 275.8 px long. The tennis ball rests right at the back edge (f0-14) at a distance of
  1.704 m (from its diameter), so the back edge is 1.704 x 275.8 / 763 = 0.616 m. Using the front edge (499.6 px) at the depth the
  plane model gives for the front edge (~0.91 m) also gives about 0.60 m. The two routes agree within 3%.
- Confidence: about ±2-3% from the scale h (0.1658-0.168, i.e. 59.2-60.0 cm) and the corner positions.
