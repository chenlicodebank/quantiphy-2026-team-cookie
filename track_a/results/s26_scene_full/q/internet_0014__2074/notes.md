# q_2074: distance between the two players at 9.00 s

- Scene: a top-down drone view of a pitch, treated as 2D, with a static camera (drift ≤2 px, corrected through x_stab).
- Scale: the prior is the centre-circle radius, 9.15 m. I fitted a circle to the line centres on frame 0 (`circle.py`, 334 edge
  points). Result: R = 116.82 px (ellipse axes 232.9 / 234.3 px, so the view is round). Scale = 0.07833 m/px.
  The scene record gives 116.9 px, which agrees.
- Players: I used the stabilised body-centre tracks from scene/tracks (`dist.py`) and checked them on a zoomed frame (frames/f270.png):
  A (light) is at about (1459, 575) and B (dark) at about (1402, 653). Neither is occluded in this window.
- Time: 9.00 s is frame 268 at the file's fps (29.764) and frame 270 at question_fps (30). The two rates differ by only 0.8%,
  so physics cannot tell them apart.
  - Frame 268: 96.29 px, 7.54 m
  - Frame 269: 96.94 px, 7.59 m
  - Frame 270: 97.21 px, 7.61 m
  
  I answered with frame 269 (7.58 m), which is within 0.6% of both readings.
- Check: reading the blob centres by eye on the frame-268 crop gives about 94 px (7.4 m), within about 2% of the track.
  A second scale check, the penalty-area depth (16.5 m / 217.5 px = 0.0759 m/px), is 3% lower. The prior's circle is
  used as the convention requires.
- Confidence: about ±3%.
