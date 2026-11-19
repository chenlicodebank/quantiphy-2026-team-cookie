# q_1908 — truck height at t = 0 s

Prior: width of the box = 1.33 m. 2D render (straight-on rear view), 120 fps (file and question agree). Frame 0.

## Measurements (measure.py, frame 0, non-white mask, threshold min(RGB) < 225)
- Cardboard box width: brown-pixel rows give 280–282 px; non-white run width over rows 200–320 has a median of 282 px
  (range 281–283). The scene record gives about 279 px. I use 282 px.
  Scale = 1.33 / 282 = 0.004716 m/px.
- Truck silhouette, measured in columns that do not include the box (640–800 and 1100–1240): the container top is at
  y = 339 and the lowest visible part (red mud-flap/wheel parts under the bumper) is at y = 1043–1044. Height = 706 px.

## Answer
706 px x 0.004716 = **3.33 m**. This is the truck itself, without the cardboard box it carries.
- If the box is included, the silhouette runs from y = 146 to 1044, which is 899 px = 4.24 m. I don't use this
  reading because the box is a separate object.
- Check with a second width: the scene record's box width of 279 px gives 3.37 m (+1%).
- Plausibility: a 3.3 m box truck is realistic.

Confidence: moderate. The main risks are the truck-versus-box definition and a possible depth offset between the box and
the container rear face (a 2D single scale ignores it).
