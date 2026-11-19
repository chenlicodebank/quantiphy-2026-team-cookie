# q_1727: height of the person (m)

Prior: boat length = 10 m. Depths: boat 133.9572 m at t=1 s and 131.2557 m at t=2 s; person 139.103 m and 139.104 m (the person's origin stays put).
File fps = question fps = 24.

## Person pixel height (person_h.py)
- Mask height at threshold 40 is 40.2 px on average while walking (range 38-42). At frame 0 the person stands in a near-rest pose and measures 41-43 px, depending on the threshold.
- The person's pixel height stays constant, so the body stays at about 139.1 m depth. They walk laterally at 25.0 px/s.
- I used a rest height of about 41 px.

## Focal length from the boat (solve.py, solve2.py)
- I placed the boat origin at the mask centroid back-projected with the given depths at t=1 and t=2. That gives a 3D velocity: 73.8 px/s lateral and -2.70 m/s radial.
- I took the hull heading to be the direction of motion and modelled the hull as a 10 m segment with a pointed bow and a square stern of width W. I fitted f so the model matches the measured hull x-extent (182 px at t=1, 188 px at t=2, and frames 3-71).
- The fit is badly conditioned in W:
  - W=0 gives f=3320 and a person height of 1.68 m (40 px).
  - W=1 gives f=3080 and 1.81 m.
  - W=1.5 has the best rms and gives f=2985 and 1.86 m.
  - W=3 gives f=2755 and 2.02 m.
- A realistic beam (3-3.5 m) would make the person about 2.0-2.1 m, which is implausible. So the extent model probably over-weights the beam: the stern is narrower than the beam and the hull ends are rounded.
- Second cue: the wheelhouse's front and side faces appear at similar widths (about 25 vs 28 px). If the wheelhouse is roughly square, the heading is about 48 deg from the line of sight. Combined with the motion, that gives f of about 3260 and a person height of about 1.72-1.75 m.
- Cross-check: the boat's mast-to-keel growth (x1.070) matches the depth ratio (x1.059). The boat moves at about 4.2 m/s, and the person's lateral walking speed comes out at about 1.1 m/s, which is plausible.

## Answer
I used f of about 3150 px, between the two routes. Height = 41 px x 139.1 m / 3150 px = 1.81 m.
Confidence is moderate: the two routes span about 1.72-1.87 m.
