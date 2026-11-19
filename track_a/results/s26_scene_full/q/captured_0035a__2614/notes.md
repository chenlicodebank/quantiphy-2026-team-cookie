# q_2614: soccer-ball displacement between 0.5 s and 0.6 s (cm)

Frames at question_fps 24 (same as the file's rate): t=0.5 s is frame 12 and t=0.6 s is frame round(14.4) = 14.
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360).

## Centres (measure.py: ball blob mask, ellipse fit, overlays in frames/m*.png)
- Frame 12: (493.0, 390.0). The scene track has (495.1, 386.2), and the bbox centre is (493.5, 392.5).
- Frame 14: (524.1, 409.4). The scene track has (521.9, 404.9), and the bbox centre is (526.5, 411.5).
- Both frames are motion-blurred, so each centre is the middle of the blur streak. Neighbouring frames step about
  18.5 px per frame, which agrees with the roughly 37 px between frames 12 and 14.

## Depth
- depth_info gives only the soccer ball at frame 14 (2.758 m) and at frame 38 (3.052 m). The 4th line
  ("soccer 2.412 at 1.6 s") is taken to be the basketball. Its implied diameter is 22.6 cm against the 23.2 cm
  prior, which is consistent.
- The ball rolls on the floor, so its centre stays on a plane. I built that plane through the two soccer-ball 3D
  points, assuming the camera has no roll (plane.py). This gives depth 2.860 m at frame 12 and reproduces 2.758 m
  at frame 14.
- A 4-point plane through both balls at frames 14 and 38 gives depth 2.83 m at frame 12 and a displacement of
  17.3 cm.

## Result
The displacement is the 3D distance between the back-projected centres: **16.7 cm** with the ellipse centres.
- Sensitivity to the choice of centre: bbox 16.8, scene track 15.7, read by eye 17.8.
- Constant-depth lower bound (ignoring the depth change): 13.0 cm.
- Answer: 16.8 cm (about 2 m/s, plausible for a kick).

Confidence: moderate, about ±7%. The main uncertainties are the depth at frame 12 (from the plane model) and the
centres in the blurred frames.
