# q1189: height of the first (bottom) step in front of the door of the nearer house

Answer: **0.138 m**

The file fps (33) is the same as question_fps (33). t=1 s is frame 33 and t=2 s is frame 66.

## Which house
The curb, the step bases and the facade lines all slope down to the right in the image (the curb base is at y≈579 at x 750,
584 at x 1065 and 593 at x 1730). So the street recedes to the left: the camera is yawed about 6.5°, the same as the bike's path.
The right-hand **stone house** (arched door) is therefore the nearer one: its step base is at Z≈14.2 m, against 14.7 m for the green house.
Both staircases are the same model: 5 risers each, with the same corner-to-corner interval pattern (25.8/23.0/22.9/24.9/22.3 px against 25.1/22.3/21.6/24.2/23.3 px).
So the reading hardly matters: stone 0.136 m, green 0.142 m.

## Scale (prior = moving bike's wheel diameter 0.65 m, plus the bike depths)
- Front-wheel circle fits (`wheel2.py`, checked by drawing them in `frames/circ33.png` and `frames/circ66.png`): outer tyre diameter 98.3 px (f30-36) and 94.8 px (f63-68).
  The rear wheel fit is biased by the fender and the inner rim, so I did not use it.
- Bike origin = hub midpoint from the track. The given distances give Z = d/|ray|.
  The front hub is about half a wheelbase ahead along a path yawed 6.5°.
  This gives f = 1878.6 px at t=1 and 1891.8 px at t=2 (they agree to 0.7%), so **f = 1885 px**, with cx, cy at the image centre.
- Camera pitch: 7 clean vertical edges converge to a vanishing point 81 000 px below the image centre, so the tilt is 1.33° down (`vert.py`).
- Camera height above the street, from the wheel contact points: 1.735 m (t=1) and 1.728 m (t=2), which agree.
- Curb face 19.9 to 20.3 px, giving a curb height of 0.14 m. Camera height above the sidewalk = 1.591 m.

## Step measurement (`risers.py`, frame 0, median of 10-px column strips)
- Each step shows a bright tread band of about 4 px above a riser, with a dark ambient-occlusion crease at the riser's base.
- Bottom riser = nosing (bright-to-riser half-max) down to the ground corner (dark-to-ground half-max):
  stone 531.8→549.8 = **18.0 px**; green 524.9→543.1 = 18.2 px. Across columns the scatter is ±1 px.
- Step base depth comes from intersecting the ray with the sidewalk plane, and the vertical face is projected with the tilt (`solve.py`):
  stone Z = 14.24 m, R = 0.136 m; green Z = 14.72 m, R = 0.142 m.
- Consistency check: the stone tread band of 4.3 px implies a tread of about 0.32 m, a normal value. This supports reading the band as the tread rather than part of the riser.

## Second route / checks
- A level-camera model (no tilt), worked by hand rather than in a script, gives about 0.138 m, so the result is not sensitive to the pitch.
- Measuring the two houses separately gives 0.136 and 0.142 m, at different depths but with the same model.
- The answer, 0.138 m, is the mean of the two staircases, which are the same model.
- The walker depths (14.77 and 15.18 m) are inconsistent with the walker's image: his feet row is constant, his apparent height drops only 1.2%, and he moves toward the image centre.
  So they are not used.
- If the riser were taken as the whole interval including the tread band (22 px), R would be about 0.17 m. I rejected that reading: geometry shows the tread is visible.

Confidence: moderate. The ±1 px on an 18 px riser is about ±6%, and the depth chain adds about ±3%.
