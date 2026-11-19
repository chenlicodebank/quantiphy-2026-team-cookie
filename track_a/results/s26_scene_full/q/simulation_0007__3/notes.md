# Q3 – minimum distance from the pier's outer end to the boat at t = 3 s

- 2D top-down render, static camera, 24 fps (file fps = question_fps, so no re-timing). t = 3 s → frame 72.
- Interpretation: "minimum distance" is the closest-point gap between the pier's outer end and the boat hull.
  I did not use the origin-to-origin distance.
- Scripts: `measure.py` and `measure2.py`. Both segment bright, low-saturation pixels; the pier mask is limited to its
  over-water part, and contours are filled. Overlays are in `frames/ov72*.png` and show clean masks.
- Pier water part: minAreaRect 84 × 180 px, angle −23.5°. Outer-end corners are (506.6, 685.0) and (583.8, 651.5).
- Boat at frame 72: centroid (625.3, 787.7), same as `scene/tracks/boat.csv`.
- Minimum contour-to-contour gap = **105.7 px**, from pier point (562, 661) to boat point (604, 758).
  - Check 1: brute force on the full masks with a distance transform gave 104.3 px.
  - Check 2: from the end corner or the end midpoint to the nearest hull point gave 106.5–106.8 px. All agree within about 2 px.
- Scale from the prior, boat length 3.62 m:
  - PCA mask length is 210.1 px at frame 0, which includes the bright stick at the bow tip.
  - It is 206.0 px at frame 36 and 204.5 px at frame 72, because the tip falls into tree shadow.
  - I used 207.5 ± 3 px, giving 0.01745 m/px.
- Answer: 105.7 × 0.01745 = **1.84 m**. The range is 1.82 m (210 px) to 1.87 m (204.5 px).
- For comparison, the origin-to-origin distance from the pier end midpoint to the boat centroid would be 143.8 px = 2.51 m.
- Confidence: good for the gap interpretation, about ±3%. The main risk is how the question is read.
