# q 2300 — height of the yellow toy (lemon plush), captured_0018

The yellow toy is the plush lemon with two dark-green leaves. The nearer (right) person holds it in their right hand,
close to their body, until it is released at frame 27. The file runs at 24 fps, the same as question_fps.

## Pixel height (mask.py, crops.py)
- On the held frames 0–27 the lemon stands upright and faces the camera. Its lower edge is partly behind the
  fingers, but the yellow edge is still visible below them.
- HSV masks (yellow body + dark-green leaves): the top of the leaves is at y≈216–221 and the bottom of the body at
  y≈271–277. That gives a total height of 55–58 px across frames 0, 5, …, 27. With 4× zoom, the visible edges at
  frame 26 run from y≈214 to y≈275, about 61 px. I used **58 ± 3 px** including the leaves.
- The body alone, without the leaves, is about 40 px tall and 24–27 px wide.
- Frames after landing are not usable: the lemon lies on the floor and is foreshortened. Frames during the fall are
  motion-blurred vertically.

## Depth of the lemon
- depth_info gives the near person at 2.002 m. The lemon is in that person's hand, about 100 px (~0.27 m) to the side
  of their body.
- Check 1: the tennis ball in the same person's outstretched left hand is ~24 px across. At a standard 6.7 cm that
  puts it at about 2.13 m. That hand reaches further toward the far person, so it should be about 0.15 m deeper than
  the lemon, which puts the lemon at about 2.0 m.
- Check 2: fitting free fall to the lemon's centre over frames 28–35 gives 2.05–2.45 m. This route is noisy: the same
  fit puts the soccer ball at 3.5 m instead of the given 2.8 m, so I only used it as a rough check.
- Chosen depth: Z ≈ 2.03 m.

## Answer
- f = 0.5959 × 1280 = 763 px.
- Height = 2.03 × 58 / 763 = **15.4 cm**, including the leaves.
- Using Z = 2.002 m instead gives 15.2 cm.
- Other reading: the lemon body alone, without leaves, is ≈ 40 px, about 10.6 cm. I answered with the full toy height.
- Confidence: moderate, about ±7%. The main uncertainties are the blurred edges at the hand and the leaf tips, and
  whether the reference height includes the leaves.
