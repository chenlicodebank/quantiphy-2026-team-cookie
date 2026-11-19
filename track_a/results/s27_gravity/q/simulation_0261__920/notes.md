# Q920: speed of the mug at t = 0.625 s

- 2D simulation, 24 fps (the file and the question use the same rate). t = 0.625 s is frame 15.
- Prior: the mug falls with a = 9.8 m/s² before 1 s, i.e. before the impact between frames 18 and 19.
- Track: scene/tracks/mug.csv (centroid cy and bbox centre). The steps grow uniformly. `fit.py` fits a quadratic to frames 1-18:
  - centroid: a = 8.833 px/frame², max residual 0.6 px, start of motion at frame -0.10;
  - bbox centre: a = 8.839 px/frame².
- Scale: 9.8 / (8.833 × 24²) = 0.001926 m/px.
- Speed at frame 15 (backward difference): the centroid step 14→15 is 129.0 px, giving 129.0 × 0.001926 × 24 = 5.96 m/s. The fitted step is 128.98 px, also 5.96 m/s.
- Check:
  - From the bbox centre: 5.96 m/s.
  - Pure kinematics, 9.8 × (14.5 + 0.1)/24 = 5.96 m/s.
  - The top and bottom edges are noisier (5.88-6.04 m/s).
- Sanity: at this scale the mug body diameter is about 0.16 m and its height about 0.17 m. That is somewhat large, but the prior is exact.
- Confidence: high, within about 1%.
