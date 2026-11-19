# q_107: distance between the yellow car and the black/white car at 2.0 s

- 2D top-down render, 24 fps (the file fps and question_fps agree), so t = 2.0 s is frame 48.
- Scale from the prior (yellow car speed 5.07 m/s). The yellow car moves at a constant pixel step, re-measured in `measure.py`:
  - yellow-pixel centroid: -9.85 px/frame over frames 12->71 and 24->71
  - front bumper: -9.83 px/frame over frames 1->71
  - rear bumper: -9.97 px/frame over frames 12->71
  - Adopted value: 9.87 px/frame = 236.9 px/s, which gives 0.02140 m/px.
- Positions at frame 48 (bbox mid, bumper to bumper):
  - yellow car x = 1415.5, dark car x = 865 to 866. These agree with the scene record (1415.5 / 866).
  - Lanes are y = 525.5 / 637.5, so dy = 112 px.
- Distance = sqrt(550^2 + 112^2) = 561.3 px, x 0.02140 = **12.0 m**.
- Check: the scene record's centres give 560.8 px x 0.02134 (from its 9.90 px/frame step) = 11.97 m. The yellow car's length of 271 px x 0.0214 = 5.8 m is a plausible car size.
- Confidence: good (about ±2%). The main uncertainty is the pixel speed (9.83 to 9.97 px/frame).
