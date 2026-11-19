# q_2822 – displacement of the trashbin, 0.4 s → 1.4 s

Question fps 24 = file fps, so the frames are 10 and 34. The trashbin is the blue printed object, the only thing that moves
(scene/ calls it `blue_object`; it is the record's track). The other objects are the "white cup" (small tumbler, 2.516 m),
the "book" (white card, 2.082 m) and the basketball (2.925 m). Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).

## Method
Depth is given only at 0.4 s, so I needed the depth at 1.4 s.
- **Floor-plane model (used):** I back-projected the ball, cup and book centres with their depth_info distances. Then I fitted
  the floor plane, assuming centre heights above the floor of ball 0.12 m (its measured diameter is 0.251 m), cup 0.062 m
  (from its pixel height, about 0.124 m) and book 0.015 m. That gives a camera tilt of 36.5°, a camera height of 1.68 m, and
  a bin centre height of 0.079 m at frame 10.
  The bin slides on the floor without rotating: its print pattern is unchanged. So its centre stays at a constant height.
  I intersected the frame-34 centroid ray with that height plane.
  - P10 = (0.554, 0.068, 2.672), which is distance 2.73 by construction.
  - P34 = (−0.112, −0.398, 3.287), distance 3.31.
  - **Displacement = 1.019 m.**
- Check against the prior: under this model the speed at frame 10 is 0.999 m/s (forward) and 0.991 m/s (backward), against a
  prior of 0.9962. The speed stays roughly constant, about 1.0–1.1 m/s.
- Consistency: depth_info only allows a tilt of about 35°. At a tilt of 40° or more the ball and cup would sit at or below
  the floor, and at 30° the ball centre would be 0.2 m up. A rough read of the cup's top-rim ellipse (minor/major ≈ 0.58)
  gives about 32°, which agrees.

## Second route and the disagreement
- Scaling depth by apparent size (sqrt(area), short side or bbox) gives Z34/Z10 ≈ 1.14–1.16 and a displacement of 0.87–0.90 m.
  This corresponds to a tilt of about 45°, which is inconsistent with depth_info as shown above.
- The object is a box seen from an angle. As it moves away the view becomes more grazing and more of its side face shows,
  so its image size shrinks more slowly than 1/D. Its long side even stays almost constant. For that reason I rejected size
  scaling.
- Constant depth would give 0.754 m.

## Sensitivity
- Varying the assumed object heights and using raw or smoothed centroids gives 0.99–1.05 m.
- Depth errors of ±2 cm give 0.97–1.08 m (std 0.03).
- Path length over 10..34 is 1.021 m, so the motion is a straight line.
- Timing: the record notes probable dropped capture frames at steps 12 and 36. They do not affect the displacement between
  frames 10 and 34.

Answer: **1.02 m**. Confidence: moderate (about ±5%, with the size-scaling alternative at 0.89).
