# q_2306: distance between the box and the soccer ball at 3.0 s, in cm

Answer: **67 cm** (low confidence; the likely range is about 56–82 cm)

## The problem
- question_fps = 24, the same as the file's rate. t = 3.0 s is frame 72, but the clip has only 49 frames (0–48, 2.04 s).
  So the state at 3.0 s **cannot be observed**. It has to be extrapolated from the last frames.
- The given numbers are: ball distance 2.80 m (at the question time), near person 2.002 m, far person 3.130 m. The box has no depth given.
  The prior (g = 9.8) is not used for scale.

## What the frames show (scene/ tracks checked against frames 39–48)
- The white box lands upright at frame 39, bounces, tips over and is lying on the floor by frame 46. At frame 48 it
  lies at a centre of about (423, 593.5) px, still sliding left by about 6 px/frame. I assume it comes to rest at about (415, 597).
- The soccer ball bounces at frame 39 (centre row 541, bottom row about 566). At frame 48 it is still rising (centre
  (554, 402.5)) and drifting right at about 2.3 px/frame, roughly 0.20 m/s.

## Geometry (estimate.py)
- f = 0.5959 × 1280 = 763 px, principal point (640, 360). Horizon row 342 is from scene.json, which gives a 1.35° upward pitch.
- Ball diameter from its pixel size: 44 px × 2.8 / 763 = 0.162 m.
- Camera height above the floor, from three independent references:
  - Ball at the bounce, assuming a distance of about 2.8 m: 0.785 m.
  - Far person's soles (row 575) under the torso at 3.13 m: 0.911 m.
  - Near person's feet (row about 685) under the torso at 2.002 m: 0.827 m.
- Box position: the ray through its resting image centre, cut at 0.035 m above the floor.
  This puts it about 2.2–2.6 m deep, about 0.7 m left of the axis.
- Ball at 3.0 s: lateral position = the frame-48 position plus 0.5–1.0 × 0.20 m/s × 1 s of drift.
  Height above the floor is between 0.08 and 0.30 m. Depth is fixed so that the distance to the camera is exactly 2.80 m.

## Results
- Central case (average camera height 0.84 m, 80 % of the drift kept, ball 0.15 m above the floor): 0.66 m.
- With each of the camera heights above: 0.73 m (0.785), 0.66 m (0.841), 0.65 m (0.911).
- Over the whole grid of assumptions: 0.56–0.82 m, median 0.674 m.

## Second check
The three camera-height references give box depths that differ by about 0.4 m. The distance changes much less,
because a deeper box sits nearer the ball's depth but farther from it sideways: the results stay within 0.65–0.73 m.
The biggest remaining uncertainty is where the ball is at 3.0 s, which is outside the clip.
