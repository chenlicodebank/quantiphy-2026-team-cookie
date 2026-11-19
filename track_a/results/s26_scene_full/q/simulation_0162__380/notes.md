# Q380: acceleration of the ball at t = 2 s (m/s^2)

Prior: ball diameter = 0.21 m. No depth_info. fps = question_fps = 24, so t = 2 s is frame 48 and no re-timing is needed.

## Scene
This is a 2D side view. The camera is static, and the ball rolls left to right along a lane that is parallel to the image plane (the bands run horizontally with no perspective). Image x is therefore linear in world X, so one metres-per-pixel scale works.

## Scale (circfit.py, prof.py)
- I fitted a circle to the maximum-gradient rim points along radial rays, leaving out the bottom of the ball because of the shadow. The diameter is about 78.4–79.0 px near the image centre (frames 44–76). Frame 48 gives 78.8 px.
- The fitted width grows to about 83.5 px at both image edges. This is the off-axis stretching of a sphere's outline (it implies f ≈ 2400 px). It is not a change in depth, so I took the scale from frames near the image centre.
- A check on the raw grey profile at frame 60 (row 647), with the partial-pixel coverage at each edge read off, gives a width of about 78.8 px.
- The scene record's 80.2–81.6 px comes from a difference-mask threshold that includes anti-aliased halo pixels, so it is too large by about 1.5 px.
- I used D = 78.8 px, so the scale is 0.21 / 78.8 = 2.665e-3 m/px.

## Acceleration (accel.py)
- x(t) from the scene track and from my own independent gradient-circle track agree within about 1 px. My own blue-mask tracker (track.py) gives the same centres too.
- The acceleration is not constant: it falls from about 400 px/s² early in the clip to about 120 px/s² at frame 48. So I fitted polynomials only over windows around frame 48:
  - Instantaneous value at frame 48: 121–127 px/s² across windows (18–93 with degree 4/5, 28–68 with degree 3, 34–62 and 38–58 with degree 2).
  - The benchmark convention (backward-difference speed, then a difference of speeds) on the smooth fits gives 123–131 px/s², since it is effectively centred at frame 47.
- I used a = 125 px/s², which gives 125 × 2.665e-3 = **0.333 m/s²**.

## Second-route check
The two independent trackers (the scene mask circle and my gradient-edge circle) give the same acceleration within 2 px/s². The two diameter methods (gradient fit and edge coverage) agree within 0.3 px. If I had used the scene record's 80.5 px diameter instead, the answer would be 0.326. Confidence: about ±5%.
