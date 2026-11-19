# q_1698: width of the rock (m)

Prior: eagle length = 0.8 m. depth_info: eagle at 100.14 m (t=1 s) and 99.52 m (t=2 s). question_fps = 24, file fps = 25
(no timing is needed for a size).

## Scale
- The eagle flies left to right, almost parallel to the image plane (its depth changes only 0.6 m in 1 s). Its length
  (beak to tail) therefore lies along image x.
- Horizontal mask extent on white-background frames 0–20 (scene/tracks/bird.csv bbox_w): 23–31 px, mean about 26 px.
  Side-view crops (frames 18, 27, 30, 45; `crops.py` -> frames/eagle_tiles.png) show a body line of about 24–27 px.
  I took L = 26.5 px.
- f = 26.5 x 100.1 / 0.8 ≈ 3316 px, which gives a horizontal FOV of about 16.5°.
- This is the only route available: there is just one reference object, so the focal length cannot be cross-checked
  against a second one.

## Rock (`measure.py`, bird-free frames 54–72)
- Silhouette x 328–959 (cut off at the right image edge), y 24–310.
- PCA extents: 630 px along the main axis, 276 px across it. Vertical extent 286 px.
- The camera sees the rock's snowy top from above. The short image extent therefore mixes the foreshortened
  front-to-back depth with the rock's height.
- For a flat rock seen from 45–60° elevation, the front-to-back extent works out to about 280–310 px. I used 300 px.
- The rock's depth is not given. I assumed it is about the eagle's depth (about 100 m); the eagle passes just in front
  of its lower part.
- Width ≈ 300 x 100 / 3316 ≈ 9.0 m. Other readings: 276 px gives 8.3 m and 350 px gives 10.6 m. The length is
  ≥ 19 m.

## Confidence
Low to moderate. The main uncertainties are the rock's depth (assumed equal to the eagle's), the foreshortening of the
front-to-back extent, and the eagle's pixel length (±10%).
