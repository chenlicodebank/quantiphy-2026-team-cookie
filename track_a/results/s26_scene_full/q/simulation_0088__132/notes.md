# Q132 body length of big bird (eagle)
2D video, 24 fps (question_fps = file fps). Scale from prior speed 17.98 m/s.
- Eagle steps steadily right-to-left: linear fit of head tip and tail end x over frames 2-14 (my measure.py, body-line rows 540-575)
  gives 119.65 px/frame (scene record 119.69) -> 2871.7 px/s -> 0.006261 m/px.
- Body length (beak tip to tail end, horizontal extent; body axis horizontal): 139.2 px (threshold 20), 137.5 px (threshold 40);
  scene record full-mask extent 138.7 px. Visual check at frame 6: head ~1027, tail ~1163.
- Length = 139 px x 0.006261 = 0.87 m (range 0.86-0.875).
Second route: scene record numbers 138.7 px / (119.69*24/17.98) = 0.868 m. Agreement within 1 pct.
Confidence: high (~2 pct), small uncertainty from faint pale beak tip edge.
