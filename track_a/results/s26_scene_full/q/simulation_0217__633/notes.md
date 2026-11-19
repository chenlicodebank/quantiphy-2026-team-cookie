# Q633: length of the dog including its tail (m)

The prior is the black cat's speed, 0.94 m/s. This is a 2D top-down render at 24 fps (question_fps is also 24). The camera is static.

## Scale from the cat
The cat walks at a steady speed along +x. I fitted linear slopes over frames 0–49 (`answer.py`, using scene tracks
whose cat mask is clean):
- centroid: 10.943 px/frame
- front edge: 10.977 px/frame
- tail-less body centroid: 10.945 px/frame

The mean is 10.955 px/frame, or 262.9 px/s. The scale is therefore 0.94 / 262.9 = **0.003575 m/px**. The routes agree
to within 0.3 %.

## Dog length (tan animal, walking −x)
`dogmask.py` builds a per-frame mask in three steps:
1. It takes the difference against a per-column background, using the temporally nearest frame in which the dog is
   elsewhere.
2. It adds the flat, untextured grey-brown head patch at the front. I detected the patch by colour (R−B > 18) and
   near-zero local texture, and kept it as part of the dog because it moves with the dog.
3. It removes the cat.

The x-extent of this mask is the world-AABB length along the walking direction. I checked the overlays (frames/m28_*.png):
- The front edge is reliable.
- The thin tail tip is sometimes missed. For example, at frame 5 the tail visibly reaches x ≈ 1420, but the mask stops at 1358.

The x-extent changes a lot over the clip because the tail swings:
- 273 px at frame 0, where the tail curls sideways.
- About 340–348 px when the tail points straight back (frames 5, 6, 18, 26, 39, 40).
- Median 285 px and mean 295 px with threshold 28. Both are slightly low because the tail is sometimes missed.

I checked the tail-extended frames by eye on gridded crops (`crops.py`): frame 5 spans 1075 to 1420 (345 px), and
frame 18 spans 960 to 1297 (about 337 px).

## Answer
The question does not name a time, so I used a representative extent of about 300 px. This is the clip average after
correcting the frames where the tail was missed. 300 px × 0.003575 = **1.07 m**.

The range is 0.98 m (frame 0 pose) to 1.23 m (tail fully extended).

Confidence is moderate. The main uncertainty is which pose the reference bounding box used (±13 %). A second, smaller
one is whether the head patch counts, which changes the length by about 35 px (about 12 %).
