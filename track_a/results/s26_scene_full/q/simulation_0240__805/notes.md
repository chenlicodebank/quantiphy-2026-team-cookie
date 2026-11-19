# Q805 – speed of the front horse at 1 s (m/s)

Prior: the horse at the back (chestnut, left) moves at 0.874 m/s. The scene is 2D, the camera is static, and fps = question_fps = 24.
"Front horse" means the pale/cream horse that leads; "back horse" means the chestnut horse that trails.

## Method
- I used the mask-centroid x tracks from scene/tracks (I checked them on frame 24, `frames/f24.png`). Both horses walk at
  the same depth in front of the brick wall, at the same apparent ground line, and their sizes stay constant. Under the 2D
  convention one metres-per-pixel scale applies to both.
- Both horses move at nearly constant pixel speed. Gait wobble in the centroid is ±2 px per frame, so I averaged the speed over
  multi-frame lags (`lags.py`) and with linear fits (`measure.py`). The chestnut horse's frame 48->49 loop reset is excluded.
  - chestnut: 3.24-3.26 px/frame for lags of 10-40 frames; 3.154 from the frame 0->48 endpoints.
  - pale: 5.94-5.97 px/frame for lags of 10-40 frames; 5.895 from the frame 0->49 endpoints.
- Scale = 0.874 / (3.245 x 24) = 0.01122 m/px. This gives a pale horse about 2.56 m long and 2.0 m tall, and a chestnut
  horse about 2.1 x 1.86 m, which is plausible.
- Speed of the front horse = 0.874 x 5.95 / 3.245 = 1.603 m/s.

## Checks
- Local fit over frames 12-36 (around t = 1 s) with mask_cx: 6.03 / 3.25 px/frame gives 1.62 m/s.
- Ratio of the endpoint (full-clip) speeds gives 1.634. A box-edge fit over the whole clip gives 1.59-1.60.
- Final answer: 1.61 m/s. Confidence is good (about ±3%). The main uncertainty is the chestnut horse's pixel speed
  (3.15-3.26 px/frame).
