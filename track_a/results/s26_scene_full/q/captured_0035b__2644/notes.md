# Q2644: basketball displacement 0.4 s -> 0.9 s (cm)

Time base: question_fps = 24, the same as the file's rate. t=0.4 -> frame 10 (ball still at rest; the kick starts at frame 12). t=0.9 -> frame 22.
Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

Centres (from scene/tracks/basketball.csv, checked visually on zoomed crops frames/f10.png and f22.png):
- f10: (829.1, 281.2), diameter 53.1 px (static frames 0-10 agree to within 0.3 px)
- f22: (667.1, 398.5), smoothed diameter 60.9 px

Depth: f22 basketball = 2.7777 m (given). The depth_info labels both t=1.4 values as soccer ball.
I assigned basketball = 2.602 and soccer = 2.373 because the size ratios are consistent that way:
- soccer: 52.5 px x 2.477 = 54.8 px x 2.373
- basketball: 2.7777 -> 2.602 against size 2.906 -> 2.641
No depth is given at 0.4 s, so I estimated Z(f10) three ways:
1. Prior size, Z = f x 0.232 / 53.1 = 3.33 m -> displacement 95.3 cm.
2. Floor plane from room geometry (room.py): the two wall baselines are taken as orthogonal floor directions, and the floor normal is set from the vertical wall corner. The ball-centre plane height is fixed from the basketball 3D points at f22 and f34 (they agree to about 4 cm). Intersecting the f10 ray with that plane gives Z = 3.25-3.35 m -> 90-97 cm.
3. Diameter ratio relative to f22 (f22 depth x 60.9 / 53.1): 3.19 m -> 86 cm. This is a lower bound, because the given f22 depth is about 4 % below the size-implied depth.
4. A plane through the soccer-ball 3D points gives 3.46 m -> 104 cm. I gave this less weight because the soccer depths imply a 17 cm ball.

Answer: Z10 ≈ 3.30-3.33 m. Displacement = |P22 - P10| ≈ 94 cm (full 3D, back-projected centres).
Confidence: moderate, about ±6 %. The main uncertainty is the depth at 0.4 s, which is not given.
