# q341: rocket speed at t = 1 s
- 2D side-view scene with a static camera at 24 fps (file fps = question fps). t = 1 s is frame 24. Speed = |p24 - p23| x 24.
- Scale comes from the prior, rocket length 2.9 m. I re-measured the rocket length (measure.py) as the distance between the 50% points
  of the along-axis profile in free-flight frames 15-22: 199.4-203.3 px, median about 201.5 px. This matches the record's 201.8.
  Scale = 2.9/201.5 = 0.01439 m/px.
- At frame 24 the nose has left the image, so I tracked the tail end, which is a point fixed on the rigid rocket. Tail advances:
  f22 59.9, f23 59.9, f24 59.7 px/frame. Cubic fits to the tail positions give 60.5-61.0 px/frame at frame 24, and a quadratic fit
  gives about 62-63, which is worse because the cubic leaves smaller residuals. The record's centre track gives 61.9.
  Adopted value: 60.5 px/frame.
- Speed = 60.5 x 24 x 0.01439 = 20.9 m/s.
- Second route: the record's centre track (tail + L/2) gives 62 px/frame, which is 21.4 m/s. The two routes agree within 3%.
- Confidence: good, about 3%. The main uncertainty is whether "length" means the rocket's long axis (as assumed here) rather than
  its tilted world-space AABB x-extent.
