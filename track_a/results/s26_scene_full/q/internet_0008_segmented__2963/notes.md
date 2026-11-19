# q 2963: speedboat length (m). Prior: sailboat length = 12 m

The file runs at 24 fps and question_fps is 30. Time does not matter for this size question.

- The speedboat is the scene record's `bottom_object`: a small dark boat near the bottom edge, fully in frame from file frame 184 to 239.
- The sailboat is the large maroon ketch.
- Method: internet planar convention with one scale = 12 m / sailboat pixel length.
- Measurement (`measure.py`): mask is min(RGB) < threshold, then connected components.
  - The extents do not change for thresholds 120 to 230, so the edges are sharp.
  - Sailboat overall length is 98-103 px, median about 100. The record's hull-only length is about 98.
  - Speedboat length is 39-42 px. Median is about 41 over frames 184-239, from both my frames and `tracks/bottom_object.csv`.
- Answer: 41 / 100 × 12 = 4.92 m.
  - Using the hull length of 98 px instead gives 5.02 m.
  - I answer 4.92 m. Confidence is moderate: there is about ±3% pixel jitter.
- Caveat: the speedboat is lower in the frame, so it is likely closer to the camera, which would make its true size smaller. The annotation convention ignores perspective, so I did not correct for it.
