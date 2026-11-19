# q2888: distance between the orange ball and the soccer ball at 1.0 s (frame 24)

The file and the question both use 24 fps, so 1.0 s is frame 24. Lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).

## Orange ball (basketball)
- Frame 24 centre: (537.9, 384.6). This is a circle fit from scene/; the ball is clean in this frame.
- Depth: 1.81 m from depth_info. It is back-projected with the method-card formula ((u−cx)/f, (v−cy)/f, 1) × depth.
- Inconsistency: the ball's apparent diameter (75.8 px at frame 12, 60.4 px at frame 24) does not match the given depths (2.24 m, then 1.81 m). With 2.24 m it is a 0.22 m basketball, and frame 24 would then be at about 2.81 m.

## Soccer ball
- Frame 24 position: the ball is still leaving the hand, and its right side is hidden.
  - Centre: about (922, 607). Taken from the visible left edge plus the radius, and consistent with frames 25 and 26 at about −3.5 px per frame.
  - Diameter: about 68 px. The visible height is about 66–70 px; frames 25–28 are about 67–71 px; a 1/d trend fit gives 65.5–69.
- Depth:
  - At t = 2.0 s the ball is at 3.254 m with a diameter of 51.9 px, so it is 0.221 m across (a size-5 ball).
  - So at frame 24, Z = 0.221 × 762.8 / 68 = 2.48 m.

## Result
- Distance = |P_orange − P_soccer| = **1.535 m**.
- Sensitivity:
  - Soccer diameter 66 or 70 px gives 1.60 or 1.47 m.
  - Using the size-based orange depth of 2.81 m instead of 1.81 m gives 1.514 m (second route).

So the answer barely depends on the doubtful orange depth. The main uncertainty is the soccer ball's size at frame 24 (about ±4%). Confidence: moderate to good.
