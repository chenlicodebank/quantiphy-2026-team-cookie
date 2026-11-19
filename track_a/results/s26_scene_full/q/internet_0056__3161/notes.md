# q_3161 – height of the leftmost tree (m)

Prior: average speed of the scooter rider = 2.64 m/s. This is an internet video, so I used a single planar scale.

- Rider speed (speed.py, scene/tracks/scooter_rider.csv, 30 fps; the file rate and question_fps agree). The rider moves
  steadily to the right, so the mean per-frame speed equals the net speed. The reference points give:
  - cx: 323.2 px/s raw, 327.1 px/s with the camera drift removed.
  - Rear and front wheel edges: 321–329 px/s.
  - I used about 325 px/s, so the scale is 2.64 / 325 = 0.00812 m/px. The range is 0.00802–0.00822.
- Leftmost tree: the large Canary palm left of centre (trunk at x≈460–530). The thin palm cut off at the far left edge
  is only partly visible and its base is hidden, so I did not use it.
  - Top: the crown is cut by the top of the frame (fronds reach y≈0–10).
  - Bottom: the trunk's visible bottom is at y≈685–695, just above the shrubs. The planter curb is at ≈745.
  - Pixel height: about 685–690 px (frames/top.png, frames/base.png).
- Height = 688 × 0.00812 ≈ 5.6 m.
- Check: the rider's cap-to-ground height of 205–215 px gives 1.67–1.75 m on the same scale, which is plausible. This
  confirms the scale. The tree is really taller, because it stands further back and its crown is cut by the frame,
  but the annotators' single-scale convention gives about 5.6 m.
- Confidence: moderate. The main uncertainty is which pixel extent the annotator took for the tree. If they measured
  to the curb (≈745 px), the answer would be about 6.0 m.
