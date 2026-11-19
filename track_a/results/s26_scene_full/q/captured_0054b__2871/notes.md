# q_2871 – soccer ball velocity at 0.5 s (frame 12 at question_fps 24 = file fps)

## Finding
At t = 0.5 s the soccer ball is **not moving**. The crouching person is holding it at rest near (918, 612) px.
It is released and starts rolling only at frame 24 (t = 1.0 s). At frames 10–14 the pushing arm passes in front
of it, which is why the scene/ track's centroid jumps around there (occlusion, not motion).

## Measurement (edges.py)
The script tracks the ball's unoccluded top edge (white vs floor, columns 898–919) frame by frame:
- median top edge = 586.0 px in every frame from 0 to 14, and 586.5 at frame 15. It only starts to shift (587–595)
  from frame 16, when the hand adjusts its grip before the release.
- The left edge is also constant (892 px) from frames 0 to 10, while it is visible.
- So the motion around frame 12 is under 0.1 px/frame. Depth from apparent size: 56 px at rest vs 37 px at
  3.254 m (t = 2 s) gives about 2.15 m, and f = 763 px. That puts the speed below about 0.01 m/s, which is
  essentially zero.

## Second route
Visual checks of zoomed crops at frames 9, 12 and 15 show the ball's top/left outline in the same place.

## Answer
The physical answer is about 0 m/s. A positive number is required, and the reference comes from clicked centres
differenced over adjacent frames, so it may hold a small noise velocity. I answer **0.05 m/s**, which is the
typical size of click/depth noise after 5-frame smoothing. Confidence is low that this matches the reference
numerically; confidence is high that the ball is at rest.
The prior (basketball/orange ball 2.21 m/s at 0.5 s) is about a different object and does not set this value.
