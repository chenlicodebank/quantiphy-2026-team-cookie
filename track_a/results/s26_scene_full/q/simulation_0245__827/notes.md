# Q827 – length of the antelope (m)

Prior: antelope speed = 1.277 m/s. depth_info: none. 2D scene with a static camera, and fps = question_fps = 30.

## Scale (measure.py)
I fitted a line to the antelope's horizontal track from scene/tracks/creature.csv, frames 0–74:
- Mask centroid: 6.470 px/frame (rms 1.6 px). Torso centre: 6.473. Rump edge: 6.497. Chest edge: 6.450. All routes agree within 0.7 %.
- 6.470 px/frame × 30 = 194.1 px/s, so the scale is 1.277 / 194.1 = 0.006579 m/px.

## Length in pixels
Length is the horizontal extent from the tail tip to the snout:
- The record's mask bbox width has a median of 474 px (range 443–514, which varies with the tail swing and gait).
- I checked it on zoomed frames with a grid (crops.py):
  - Frame 0: 76 → 552, so 477 px.
  - Frame 30: about 257 → 733, so about 476 px.
  - Frame 60: about 477 → 947, so about 470 px. The mask misses about 20 px of the pale snout here.
- I used about 476 px.

## Answer
476 × 0.006579 = 3.13 m.

Other reading: without the tail (rump to snout, about 323 px), the length would be about 2.1 m. I did not use it, because the AABB includes the tail.

Confidence: moderate. The uncertainty comes mainly from the tail pose and the AABB convention. The scale itself is good to about 1 %.
