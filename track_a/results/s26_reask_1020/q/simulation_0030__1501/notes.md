# q1501 – length of the eagle (m)

The file runs at 25 fps and question_fps is 24. Frame indices are used directly: the depth given for t = 0.5 s belongs to frame 12.

## Scale (geom.py)
- Prior: speed 12 m/s, so the eagle moves 0.5 m per frame at 24 fps.
- Track (scene/tracks/bird.csv, checked on crops): u rises linearly at 15.32 px per frame over frames 0–36. The camera is static.
- Given depths: 25.328 m at frame 0 and 24.899 m at frame 12. Requiring a 3D displacement of 6.0 m between those frames gives f ≈ 740–757 px (HFOV about 65°). The flight direction is about (0.998, 0.02, -0.058), so the flight is almost entirely lateral.
- Scale at the bird: 0.499 m per 15.32 px = 0.0326 m/px. This is the same as Z/f with Z ≈ 24 m along the optical axis. The 34.5 m neon-sign depth was not needed.

## Length in pixels (measure.py)
- The mask is the difference from a median background (frames 45–74), measured at 25 % and 50 % of the bird's peak contrast. The length is the horizontal extent along the direction of travel.
- Flat wings that reach toward or away from the camera add horizontal extent through perspective. That effect is near zero around u ≈ 520 (frames 9–13) and grows toward the right edge (frames 28–31 measure 29–33 px).
- In frames 9–22, where the wings are up or down and add little, the extent is 19–24 px at 25 % (mean 21.9) and 18–21 px at 50 %. I used 22 px, the 25 % threshold, because the beak and tail tips are thin and the 50 % threshold cuts them short.
- Length = 22 × 0.0326 ≈ 0.72 m.

## Second route
Frame 5 has the wings flat and is near the image centre. Its width is 27–29 px. The wing-projection factor there is about 0.086, so a wingspan of about 2 m adds roughly 5–6 px, which leaves about 22–23 px for the body. That is consistent with the first route.

## Sanity check and confidence
0.72 m is a realistic eagle length (0.66–1.0 m).

Confidence is moderate, about ±10 %. The main uncertainties are the antialiased beak and tail tips and how the wing-flap pose enters the reference bounding box. Readings range from 0.63 m (50 % threshold) to 0.75 m.
