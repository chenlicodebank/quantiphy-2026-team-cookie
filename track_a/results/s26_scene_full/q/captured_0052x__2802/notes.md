# q2802: yoga ball diameter (cm)

The file rate and question_fps are both 24 fps. So t = 1.0 s is frame 24. The ball's depth at that time is 2.612 m.
The focal length comes from the lab card: f = 0.5959 x 1280 = 762.8 px.

## Pixel diameter at frame 24 (measure.py, measure2.py)
- **Robust circle fit** to every free ball edge that borders the green screen. It covers 330 deg of arc, with a residual of
  about 1 px: D = 146.3 px. The overlay (frames/fitall24.png) sits on the outline. A dark blob under the ball (the person's
  knees) is excluded.
- **Mask row width** through the centre: 146 px. **Twice the centre-to-top distance**: 148.4 px.
- **Smooth trend:** I fitted 1/D linearly in time over frames 21-32, while the ball rolls toward the camera, and evaluated it at
  frame 24. Depending on the window this gives 148-152 px.
- **scene/ record:** its arc fit gives 152.5 px. It uses only the left and top arc, so it is slightly large.
- Value adopted: **148 px** (±3).

## Size
D = 2.612 x 148 / 762.8 = 0.507 m, so the answer is **50.7 cm**.

- Single-frame values: 146.3 px gives 50.1 cm and 152 px gives 52.0 cm.
- **Exact sphere projection:** with the off-axis correction (the ball centre is about 14 deg off-axis) the result would be
  about 48 cm. If instead the depth were to the front surface rather than the centre, it would be about 53-55 cm. I used
  the method card's convention.

## Checks
- **Basketball at frame 24** (bball.py): 92 px wide at depth 1.9365 m gives 23.4 cm. That is a plausible basketball size
  (size 6 is 23.2 cm, size 7 is 24.3 cm), so the same depth and focal convention reproduces a known size.
- **The velocity prior** does not constrain the diameter, because depth at t = 1 is given. It is therefore not used as a
  scale.

## Confidence
About ±5%, mainly from the depth and projection convention.
