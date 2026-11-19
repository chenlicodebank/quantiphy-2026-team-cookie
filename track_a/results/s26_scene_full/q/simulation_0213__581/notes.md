# q_581 — dog speed at t = 1 s (frame 24, 24 fps; file fps = question fps)

## Scale (prior: black cat speed 0.94 m/s)
- Cat walks left→right at constant pixel speed: nose (bbox_x1) 529→921 px over frames 0–22 = 17.8 px/frame
  (record: 17.76, rms 0.7 px). 17.78 px/frame × 24 = 426.7 px/s → 0.94/426.7 = 0.002203 m/px in the cat's plane.

## Dog pixel speed at frame 24
- match.py: template-matches three dog torso patches (front, mid, rear; y 790–900) between consecutive frames.
  Backward shift 23→24: front 21.2, mid 21.2, rear 21.0 px → 21.1 px/frame = 506 px/s.
- Second route: scene record torso_cx / nose x0 steps around frame 24 (17–25 px/frame, mean ≈ 21–22) agree.

## Depth correction (the main uncertainty)
- The dog walks in a nearer lane (paws at y≈1066 vs cat's ≈1020; it hides the cat). With a level camera
  (horizon ≈ y 540) the dog's depth / cat's depth = (1020−540)/(1066−540) ≈ 0.91. If the camera is tilted
  down the ratio is 0.93–0.96. I could not pin the horizon down from the props.
- Same-plane value: 21.1/17.78 × 0.94 = 1.116 m/s. Depth-corrected (0.913): 1.019 m/s.
- Answer 1.06 m/s, which is between the two. It is within about 5% of both the level-camera value and the
  pure 2D value, and close to the tilted-camera range.

Confidence: pixel speeds ±2%. The depth factor adds about ±5%.
