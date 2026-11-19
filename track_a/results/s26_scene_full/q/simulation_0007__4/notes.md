# Q4: speed of the boat at 1.0 s (m/s)

- 2D top-down video with a static camera, 24 fps (file fps = question_fps, so no re-timing). t = 1.0 s is frame 24.
- Prior: boat length = 3.62 m. The scale is boat length in pixels along its axis. I re-measured it at frame 0
  (measure.py, crop.py, and zoomed crops):
  - hull tip to hull tip (upper-right (943.5, 667) to lower-left (755.5, 744)), projected on the axis (-22 deg): about 203 px.
  - including a thin stick/oar end sticking out past the lower-left end (to x = 747): 209.7 px. The mask extent at frame 0 agrees.
  - I can't tell whether the asset's bounding box includes the stick, so I used L = 207 px (within 1.6% of both values).
    That gives 0.01749 m/px.
- Speed in pixels (speed.py, from the scene track centroids, checked as constant velocity): a linear fit over frames 14-34
  gives 3.249 px/frame. Quadratic fits over frames 10-38 and 0-73 give 3.247 and 3.245 px/frame at frame 23.5. The raw
  one-frame backward step is 3.16 px/frame, which is segmentation noise (std 0.13 px).
- Speed = 3.249 x 24 x 3.62 / 207 = 1.364 m/s. Answer: 1.36 m/s.
- Range: 1.346 m/s (L = 209.7 px) to 1.389 m/s (L = 203.2 px). The second route (fits over different frame windows)
  agrees to within 0.1%.
- Confidence: good. The main uncertainty is about ±1.6% from which length definition the reference used.
