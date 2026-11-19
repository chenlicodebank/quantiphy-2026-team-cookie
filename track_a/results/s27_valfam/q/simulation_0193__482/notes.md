# Q482: Ganymede speed at 1 s (m/s)

The scene is a 2D, top-down Jupiter system. The file rate and question_fps are both 30, so t = 1 s is frame 30.
In the frame at t = 1 s, the labels show that Ganymede is on the 3rd orbit and Callisto on the outermost one, as the prior says.

Scale comes from the prior, Callisto's speed of 0.627 m/s. All moons move in one plane, so a single m/px scale applies. Every moon moves in uniform circular motion (from the scene record, checked here), so its speed at 1 s equals its constant model speed.

- Route 1 (scene record, model fit): Ganymede 78.6 px/s, Callisto 61.0 px/s, ratio 1.2885.
- Route 2 (measure.py, my own centroid tracking with the circle and angular-rate fit): Ganymede 79.06 px/s, Callisto 61.35 px/s, ratio 1.2887, giving 0.808 m/s.
- Mean of the per-frame step speeds: ratio 1.276, giving 0.800 m/s. This is consistent within the noise.
- The raw one-frame speeds at frame 30 are dominated by centroid noise (±5–8 px/s), so I used the uniform-motion speed.

Answer: 0.627 × 1.2886 = **0.808 m/s**. Confidence is high (about 1 %).
