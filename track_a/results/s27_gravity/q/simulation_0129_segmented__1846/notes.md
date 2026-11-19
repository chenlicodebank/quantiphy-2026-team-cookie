# q_1846 — ball diameter (simulation_0129_segmented)

Question: "What is the diameter of the ball in meters?" Prior: gravity acc = 9.8 m/s^2. No depth_info. The file and the question are both 24 fps.

## What the video contains
- The video has only one object, an orange and black Toyota forklift in side view, driving right along y ≈ 928 (wheel bottoms). The scene/ record says the same.
- **There is no ball in any frame.** scan.py and scan2.py search all 40 frames for connected non-white components, at difference thresholds of 15 and 4 grey levels. Each frame has only the forklift blob. The few other blobs have 4–180 px of area, and are either compression specks or stick to the forklift's mast top. None of them persists, is round, or moves ballistically.
- Nothing in the clip falls, so the gravity prior gives no usable scale for a ball.

## Measurements made (fit.py)
- Forklift: about 257 px long and 194 px tall, with a wheelbase of about 158 px.
- It accelerates uniformly from rest starting at t ≈ 0. A quadratic fit over frames 4–39 gives 528 px/s² from the rear edge and 530 px/s² from the mask centroid.
- **Scale from the forklift's real size.** A Toyota 8-series forklift is about 2.5 m long to the fork face, about 2.1 m high at the overhead guard, and has a wheelbase of about 1.6 m. That gives about 0.0103 m/px. At this scale the forklift accelerates at about 5.4 m/s², not g.
- **Check of the alternative.** If the forklift's acceleration were 9.8 m/s², the scale would be 0.0185 m/px. That makes the forklift 4.8 m long and 3.6 m tall, which is implausible. So the gravity prior does not describe the forklift's motion.

## Answer
The ball can't be measured because it doesn't appear in this segmented clip. The answer, 0.22 m, is a guess at a typical real-world ball (soccer, basketball or bowling ball, all about 0.22–0.24 m), consistent with a scene built at real-world scale. **Confidence: very low.**
