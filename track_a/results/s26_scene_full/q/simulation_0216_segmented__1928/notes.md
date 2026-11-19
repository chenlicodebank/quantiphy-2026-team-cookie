# Q1928: height of the wooden bench (m)

- This is a 2D side-on render: 24 fps, 50 frames, static camera. The file fps and question_fps are both 24, so there is no re-timing.
- Scale comes from the prior (cat speed = 0.94 m/s). The cat walks steadily. Its net horizontal centroid motion over frames 0 to 49 is
  423.3 px/s with `cx`, 422.4 px/s with `bbox_cx` and 427.9 px/s with `dark_cx`. I used about 424 px/s, which gives 0.94/424 = 0.002217 m/px.
  The mean of per-frame |Δ| speeds (428.6 px/s) is inflated by gait jitter in the centroid, so I did not use it. The rig root moves steadily.
- Bench height: I re-measured it in `measure.py` on frame 49, where the cat is clear of the bench, with a non-white mask. It runs from y = 779 to 992,
  which is 214 rows; the outer rows are anti-aliased, so the height is about 213 px. This matches the record (213 px).
- Height = 213 × 0.002217 = 0.472 m.
- Check: the bench width (466 px) comes out at 1.03 m, so the 1.03 m × 0.47 m bench has plausible proportions. Using the `dark_cx` speed instead
  gives 0.468 m, so the spread is under 1%.
- Caveat: the furniture feet sit about 30 px above the cat's paws, which suggests the bench is slightly behind the cat's line. I ignored this,
  following the 2D single-scale convention.
- Confidence: good (about ±3%).
