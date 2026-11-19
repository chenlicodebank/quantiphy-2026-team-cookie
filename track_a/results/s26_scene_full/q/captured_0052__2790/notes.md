# q_2790 — distance trashbin to basketball (m)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). Both objects are static (scene record shows identical masks at frames 0/24/47).
Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). The centres come from colour masks at frame 24 (t = 1.0 s), computed in dist.py:
- Blue bin mask bbox 680-775 x 482-591, centre (727.5, 536.5). Depth 2.977 m.
- Orange basketball mask bbox 756-847 x 624-709, centre (801.5, 666.5). Depth 1.9365 m.
- I back-projected each centre along its unit ray times the Euclidean depth: bin (0.331, 0.667, 2.882), ball (0.373, 0.708, 1.763).
- 3D distance = **1.121 m**.

Checks:
- Moving the bin centre ±5 px vertically changes the distance by ±0.005 m (1.116-1.126).
- If depth is read as z-depth instead of ray distance, the result is 1.047 m. I kept the Euclidean reading because that is the stated convention.
- Sizes from the same scale: basketball 1.9365 x 91 / 763 = 0.231 m (a real one is about 0.24 m) and bin width about 0.37 m. Both are plausible, so the focal length and depths are consistent.
- The prior (exercise-ball velocity) is not needed: the depths set the scale.

Confidence: good (about ±3 %). The distance is dominated by the depth difference, which is given.
