# q1862 speed of astronaut at t=2 s (frame 48)
2D segmentation video, fps 24 (= question_fps), single scale from prior height 2.2 m.
- Height in px: upright bbox height f0-f2 = 90/91/90 px; PCA axis length mean 90.4 px over clip (rigid pose). Used 90.7 px -> 0.02426 m/px.
- Own tracking (measure.py, track_own.csv): binary-mask centroid and darkness-weighted centroid.
  Per-frame speeds f44-52 ~4.6-5.3 px/frame (jitter +-0.3). Mean f46-50 = 4.95 px/f; local quadratic fit f40-56 derivative at 47.5 = 4.93 px/f (both centroid types agree).
- Speed = 4.93 px/f x 24 x 0.02426 = 2.87 m/s. Second route (raw backward diff f48 = 4.66-4.69 px/f is noise-dominated; smoothed values agree with scene record 5.0-5.3 px/f peak region).
- Confidence: good (~3-5%), dominated by height-in-px uncertainty (+-1 px) and centroid-vs-pelvis offset under slow rotation.
