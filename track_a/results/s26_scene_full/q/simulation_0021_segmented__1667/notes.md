# q_1667 — streetlight height

The file is 29 fps and question_fps is 30, so t = 1 s is frame 30.

Pixel measurements (checked on frames 0 and 81 against scene/ record):
- Lamp post spans y 330 to 893, which is 563 px, with its axis at u = 193.
- Man's standing height is about 222 px (head top ~650, ground ~872). His pelvis is at (85.8, 754) at frame 0 and (135.8, 753) at frame 30.

Method (solve.py): pinhole camera, principal point at the image centre, camera assumed untilted, z = d / sqrt(1 + ((u-cx)/f)^2 + ((v-cy)/f)^2).
- Route A, from the prior: man height 1.87 m gives f = 1570 px (horizontal FOV 38°). This reproduces the given d(t=1) as 13.771 against 13.768.
- Route B, independent of the prior: the change in the man's depth from 13.882 to 13.768 while he walks parallel to the image plane gives f = 1549 px. Under this f the man measures 1.893 m, against the prior's 1.87.
- Lamp height = 563 px × z_lamp / f:
  - origin at lamp centre: 4.31 m (f_A) / 4.37 m (f_B)
  - origin at lamp base: 4.22 m (f_A) / 4.27 m (f_B)
- Hydrant height comes out at about 1.02 m, which is plausible.

Answer: 4.30 m. This uses the centre-origin reading with f between the two routes. Confidence: about ±3%.
