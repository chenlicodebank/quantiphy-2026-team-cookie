# Q71: distance between the black-shirt and white-shirt persons at t = 1.0 s (frame 24)

- The camera is top-down and static, and both people walk at the same depth (their apparent sizes stay constant), so this is treated as 2D with one m/px scale.
- Frame 24 checked visually: black torso is at about (1273, 413) and white torso at about (657, 610). This matches scene/tracks.
- Scale comes from the prior (black speed = 1 m/s). Mean black torso step over frames 2–71 is 11.48 px/frame, which is 275.5 px/s. That gives 0.003630 m/px.
  - The per-frame step varies ±8% with gait (10.6–12.6 px). The mean is used as the constant walking speed.
- Torso–torso distance at frame 24 is 646.1 px, which gives **2.345 m**.
- Checks:
  - Using the instantaneous step at frame 24 (11.11 px) gives 2.42 m.
  - Using the head points (716 px apart, 12.14 px/frame) gives 2.46 m. The head sits ahead of and above the pelvis, so it inflates the separation once the two have passed each other.
  - Perspective scaling of the pelvis height relative to the torso cancels in the ratio, because both people are at the same height.
- Answer: 2.345 m. Confidence is moderate (about ±4%).
