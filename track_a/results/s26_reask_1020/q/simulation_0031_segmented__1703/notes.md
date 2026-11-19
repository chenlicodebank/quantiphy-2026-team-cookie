# q1703 — height of the person (simulation_0031_segmented)

Answer: **1.48 m** (rest standing height).

File is 25 fps; question_fps = 24 is used for all times and speeds (frame 24 = t 1 s, frame 48 = t 2 s).

## Facts used
- Prior: the person walks at 1.3 m/s. The person's depth_info is 139.95 m at t=1 and 139.98 m at t=2. It barely changes
  although the body clearly moves, so the origin stays put. The body walks left and **toward** the camera: the image
  track (mask centroid, scene/tracks/human.csv) is -1.22 px/frame in u and +0.555 px/frame in v, linear over two
  gait cycles (0-36 and 36-72). There is no camera roll (the body and the mast are vertical).
- Pixel height (hpx.py): the head is almost white in this render, so the top is taken from frames where the hair or
  edge is caught. Frame 0 has the legs together: top 563.3, sole 637.8, so **74.5 px**. The envelope over all
  frames is consistent (head top ≈ 563.3 + 0.57·i, sole ≈ 637.9 + 0.57·i).

## Camera pitch / focal length (pinhole, no roll)
1. **Boat cabin roof** (roof_bottom.py, solve.py): the two near lower edges of the red roof slab are fitted per frame
   (64 frames). The roof is a horizontal rectangle, so we require a right angle on a horizontal plane. This gives
   β(f) ≈ 11.1–11.5° (ray depression at the roof ≈ 13.2 ± 1°).
2. **Eagle level flight** (eagle_beta.py): the given eagle depths are 139.76 m at frame 24 and 130.25 m at frame 48.
   These two frames are two flap periods apart, so they are in the same phase. Equal heights give β(f): 13.2° at
   f = 6000 and 11.4° at f = 7000.
3. The two curves cross at **f ≈ 7008 px, β = 11.41°** (hfov ≈ 7.8°). This does not use the person. The ray
   depression at the person is 12.4°.
4. **Check with the prior:** at that camera, the person's ground track (centroid ray on a horizontal plane at depth
   139.95) gives 1.35 m/s against the prior's 1.3, which is 4% off. Taking the roof pitch and solving for exactly
   1.3 m/s gives f = 7281 px.

## Height
H is found by back-projecting the head-top and sole rays at frame 0 onto a vertical line on the ground plane. A
correction of 0.12 m·tanα removes the bias from the toe sitting nearer the camera than the head.
- roof × eagle (f 7008): H = 1.50 m (the simple hpx·Z/f gives 1.49)
- roof + speed prior (f 7281): H = 1.44 m (the speed route does not depend on depth)
- Answer is the mean, about **1.48 m**.

Sanity checks at f ≈ 7000–7300:
- The boat's cabin door (about 100 px at about 127 m) comes out at 1.74–1.8 m, which is realistic.
- The boat including its mast is about 8 m tall.
- The eagle's wingspan is about 1.5 m after correcting for heading foreshortening. That is smallish for an eagle but
  within 40%.

## Caveat
1.48 m is just under the 1.5 m adult plausibility bound. To get a 1.75 m person, the pitch at the person would have
to be about 16.8°. Both independent pitch measures (roof right angle, eagle level flight) give 12.4°, 3–4° below
that, and the speed prior agrees with them to within 4%. I found no error in the geometry, so I kept the measured
value.

Confidence: moderate, ±5–8%. The head top is pale and uncertain by about 1.5 px (2%), and the pitch has about 1° of
error, which shifts H by about 4% through the speed route.
