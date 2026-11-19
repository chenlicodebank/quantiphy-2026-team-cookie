# q3009: distance traveled by the black-shirt player, 0.5 s to 5.53 s

- Object: the dark-kit player (scene `goalkeeper_dark`), standing near the top of the goal area. I checked them on frames 15 and 165 (frames/f05.png, frames/f553.png). The track positions match the frames to within about 3 px.
- Time: file fps 29.80 vs question_fps 30. Either way the window is frames 15 to 165 (or 166), and the difference changes the path by less than 2%.
- Scale: goal frame length 7.32 m. The posts are 97.9 px apart centre to centre and the outer frame is about 101 px, so I used 98.5 px, which gives 0.0743 m/px. The view is near-nadir, so one planar scale is enough.
- Path length (path.py, stabilized centroid, frames 15 to 165):
  - raw centroid: 56.6 px, inflated by ±1–2 px of limb jitter
  - Gaussian smoothing with sigma 2, 3, 5, 8: 40.4, 39.6, 39.1, 38.4 px
  - straight-line net displacement: 38.3 px (the walk is almost straight)
  - adopted value: about 40 px, which is 40 × 0.0743 ≈ 2.97 m
- Second-route check: the net displacement (38.3 px, 2.85 m) is a lower bound and sits within 5% of the answer. The player stands still until about frame 84, then walks about 2.8 m in about 2.7 s, roughly 1 m/s. That is a plausible slow walk.
- Confidence: moderate-high. The main uncertainty is how much an annotator's frame-by-frame clicks would add as jitter.
