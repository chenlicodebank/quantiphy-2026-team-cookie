# Q700 – length of the black cat including its tail (m)

The scene is a 2D top-down render at 24 fps (question_fps is also 24). The black cat walks in +x at a constant speed and is the only moving object.
Prior: the cat's speed is 1.041 m/s, which is constant, so it can be used at any time.

## Measurements (`measure.py`, all 50 frames, gray thresholds 40/50/60/75)
- Pixel speed: linear-fit slopes of x(frame) are 5.45 px/frame for the tailless body centroid, 5.46 for the head tip and 5.52 for the tail tip. The mean per-frame step is 5.44. I took 5.455 px/frame = 130.9 px/s.
- Scale: 1.041 / 130.9 = 0.00795 m/px.
- Full silhouette x-extent (bounding box, including the tail): mean 107.3–108.1 px across thresholds, median 107–108 px, range 104–111 px. This agrees with the record's PCA length of 107.5 px. I used 107.8 px.
- Length = 107.8 × 0.00795 = 0.857 m.

## Second-route check
Using the head-tip speed (5.465 px/frame) instead of the body speed gives 0.856 m. Using the minimum and maximum frame extents gives 0.83–0.88 m.
A cat about 0.86 m long including its tail is plausible.
Confidence: good, roughly ±3%.
