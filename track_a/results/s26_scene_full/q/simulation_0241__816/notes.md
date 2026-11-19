# q_816: speed of the rabbit at 1 s (m/s)

Prior: the horse at the back moves at 0.874 m/s. No depth_info. The scene is 2D (top-down, static camera), fps = question_fps = 24, so t = 1 s is frame 24.

## Identification
- Horse at the back = the brown horse (scene `brown`, upper, y≈777). It trails the other animals and is farthest from the front of the group.
- Rabbit = the small tan animal (scene `small`, y≈924), about 36x21 px. It hops: the rear bunches up and then extends, while the head moves forward fairly steadily (frames/strip.png).

## Scale (from the horse)
- Horse pixel speed from template matching of the horse crop between frames at the same gait phase (tmatch.py): 0→24, 24→48, 0→48, 0→47 and 2→48 all give 2.637-2.670 px/frame, median ≈ 2.648 px/frame = 63.55 px/s.
  (Scene-record centroids: endpoints give 2.593 and the linear fit gives 2.70. Both are noisier because of the colour mask.)
  Frame 49 is the horse's loop reset and is excluded.
- Scale = 0.874 / 63.55 = 0.01375 m/px. Sanity check: horse length 144 px ≈ 1.98 m, which is plausible.

## Rabbit speed
- Template matching of the rabbit between frames one and two hop cycles apart (period = 21 frames; tmatch_rabbit.py, 36 pairs, correlation > 0.95) gives 4.544 px/frame (spread 4.531-4.558). That is 109.1 px/s, or **1.50 m/s**.
- Second route: linear fits of the scene-record tracks (centroid, front edge, rear edge) give 4.538-4.556 px/frame (1.47-1.48 m/s with the centroid-fit scale, 1.50 m/s with the template scale). The mean per-frame step is 4.59 px, giving 1.51 m/s.
- Caveat: the mask centroid's one-frame step at frame 23→24 is 6.76 px (≈2.2 m/s), because the hop deforms the body (the rear end catches up). The horse prior is a single constant value, which suggests the rig origins move uniformly, so I answer with the cycle-averaged root speed. If the reference used a hip point that surges with the hop, the answer would be about 2.2 m/s instead.

Answer: 1.50 m/s. Confidence: moderate. The scale is good to about 1%; the main risk is the uniform-root assumption.
