# q_2761 — path length of the white "ball" (the white toy) from 1.5 s to 1.9 s, in cm

- File fps = question_fps = 24, so the window is frames 36 to 46 (round(1.9 x 24) = 46).
- Object: the only moving object, scene/tracks/white_toy.csv. I checked the centroids on overlays for frames 35-47
  (frames/ov.png) and they sit on the toy. There is a bounce at frame 41 inside the window; frames 40-41 are faded by
  the segmentation, but the centroids still look right.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depth: depth_info gives 0.7045 m at t = 1.5 (frame 36) and 0.6270 m at t = 2.0 (frame 48). I interpolated it linearly
  per frame. The apparent size grows too, which agrees that the toy is approaching the camera; size is not used as a
  depth source because the shape is oblong and rotates.
- Back-projection as in the lab card: P = ((u-cx)/f, (v-cy)/f, 1) x depth. Path = sum of the 10 frame-to-frame 3D
  displacements.

## Results (cm)
| reference point | card (depth used as Z) | depth used as Euclidean range | 3-frame smoothed (card) |
|---|---|---|---|
| mask centroid | 37.95 | 35.57 | 35.91 |
| bbox centre | 38.17 | 35.75 | 36.10 |

Net displacement from frame 36 to 46: about 29.5 cm, so the path is longer than the straight line, as it should be with a bounce in between.

The second route (bbox centre instead of mask centroid) agrees within 0.6 pct. The main uncertainties are the
depth model (linear interpolation) and whether the reference smoothed its positions; smoothing lowers the result by about 2 cm.
Answer: 37.5 cm, a value between the raw card result and the lightly smoothed one. Confidence: moderate, roughly ±8 pct.
