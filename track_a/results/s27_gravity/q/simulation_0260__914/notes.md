# q_914: speed of the mug at t = 0.4 s

- This is a 2D scene: the mug falls straight down along x ≈ 1243 px. Both the file and question_fps are 30 fps, so t = 0.4 s is frame 12.
- The prior says the acceleration before 0.5 s is 9.8 m/s². The scale comes from fitting a parabola to the pixel free fall, frames 5-15. Contact with the table happens between frames 15 and 16.
- Re-measured in `measure.py`: the mask is the difference from frame 0, warm pixels only, cut at y = 869. The tracks agree with scene/tracks/mug.csv to within 1 px.
- Fit (`fit.py`): the pixel acceleration is 6.78-6.93 px/frame², so the scale is about 0.00157-0.00164 m/px.
  - Bottom edge: a = 6.93 px/frame², and the extrapolated rest point is frame 0.0, which means release from rest at frame 0.
  - Middle of the silhouette and the centroid: a = 6.81-6.87 px/frame², rest point at frame -0.2 to -0.3.
  - Top edge: a = 6.7, rest point at frame -0.5 to -0.7. The top is biased by perspective, because the mug's apparent height shrinks from 71 to 53 px as it falls.
- Speed at frame 12 is the backward difference (p12 − p11) × fps × scale. This equals g × (11.5 − t0_frame) / 30.
  - Bottom edge: 3.73-3.77 m/s.
  - Middle and centroid: 3.80-3.87 m/s.
  - Clean release at frame 0: 9.8 × 11.5 / 30 = 3.757 m/s.
- **Answer: 3.80 m/s**, between the release-at-frame-0 value and the centre-track value.
- **Second route:** the raw one-frame differences on each track agree with the fitted values to within 0.5%.
- **Confidence:** the answer is within about ±2% of every route.
