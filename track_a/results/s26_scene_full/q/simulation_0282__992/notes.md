# q992 — dragon body length (m)

2D top-view clip with a static camera, 24 fps (fps and question_fps agree). Prior: dragon speed = 1.29 m/s.

## Scale (from the prior)
- I used the hip/torso body point from scene/tracks/dragon.csv (template-tracked; I checked it on frames).
  `speed.py` gives per-frame steps of 32.4–36.7 px. The mean over frames 1→71 is 34.42 px/frame, the median is 34.36 and a linear fit over frames 2–66 gives 34.45.
  So the speed is 826.2 px/s, which is nearly uniform.
- Scale = 1.29 / 826.2 = 1.561e-3 m/px.

## Body length (px)
- The light-grey cone on the snout is part of the model, so I count it as the nose tip. The soft shadow to the left is not part of the dragon.
- `length2.py` finds the nose as the leftmost sharp edge near the spine (Sobel) and the tail tip as the rightmost pixel of the dragon's mask. It covers frames 4–63; the results are in lengths.csv.
  Some frames (20, 22, 26–31, 42, 54, 61, 63) missed the cone; those have nose offsets near −151 and I ignored them.
- The nose-to-tail x-extent changes with pose because the tail swings and the head moves:
  - Straight-tail pose (frames 7–12): 545–551 px. Nose at −207 px and tail tip at +341 px from the hip.
  - Frames 32–41: about 522 px.
  - Glide (frames 47–59): 477–485 px, with the tail angled sideways.
  - Overall median: 485 px.
- I checked by eye on zoomed frames:
  - Frame 10: 1836 → 2390, about 554 px.
  - Frame 40: 825 → 1352, 527 px.
  - Frame 52: 416 → 897, 481 px.
  - Frame 24: 1373 → 1840, 467 px.

## Answer
I take "body length" to mean the model's nose-to-tail length with the tail straight (rest-pose dimension): about 545 px × 1.561e-3 = **0.85 m**.
Other readings:
- Glide-pose AABB length: 481 px → 0.75 m.
- Median over all poses: 485 px → 0.76 m.
- Frames 32–41 pose: 522 px → 0.82 m.

Confidence: moderate. The scale is good to about 2%; the main uncertainty is which pose the reference used (±12%).
