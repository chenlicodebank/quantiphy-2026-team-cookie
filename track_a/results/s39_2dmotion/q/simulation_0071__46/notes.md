# Q46 – speed of the walking pedestrian at 1.0 s (m/s)

Prior: yellow car length = 5.44 m. 2D top-down render, 24 fps (the file and the question use the same rate), so t = 1.0 s is frame 24.
The "yellow car" is the only car (peach/cream sedan). The pedestrian walks +x along the bottom-right sidewalk at y ≈ 842.

## Scale (car length)
- `car_profile.py`: half-max edges of the car colour (R−B) profile along the car axis give 218.2 px at frame 0 (car vertical, static) and 218.5 px at frame 71 (car horizontal).
- SAM 3 "yellow car" masks: length 217.3 px at frame 0; at frame 71 the bbox is 219.2 px wide (its PCA length_px of 224 is inflated).
- The scene record says 222.5 px, and my background-difference mask (`car_len.py`) says 217–227 px with width 95–103 px. Both of these include a faint shadow/edge halo; the record's width of 88 px vs SAM's 78–81 px points the same way. The colour profile and SAM agree within 1%, so I use L = 218.5 px.
- Scale: 5.44 / 218.5 = 0.02490 m/px.

## Pedestrian speed
- `ped_speed.py`: an intensity-weighted background-difference centroid for every frame (saved in ped_track.csv). Per-frame steps are noisy (0.9–4 px) because the blob is small and its shape changes with the stride, so I take the local slope with linear fits around frame 24:
  - frames 20–28: 2.07 px/frame
  - frames 14–34: 2.12
  - frames 10–24: 2.07
  - frames 18–30: 2.16
  - whole walk (frames 2–71): 2.02
- Scene record, smoothed cx: (1382.87 − 1371.75)/6 = 1.85 px/frame over frames 21–27, and 2.12 px/frame over frames 14–34.
- SAM centroid at frame 24 is (1378.4, 840.9), against the record's 1377.97 and my 1380.3: they agree within 2 px. A SAM video track of "person" was unusable (it jumps between objects), so I relied on my own track.
- Adopted: 2.07 px/frame × 24 = 49.7 px/s.

## Answer
49.7 px/s × 0.02490 m/px = **1.24 m/s**.
Second route: the average speed over the whole walk gives 2.02 × 24 × 0.0249 = 1.21 m/s, about 2.5% lower. A plausible walking speed is a sanity check.
Confidence: moderate-high, about ±5%. The main uncertainty is the per-frame gait variation of the pelvis speed, which the centroid noise hides.
