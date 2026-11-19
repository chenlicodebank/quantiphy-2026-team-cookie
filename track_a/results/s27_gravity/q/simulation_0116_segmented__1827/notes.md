# q_1827 – width of each door (m)

2D segmentation clip, 24 fps (file fps = question_fps = 24). Prior: gravity 9.8 m/s². No depth_info.

## Scale from the falling football (fit.py)
I fitted a quadratic to the football's centroid y(t) from scene/tracks/football.csv (checked: one object, falling
straight down, no bounce):
- frames 0-31: a = 1798.0 px/s² (rms 0.55 px); frames 0-25: 1797.7; frames 1-25: 1798.7; frames 5-31: 1799.5;
  bbox-centre variant: 1799–1804.
- I took a = 1799 px/s², so the scale is 9.8 / 1799 = 0.005448 m/px.

## Door width
Both "doors" (yellow cabinet doors with frame and dark top band) were measured in code on frame 12 using the mask min(RGB) < 240.
For each row I took the left and right edges of the mask, then the median over several row bands:
- upper door: 160 px (x 648-807); lower door: 160-161 px. Both are the same width.
- width = 160.5 px × 0.005448 = 0.874 m → **0.87 m**

## Checks
- Lower door height: 342 px → 1.86 m, and width 0.87 m. Both are realistic for a door with its frame, so the gravity
  scale gives real-world sizes.
- The football (~65 × 44 px → 0.35 × 0.24 m) comes out about 25 % larger than a regulation ball (0.28 m). It is probably
  somewhat closer to the camera than the doors. Its size is not used for the scale.
- If "width" means the door leaf only, without the frame (~150 px), the width would be about 0.82 m. I answered with the full door
  extent (the world bounding box).

Confidence: moderate-high. The scale is very stable (±0.3 %). The main uncertainty is whether the ball and doors are in the same
plane.
