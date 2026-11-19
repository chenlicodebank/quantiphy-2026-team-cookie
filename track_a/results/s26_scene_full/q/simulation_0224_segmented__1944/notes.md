# q_1944 — speed of the red general chess piece at t = 0.5 s

- The only moving object is the cream piece sliding down the ramp trough (scene/ calls it "block"). Seen side-on it
  is a rounded rectangle about 81 px long, so it is the Chinese chess piece, with its diameter along the motion axis.
- fps = question_fps = 24, so t = 0.5 s is frame 12. The video is treated as 2D, as labelled.
- Scale: diameter 0.097 m = 81.3 px (median length along the main axis in scene/tracks/block.csv, range 79.6–83.6
  px), so 1.193e-3 m/px. Foreshortening along the ramp affects the size and the motion the same way, so it cancels.
- Timing: the video repeats frames (6, 13, 25, …) and skips some (5, 10, 23, …). In scene/notes.md each video frame
  is mapped to its render index, and with that mapping the steps grow smoothly, with constant acceleration of about
  1.00 px/frame². Video frame 12 shows render frame 13.
- Method (fit.py): fit s(render index) along the straight path with quadratic and cubic polynomials over 4 windows.
  - Backward difference at render frame 12: 11.1–11.3 px/frame, which is 0.318–0.323 m/s.
  - Directly measured step from render frame 11 to 12 (video frames 10 to 11): 11.04 px, which is 0.316 m/s.
  - If the reference instead used video frame 12 (render frame 13): 12.1–12.3 px/frame, which is about 0.351 m/s.
- Answer: 0.33 m/s. This is the original render-frame reading (0.322), nudged slightly towards the alternative
  reading. Confidence: moderate-high; the main uncertainty is which frame index the reference used (about 8% apart).
