# q_1713: diameter of the ball (m)

The file rate and question_fps are both 30.

## Measurements (scripts fit.py and held.py, plus scene/tracks/ball.csv)
- Ball apparent diameter in flight (frames 24-78): 35.06 ± 0.84 px. The given depth is 13.80 m at t=1 s and t=2 s (frames 30 and 60).
- Ball held at the waist (frames 1-2, red component): 32-35 x 35-36 px. That is the same size as in flight, so the held ball is at about the same depth.
- Player standing (frames 60 and 90): head top to soles is 217 px. The player faces the camera, and the ball is held about 0.3 m in front of the body, so the player is at about 14.1 m.
- The cars named in depth_info (orange and green) do not appear in this segmented video, so they cannot be used.

## Gravity prior: no usable scale
The ball's motion is keyframed, not ballistic:
- In flight, the image vertical acceleration is 116-211 px/s² and the horizontal speed changes strongly.
- Taking g = 9.8 at Z = 13.8 m would need f ≈ 220-300 px, which is a horizontal FOV above 145°. That is impossible.
- Below the net, the ball falls at a constant ~13 px/frame (frames 108-114) and then slows down before it reaches the floor (frames 115-119). Free fall cannot do that.
- The bounce timing gives nonsense (a ball of about 0.05 m).

So the scale has to come from objects of known size.

## Scale from standard objects (they disagree by about 20%)
- If the ball is a regulation basketball (0.24 m): f = 35.06 × 13.8 / 0.24 = 2016 px (HFOV 51°), and the player comes out at 217 × 14.1 / 2016 = 1.52 m. That is at the lower bound for an adult.
- If the player is 1.80 m: the ball is 35.06 × 13.8 / (217 × 14.1 / 1.80) = 0.285 m (0.29 m if the player and ball are at the same depth).
- Ratio check: player / ball = 6.2-6.3 in this scene. In reality it is about 7.5.

## Answer
I compromised between the two readings and answered 0.26 m. That implies f ≈ 1860 px (HFOV 55°) and a player height of about 1.65 m. Confidence is low to moderate: the true value is likely between 0.24 and 0.30 m.
