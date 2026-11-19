# q_1985 — length of the rabbit (m)

Prior: speed of the deer (the horned quadruped) = 1.277 m/s. No depth_info. File fps = question_fps = 30.

Method (script `m.py`, own re-segmentation; output `rabbit_bbox.csv`):
- Both animals walk left→right parallel to the image plane, feet on the same image row (y≈800), with constant
  apparent size, so they are at about the same depth and one m/px scale applies to both.
- Deer pixel speed: mask-centroid linear fit 7.90 px/frame (mean |step| 7.93; scene record 7.87–7.96; bbox
  edges 7.44–8.01). 7.90 × 30 = 237.0 px/s → scale = 1.277 / 237.0 = 0.005388 m/px.
- Rabbit, seen side-on: horizontal bbox width (nose to tail) 77–99 px, depending on the hop phase (stretched at
  take-off); mean 84.2, median 83, frame 0 81 px. Thresholds of 225 and 240 agree to within 1 px.
- Length = 83–84 px × 0.005388 = 0.447–0.454 m (frame 0: 0.436 m; range 0.41–0.53 m).

Second route: rabbit centroid speed 7.66–7.74 px/frame ≈ the deer's (the rabbit keeps pace with it), which is
consistent with both being at the same depth. Using the bbox-centre speed of the deer (7.72 px/frame) gives
0.00551 m/px → 0.46 m.

Answer: 0.45 m. Confidence moderate. The main uncertainties are the pose (hop phase) used for the reference
bounding box (±10 %) and whether the two animals are at exactly the same depth.
