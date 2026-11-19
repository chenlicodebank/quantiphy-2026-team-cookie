# q2961: average speed of the sailboat (prior: sailboat length = 12 m)

- File rate is 24 fps (240 frames); question_fps = 30. Per the convention, the per-frame displacement is multiplied by question_fps (30).
- Measurement (`measure.py`, `track_own.csv`): the mask is min(RGB) < 200 with the watermark excluded, using the largest component, on all 240 frames.
  - Boat length (horizontal extent along the motion, bow to stern): bbox median 100 px, hull (bottom 15 rows) median 99 px. SAM 3 masks at frames 0/60/120/180/239 give 99/100/97/97/97 px (mean 98). These differ by less than 3 percent, so the length used is 99 px. Scale = 12/99 = 0.1212 m/px.
  - Motion: the boat moves steadily in +x and y stays constant. Centroid slope 1.4166 px/frame, mean |per-frame displacement| 1.412 px/frame, 5-frame-smoothed 1.411 px/frame. Bbox and hull-centre series give 1.410-1.418 px/frame.
- Second route: the SAM 3 centroid moves from 290.8 (frame 0) to 628.3 (frame 239), so (337.5/239) = 1.412 px/frame, which agrees.
  - Note: the SAM `track` output is corrupted (it jumps to other boxes) and was not used. The SAM `segment` checks agree with my own masks within about 1 px in centroid.
- Speed = 1.414 px/frame x 30 x 12/99 = 5.14 m/s. If the length is 98-100 px, the result is 5.09-5.20.
- Camera: the white background means a pan cannot be checked, so the speed is measured relative to the frame (as the annotators would have done).
- Confidence: good. The main uncertainty is the 24-vs-30 fps convention; at 24 fps the result would be 4.11 m/s.
