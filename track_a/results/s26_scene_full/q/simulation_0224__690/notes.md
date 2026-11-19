# q_690: speed of the moving chess piece at t = 0.5 s

- fps = question_fps = 24, so t = 0.5 s is frame 12. The only moving object is the flat Chinese chess disc
  sliding down the ramp channel (the "block" in scene/). Frame 12 checked visually (frames/f12.png).
- Scale: the disc's extent along the slope is its diameter, 81.5 px (median over frames 0-38, range 80-83).
  So 0.097 m / 81.5 px = 1.190e-3 m/px (one scale, 2D convention).
- Motion: s along the ramp (scene/tracks/block.csv). The file has duplicate and skipped frames, so I fit s against
  the record's re-indexed source frame with a quadratic (fit.py, frames 3-38 without duplicates, rms 0.8 px).
  Acceleration is about 0.69 m/s^2, so the motion is uniformly accelerated.
- Speed estimates at frame 12:
  - Backward difference on the fit at source frame 12: 0.321 m/s. At source frame 13 (the frame the video shows
    at index 12): 0.350 m/s.
  - Instantaneous derivative at frame 12: 0.336 m/s.
  - Raw file differences: f12-f11 = 0.366, f11-f10 = 0.320 (noisy because of the frame jitter).
- Answer: 0.335 m/s, which is within about 5% of both the frame-12 and frame-13 interpretations.
- Confidence: moderate-high. The scale is good to about 2%. The main uncertainty is the ±1-frame timing ambiguity.
