# q_1804: length of the shark (m)

Prior: the shark's acceleration is 1 m/s². This is a 2D side-view clip at 24 fps (question_fps is also 24, so no re-timing), with a static camera.

## Scale from the prior
- Shark x tracks (scene/tracks/shark.csv), frames 2–58, while the shark is fully in frame. I fitted a quadratic
  x(frame) to each track (fit.py):
  - template_dx: 0.1480 px/frame², which is 85.2 px/s². Fitting only the first half (frames 2–30) gives 85.9 and only the second half (30–58) gives 84.8.
  - bbox_x0 (nose): 86.7 px/s². bbox_x1 (tail): 85.6 px/s². bbox centre: 86.2 px/s².
  - Taken together, the pixel acceleration is about 85.5 px/s² (±1 %). The acceleration stays constant across the
    clip, as a uniform acceleration should.
- Scale = 1 m/s² ÷ 85.5 px/s² = 0.0117 m/px.

## Shark length
- The nose-to-tail x extent of the mask is 280 px (median; range 278–286 because the tail flaps). I checked this by
  eye on a zoomed frame at t = 1.0 s: the nose is at about x 464 and the tail tip at about 743, so 279 px.
- Length = 280 × 0.0117 = 3.27 m.

## Second-route check
The independent fits (nose track, tail track, template track, and the two halves of the clip) give accelerations
between 84.8 and 86.7 px/s². That puts the length between 3.23 and 3.30 m.

Confidence: high (about ±3 %).
