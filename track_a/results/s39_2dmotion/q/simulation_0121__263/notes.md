# q_263: speed of the left first ball at 1.0 s

- Question fps 30, so t = 1.0 s is frame 30. The file runs at 30.0075 fps, so I used frame indices, not the record's seconds. Speed = |p30 − p29| × 30.
- The asked object is ball1, the leftmost ball. It hits the row between frames 27 and 28. After that it drifts slowly left, about 15 px out by frame 54, then swings back. At frame 30 it moves about 0.9–1.0 px per frame.
- **Scale (2D video):** prior ball diameter 2 m = 163 px, so 0.01227 m/px.
  - The record's fixed-radius rim fit gives 163 px; its free-radius fit gives 162.7–162.8 px.
  - SAM masks of ball1: frame 30 gives horiz 166, vert 162, and an area-equivalent diameter of 163.2 px. Frame 29 gives 167 × 169 px (area-equivalent 166.1 px).
  - SAM is at most about 2.4 % above 163 px, so the two agree within 3 %. I kept 163 px because the rim fit is sharper than the SAM outline.
- **Ball1 x positions:**
  - Record track, frames 28–34: 637.48, 636.59, 635.56, 634.74, 633.81, 633.02, 632.07. y stays at 783.0.
  - The raw step from frame 29 to 30 is 1.03 px, which gives 0.380 m/s.
- **Smoothed estimate (`fit_speed.py`):** a sinusoid fitted to the post-impact pendulum swing (frames 29–79, RMS 0.09 px) gives a step of 0.949 px from frame 29 to 30, so 0.949 × 30 × 2/163 = **0.349 m/s**.
  - Local linear fits over frames 28–33 and 29–32 give 0.90–0.92 px/frame (0.33–0.34 m/s).
- **Second route (`leftedge.py`, my own measurement):** phase correlation of the ball1 image patch between consecutive frames.
  - Steps: −0.98 px (28→29), −0.87 px (29→30), −1.04 px (30→31), −0.91 px (31→32). The mean is about 0.92–0.95 px/frame, which agrees with the fit.
  - The left-silhouette-edge method gave 0.5–0.8 px/frame. It is biased because the threshold depends on the changing chrome reflections, so I rejected it.
  - My circle fit on the background difference (`measure.py`) took in the shadow and reflection, which pushed its y about 9 px too low (radius 73–80 px, noisy). I used it only as a rough check: about 0.94 px/frame over frames 29–39.
- **SAM centroids** of ball1: 636.4 (frame 29) and 635.1 (frame 30). That is a step of about 1.3 px, with mask-quantisation error of about 1 px. It agrees with the record within about 1.6 px in position.
- **Answer: 0.35 m/s.** The plausible range is 0.33–0.38. Confidence is moderate, because the motion is small (about 1 px per frame), so sub-pixel noise of ±0.1 px is about ±10 %.
