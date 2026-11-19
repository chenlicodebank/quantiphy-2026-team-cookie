# q_3002 — ball displacement 0.30 s → 0.40 s (prior g = 9.8 m/s²)

Time base is 50 fps (file fps = question fps), so t = 0.30 s is frame 15 and t = 0.40 s is frame 20.

**Positions** come from scene/tracks/ball.csv (mask centroids; the camera is static):
- Frame 15: (548.5, 330.4)
- Frame 20: (540.9, 606.1)
- Displacement: 275.8 px (vertical 275.7 px)

**Timing irregularity:** one source frame is missing every 5th output frame (the doubled steps at 7, 12, 17, 22 and 24). This looks like 60 → 50 fps. On a 60 fps source-frame clock the second difference is a steady ~2.5 px/frame². Frames 15 to 20 cover 6 source frames, which is 0.1 s at 60 fps, so the clip's real time matches the question's 0.1 s.

**Scale from gravity:** I fitted a parabola of y against source time (src/60) (fit.py).
- Frames 8–23: a = 8887 px/s² (rms 0.56 px), giving 0.304 m.
- Frames 13–21: a = 8698 px/s², giving 0.311 m.
- Frames 9–21: a = 8946 px/s², giving 0.302 m.

**Alternative conventions:**
- Naive 50 fps parabola fit over frames 8–23: a = 9473, giving 0.285 m.
- Mean naive second difference: about 3.09 px/frame², giving 0.35 m.
- Clean naive second difference only, 2.5 × 2500: gives 0.43 m. This ignores the dropped frames and is physically inconsistent.

**Sanity check:** the ball diameter is 76 px, so about 8.4 cm, which is plausible.

**Answer: 0.306 m** (physically consistent route). Confidence: moderate, because the annotators' handling of the dropped frames is unknown.
