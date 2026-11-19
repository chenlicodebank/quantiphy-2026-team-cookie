# q_375: speed of the ball at t = 0.5 s

- question_fps = file fps = 30, so t = 0.5 s is frame 15. 2D top-down pool table; the moving ball is ball 13 (orange stripe).
- Scale from prior: ball diameter 0.0757 m.
  - Own diff-mask (measure.py, median background, threshold 45, convex hull): 48 x 48 px at frames 14-16.
  - SAM 3 ("billiard ball", no box) frame 15: box 48.7 x 47.7 px, area 1847 px² (equivalent diameter 48.5 px); frame 14: box 47.4 x 48.0 px.
    A box-prompted SAM mask was bloated (98 px; it took in the felt) and was discarded after I checked the overlay.
  - Used D = 48.2 px, so the scale is 0.0757/48.2 = 1.571e-3 m/px.
- Position:
  - Own centroids: frame 14 at (1059.29, 505.28), frame 15 at (1031.39, 505.38). The backward step is 27.90 px.
  - SAM centroids: 1059.7 and 1030.9, a step of 28.8 px. That is about 3% off, which is within the ±0.5 px centroid noise of SAM's rough edges. The diff mask is cleaner.
  - Neighbouring clean steps: 28.0 (frame 14), 27.9 (frame 15), 29.0 (frame 16). Frame 15 is not one of the duplicated or skipped frames flagged in scene/notes.md (5, 9, 10, 11, 13, 17, ...).
  - Smoothed local step is about 28.0 px/frame.
- Speed = 28.0 px/frame x 30 fps x 1.571e-3 m/px = 1.32 m/s.
- Second route: the SAM centroid step (28.8 px) gives 1.36 m/s, and the raw single-frame step (27.9 px) gives 1.31 m/s. Both are within about 3%.
- Confidence: good (about ±3%). The main risk is the video's repeated and skipped frame timing, which does not touch frame 15.
