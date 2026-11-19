# q_2148 – displacement of the ball between 1.0 s and 1.3 s (cm)

File fps = question_fps = 24 -> t=1.0 s = frame 24, t=1.3 s = frame 31.
Correction to scene/ record: the "white board" is the slope (depth_info names slope ends); the ball rolls
down its face toward the camera from frame ~27 (not a free fall in front of a board).

## Pixel centres (measured in code)
- Frame 24 (ball at rest at slope top, against green): diff-vs-frame-48 mask centroid (616.0, 282.4)
  (measure.py); record bbox centre (616.5, 283.0). Used (616.25, 282.7).
- Frame 31 (ball faint over white slope): yellowness-difference blob (measure2.py) centroid (617.5, 317.8);
  record (617.5, 318.5); interpolation of frames 30/32 (305.1, 335.4) with ~2.5 px/frame^2 acceleration
  gives ~319. Used (617.5, 318.2). Visual crop (frames/c31.png) agrees.

## 3D
f = 0.5959*1280 = 763 px, principal point (640, 360). Back-projected with given depths
(1.779 m at 1.0 s, 1.736 m at 1.3 s, depth = Euclidean distance along the ray):
P24 = (-0.0551, -0.1792, 1.7691) m, P31 = (-0.0511, -0.0949, 1.7327) m.
Displacement = |P31 - P24| = 0.0919 m (0.0911 m with v31 = 317.8).

## Checks
- Pixel steps 30-35: 12.7, 17.6, 18.9, 24, 27.3 px -> ~3 px/frame^2 x ~2.6 mm/px x 576 ≈ 4-5 m/s^2,
  consistent with prior 4.05 m/s^2 at t=1.4.
- Kinematic: release between frames 26-27; 0.5*4.05*(0.19-0.21 s)^2 ≈ 7.3-8.8 cm, same order (start-up
  of rolling is gradual, roughly consistent).
Answer 9.15 cm. Confidence moderate (±2 px at frame 31 -> ±0.5 cm).
