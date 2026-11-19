# q187 — speed of the boat at 1.0 s (m/s); prior: boat length = 10 m

2D video, 1920x1080, file fps 24 = question_fps 24 → t = 1.0 s is frame 24. Single px→m scale from the boat length.

## Measurements (own code: measure.py, extent.py; background-difference masks vs. a clean plate stitched from frames 0/57)
- Motion: the boat translates purely horizontally at a constant rate. Sub-pixel bow edge (mean over rows 400–600):
  linear-fit slope over frames 2–57 = 17.877 px/frame; span (57−1)/56 = 17.878; per-frame steps around frame 24
  are 17.82–17.96 (noise ±0.05). Backward difference at frame 24: 17.955 (raw); the motion is uniform, so I use 17.877.
- Length, stern to bow (max over rows; bow tip is at row ~360, stern bulge at row ~520):
  frame 24: 72–932 → 860 px (th 20) / 74–932 → 858-859 (th 40); frame 40: 362–1218 → 857; frame 57: 666–1522 → 857.
  Adopted 858.5 ± 1.5 px. (My first pass in measure.py used rows 380–640 and missed the bow tip at row 360, which gave 854.
  The row-wise check in extent.py fixed that.)
- SAM 3 (segment "boat"): frame 24 horiz 860 px (box 73.1–933.0), frame 23 horiz 861 px, frame 57 horiz 857 px. That is
  within 0.3 % of my value. Box shift 23→24: x0 +17.8, x1 +17.8 px. Agrees with the bow-edge track. The record in scene/ (859 px,
  17.876 px/frame) also agrees.

## Result
scale = 10 m / 858.5 px = 0.011648 m/px
speed = 17.877 px/frame × 24 fps × 0.011648 = 4.998 m/s → 5.0 m/s

Second route: SAM box edges (frames 23→24, 17.8 px/frame, length 860 px) give 17.8×24×10/860 = 4.97 m/s.
Raw single-step backward difference at frame 24 gives 17.955×24×10/858.5 = 5.02 m/s. All routes give 5.0 ± 0.03.
Confidence: high.
