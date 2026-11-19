# q730: paper airplane acceleration at t = 1 s (frame 24, fps 24 = question_fps)

Where the earlier answers part ways: the convention, not the track. Both sessions have the same track. C2 (8.7)
gave the magnitude of the vector acceleration, sqrt(ax²+ay²); ay (about 3.7 px/f²) is the plane's vertical
curvature. C1 (3.1) gave the change of scalar speed, which is what the benchmark convention asks for:
acc = (speed(i) - speed(i-1)) x fps, with backward-difference speeds. I agree with C1.

My measurement (acc.py): I re-tracked the plane myself (median background, diff mask, weighted and binary centroids)
and also used the scene track's nose/tail midpoint.
- Change of scalar speed s24 - s23, taken on fitted positions (deg 2 and deg 3, windows 16-32, 18-30 and 20-28) and
  from the slope of a line fitted to speed: -1.08 to -1.59 px/frame². Central value about -1.4 px/f², which is
  -806 px/s².
- The raw single-frame difference is too noisy to use: -0.7 / +2.5 / +8.8 depending on the reference point.
- At the apex (frame 23) vy is about 0, so d|v|/dt is about equal to ax. ax is -1.3 to -1.5 px/f², which agrees.
- Scale: chalkboard length 5 m. Outer frame 1372 px gives 3.644 mm/px; green surface 1328 px gives 3.765 mm/px.
  - Outer frame: 806 x 3.644 = 2.94 m/s².
  - Green surface: 806 x 3.765 = 3.03 m/s².
  - Answer 3.0 m/s² (magnitude; the plane is slowing down).
- Confidence: moderate, about ±12 %. This is a second difference of noisy pixel positions.
