# q142: speed of the big bird (eagle) at 0.2 s
- 2D video, fps 24 (same as question_fps). t = 0.2 s -> frame 5. Both birds fly level at y ≈ 600 in the same plane, so one scale is used.
- Scale from the prior: the small bird (crow) moves at 11 m/s and its pixel speed is uniform. x0 goes 1603 (frame 2) -> 72/73 (frame 18), which is 95.7 px/frame. Template matching gives 95 px/frame.
  This gives 11 / (95.7 × 24) m/px.
- Eagle pixel speed. Its motion is uniform from frame 2 onward. x0 goes 1392 (frame 2) -> 142 (frame 10), which is 156.25 px/frame.
  At frame 5 the backward difference of x0/x1 is 157 px and body template matching gives 156 px.
- Speed = 11 × 156.25 / 95.7 = 17.96 m/s.
- Check: the record's tracks (scene/) agree with my own connected-component edges and template matching (measure.py). The per-frame values of 155–157 px give 17.8–18.0 m/s.
- Confidence: high, with an error of about ±1%.
