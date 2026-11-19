# q_693 — acceleration of the moving chess piece at t = 1 s

- The "block" in scene/ is the Chinese chess piece: a disc lying flat on an inclined chessboard, which slides
  down-left. Seen from a low angle, its extent along the slope is its diameter. 2D scene, so one m/px scale is used.
  fps = question_fps = 24.
- Scale: the diameter along the slope is 81.5 px in the record (median of frames 0-38). My own check in size.py
  (difference against frame 44, threshold 60) gives 79.3-80.2 px. I used about 80.5 px, so 0.097/80.5 = 1.205e-3 m/px.
- Motion: the video has duplicated and skipped frames (see scene/notes.md). Fitted against the re-indexed
  `source_frame_est`, s(t) is quadratic with rms 0.4-0.9 px, so the acceleration is uniform. fit.py gives:
  - frames 3-38: 578 px/s²
  - frames 3-30: 590 px/s²
  - frames 10-38: 567 px/s²
  - frames 18-32 (around t = 1 s): 568 px/s²
  - frames 15-38: 561 px/s²
  Adopted value: about 570 px/s².
- a = 570 x 1.205e-3 ≈ 0.687 m/s². With the 81.5 px scale it is 0.68 m/s²; the window spread is about ±3 %.
- Raw single-frame differences at frame 24 are meaningless here because of the frame skip at 23 and the
  duplicate at 25. I used the constant acceleration of the uniformly accelerating slide instead.
- Answer: 0.685 m/s². Confidence: moderate to high, about ±4 %.
