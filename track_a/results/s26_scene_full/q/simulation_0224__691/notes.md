# q_691: acceleration of the moving chess piece at t = 0.5 s

- The scene/ record's "block" is the Chinese chess piece, seen edge-on as it slides down the tilted board. It is the
  only object that moves. The file fps (24) matches question_fps (24), so the time base is t = frame/24, and t = 0.5 s
  is frame 12.
- Scale: the diameter is the piece's long extent along the slope. The record measured it at 81.5 px (background-subtraction
  mask, frames 0-38, range 80.2-82.7). I checked it by eye on a 6x zoom of frame 15 (about 80.5 px end to end).
  A brightness mask (size.py) gave 77 px, but it misses the shaded lower-left part of the piece (checked on
  frames/m15.png), so I did not use it. I used D ≈ 81.3 px, which gives 0.097/81.3 = 1.193e-3 m/px. The motion is
  along the same image direction as the diameter, so any foreshortening of the slope cancels out.
- Motion: s_along_ramp_px from the record (the path is a straight line, rms 0.2 px). The video has duplicated and
  skipped frames, so I fitted s against the record's source_frame_est/24 using only the non-duplicate frames
  (measure.py). Frames 10-12 are clean consecutive source frames.
  - Quadratic fit over frames 8-20 (around 0.5 s): 591 px/s², rms 0.25 px.
  - Frames 5-30: 586. Frames 3-24: 595. Frames 3-38: 580.
  - Cubic fits evaluated at 0.5 s: 598-606.
  - The quadratic fits all put the start of motion at t ≈ 0.01-0.03 s, which matches a piece starting from rest
    under constant acceleration.
- Adopted value: 590 px/s² × 1.193e-3 m/px = **0.704 m/s²**.
- Second route: the different fit windows and the quadratic vs. cubic models span 580-606 px/s², which is
  0.69-0.72 m/s². The uncertainty in the diameter adds about ±1.5%. A raw second difference at frame 12 is
  dominated by pixel noise (±1 px gives ±576 px/s²), so I did not use it.
- Confidence: fairly good, about ±4%.
