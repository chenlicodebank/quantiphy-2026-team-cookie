# q_3086: height of the plastic (iced-tea) bottle, in cm

Prior: the rolling cylinder's velocity is 107.3 cm/s. Following the internet-video convention, I used one planar scale = prior / the cylinder's pixel speed.

- **Time base:** the file runs at 30.013 fps and the question states 30 fps. The difference (0.04 %) does not matter, so I used 30 fps.
- **Cylinder pixel speed** (`speed.py`, using the stabilised centroid track in scene/tracks/cylinder.csv, checked against the leading edge bbox_x0):
  - Per-frame steps go from about 50 to 75 px. The speed dips in the middle of the clip and rises near the end, partly because of perspective (the cylinder comes closer to the camera).
  - Frames 4-30: the mean of the per-frame speeds is 1839 px/s and the net displacement gives 1835 px/s. Using the leading edge gives 1784 px/s.
  - Frames 4-28: 1805 px/s. Frames 8-24: 1733 px/s.
  - I took 1810 px/s as the representative full-clip average.
- **Bottle height:** 426 px at frame 44, from the cap top at y ≈ 291 to the base at y ≈ 718. I checked this on a 50-px gridded crop (frames/bottle.png); it agrees with scene/static_objects.json.
- **Scale:** 107.3 / 1810 = 0.0593 cm/px, so the height is 426 × 0.0593 ≈ 25.2 cm.
- **Range by choice of speed window:** 24.9 cm (1839 px/s) to 26.4 cm (1733 px/s).
- **Sanity check:** a 500 ml bottle is about 21-23 cm tall. The bottle stands farther back than the cylinder rolls, so a single planar scale is expected to overstate its height.
- **Confidence:** moderate. The main uncertainty is which speed window the annotators used for the prior.
