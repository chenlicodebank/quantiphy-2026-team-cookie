# q 3237 – displacement of the ball, 1.90 s to 2.00 s

- question_fps = file fps = 30, so the interval runs from frame 57 to frame 60.
- The prior is gravity (9.8 m/s^2), but the ball rolls flat across the floor in a top-down view. No fall or parabola is visible, so gravity gives no scale. The scale comes from the ball as a standard object: a regulation size-7 basketball is 0.24 m across (29.5 in circumference gives 0.239 m).
- Ball diameter: 256 px, the median blur-free vertical extent over frames 53–69 in scene/tracks/ball.csv (range 250–261). The mask overlays in frames/f57.png and f60.png confirm the ball sits at about x 1160–1430 (f57) and x 896–1150 (f60), which matches the record's centres.
- Scale = 0.24 / 256 = 9.375e-4 m/px. Planar, one scale, as the annotators did.
- Ball centre (scene record): frame 57 is cx 1294.1, cy 433.8; frame 60 is cx 1026.4, cy 436.0. The direct difference is 267.7 px.
- Second route: a linear fit of cx over frames 53–69 gives 90.9 px/frame in the record. My own independent mask (measure2.py, redness-based, less complete) gives 91.0 px/frame. A local fit over frames 55–62 gives 90.5 px/frame, so 3 frames is about 271–273 px. The vertical change is about 2 px, which is negligible.
- Adopted displacement: 270 px x 9.375e-4 m/px = 0.253 m. The direct reading gives 0.251 m and the fit gives 0.255 m.
- Sanity check: the speed is about 2.56 m/s, a plausible pace for a rolled ball.
- Confidence: moderate. The pixel displacement is good to about ±2%. The main uncertainty is the scale assumption, the ball's real diameter (0.23 m for a size 6 would give 0.243 m).
- Scripts: measure.py (overlay, rough mask that includes the shadow and blue line, not used) and measure2.py (independent slope check).
