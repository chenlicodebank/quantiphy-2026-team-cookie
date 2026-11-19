# q_687 – speed of the moving red general at t = 1.5 s

- 2D top-down scene, fps 24 (file and question agree). t = 1.5 s → frame 36.
- Track (scene record, re-measured with measure.py: background-difference mask centroid):
  frame 35 = 811.3 / 811.8 px, frame 36 = 849.3 / 849.6 px (record / mine). Frames 34 and 35 are the same image;
  frame 35 is its true position (the 33→35 step of 72.6 px is two normal steps), so 35→36 is a clean step.
  One-frame step 35→36 = 38.0 / 37.8 px → 37.9 px/frame.
- Check: neighbouring clean steps 36→37 = 39.0, 37→38 = 40.0, mean of 33→35 = 36.3 px/frame. They grow linearly
  (about 1 px/frame²), which gives 38.0 at frame 36, the same as the direct value.
- Scale: the general's diameter is 85.2–86 px (half-max edge profiles at frames 0 and 36 in diam.py, and a threshold-100
  mask of 86 px). The crop at frame 0 shows that the dark ring is the board gap between touching pieces, not part of
  the piece. I used 86 px, so 0.097/86 = 1.128e-3 m/px.
- Speed = 37.9 × 24 × 0.097/86 ≈ 1.027 m/s.
- Confidence: about ±2 %. The diameter's pixel value (85–87 px) is the main source of uncertainty.
