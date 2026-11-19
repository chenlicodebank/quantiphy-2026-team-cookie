# Q979: raccoon displacement from 0.5 s to 1.0 s (m)

- 2D side-view render, fixed camera, 24 fps (file fps = question_fps, so no re-timing). The times are frames 12 and 24.
- **Scale (prior: length with tail = 1.51 m).**
  - I re-measured nose-to-tail-tip per frame in `length.py`: background-difference mask with threshold 18, restricted to body rows 750–835.
  - The scene record's `x1` missed the faint snout in some frames. In frame 12, for example, the record has 1083 but the nose is really at 1111.
  - In frames with the tail held out, the length is 315–332 px (frame 12: 327, frame 24: 319; median of the clean stretched frames about 320).
  - I used 320 px, so the scale is 1.51 / 320 = 0.00472 m/px.
- **Displacement.**
  - Torso template matching from frame 12 to frame 24 (`measure.py`, 4 different torso windows) gives dx = 277–281 px and dy = 5–6 px.
  - Mask-centroid route (scene track `cx,cy`): 958.6→1239.7 and 788.4→791.7, which is 281.1 px.
  - Tail tip moves 785→1061 (276 px) and nose 1111→1379 (268 px; the head pose changes).
  - Adopted value: about 279.5 px, which gives 1.319 m.
- **Uncertainty:** mainly the pixel length that matches the prior, because the length changes with gait (314–330 px). Over that range the answer is 1.28–1.34 m. Confidence is moderate to high, within about 4%.

Answer: 1.32 m
