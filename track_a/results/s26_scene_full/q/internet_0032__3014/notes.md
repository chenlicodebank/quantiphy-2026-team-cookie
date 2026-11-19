# q_3014: boat distance traveled from 2 s to 4.5 s

- Time base: question_fps is 30 and the file runs at 29.85 fps, almost the same. Frames are 60 to 135 (at 29.85 fps they would be 60 to 134, which changes the result by under 1%).
- Track: scene/tracks/boat.csv, hull-box centre `cx_hull`. I checked it on zoomed frames (view.py, frames/f60.png and frames/f135.png): the bow and stern sit at about 672 and 897 px in frame 60, and at about 553 and 790 px in frame 135. Both agree with the track. The camera is static.
- Pixel distance (measure.py):
  - Net displacement is 112.5 px.
  - Path length is 113.8 px raw, 112.8 px with a 5-frame smooth and 112.5 px with a 9-frame smooth. The raw value includes mask jitter.
  - A linear fit gives 1.50 px/frame × 75 frames = 112.6 px.
  - I use 112.5 px. The motion is a straight line, so path length equals net displacement.
- Scale: the prior is a boat length of 3.5 m, measured bow to stern in pixels. The boat approaches the camera, so its pixel length grows from 224 to 235 px over the interval, with a mean of 230.6 px. The median over the whole clip is 232 px.
  - With the interval mean: 3.5 / 230.6 m/px gives **1.71 m**.
  - Other choices: the clip median gives 1.70 m and frame 0 (212 px) gives 1.86 m.
- Confidence: moderate-high. The main uncertainty is which frame the annotators measured the prior's pixel length on, about ±5%.
