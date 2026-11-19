# q_101 — speed of black/white car at 1.0 s

- 2D top-down scene, static camera, fps 24 (= question_fps), t=1.0 s -> frame 24.
- Scale: yellow car length 270 px near image centre (record + own measure.py: 270 px in frames 0–28) = 5.67 m
  -> 0.021 m/px.
- Black car motion: constant velocity from frame 2. Own measurement of rear edge (dark rear half): frames 16->32
  860->1084 (14.0 px/frame), 20->28 916->1028 (14.0 px/frame); single-frame 23->24 = 13, 24->25 = 15 (1-px quantisation).
  Record bbox centre: 1091->1105->1119 (14 px/frame), mean 13.96 px/frame over the clip.
- Speed = 14.0 px/frame x 24 fps x 0.021 m/px = 7.06 m/s.
- Second route: record bbox-centre track gives the same 14.0 px/frame; with 13.96 -> 7.04 m/s.
- Confidence: high (~2%); main uncertainty is the 1-px quantisation in the single-frame difference, but motion is constant.
