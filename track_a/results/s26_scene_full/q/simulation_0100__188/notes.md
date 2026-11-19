# Q188 — speed of the shark at 1.0 s (m/s)

2D simulation, fps = question_fps = 24, so t = 1.0 s is frame 24. Prior: the boat is 10 m long. I used one scale for the whole picture (single-scale 2D convention).

## Scale
- Boat length at frame 57 (whole hull visible): from the stern at x≈665 (`measure.py`, edge scan of rows 500–530) to the bow tip at x≈1518–1523 (rows 360–380, plus the diff-mask max of 1522). The record gives 859 px, which agrees.
- Scale: 10 m / 859 px = 0.01164 m/px.

## Shark motion
- `shark_track.py`: sub-pixel template matching of the frame-24 shark over all frames. It moves left at a constant speed from frame 2 on.
  - Fit slope over frames 2–57: −10.833 px/frame (residual 0.12 px).
  - Spans 12–36, 18–30 and 20–28 give 10.83, 10.83 and 10.81 px/frame.
  - The one-frame step at frame 24 is 10.86 px/frame.
- `measure.py` gives a second check with a different template window: 10.80–10.84 px/frame.
- The record's centroid fit (10.73) is a little lower. The mask centroid is noisier (it is affected by tail jitter), so I used the template value of 10.83 px/frame.

## Answer
Speed = 10.83 px/frame × 24 frames/s × 0.01164 m/px = **3.03 m/s**. Using the centroid value gives 3.00. I answer 3.02 m/s.

Confidence: high. The motion is uniform, and the main uncertainty is the boat's pixel length (about ±0.3%).
