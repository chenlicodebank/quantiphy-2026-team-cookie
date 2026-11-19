# Q513: droplet speed at t = 0.1 s

- 2D clip, static camera, fps = question_fps = 60, so t = 0.1 s is frame 6. Frames 0–6 come before the duplicate/missing-frame
  anomaly described in scene/notes.md (video frame 7 duplicates frame 6), so that anomaly does not affect this answer.
- `measure.py` re-measures the drop: full-resolution background difference against frame 13 (threshold 18, close/open,
  largest contour filled). The centroids agree with scene/tracks/drop.csv to within about 0.5 px.
- Scale comes from the prior a = 9.7 m/s². Pixel acceleration from a quadratic fit of frames 0–6 is 31.67 px/frame²,
  which is 114,000 px/s², giving 8.51e-5 m/px. The per-frame second differences are 32.5, 31.1, 31.3, 31.6 and 32.8
  (mean 31.9).
- Speed at frame 6 is the backward difference |p6 − p5| × 60 × scale:
  - Raw step 176.4 px gives 0.900 m/s.
  - The same difference on the fitted quadratic gives 0.897 m/s.
- Check: free fall from rest at frame 0 gives 5.5 × a / 60 = 0.889 m/s. Using the mean second difference (31.9) gives
  0.895 m/s. All routes fall between 0.889 and 0.900.
- Answer: 0.897 m/s. Confidence is high (within about 1–2 %).
