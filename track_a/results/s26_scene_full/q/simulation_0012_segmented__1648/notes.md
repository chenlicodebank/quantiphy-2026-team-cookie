# q_1648: width between the two widest eaves of the house (m)

Prior: bird speed = 6 m/s. There is no depth_info, so I treated the clip as 2D and used one metres-per-pixel scale taken from the bird.

## House (house.py)
- The house is the wooden building at the top of the frame, a static leftover from segmentation. Its two widest eaves are the
  slanted beams that form an inverted V at its bottom edge.
- To find the outer tips, I took the leftmost and rightmost non-white pixels in rows 600-700, on frames 0, 10, ..., 60.
  - Left tip: x = 400-404 (frames 0-20), then 419-420 (frames 30-60), at y about 660-675. This tip flickers because of segmentation noise.
  - Right tip: x = 1385-1387, at y about 650-659. It is stable.
- Horizontal span: 966-985 px. I used 976 px. The plank wall itself spans 930 px, which is narrower.

## Scale (speed.py, using scene/tracks/bird.csv body_mid_x/body_y)
- The bird's per-frame step changes with an ease-in/ease-out: about 7 px at the start, about 20.5 px while cruising, about 6 px at the end.
  - The video has 61 frames; total path is 969 px; mean step is 16.15 px/frame over 60 steps (15.6 px/frame if each of the two double steps counts as two source frames).
- Time base: the file is 22 fps and question_fps is 24. The two doubled steps show the clip was cut from other footage. I used 24 fps,
  the rate stated with the question, for the original timing.
- I took the prior to be the mean speed (the benchmark's average-speed convention): 16.15 px × 24 = 388 px/s → 0.0155 m/px.
- Answer: 976 × 0.0155 ≈ 15.1 m. I rounded to **15.3 m**, which splits the remaining readings below.

## Other readings (this is where the uncertainty is)
- 6 m/s as the cruise (peak) speed, 20.5 px/frame at 24 fps → 0.0122 m/px → 11.9 m.
- Mean speed at 22 fps → 0.0169 m/px → 16.5 m.
- 6 m/s as the average of a full Bezier ease-in/ease-out animation (peak/1.5) → about 17.9 m.
- The house may not be at the bird's depth. There is no data to correct for that.

## Confidence
Low to medium. Which speed the prior means sets the scale to within about ±20 %.
