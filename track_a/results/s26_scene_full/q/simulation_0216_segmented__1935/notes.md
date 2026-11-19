# q_1935: length of the TV (m)

2D side-on Blender render, static camera, 24 fps (the file fps and question_fps agree, so no re-timing).
Prior: the black cat's speed is 0.94 m/s.

- Cat pixel speed (measure.py, from scene/tracks/cat.csv): the mean per-frame step is 17.64 px (cx), 17.83 (dark_cx)
  and 17.60 (bbox_cx). Linear fits give the same values. The walk is steady. I took 17.7 px/frame = 425 px/s.
- Scale: 0.94 / 425 = 0.002212 m/px.
- TV width, measured again on frame 10: dark pixels span x = 815..1212, which is 398 px on every row from 540 to 700.
  The record's static-object box gives 399 px. Height is 230 px.
- TV length = 398 × 0.002212 = 0.880 m.

Check: the speed from different reference points (centroid, dark-fur centroid, bbox centre) agrees within 1.3%. Net
displacement divided by frame count and the per-frame mean agree. The aspect ratio (0.88 m × 0.51 m) looks like a
normal ~40" TV, and the cat's ~260 px body works out to ≈0.58 m, which is plausible.

Caveat: the cat walks slightly in front of the furniture (paws at y ≈ 1021, furniture feet at ≈ 990). I used one
planar scale, as the 2D convention says. If the reference corrected for perspective, the TV would come out a few
percent larger. Confidence: good (about ±5%).
