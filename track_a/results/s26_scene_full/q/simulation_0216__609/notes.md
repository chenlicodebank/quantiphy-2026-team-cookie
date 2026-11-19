# q_609 — length of the black cat including its tail (m)

Prior: cat speed = 0.94 m/s. depth_info: none. fps = question_fps = 24, so no re-timing question.
The video is 2D: the cat walks left to right, parallel to the image plane, at one depth (paws at y ≈ 1020 throughout),
and the camera is static.

## Scale (from the prior)
- Matched upper-body track (scene/tracks/cat.csv, checked with stats.py): 17.73 px/frame. Torso centroid net: 17.61.
  bbox x0 net: 17.67.
- My own readings: nose 670.5 (f8) → 1239 (f40) = 17.77 px/frame. Tail tip 367 → 938 = 17.84 px/frame.
- I used 17.75 px/frame = 426 px/s, which gives 0.94 / 426 = 2.207e-3 m/px.

## Length (world AABB x-extent, tail tip to nose)
The tail curves up and back, so its tip (y ≈ 800) is the cat's rearmost point, and the nose is the front.
The record's mask misses the grey face (bbox_x1 is about 20 px short, e.g. 933 vs 955 at f24). So I re-read both ends
by eye on 4× gridded crops (zoom.py → frames/z_*.png):

| frame | tail tip x | nose x | length px |
|---|---|---|---|
| 8 | 367 | 670.5 | 304 |
| 16 | 513 | 814.5 | 302 |
| 24 | 648 | 955 | 307 |
| 32 | 796.5 | 1098 | 301.5 |
| 40 | 938 | 1239 | 301 |

Mean is 303 px (spread ±3), so the length is 303 × 2.207e-3 = **0.669 m**.

## Cross-checks
- The record's automatic bbox length averages 294 px. It runs short because the face is under-segmented. That would give
  0.65 m, a lower bound.
- The speed from the nose and from the tail tip agrees with the body track to within 0.6 %.
- Nose to rump alone is ≈ 245 px = 0.54 m. With the tail the cat is ≈ 0.67 m, which is a plausible real cat size.

Confidence: moderate to high. The main uncertainty is whether the reference AABB matches the walking pose shown,
which is about ±3 %.
