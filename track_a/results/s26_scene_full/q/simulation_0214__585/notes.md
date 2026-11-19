# Q585: black cat length including tail (m)

- This is a 2D top-down Blender clip at 24 fps. The file and the question use the same rate. The camera is static.
- The prior gives the black cat's speed as 0.94 m/s. The cat walks at a steady speed along +x.
- `measure.py` makes a dark mask of the cat for each frame (gray < 50/60/75; the largest blob). Linear fits over frames 0–49:
  - head front x1: 10.975 px/frame
  - centroid: 10.966 px/frame
  - tail end x0: 11.21 px/frame
  - These give 10.97 px/frame = 263.3 px/s.
- Scale: 0.94 / 263.3 = 0.003570 m/px.
- The cat's x-extent including the tail is 183–200 px; it changes with gait. The median is 190.5 at threshold 50 and 192 at threshold 60. The soft anti-aliased edges add about 1–2 px, so I used 193 px.
- Length = 193 × 0.003570 = **0.689 m**. The full range is 0.65–0.71 m.
- Check: the scene record gives the same numbers (11.0 px/frame and a 191 px median). A zoomed gridded frame at t = 1 s reads about 718–911 px, which is 193 px.
- Confidence: moderate-high. The main uncertainty is gait and tail pose against the reference's AABB pose, about ±4%.
