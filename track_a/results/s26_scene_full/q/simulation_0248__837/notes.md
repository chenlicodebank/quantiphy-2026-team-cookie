# q_837 — height of the front horse (m)

- Front horse = dun horse (ahead in the direction of motion, also slightly nearer: hooves y 634 vs 630). Horse at the back = red horse.
- fps = question_fps = 24, so no re-timing issue.
- 2D scene, static camera, so one metres-per-pixel scale comes from the prior.
- Red horse pixel speed: linear fit of the torso-centroid x over frames 0-48 (frame 49 is a loop-reset jump and is excluded) gives
  3.224 px/frame, with a residual std of 0.5 px. That is 77.4 px/s. Other reference points agree: centroid 3.219 and front edge 3.199 px/frame.
- Scale = 0.874 / 77.4 = 0.01130 m/px.
- Dun horse height (ear tip to hoof, mask y extent) over 50 frames: median 183 px (range 178-188).
- Height = 183 × 0.01130 = **2.07 m**. Using the red horse's front-edge speed instead gives 2.08 m.
- Caveat: there is a small depth offset (4 px difference in ground row). If corrected, the answer could be up to about 4% smaller.
  It is ignored here, following the 2D single-scale convention.
- Confidence: moderate-high, about ±5%.
- Script: speed.py
