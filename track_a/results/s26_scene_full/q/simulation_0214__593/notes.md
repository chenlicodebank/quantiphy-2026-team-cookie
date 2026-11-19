# q_593: speed of the dog at t = 1.5 s (m/s)

Prior: the black cat's speed is 0.94 m/s. No depth_info. fps = question_fps = 24, so t = 1.5 s is frame 36 and the speed is the step from frame 35 to frame 36.

## Identification
The scene is shown top-down with two animals. scene/ calls the lower, larger orange/brown animal "tabby_cat". It is clearly bigger than the black cat (body about 251 px against 156 px; width 104 px against 41 px). It is the only animal besides the black cat, so it is **the dog** in the question.

## Scale (2D, one scale for the shared floor plane)
- The black cat walks at a steady pace along +x.
- Linear fits over frames 0–49 give 10.94 px/frame from body_cx, 10.98 from bbox_x1 and 10.96 from cx. Half-clip windows give 11.00 and 10.94.
- I use 10.97 px/frame, which gives 0.94 / (10.97 × 24) = 3.57e-3 m/px.

## Dog step from frame 35 to 36
- I wrote my own NCC template tracking (track_rump.py) with sub-pixel peaks:
  - rump patch (near the pelvis): 11.50 px
  - mid-body: 11.25 px
  - whole body: 11.24 px
- The record's torso track gives 11.18 px. Vertical motion is about 0.2 px.
- The neighbouring steps are smooth (12.1 at frame 35, 10.7 at frame 37), so no smoothing is needed.
- Dog step: **11.3 px/frame** (±0.15).

## Result
- Dog speed = 11.3 / 10.97 × 0.94 = **0.968 m/s** (pure planar ratio).
- Perspective: the walls' inner faces show a perspective camera. The tracked surfaces are the animals' backs, and the dog's back is higher (about 0.3 m) than the cat's. That makes the dog's image speed slightly too large compared with its true speed.
- The camera height is not well constrained:
  - vase and lamp parallax suggest about 5–13 m
  - the furniture shows almost no side faces
- So the correction is somewhere between 0 and −6%. I applied a hedged −2%, giving a final answer of **0.95 m/s**.

## Second route
- Over frames 34→38 the dog averages 11.1–11.3 px/frame, depending on the track.
- Local quadratic fits of body_cx give 11.6, but they are biased by the speed peak at frame 32.
- All routes give 0.94–1.00 m/s before the perspective correction.

Confidence: moderate-high (±4%).
