# q_843: speed of the front horse at 1 s (m/s)

Prior: speed of the back horse = 0.874 m/s. No depth_info is given. Both fps and question_fps are 24, so frame 24 is t = 1 s.

## Scene
- The scene is 2D: a top-down camera looks at the ground plane, and all animals walk toward +x in parallel lanes. One m/px scale applies to the whole image.
- **Front horse:** the tan horse in the middle lane. It is ahead in x, at about 1157 px at frame 24.
- **Back horse:** the brown horse in the top lane, at about 703 px at frame 24.
- Both horses walk at a constant speed throughout the clip.

## Method (`period.py`)
- I used non-chained template matching of the whole animal from frame a to frame b. The pair (a, b) with the highest correlation is the frame one gait cycle later, where the pose is identical. Its displacement is therefore a pure root displacement, with no gait or pose bias.
- **Back horse:** the cycle is about 43–44 frames. Pairs (0→43/44), (4→46), (8→48) give 4.45 px/frame (4.447–4.454), and dy ≈ 0.
- **Front horse:** the cycle is about 31–32 frames. Pairs (0→31), (4→36), (8→40), (12→44) give 7.80 px/frame (7.789–7.821), and dy ≈ 0.
  - The lane wobble of ±7 px in the scene record's cy is body sway within the gait cycle, not root motion.
  - Speeds measured from different start frames agree, so the speed is constant and the speed at 1 s equals this value.
- **Scale:** 0.874 m/s / (4.45 × 24 px/s) = 0.008184 m/px.
- **Front horse speed:** 7.80 × 24 × 0.008184 = **1.532 m/s**.

## Second route
I took linear fits of the scene record's torso-core centroids:
- back horse: 4.36–4.44 px/frame
- front horse: 7.72–7.73 px/frame

The ratio is 1.74–1.77, which gives 1.52–1.55 m/s and agrees with the main route.

Chained frame-to-frame template matching drifts (4.03 and 7.54 px/frame), so I did not use it.

The record's claim that the back horse is stationary at frames 46–48 is a bbox artifact: pose matching shows it moving steadily. Frame 49 is a loop reset, so I excluded it.

## Confidence
High. The answer depends only on the ratio of the two speeds, and that ratio is measured to about 1%.
