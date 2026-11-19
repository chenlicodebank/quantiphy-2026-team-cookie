# Q973: raccoon displacement from 0.5 s to 1.0 s

- 2D render at 24 fps (the file's rate and question_fps agree). t = 0.5 s is frame 12 and t = 1.0 s is frame 24. The camera is static.
- Scale: the prior gives a nose-to-tail-tip length of 1.51 m. The bbox width is 329 px at frame 12 (I checked tail tip x≈785 and snout x≈1113 on a zoomed crop, which matches the record), and its median over the clip is 328 px. So 1.51 / 329 = 0.004590 m/px.
- Displacement of the mask centroid from frame 12 to frame 24 is 272.2 px (dx 272.16, dy 3.55), which gives **1.249 m**.
- Checks:
  - bbox-centre displacement: 272.5 px, which gives 1.251 m.
  - Linear fit of the speed over the whole clip times 12 frames: 269.9 px, which gives 1.239 m.
  - Using the median length of 328 px for the scale instead gives 1.253 m.
- Answer: 1.25 m. Confidence is high, about ±2%. The main uncertainty is which pixel length matches the prior's 1.51 m; the record ranges from 324 to 333 px.
- Script: measure.py, which uses scene/tracks/raccoon.csv.
