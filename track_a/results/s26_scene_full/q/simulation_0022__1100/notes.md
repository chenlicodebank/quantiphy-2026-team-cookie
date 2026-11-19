# Q1100 – height of the boat (prior: boat length = 10 m)

Method: I treated this as a size-to-size ratio in one image plane. The boat is seen side-on, so height = 10 m × (pixel height / pixel length), both measured on the same frame.
- Length: bow tip to stern of the red hull, on frames where the whole boat is visible (35–74). The scene record gives 288 px at frame 50, 290 at 60, 292 at 70 and 292–293 at 74. The pixel length grows as the boat slowly approaches the camera, so I took the length and height from the same frame each time.
- Height: from the mast top to the bottom of the dark keel/underside. `measure.py` checks this with column profiles. The mast top is at y = 388–391 on every frame. The dark underside ends at y ≈ 682–684, where the brightness jumps to water. That gives a height of about 294 px at frame 50. The record's bbox heights (297–301 px) include 2–4 px of dark water.
- Ratio: my measurement gives 294/288 = 1.02. The record's bboxes give 1.027–1.031 (frames 50, 60, 74). I used about 1.02–1.025, which gives a height of **10.2 m**.

Second route: on frames 60, 70 and 74 the height/length ratio stays between 1.02 and 1.03, so the answer is the same whichever frame is used. The fps (25 vs 24) does not matter for a size.

Caveat: any part of the hull below the waterline (the stern legs and rudder reach into the water) cannot be seen. If the model's bounding box includes it, the true height would be a few percent larger. Confidence: moderate-high, about ±5%.
