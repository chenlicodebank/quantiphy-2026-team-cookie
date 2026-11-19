# Q367 — How long is the shark (m)?  Answer: 4.46 m

Prior: turtle acceleration = 2.639 m/s^2. No depth_info. 2D scene (static camera, both animals swim
right-to-left in a plane facing the camera). fps = question_fps = 24, so no re-timing issue.

## Scale from the turtle's pixel acceleration
- Turtle x-track from scene/tracks/turtle.csv (rigid carapace template); for frames 27-47 I re-tracked with a
  multi-scale carapace template (track_scale.py): positions agree with the record within 1-2 px, apparent scale
  0.99-1.01 (no depth change, no perspective effect).
- Turtle starts from rest at t=0 and accelerates uniformly:
  - x = x0 + a t^2/2 fit, all 48 frames: a = 540.5 px/s^2 (rms 1.7 px); halves 536 / 540.
  - free quadratic, all frames: 542 px/s^2, v0 ≈ 0.
  - local speeds (9-frame quadratic fits) vs t: linear slope 538.7 px/s^2, intercept ≈ 0; v/t = 492-561, ~535 mean.
  - two-point (d at frames 36, 47): 529 px/s^2.
  - Late-window-only free fits give ~480-490 with nonzero v0; that comes from the record's template switch at
    frame 25/26 (small offset) plus poor conditioning — rejected.
  - Adopted a_turtle = 538 px/s^2 → scale = 2.639 / 538 = 0.004905 m/px.

## Shark length in pixels
- Frame 30 zoom (frames/shark30.png): snout tip x ≈ 670, upper tail-lobe tip x ≈ 1579 (lower lobe ~1553),
  body horizontal → AABB length ≈ 910 px. Record gives 911 (908-916 over frames 26-37). Constant over frames
  26-37, which also confirms no perspective change across the frame.

## Result
L = 910 px × 0.004905 m/px = 4.46 m.
Range from the acceleration alternatives (529-542 px/s^2): 4.43-4.54 m.
Sanity: turtle whole-animal ~320 px → 1.57 m (leatherback-like); shark 4.5 m (great white-like). Shark pixel
acceleration 1410 px/s^2 (ratio 2.62 to the turtle, matching the displacement ratio 2.64) → 6.9 m/s^2 in the same plane.
Confidence: good (~±3 %), assuming the shark moves in the same plane as the turtle (2D convention).
