# Q3289 - distance between the two players at 4.50 s

**Time base:** the file runs at 23.976 fps but was made from a ~30 fps source by dropping every 5th frame (see the scene
notes). So real time = file frame / 23.976. With question_fps = 30, t = 4.50 s would be frame 135, which is past the end
of the clip (122 frames). I therefore used file frame 108 (t = 4.5045 s), which matches the real time.

**Scale (2D, top-down drone view):** at frame 108 the court lines (scene/tracks/court_lines_per_frame.csv) are
1253.90 and 337.05 px, so the court is 916.85 px wide (line centre to centre). That gives 6.1 / 916.85 = 0.006653 m/px.
Check: the court length is 2023.3 px, which is 13.46 m at this scale (regulation is 13.41 m, 0.4% off), so the view is
close to planar.

**Player positions at frame 108** (checked on zoomed crops, frames/far.png and frames/near.png):
| reference point | far player | near player | px | m |
|---|---|---|---|---|
| body-mask centroid (scene record) | (847.5, 605.4) | (959.7, 2021.0) | 1420 | 9.45 |
| hips / shorts (by eye) | (830, 622) | (950, 2022) | 1405 | 9.35 |
| feet, where the shadow meets the body (by eye) | (825, 652) | (965, 1978) | 1333 | 8.87 |

Each player leans, and the drone's perspective pushes their heads away from the image centre. As a result the body
centroids sit about 90 px further apart than the feet.

**Answer: 9.2 m.** I don't know which point the annotators clicked (body centre or ground point), so the answer sits
between the routes: about 3% from the centroid value and about 4% from the feet value. All the routes agree on
8.9-9.45 m.

**Confidence:** moderate-high. The scale is reliable to about 1%. Most of the uncertainty is the choice of reference
point (about ±3%).
