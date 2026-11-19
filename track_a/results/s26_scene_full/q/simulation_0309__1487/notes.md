# q_1487: displacement of the dragon from 0.5 s to 1.0 s

Question fps = file fps = 24, so the interval is frames 12 to 24. Prior: speed = 1.29 m/s, with no time attached, so I read
it as a constant speed. depth_info: 5.2108 m at frame 24 and 6.3261 m at frame 48.

## Method (fit.py)
- I used the hip track from scene/tracks/dragon.csv and took the principal point at the image centre (1439.5, 719.5).
- Assuming a straight path at constant speed, I put the frame 24 and frame 48 points on their rays at the given depths.
  I then solved for the focal length that makes their separation 1.29 m (1.29 m/s x 1 s): f ≈ 3490 px, which is a
  horizontal field of view of about 40° over the 2560 px active width.
- Check: projecting this constant-velocity straight line back onto the image reproduces the hand-marked hip at
  frame 0 ((2113, 1049) against (2115, 985)) and the whole track from frame 0 to 48. The deviations are within the hip's
  flapping bob (≤ about 60 px, mostly in y during strokes). The motion is consistent with a straight path at constant
  speed.
- Glide size check: the bbox shrinks by a factor of 1.165 from frame 52 to 71. The model's depth ratio is about 1.135.
  These agree.
- Displacement = 1.29 m/s x 0.5 s = **0.645 m**. Model depths: 4.69 m at frame 12 and 5.21 m at frame 24.

## Second route (fit2.py)
I fitted the line with both f and speed free to the pixel track. This route is degenerate: focal length and speed
trade off along the nearly radial path, and the fits gave 1.1 to 2.2 m/s. So the pixel track cannot fix the speed
independently. It only confirms that the path is close to straight and the velocity close to constant. The prior
therefore sets the scale.

## Confidence
Moderate to high, if the rig moves at constant speed in a straight line, which the track supports. The answer would
be wrong if the prior speed applies only to some other moment.
