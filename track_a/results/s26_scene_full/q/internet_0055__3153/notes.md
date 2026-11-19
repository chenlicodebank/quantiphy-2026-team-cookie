# q3153 – width of the DO NOT ENTER sign (m)

Prior: "average speed of the person riding scooter = 1.95 m/s". There is no scooter in the clip: the only moving person is
the woman walking right to left across the far end of the bike path, in all 75 frames. I take her as the prior's object.
Time base: 30 fps; the file and question_fps agree.

Method (the annotators' convention for internet videos: one planar scale from the prior):
- Pedestrian pixel speed comes from scene/tracks/pedestrian.csv. I checked it on the contact sheet: the track follows the woman.
  Mean per-frame speed of the background-stabilised bbox centre is 245-252 px/s, depending on smoothing (1-9 frames).
  The net displacement over 74 frames gives 251.6 px/s. With the centroid, the head top or unstabilised coordinates it is 241-251 px/s.
  Value used: 247 px/s.
- Scale = 1.95 / 247 = 0.00789 m/px.
- Sign panel width is measured in code (measure.py): the run of non-sky pixels across the sign along rows y = 170-235.
  It is 148-150 px at frame 0 and 146-148 px at frames 37 and 74. The scene record says 153 px from its bbox.
  Value used: 150 px.
- Width = 150 x 0.00789 = 1.18 m.

Second route: the extreme combinations (148 px / 251.6 px/s and 152 px / 242 px/s) give 1.15-1.22 m.
Sanity check: a real DO NOT ENTER sign is about 0.75 m. The sign is farther from the camera than the walker, and that
explains the difference under the planar convention. A 1.95 m/s walk is also fast, so the prior itself is generous.
Confidence: moderate. The answer follows the annotators' single-scale convention.
