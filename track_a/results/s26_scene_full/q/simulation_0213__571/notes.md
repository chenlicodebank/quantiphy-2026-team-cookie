# Q571: length of the black cat, tail included (m)

Prior: the cat's speed is 0.94 m/s. This is a 2D side-view clip at 24 fps (the file fps and question_fps agree). The cat walks steadily from left to right in its own floor lane. The prior and the question both concern the cat, so a single m/px scale taken from the cat's own speed applies, and the dog's different depth does not matter.

- Pixel speed: I fitted straight lines to the cat's position over the 29 frames where it is visible (0-22 and 44-49), using `measure.py` on scene/tracks/cat.csv.
  - Nose (bbox_x1): 17.76 px/frame, rms residual 0.7 px.
  - Torso: 17.86 px/frame.
  - Box centre: 17.71 px/frame.
  - Centroid: 17.81 px/frame.
  - Mean of nose, torso and box centre: 17.78 px/frame = 426.7 px/s, which gives 0.002203 m/px.
- Length: I took the horizontal extent of the full silhouette, tail and paws included (the AABB extent along the walking direction), over the visible frames. It ranges from 301 to 324 px with the gait; the median is 307 px and the mean 308.8 px. The tail is held upright, so its tip barely adds to the horizontal extent.
- I checked the record by eye on frame 6 with a grid: the tail tip is at x≈328 and the nose at x≈636, so the extent is about 308 px, which matches the track's 309.
- Answer: 307 × 0.002203 = **0.676 m**.
  - The mean length gives 0.680 m.
  - Scaling with the nose speed alone gives 0.677 m, and with the torso speed alone 0.673 m.
- Confidence: good, within about 3%. The main uncertainty is which pose the reference box used, since the gait changes the length by up to about 5%.
