# q3258: cup displacement from 2.30 s to 2.50 s (cm)

- **Time base:** I used 30 fps. The file's rate (30.013) and question_fps (30.0) differ by only 0.04%, so 2.00 s, 2.30 s and 2.50 s are frames 60, 69 and 75.
- **Camera:** essentially static (background drift of a few px, against motion of 70-95 px/frame), so I made no correction.
- **Prior scale:** the prior is the acceleration from 2.00 to 2.30 s, 0.32 m/s². I fitted the pixel acceleration with quadratics over frames 60-70:
  - body centre over frames 62-70/72/75: 1429-1439 px/s²;
  - right (leading) edge over frames 58-72: 1350-1477 px/s²;
  - finite difference of the right edge, v(69) − v(60): 1500 px/s².
  - I adopted 1430 px/s², giving a scale of 0.32 / 1430 = 2.24e-4 m/px.
- **Displacement, frames 69 to 75:**
  - body centre: 501.5 px;
  - leading edge: 509 px;
  - trailing edge: 494 px (490 px from my own re-detection in band y 780-840).
- **Answer:** 501.5 px × 2.24e-4 m/px = 0.112 m = **11.2 cm**.
- **Check:** I re-ran the edge detection myself (diff against frame 100, band y 780-840). It agrees with scene/tracks/mug.csv to within 4 px at frames 67-72. The upper band (y 600-660) was unreliable and I discarded it.
- **Spread:** the answer ranges from 10.7 to 11.8 cm depending on which point and which acceleration estimate is used. The main uncertainty is the pixel acceleration (about ±5%).
- **Confidence:** moderate to good.
