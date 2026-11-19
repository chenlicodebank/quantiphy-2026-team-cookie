# q_1946 — speed of the red general chess piece at t = 1 s (m/s)

Prior: diameter of one Chinese chess piece = 0.097 m. 2D video, no depth_info. Both the file and the question run at
24 fps, so t = 1 s is frame 24.

## Object
The scene record calls the only moving object a "block". It is the chess piece: a beige disc seen almost edge-on,
sliding down the ramp trough. It is both the asked object and the prior's object. Its track is
`scene/tracks/block.csv`, which I checked against SAM 3 (below).

## Scale (diameter in px)
- The disc is seen nearly edge-on, so the long axis of its silhouette is the diameter (thickness only adds across).
- Frame 43: the piece is in the air on a white background. Silhouette from a half-contrast threshold
  (`diam_f43.py`): 82.9 px with thresholds at 0.3, 0.5 and 0.7 of the piece's contrast; the sub-pixel chord is 82.7 px.
  **D = 82.8 px**, which gives 0.001171 m/px.
- On the ramp the record has 81.3 px (median). It loses 1–2 px where the lower edge merges with the trough.
- SAM 3 masks: 84.4–86.1 px on frames 12, 24 and 26, and 86.5 px on frame 43. That is about 4.5 pct larger than my
  measurement. The zoomed overlays (`frames/cmp_f24.png`, `frames/cmp_f43.png`; green is SAM) show the SAM outline
  sitting about 1–2 px outside the piece at both ends. My threshold value of 82.8 px is right; SAM's outline is too
  wide.
- SAM's centroids match the track: frame 24 SAM (958.7, 662.2) vs track (959.2, 659.8); frame 43 (419.8, 1019.1) vs
  (419.8, 1019.0). The ~2 px y difference on the ramp comes from the dilated mask and does not affect the steps.

## Speed (`speed.py`)
- The video has frame-timing irregularities. Video frame 23 is a double step (46.3 px), 24 is a normal step
  (24.7 px), 25 repeats 24, and 27 is a double step again. The scene notes' remap puts video frame 24 = render frame
  25 and video frame 23 = render frame 24.
- Route 1, the raw backward difference at video frame 24: 24.70 px → 0.694 m/s.
- Route 2, a quadratic fit of the path coordinate against the true render index. Acceleration is 1.00 px/frame²
  and residuals are 0.36–0.68 px rms.
  - Render step 23→24, the backward difference at frame 24 of the simulation: 23.3–23.4 px → 0.655–0.659 m/s.
  - Instantaneous v(24): 0.669–0.673 m/s.
  - The result is stable across the windows 3–40, 14–34 and 18–30.
- Check: half of the render 22→24 double step is 23.14 px. This agrees with the fit.

## Answer
**0.67 m/s.** The ground truth is either the render backward difference (≈ 0.657) or the raw video difference
(≈ 0.694). 0.67 is within 3.5 pct of both and equals the smooth instantaneous speed at frame 24. Using the ramp
diameter of 81.3 px instead would raise all values by 1.8 pct.

Confidence: moderate to high. Most of the uncertainty is about which frame the reference treats as "frame 24", not
the measurement itself.
