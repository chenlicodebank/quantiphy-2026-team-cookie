# q_2937 – height of the mario toy (cm)

- The file and question_fps are both 24, so t = 1.4 s is frame 34. The toy is static (the record calls it "teddy_bear": a brown plush
  lying on its back at the bottom centre, about (630, 623) px). It is the only toy, so it is the "mario toy".
- It lies on the floor, so its height (head to feet) is the long axis of its image outline (feet at the upper left, head at the lower right, arms spread).
- Script: `measure_mario.py`. The background (a smooth SAM2 gradient) is fitted with a cubic surface outside the toy box. The mask is
  |img - bg| > threshold, cleaned with open and close. The overlay is in `frames/mario_mask.png` and fits the outline well.
- The long-axis extent was measured on frames 30, 34 and 38, with thresholds 40, 60 and 90:
  - min-area rectangle: 117.3-118.6 px
  - PCA extent: 115.8-117.9 px
  - It is identical across frames.
- Scale (lab method card): f = 0.5959 x 1280 = 762.8 px, and the given depth to the toy is 2.016 m.
  H = 2.016 x L / f = 30.6-31.3 cm (min-rect 31.2, PCA 30.9).
- Answer: **31.1 cm**.
- Confidence: moderate. The main uncertainty is foreshortening, because the toy lies on a floor viewed obliquely.
  Its axis is mostly image-horizontal (about 20 deg), so the effect should be small. The prior (board velocity) is not
  needed for a size.
