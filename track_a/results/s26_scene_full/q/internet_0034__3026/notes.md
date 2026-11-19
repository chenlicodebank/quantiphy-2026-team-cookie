# Q3026 – displacement of toilet roll, 0.5 s -> 1.73 s (cm)

## Time base
File says 24.098 fps, question says 30 fps. I used 30 fps: the clip has exactly 60 frames, which is 2.000 s at 30 fps
(a clean cut length), and 1.73 s matches a whole frame only at 30 fps (52/30 = 1.733), not at 24.1 fps (41.7).
So 0.5 s -> frame 15 and 1.73 s -> frame 52. (With 24.1 fps it would be frames 12 -> 42, giving 11.8 cm.)

## Scale
Prior: roll size = 100 mm. The roll is seen side-on and moves mostly horizontally. Its length along the axis (end to end,
horizontal) is 590.7 px (mean of frames 50-59 in scene/tracks), and the vertical diameter is ~697 px. 100 mm fits the
axis length (a normal roll is ~10 cm wide and ~11-12 cm across; 697/590.7 x 10 = 11.8 cm). One planar scale:
10 cm / 590.7 px = 0.01693 cm/px.

## Measurement
Camera is static (scene record: <0.3 px shift). Overlays of the tracked corners on frames 15 and 52
(frames/ov15.png, ov52.png) fit the roll outline well.
- Centre (mean of 4 corners): f15 (2719.9, 1328.4) -> f52 (1948.2, 1410.9): 776.1 px -> 13.14 cm.
- Corners give 733-811 px because the roll's tilt changes by ~5 deg in between (the centre is the right reference point).

## Second route
ECC (Euclidean) registration of the roll's surface texture from f15 to f52: the f15 centre maps to (1952.4, 1401.4),
4.7 deg rotation, displacement 771.0 px -> 13.05 cm. Agrees with the track within 0.7 %.

Answer: 13.1 cm. Confidence: good on the pixels (~1 %); the main risks are the time base (24 fps reading gives 11.8 cm)
and which roll dimension the prior names (diameter reading would give 11.1 cm).
Scripts: overlay.py, measure.py.
