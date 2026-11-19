# Q623: length of the black cat, tail included (m)

- 2D top-down render, 24 fps (the file and the question both use 24), camera static. Prior: the black cat's speed is 0.94 m/s.
- `measure.py` re-segments the cat on every frame (max(BGR) < 60, largest component). I checked the mask on overlays
  (`frames/ov_*.png`): it is clean and includes the whole tail.
- Pixel speed (the cat walks at a steady pace along +x, and y stays almost constant):
  - Front edge: 10.98 px/frame from the mean step, 10.98 from a linear fit.
  - Centroid: 10.92 / 10.94.
  - Back edge: 11.20 (tail motion makes it noisier).
  - Value used: 10.95 px/frame = 262.8 px/s, giving a scale of 0.94 / 262.8 = 3.577e-3 m/px.
- Nose to tail tip, measured as the x-extent of the bounding box: mean 191.3 px, median 190.5, range 185–200 px over
  50 frames (it varies with the tail pose). With a darker threshold of 40 the mean is 190.1 px.
- Length = 191.3 × 3.577e-3 = **0.684 m**.
- Second-route check: the centroid speed alone gives 0.686 m and the front-edge speed alone gives 0.683 m. The
  frame-by-frame range of the extent is 0.66–0.72 m.
- Confidence: moderate to high. Most of the uncertainty comes from the tail pose (about ±4%).
