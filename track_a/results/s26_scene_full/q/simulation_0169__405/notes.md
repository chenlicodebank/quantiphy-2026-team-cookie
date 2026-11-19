# Q405 — speed of the astronaut at t = 2 s (m/s)

- 2D render, fps = question_fps = 24 → t = 2 s is frame 48. Static camera; the astronaut is the only moving object.
- Scale: the prior says the astronaut is 2.2 m tall. The upright figure at frames 0-5 is 89-91 px tall
  (threshold 25: 90-91 px, threshold 60: 89-90 px; scene record bbox 91 px; body-axis length ≈ 91.5 px all through the clip,
  so depth stays constant). I used 90.5 px, which gives 0.02431 m/px.
- Speed: `measure.py` re-segments the astronaut (with the moon cropped out) and takes the mask centroid and the
  intensity-weighted centroid at two thresholds.
  - The raw one-frame step at frame 48 is 4.4-4.7 px/frame. This is noisy: neighbouring steps are 5.3 (47) and 4.8 (49).
  - A cubic fit to the positions over frames 40-56, then the backward difference 47→48: 4.96-4.99 px/frame.
  - Mean of the steps over frames 45-51: 4.95-4.97 px/frame.
  - The scene record's steps agree (5.30, 4.70, 4.83 around frame 48). The motion is a smooth ease-in/ease-out that is
    just leaving its ≈5.1-5.2 px/frame plateau.
- Answer: 4.96 px/frame × 24 × 0.02431 m/px ≈ 2.89 m/s.
- Confidence: about ±4%. Most of this comes from the pixel height (±1 px of glow edge ≈ ±1%) and from smoothing versus the
  raw single step (the raw step would give ≈2.6-2.7 m/s).
