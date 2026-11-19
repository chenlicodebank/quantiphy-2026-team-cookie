# q_625 — length of the wooden bench (m)

Prior: black cat speed = 0.94 m/s. depth_info: none. fps = question_fps = 24, so no re-timing.

Scene: a top-down 2D render with a static camera. The cat walks in a straight horizontal line at a near-constant speed.

## Cat pixel speed
Taken from scene/tracks/black_animal.csv; I checked it in measure.py.
- Front edge (bbox_x1): 10.98 px/frame.
- Centroid: 10.92 px/frame. The mean of the per-frame step magnitudes is also 10.92.
- Body centroid: 11.01 px/frame.
- Taken together: 10.95 px/frame = 262.8 px/s.

Scale: 0.94 / 262.8 = 0.003577 m/px.

## Bench pixel length (bench.py)
- Method: an HSV mask of the orange wood (S > 120, H < 20), with column profiles across frames 0, 25 and 49.
- Edges: left at x ≈ 294.5, right at x ≈ 583.5, so the length is 289 px. The width is 118 px.
- This agrees with the scene record's 288 px.

## Result
289 × 0.003577 = 1.034 m.

Perspective: the bench top (about 0.45 m) is higher, and so closer to the camera, than the cat's origin (about 0.2 m). It therefore looks slightly enlarged. The walls show weak perspective (camera height of roughly 10 m in scene units), so the correction is about 1–2%.

Final answer: 1.02 m.

## Checks
- Sanity check: with the same scale, the cat is 0.54 m long without its tail and 0.68 m with it, which is plausible for a cat. A bench length of about 1 m is also plausible.

Confidence: good, ±5%. The main uncertainties are the size of the perspective correction and the frame-to-frame jitter in the cat's speed.
