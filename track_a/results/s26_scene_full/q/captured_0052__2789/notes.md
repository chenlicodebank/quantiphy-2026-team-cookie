# q_2789 — distance trashbin to shoe (m)

File fps = question fps = 24. Both objects are static (scene/static_measure.json: identical at frames 0/24/47).

Method (lab card): f = 0.5959*1280 = 762.75 px, principal point (640,360). Each centre is back-projected
along its unit ray, scaled by its depth_info distance (bin 2.977 m, shoe 2.231 m at t = 1.0 s), and then the
3D Euclidean distance is taken.

Pixel centres were measured in code (measure.py, frame 24, overlay frames/masks.png):
- Bin: blue mask bbox 680-775 x 483-591 (the scene record's value; my mask at frame 24 bled left to x=672
  onto the dark region beside the bin). bbox centre (727.5, 537). The mask centroid (726, 528) sits higher
  because the bin is wider at the top.
- Shoe: white mask bbox 253-314 x 626-678, centre (283.5, 652). Centroid (283, 654).

Results:
- bbox centres (bin 727.5/537, shoe 283.5/652): 1.559 m
- my mask bbox centres: 1.556 m; mask centroids: 1.569 m
- ±5 px shifts of either centre: 1.539 to 1.573 m

Answer: 1.56 m. Confidence is good (about ±2 %). The main uncertainty is where the annotator clicked the
centres; the depths are given.
The prior (yoga-ball velocity) is not needed, because depth_info sets the scale directly.
