# q82 – distance walker ↔ bike at t = 0.5 s (frame 12)

- fps 24 = question_fps, so t = 0.5 s is frame 12. 2D top-down view with a static camera, so one metres-per-pixel scale applies everywhere.
- Scale: bike length prior 1.7 m. In my own cyan mask at frame 12 the bike spans x 220–593 (374 px). The scene record gives 378 px (376–381 over frames 0–16). I used 377 px, so the scale is 0.00451 m/px.
- Bike origin = centre of the bike's bounding box: (406.5, ~642). The record's root_x is 406.5, and the cyan mask gives the same value.
- Walker pelvis = centre of the torso. Torso/shirt bbox centre from the record: (1090, 447.5). My own measurements were a whole-body centroid of (1084.6, 452) and a hair-region mean of (1088, 446). I took (1087, 444).
- The pixel distance is sqrt(680.5² + 198²) = 708.7 px, which gives **3.20 m**.
- Check: using the record's numbers only, sqrt(683.5² + 196.5²) = 711 px, × 1.7/378 = 3.20 m. Frames 11 and 13 give 2.95 m and 3.47 m, a smooth trend. The pelvis proxy is uncertain by ±10 px, which is about ±0.05 m.
- Confidence: good, roughly ±3%.
