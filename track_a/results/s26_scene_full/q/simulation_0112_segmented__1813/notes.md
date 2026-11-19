# Q1813: height of the car (m)

Prior: car speed = 6.66 m/s. This is a 2D side-view clip at 24 fps (file fps and question_fps agree), with a static camera and the car moving uniformly left to right.

## Method (measure.py)
- Mask: pixels above the platform (y < 540) that are not white, in frames 13-36, where the car is fully in view.
- Silhouette bbox centre: linear fit gives **27.28 px/frame**. This matches the scene record's 27.285.
- Scale: 6.66 / 24 = 0.2775 m/frame, so 0.2775 / 27.28 = **0.010173 m/px**.
- Height, from the bottom of the tyres to the roof: 124-128 px, median **126 px**. The scene record also gives 126 px (bbox y 413/414-539). I checked it visually on frame 25.
- Height = 126 x 0.010173 = **1.282 m**.

## Checks
- Length from the same scale: 422 px gives 4.29 m. For a Porsche 911 Turbo-like coupe (about 4.29 m long and 1.29-1.31 m tall) both values are plausible.
- The near-side wheels move about 3.5% faster (28.23 px/frame) because of perspective. A scale based on the wheels would give 1.24 m. The silhouette is the better proxy for the origin's depth, and the roof and bumper extremes lie near the centreline, so I kept the silhouette scale.

Confidence: good, within about 3%.
