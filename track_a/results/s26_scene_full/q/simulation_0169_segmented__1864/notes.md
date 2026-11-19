# Q1864: speed of the astronaut at t = 3 s

- This is a 2D video at 24 fps (file rate and question_fps agree). t = 3 s is frame 72.
- Scale: in my own segmentation (measure.py: min RGB < 225, largest blob, PCA axis), the astronaut is 91.4 px from head to feet. This is stable across the clip (bbox height at f0 is 90 px, upright). With the 2.2 m prior that gives 0.02408 m/px.
- Reference point: the mask centroid, used as the pelvis proxy. The pose is rigid.
- Raw backward step at f72 is 1.700 px/frame. The neighbouring steps are 1.88 (f71) and 1.74 (f73).
- Local polynomial fits of x(t) and y(t) around f72, evaluated as p(72) - p(71), give 1.65 to 1.71 px/frame depending on the window (5-10 frames, degree 2-3). That is 0.954 to 0.986 m/s.
- Second route: from the record's centroid, (cy70 - cy73)/3 = 1.77 px/frame centred at f71.5, and the bbox centre gives about 1.6 px/frame. Both are consistent.
- Answer: about 1.69 px/frame × 24 × 0.02408 = **0.975 m/s**.
- Confidence: moderate-high. The object is decelerating near its stop, and centroid jitter adds roughly ±3%.
