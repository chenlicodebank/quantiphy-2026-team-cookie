# Q818: length of the antelope (m)

Prior: speed of the antelope = 1.277 m/s. depth_info is null. This is a 2D scene: the camera is static and the animal walks fronto-parallel at constant depth (its hoof line and apparent height stay fixed). fps = question_fps = 30.

## Scale (m.py)
- I fitted a straight line to x(frame) for several trunk features. chest_front_x and ref_x give 6.561 px/frame, cx_mask 6.538, nose 6.495 and rump 6.476. The mean |step| is 6.5 px/frame.
- Pixel speed = 6.561 x 30 = 196.8 px/s. Scale = 1.277 / 196.8 = 0.00649 m/px. Using the mean of the per-frame steps (6.5) instead gives 0.00655, a 1% difference.

## Length (ov.py, frames/ov.png)
- I drew the bounding boxes on frames 0, 12, 24, 36, 48, 60 and 74 and checked them. Each box runs from the tail tip (left) to the muzzle (right) and fits the silhouette well.
- The tail swings, so the box width changes: 408 to 508 px, median 487 px (10th to 90th percentile 456 to 504).
- Answer (world bounding-box length, tail included): 487 px x 0.00649 = **3.16 m**.
- Other readings:
  - nose to rump without the tail: 344 px, about 2.23 m;
  - frame-0 box, where the tail hangs under the body: 408 px, about 2.65 m.
- Second route: the per-frame-step scale (0.00655) gives 3.19 m, so the scale is stable.
- Confidence: medium. The scale is solid. The main uncertainty is what the reference counts as length: whether the tail is included and which pose was used.
