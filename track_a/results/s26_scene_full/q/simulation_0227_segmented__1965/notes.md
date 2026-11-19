# q_1965: acceleration of the "red general chess" at t = 1.5 s

## Object identification
No chess piece is visible anywhere in the frame. Over the whole image (scan.py), the only red or pink pixels belong to
the pink inflatable flamingo float. The only moving objects are the cat (a steady walk, about zero acceleration)
and the float, which speeds up and then slows down. So I took the asked object to be the float (the label looks like
an asset-name mismatch in the question). This identification is the main uncertainty.

## Time base
fps = question_fps = 24, so t = 1.5 s is frame 36.

## Scale (2D convention, one m/px from the prior)
The cat's centroid x is linear in time: slope 5.465 px/frame (its bbox front edge gives 5.463), and vy is about 0.
That is 131.15 px/s. With the prior of 1.041 m/s, the scale is 0.007937 m/px.

## Float motion
Centroid track from scene/tracks/flamingo_float.csv (checked: the float's width stays at 158 px, so its depth is
constant, and y drifts only about 3 px). The x(t) curve fits a Blender Bezier ease-in-out (smoothstep) almost
exactly: x = 733.2 + 429.4·S((i - 0.05)/49.05), with rms 0.41 px. That puts the keyframes at video frames 0 and 49.
- From the smoothstep fit, using the paper's convention (backward-difference speed, then the difference of speed),
  the acceleration at frame 36 is -262.2 px/s², which is -2.081 m/s².
- Second route: a cubic polynomial fitted to the whole range gives -2.081 m/s². Using the bbox-midpoint reference
  instead of the centroid gives -2.094 to -2.097 m/s².
- Local quadratic fits centred on frame 36 give -2.05 (±4 frames) to -2.24 (±8 frames) m/s². This is consistent:
  the deceleration grows with time on a smoothstep. The raw noisy one-frame value is -2.7 m/s², which is just noise.

Answer: the magnitude is 2.08 m/s² (the float is decelerating).

## Confidence
The measurement and the scale are good to within a few percent. Two caveats:
- The float and the cat may sit at different depths. The 2D single-scale convention was assumed.
- The object identification above.
