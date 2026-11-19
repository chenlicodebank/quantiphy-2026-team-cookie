# Q375: speed of the ball at t = 0.5 s (m/s)

- The scene is a 2D top-down pool table. Only ball 13 (orange stripe) moves. fps = question_fps = 30, so t = 0.5 s is frame 15.
- **Scale.** Prior: diameter 0.0757 m.
  - My half-max (R−G) area-equivalent diameter of the solid balls 3 and 5 is 47.9 px (`diam2.py`). The record gives 48.4 px for ball 13 and about 48 px for the static balls.
  - I used 48.0 px, so 0.0757/48 = 1.577e-3 m/px.
- **Track.** I used `scene/tracks/striped_ball.csv` (centres ±0.5 px; overlays were checked in the record).
  - The video has duplicate and skipped frames (dups 5, 10, 13, 19, 26, 28, 35; double steps 9, 11, 17, 24, 27, 34, 37). From these I rebuilt the mapping from video frame to the underlying sim frame (`speed.py`).
  - Video frame 15 shows sim frame 14, and video frame 16 shows sim frame 15.
- **Speed at sim frame 15.**
  - Backward step 28.98 px/frame → 1.371 m/s.
  - Second route: quadratic and cubic fits of the sim-frame positions over windows 10–20, 8–22 and 12–18 give 28.96–29.14 px/frame → 1.370–1.379 m/s.
- **If the reference used the raw video frame 15 instead.** Its step is 27.90 px → 1.320 m/s, which is only 4 % lower.
- **Answer:** 1.372 m/s. Confidence: high. The uncertainty is about ±3 %, mostly from the pixel diameter and the frame-mapping ambiguity.
