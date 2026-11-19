# q_1926 — height of black cat (incl. tail), prior: cat speed 0.94 m/s

2D side-on walk, static camera, 24 fps (file fps = question_fps, so no re-timing). One metres-per-pixel scale from the speed prior.

- Speed in pixels: the cat walks steadily (no start or stop). Net centroid travel over 49 frames:
  cx 17.64 px/frame = 423.3 px/s; dark-fur centroid 17.83 px/frame = 427.9 px/s.
  Scale = 0.94 / v gives 0.002221 or 0.002197 m/px.
- Height in pixels: bounding box from the tail tip / ear top down to the paws. Some track frames (13–17, 27–35, 42–49)
  lose the pale paws from the mask; frame 43 is a clear example, where y1 is 997 but the paws visibly reach about
  1020. So I used only frames with y1 ≥ 1021: the median is 223.5 px (range 212–227). Zoomed frames 0 and 43 confirm
  a tail top near y ≈ 798–800 and paws near y ≈ 1022, which is about 223 px.
- Height = 223.5 px × scale: 0.496 m (cx route) and 0.491 m (dark_cx route). Answer = mean of the two, **0.494 m**.
- Second-route check: the two centroid speed routes agree within 1%. The tail pose varies the height by about ±3%.
- Confidence: moderate-high, about ±5%. The main uncertainty is which frame or pose the reference box uses.
