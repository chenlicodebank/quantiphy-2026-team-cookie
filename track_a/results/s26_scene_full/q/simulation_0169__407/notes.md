# Q407: speed of astronaut at t=3 s (frame 72, fps 24 = question_fps)
2D video, static camera. Scale from prior: astronaut height 2.2 m = 91 px (upright bbox at frame 0; mask height 91/90/89 px at
thresholds 25/50/80) -> 0.02418 m/px.
Pixel speed at frame 72 (backward difference 71->72), measure.py:
- mask centroid (thr 25): 1.76 px/frame; thr 60: 1.79; intensity-weighted: 1.74-1.77
- phase correlation of figure crops: 1.67 px/frame
- local linear trend of steps over frames 70-74 (ease-out deceleration): 1.67
Adopted 1.72 px/frame -> 1.72*24*0.02418 = 1.00 m/s (range 0.97-1.04).
Second route (phase correlation, independent of segmentation) agrees within 3 pct. Confidence: good (~±4 pct).
