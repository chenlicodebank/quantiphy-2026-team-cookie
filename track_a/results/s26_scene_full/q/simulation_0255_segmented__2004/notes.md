# q_2004: acceleration of the tennis ball at t = 1 s

- 2D segmentation video, 24 fps (question_fps is also 24), static camera, one ball moving horizontally to the right and slowing down evenly. There are no bounces.
- Tracking (`measure.py`): soft-mask weighted centroid in every frame (0–40), saved in track_mine.csv. y is constant at about 564.3 px.
- Pixel acceleration (x is quadratic in the frame number):
  - global quadratic fit: −0.2666 px/frame², residual 0.19 px
  - cubic fit evaluated at frame 24: −0.2655
  - local quadratic fits around frame 24 (±5, ±8, ±12 frames): −0.2627, −0.2624, −0.2662
  - first half / second half: −0.2699 / −0.2648
  - Taken value: −0.2665 px/frame² × 24² = −153.5 px/s².
- Diameter (`diam.py`): vertical bbox extent 25 px; soft-mask equivalent diameter 24.99 px; vertical profile FWHM 24.76 px. Taken value: 25 px, so the scale is 0.17/25 = 0.0068 m/px.
- Acceleration = 153.5 × 0.0068 ≈ 1.044 m/s² (a deceleration; the magnitude is reported).
- Second route: the scene record's mean second difference (about −0.28 px/frame²) gives about 1.10 m/s². That value is the noisy mean of single-frame differences; the fits are steadier and agree within about 1.5%.
- Confidence: high. The main uncertainty is the diameter (about ±2%).
