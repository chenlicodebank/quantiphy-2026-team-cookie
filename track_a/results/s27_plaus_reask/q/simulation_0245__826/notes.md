# Q826 – height of the antelope (m)

Prior: antelope speed = 1.277 m/s. depth_info: none. This is a 2D scene: the camera is static and the animal walks parallel to the image plane at a constant apparent size. File fps and question_fps are both 30.

## Scale from the prior
- I fitted a line to x against frame for several body-fixed points from scene/tracks/creature.csv (measure.py). The slopes were: centroid 6.470, torso centre 6.473, rump 6.497, chest 6.450, tail tip 6.540 and bbox centre 6.423 px/frame. Net displacement over frames 0–74 gives 6.32–6.51.
- I adopted 6.47 px/frame = 194.1 px/s. The vertical gait bob is only a few px, so it does not affect this.
- Scale: 1.277 / 194.1 = 0.006579 m/px.

## Height
- The height is the world-AABB vertical extent, with the horn included: from the horn tip (y≈1123) to the hoof contact line (y≈1549).
- bbox_h median is 427 px (range 422–432), and it is stable across all 75 frames. I checked it on frame 30 with a gridded view: the horn tip is at ≈1125 and the hooves at ≈1548.
- Height = 427 × 0.006579 = **2.81 m**.

## Checks
- An independent route is the same height read off frame 30 by grid: 423 px → 2.78 m. This agrees within 1%.
- Plausibility: the shoulder is about 260 px above the ground, which is ≈1.7 m. That is the size of a large antelope such as an eland. The extra height comes from the tall horn.
- The rabbit is about 76 px long (≈0.5 m), which is large but within range for this fantasy scene.

Confidence: moderate-high. The main uncertainty is whether the reference "height" includes the horn. Without the horn, the top of the head is ≈1210 → ≈2.2 m.
