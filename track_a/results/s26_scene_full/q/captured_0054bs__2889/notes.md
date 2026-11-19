# q_2889: distance between the green and white balls at t = 1.0 s

Frame 24 (question_fps 24, the same as the file's rate). Green ball = scene `yellow_object` (a tennis ball). White ball = scene `grey_object`.
Size check: the green ball's width across the blur is about 39 px; at 1.331 m that is 6.8 cm, which fits a tennis ball. The white ball is about 50 px; at 1.235 m that is 8.1 cm.

## Centres at frame 24
Both balls are motion-blurred and overlap. The mask centroid of a blurred ball is its position at mid-exposure.
- **Green:** (325, 270). The track gives (324.9, 269.5). My own colour segmentation (`measure.py`) gives (325.1, 269.6). The midpoint of frames 23 and 25 is (324.3, 272.8).
- **White:** (380, 251).
  - The track gives (381.1, 249.9).
  - The midpoint of frames 23 and 25 is (378.5, 253.8).
  - My mask gave (375.0, 253.4), but it is biased: it picked up the dark rim of the green ball and missed the light top of the white ball (see `frames/mask24.png`).

## Geometry
- f = 0.5959 × 1280 = 762.75 px, principal point (640, 360).
- Each position = ((u − cx)/f, (v − cy)/f, 1) × depth, following the lab method card. The depth is taken as the depth-camera z value.
- Depths from depth_info: green 1.331 m, white 1.235 m.

## Result
- **Distance = 0.162 m.** Across the candidate white centres it ranges from 0.157 to 0.163 m.
- **Other reading of depth:** if depth_info is the Euclidean range (normalised ray × distance), the distance is 0.124 to 0.131 m. I chose the method card's (u, v, 1) × depth form.
- **Confidence:** moderate. The main uncertainty is the depth convention, not the pixel measurement.
