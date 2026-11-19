# q_657: length of the white sofa (m)

Prior: vacuum diameter = 0.438 m. Top-down 2D view, static camera, so one m/px scale is used. fps 24 = question_fps; time does not matter here.

- Vacuum diameter: the scene record gives 120.7-120.9 px near x 650-1100, the same image region as the sofa. My own edge profiles at frame 77 (measure_vac.py) give 120 px vertically; horizontally it is 116-121 px, depending on whether the inner or outer rim edge is picked. I used 120.8 px, so the scale is 0.438/120.8 = 3.626e-3 m/px.
- Sofa length (its long axis is horizontal in the image): measure_sofa.py takes the strongest edge on each row, frame 0. The widest rows are y 760-800: left edge 565.5, right edge 1451.5, so the extent is 886 px. This matches the record's loose box of about 885 px.
- Raw result: 886 x 3.626e-3 = 3.21 m.
- Perspective check: the vacuum's apparent diameter grows by about 2 px at the far right of the image (side-wall effect). This suggests h/Z is about 0.005 for the vacuum, so the camera is high (FOV about 20 deg). The sofa's widest outline sits above the floor, at roughly arm height, and its side walls may add about 1-2% to the measured width. A corrected value would be about 3.16 m.
- Answer: 3.19 m, between the raw and corrected values. Confidence: good, about ±3%.
