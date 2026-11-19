# q_1059 — height of the house's door (simulation_0011)

File fps = question_fps = 24. Prior: gravity 9.8 m/s². Depths: nest 17.27/17.25 m (t=0/1, on the branch),
bird 46.65 -> 43.97 m, cart 33.235 m, house 63.603 m.

## Door pixel size (door_measure.py, frame 0)
- Plank door leaf (open against the wall, left of the opening): y 1154 -> 1353, about 199 px tall, 75 px wide.
- Dark door opening: y 1151 -> 1355, about 204 px. I used about 200 px for the door.
- Depth of the front wall: ground-plane fit y = y_h + K/Z using the nest's ground contact (y 1577, Z about 17.2) and the cart
  wheels' ground contact (y 1435, Z about 33.2). This gives K about 5070 and y_h about 1282, so the house base (y 1365) is at
  Z about 61.4 m, about 2 m in front of the house origin (63.6 m). Door depth is about 61.4 m.

## Gravity route (rejected as a scale source)
The "nest" is the black fuzzy object. track2.py tracked it: from frame 31 to 48 its centroid speeds up steadily, with a
fitted pixel acceleration of 1050-1250 px/s² (rms about 1 px). Taking f from a_px x Z / g gives f about 1760 px.
That f makes everything about 3x too large: door about 6.8 m, barrels about 2.9 m, cart wheel about 3.2 m,
crow wingspan about 3.3 m, nest about 1 m, which is implausible. The objects keep consistent proportions with each other,
and the crow's speed and wingbeat (1.4 Hz) also look slowed. So the fall seems to be slow motion (time-scaled or a damped
soft body; the nest deforms), not free fall at 9.8 m/s² at 24 fps. I could not make the gravity route fit, so per the
instructions I took the scale from standard objects of known real size.

## Scale from standard objects (consistent with each other)
- Crow wingspan: bbox_w x depth is about 5800-6000 px·m and stays constant as the crow comes closer (134 px at 43 m,
  152 px at about 40 m), which checks the bird depths. A crow wingspan of about 1.0 m gives f about 5900-6000.
- Cart wheel: 172 px at 33.2 m. A wheel of about 0.95-1.0 m gives f about 5700-6000.
- Barrels at the front wall: 90 px tall, ratio door/barrel = 2.2. A barrel of about 0.9-0.95 m gives a door of 2.0-2.1 m.
- With f about 5960: door = 200 x 61.4 / 5960 = 2.06 m. Check: nest 0.33 m, wheel 0.96 m, barrel 0.92 m,
  crow 1.0 m, camera height about 0.85 m. All are plausible.

Answer: 2.05 m. Confidence is moderate. The answer rests on the real-scale assumption. If the scene really were 3x scale
(the gravity route), the door would be about 6.8 m.
