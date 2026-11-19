# Q931: speed of the spacecraft (hover car) at 0.5 s

- Prior: the acceleration at 1.0 s is 4 m/s². The video is a 2D render at 24 fps, matching question_fps. There is one vehicle, and it accelerates left from rest.
- Track: scene/tracks/hovercar.csv. The front edge x0 is visible and clean in frames 0–52. ref_x is the bbox centre, and x1 is the rear edge.
- Method (fit.py): I fitted x = xs − ½·a·(f − f0)² for f ≥ f0, and x = xs before that, by least squares over f0.
  - x0: a = 1.138 px/frame², f0 = 0.12, rms 0.49 px.
  - x1: a = 1.178 px/frame², f0 = 0.155.
  - ref_x: a = 1.146 px/frame², f0 = −0.22. This is the noisiest series.
  - A free quadratic on frames 9–52 gives a vertex at f ≈ 0.15–0.16 for all three edges. The cubic terms are negligible, so the acceleration is uniform from rest, starting at about frame 0.15.
- Since the acceleration is constant, the scale cancels: v(0.5 s) = speed at frame 12 (backward difference) = a·(12 − f0 − 0.5)/24 = 4·(11.35)/24 ≈ 1.89 m/s.
  - Different edges give between 1.89 and 1.95.
  - If the motion started exactly at frame 0, the result would be 1.917.
- Second route: the px-scale route gives the same value. The scale is 4/(1.15·576) m/px. The step at frame 12 is about 13.0–13.4 px/frame, so v ≈ 13.2·24·4/662 ≈ 1.91 m/s.
- Answer: 1.9 m/s. Confidence is high (±3%).
