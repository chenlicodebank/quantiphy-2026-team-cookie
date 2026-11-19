# q_692: speed of the moving chess piece at t = 1 s (m/s)

Prior: the diameter of the Chinese chess piece is 0.097 m. 2D sim, 1920x1080. File fps = question_fps = 24, so t = 1 s is frame 24.
The "white block" in scene/ is the chess piece: a disc lying on the tilted board, seen almost edge-on. It is the only moving object.

## Scale (pixel diameter)
- The silhouette's long upper edge runs at 25.2° (shape_dirs.py). The path runs at 25.9°. The piece's face ellipse
  has its major axis (the unforeshortened diameter) along the motion, so the motion is in a plane facing the camera.
  One scale is valid.
- Diameter = extent along the long axis, with each end at half of the local contrast in |frame - frame44|. Frame 44
  is a clean background, with the piece gone from the board. halfmax_len.py on 14 frames (12-33) gives
  **78.2 px (sd 0.3)**. There is no trend with speed, so there is no motion blur.
- Other readings and why I did not use them:
  - The record's 81.5 px and my own low-threshold (diff > 40) mask's 81.5 px include the blurred rim.
  - The diff > 90 threshold gives 78.0 px.
  - SAM 3 ("cream colored piece", frames 23 and 24) gives length_px 86.9 and along-slope 86.9. That is 11% more.
- Zoomed check (frames/cmp_f24.png, frames/zoom_24.png, frames/zoomdiff_24.png): the SAM outline runs about
  1-2 px outside the piece at both ends, taking in the dark channel rim and shadow. The half-contrast edge is the right one.
- Scale: 0.097 / 78.2 = 1.2404e-3 m/px.

## Motion (fit_speed.py)
- Track: scene/tracks/block.csv centroids. Checked against SAM 3 masks:
  - Frame 24: SAM (959.0, 662.3) vs record (958.8, 662.0).
  - Frame 23: SAM (981.1, 651.5) vs record (980.8, 651.2).
  - The 23→24 step is 24.6 px (SAM) vs 24.53 px (record). Agreement is under 1%.
- The video has duplicated and skipped frames (record: skip into 23, duplicate at 25). Against the record's
  source_frame_est, s(t) is a smooth quadratic: a = 1.006 px/frame² (0.72 m/s²), rms 0.8 px. A cubic fit has rms 0.4 px.
- Two readings of "frame 24":
  - A: render frame 24 on the smooth trajectory, backward difference: 0.694 m/s (quadratic), 0.698 (cubic),
    0.702 (local quadratic on source frames 21-27).
  - B: video frame 24, which shows render frame 25. The raw step 23→24 is 24.53 px, giving 0.730 m/s.
    The smooth backward difference at render frame 25 is 0.724.
- Answer **0.71 m/s**, between the two readings: about 2% from A and about 3% from B.
- Second-route check: the SAM centroid step 23→24 (24.6 px) gives 0.732 m/s, which matches reading B.
  The speed of the uniformly accelerating fit agrees with the raw steps around this time (20.8 px at frame 22,
  24.7 px at frame 26).

Confidence: the diameter is good to about ±1.5%. The main uncertainty is the ±2.5% from the frame-timing ambiguity.
