# Q2347 - distance between the tennis ball and the soccer ball at 3.0 s (cm)

The file and the question both run at 24 fps. **The clip has only 49 frames (0-48, ending at 2.0 s). t = 3.0 s would be frame 72, which is not in the file**, so the answer is extrapolated.

## Method (lab card)
- f = 0.5959 x 1280 = 763 px, principal point (640, 360). Back-projection: ((u-cx)/f, (v-cy)/f, 1) x depth.
- Depths: soccer ball 2.80 m (given). The tennis ball's depth is not given, so I used the near person's distance (2.002 m), because she holds and drops it.
  - Cross-check: a real tennis ball (6.7 cm) at 20.5 px would be about 2.5 m away, and its floor-contact row also suggests it is farther than 2.0 m. So the true depth may be larger. I kept 2.002 m because that is the value depth_info provides.
- The ball centres come from the scene tracks (bbox centres), which I checked on frames 0 and 48.
- By 3.0 s both balls are on, or bouncing low over, the floor:
  - Tennis ball: e^2 ≈ 0.5, so several bounces have died out by 3.0 s.
  - Soccer ball: the rebound apex is at about 2.0 s.
- Vertical positions at 3.0 s were taken at floor level: soccer centre v ≈ 554.5 (contact at y = 577), tennis centre v ≈ 606 (contact at y = 616).
- Horizontal drift after the bounce, from a fit:
  - Soccer ball: +2.06 px/frame (moving right).
  - Tennis ball: -0.23 px/frame.
  - Extrapolated over 24 frames with partial damping (fraction 0.5-1.0).

## Results (compute.py)
- Frame 48 (t = 2.0 s): 1.000 m.
- t = 3.0 s on the floor, by drift fraction: 0 → 1.001 m, 0.5 → 0.946 m, 0.7 → 0.925 m, 1.0 → 0.897 m.
- Most of the separation is depth (0.80 m). The horizontal part is 0.39-0.60 m and the vertical part is under 0.1 m.

## Answer
**93 cm.** Confidence is low to moderate:
- The time asked for lies beyond the end of the clip.
- The tennis ball's depth is assumed.
