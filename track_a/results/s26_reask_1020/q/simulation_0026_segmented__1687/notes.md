# q_1687 – height of the boat (m)

File is 25 fps; question_fps = 24, so t=1 s -> frame 24, t=2 s -> frame 48.

Method (pinhole, 3D render): focal length from the person (prior 1.75 m, depth 114.83 m at both times),
then boat height = pixel height x boat depth / f. Height = full vertical extent, keel to mast top
(world AABB includes the mast).

Measurements (scripts enh.py, person.py, keel.py; darkness d = 255 - min(RGB)):
- Person pixel height (head top is pale/faint): frame 24 ~ 532..583.5 -> ~51-52 px; frame 48 ~ 537..586.5 -> ~50 px;
  median over all clean frames (th 12) 50-51 px, + ~1 px for faint head -> 51 px.
  f = 51 x 114.83 / 1.75 = 3346 px.
- Boat: frame 24 mast top ~306.5, keel bottom 627.5 -> 321.5 px; frame 48 mast top ~311.5, keel 622.5 -> 311 px.
- Height t=1: 321.5 x 103.157 / 3346 = 9.91 m. t=2: 311 x 106.091 / 3346 = 9.86 m.

Check: boat pixel-height ratio 321.5/311 = 1.034 vs depth ratio 106.09/103.16 = 1.028 — consistent (rigid object).
Off-axis corrections are negligible (objects within ~110 px of centre, f ~3300 px).

Answer 9.9 m. Main uncertainty: the person's faint head (+-2 px of 51 -> +-4 %).
