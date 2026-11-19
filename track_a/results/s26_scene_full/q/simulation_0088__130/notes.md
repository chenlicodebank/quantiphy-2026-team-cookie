# Q130 – speed of the small bird (crow) at t = 0.3 s

2D render, 24 fps (file fps = question_fps, so no re-timing). t = 0.3 s is frame round(7.2) = 7.
Both birds fly horizontally at constant speed in the same plane, so one m/px scale applies to both.

Scale from the prior: the big bird (eagle) moves 17.98 m/s.
- Eagle per-frame step: 119–120 px every frame f2–f14 (mean 119.69 px/frame from scene tracks; 119.75 from my own
  tail-end mask f2→f14 in check.py).
- Crow per-frame step: 73–74 px every frame f2–f24 (mean 73.26 px/frame from tracks; 73.25 f2→f14 in check.py).
  At frame 7: head-tip and tail-end both move 73 px (f6→f7).

Crow speed = 17.98 × 73.25 / 119.75 = 11.00 m/s (route 1, mean steps from tracks: 17.98 × 73.26/119.69 = 11.005;
route 2, my own masks: 10.998). The single-frame step at f7 (73 px) would give 10.96, but it is within the 1-px
quantization noise of a constant motion, so I use the mean.

Answer: 11.0 m/s. Confidence: high (motion is uniform; ratio of pixel steps known to ~0.3 %).
Scripts: m.py (per-frame steps from the tracks), check.py (independent segmentation from the video).
