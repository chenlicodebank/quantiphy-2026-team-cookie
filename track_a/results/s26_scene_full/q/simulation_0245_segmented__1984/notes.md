# q_1984: length of the rabbit (m)

- 2D scene at 30 fps (the file fps and question_fps agree). The "deer" in the prior is the large horned quadruped (the record calls it an ibex), the only other animal in the clip.
- I re-measured from the video with `measure.py`, which writes `meas.csv`. Masks: min(RGB) < 247, then opening, then connected components.
- Deer pixel speed: the linear-fit slope is 6.520 px/frame for the centroid, 6.524 for the trunk's right edge and 6.519 / 6.523 for the bbox left / right edges. The mean per-frame centroid step is 6.535 px/frame. I used 6.52 px/frame = 195.6 px/s.
- Scale: 1.277 / 195.6 = 0.006529 m/px.
- Rabbit length (bbox x extent): I used the 63 frames where the rabbit is unclipped and its mask has no hoof fragments. The median is 72 px, the mean 73.6 px, and the range 68-88 px, which changes with the hop pose. I checked the mask on a zoomed crop.
- Length = 72-73.6 px × 0.006529 = 0.470-0.481 m. **Answer: 0.473 m.**
- Second-route check: the scale is the same within 0.3% whichever deer reference point is used (centroid, trunk edge, bbox edges). The main uncertainty is which pose the reference bbox used, about ±3%.
