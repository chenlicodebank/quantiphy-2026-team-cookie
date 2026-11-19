# q_2807 – width of the book (cm)

The book is the static white box/card in scene/ (about (666,612)). It lies flat on the floor, with its long axis tilted
about 60 deg in the image. The file rate equals question_fps (24). t=0.4 s is frame 10. The book does not move
(its mask is identical in frames 5-47).
Scale: book depth 2.082 m (depth_info), f = 0.5959 x 1280 = 763 px, principal point (640,360). The trashbin velocity
prior is not needed for this size.

## Measurements (book.py, geom.py, profile.py)
- Top-face mask (gray threshold 175-190, frame 10). Quad corners are about (630,588), (668,577), (700,634), (661,650).
  Short edges are 39.6-43.9 px and long edges 65-71 px. The min-area rect is 43.7 x 72.6 px. A grey strip on the
  lower-left long side is the book's thickness face; it is not part of the width.
- 50 pct-crossing profiles across the short dimension: median 44 px. This includes part of the thickness strip on
  the left, so the top-face width is about 41-44 px.

## Route 1 (lab method card): 2.082 x px / 763
- 41.8 px -> 11.4 cm; 43.7 px -> 11.9 cm; 44 px -> 12.0 cm.

## Route 2 (floor-plane back-projection, foreshortening corrected)
- Floor plane fitted through the book centre (2.082 m, about 1 cm above the floor), the basketball centre (2.925 m,
  R about 0.13 m) and the cup centre (2.516 m). Result: tilt about 35 deg, roll under 1 deg, camera height 1.68-1.72 m.
- Back-projecting the quad corners onto the top face gives short edges of 10.7-11.4 cm (threshold 175/190) and long
  edges of 19-20.5 cm. With the profile crossings it gives 11.8 cm, which includes the side strip.

## Answer
Width (the shorter horizontal extent of the face) is about 11.3 cm. The routes span 10.8-12.0 cm.
Confidence: moderate, about ±5 pct. The main uncertainties are edge blur and the thickness strip.
