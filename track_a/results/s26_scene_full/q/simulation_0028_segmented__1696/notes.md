# q_1696: length of the rock (m)

Prior: eagle length = 0.8 m. depth_info: eagle at 100.14 m (t=1 s) and 99.52 m (t=2 s), so its depth is nearly constant.
The file runs at 25 fps and the question at 24 fps. Time conversion does not matter here because the rock is static.

## Measurements (measure.py, crops.py)
- **Eagle:** it flies left to right, roughly parallel to the image plane, so its beak-to-tail length lies along image x.
  - I measured its horizontal extent on the white-background frames 0–19 at three dark thresholds (25, 60, 128).
  - The extent is 23–30 px and changes with the wingbeat; the wings-level and median frames give about 25 px.
- **Focal length:** f ≈ 25 px × 100 m / 0.8 m ≈ 3120 px, which is a horizontal field of view of about 17°.
  - Cross-check: the eagle moves about 16.5 px per frame, which gives about 12 m/s. That is a plausible flight speed.
- **Rock:** its horizontal silhouette spans x 328–959, i.e. 632 px. It is at most a few px cut off at the right
  image edge (only 7 rows touch x = 959).

## Scale and answer
- The rock's depth is not given.
- If the rock is at the eagle's depth (100 m): 632 × 100 / 3120 = 20.3 m.
- The eagle passes in front of the rock's lower front edge without being hidden, so the rock's origin is probably
  somewhat behind the eagle (around 105 m). At that depth the length is about 21.3 m.
- **Answer: 21 m.**

## Confidence
Low to moderate. The answer is sensitive to:
- the eagle's pixel length (±10 %, wingbeat);
- the rock's unknown depth;
- the rock's yaw: the image-horizontal extent may mix its length with its width.
