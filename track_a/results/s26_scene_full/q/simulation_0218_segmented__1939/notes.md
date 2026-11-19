# q_1939 – length of the big robot (m)

Prior: speed = 5.924 m/s. 2D video, static camera, 24 fps (file and question rate agree). Only one robot,
driving right at constant speed.

## Scale
- scene/ record: chassis tread band moves 50.79 px/frame (linear fit, residual < 0.5 px) = 1218.9 px/s.
- Check (measure.py): the robot's rear (left) silhouette edge moves 29 -> 182 -> 335 -> 488 -> 641 -> 793 -> 946 px
  at frames 9..27 (step 3) = 50.9 px/frame, which agrees. (My own tread template match failed on clipped frames, so I
  used the record's fit plus this edge check.)
- Scale = 5.924 / 1218.9 = 0.004860 m/px.

## Length
- Mask bbox horizontal extent (rear lens head to drill tip): f20 636 px, f21 640 px. At f21 the robot is centred
  on the image (bbox centre x = 960.5), so that is the most side-on view. Perspective makes it 613-696 px
  elsewhere.
- Length = 638 px (mean of f20 and f21) x 0.004860 = 3.10 m (f20 alone: 3.09, f21 alone: 3.11).
- Height for comparison: 623 px = 3.03 m.

Confidence: moderate. The scale comes from the near-side chassis points. Perspective in the silhouette may
add a few percent.
