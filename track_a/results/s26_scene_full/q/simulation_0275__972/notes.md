# Q972 – raccoon speed at t = 1.0 s (frame 24)

- Video type: 2D simulation, 24 fps (same as question_fps). Static camera, motion is horizontal, and the apparent size stays constant, so one planar scale applies.
- Scale from the prior (length with tail = 1.51 m): nose-to-tail-tip bbox width is a median of 328 px over all frames (range 310–333; it is shorter when the body is compressed in the gait). My own segmentation (measure.py) gives the same median, 328 px, as scene/. Scale = 1.51/328 = 4.604e-3 m/px.
- Pixel speed: the centroid's linear fit over frames 1–71 gives 22.48 px/frame (scene/ record: 22.59). The tail tip and nose tip give the same slope (22.48 and 22.46). Over one gait cycle around frame 24 the mean is 22.43 px/frame. The raw one-frame step at frame 24 is 22.75–22.88 px, which includes gait wobble. The rig root should move evenly, so I used about 22.5 px/frame = 540 px/s.
- Speed = 540 × 4.604e-3 ≈ 2.49 m/s. With the raw frame-24 step it would be 2.52; with the maximum length of 331 px as the scale it would be 2.46.
- Answer: 2.48 m/s. Confidence: good (about ±3%).
