# q_2525: distance between the ping pong (white) ball and the tennis (yellow) ball at t = 1.6 s

- Time: question_fps = 24 (same as the file's rate), so t = 1.6 s is frame round(38.4) = 38.
- Centres at frame 38 come from the scene/ circle-fit tracks, checked against a zoomed frame (frames/f38.png):
  yellow (739.45, 453.37) px, diameter 50.8 px; white (662.21, 443.81) px, diameter 24.5 px.
- Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Each centre is back-projected
  along its unit ray to the given Euclidean camera distance (tennis 1.190 m, white 0.994 m). Then I take the 3D distance.
- Result: **22.44 cm**. Frames 37 and 39 give 22.45 and 22.39 cm, so the result is stable.
- Check: with the given depths, the tennis ball's pixel size comes out at 7.9 cm, not the prior's 6.7 cm, and the white ball at 3.2 cm, not 4.0 cm.
  In the image the yellow ball is clearly the nearer one (lower and bigger), so the two depth labels look swapped.
  Swapped, the sizes come out at 6.6 cm and 3.8 cm, which fits the prior. With the depths swapped the distance is still 22.44 cm,
  identical to within rounding, so the answer does not depend on which label is right.
- A second route uses depth from pixel size only (Z = f·D/d, tennis 6.7 cm, ping pong 4.0 cm). It gives about 25.6 cm. That route is very
  sensitive to the white ball's small, uncertain diameter, so I trust the given depths instead.
- Confidence: moderate to high, about ±5%.
