# q1117 – eagle wingspan (simulation_0028)

File fps 25, question_fps 24 (t=1 s -> f24, t=2 s -> f48). Prior: eagle length 0.8 m. depth_info ≈100 m at t=1 and 2.

## Geometry
- The camera is static and looks at the bird almost side-on. The bird flies left to right across the image. Its body
  (tail to beak) is the horizontal bar at the bottom of the silhouette, and the wings flap up and down in the image.
- Camera depression (geom.py): I back-projected the bird at f24 and f48 with the given depths, assumed level flight,
  and got δ ≈ 17–20° (centroid, cycle-mean and body-line references). Speed ≈ 11.4 m/s. The motion is nearly
  parallel to the image plane, so the body length is not foreshortened.
- Scale: the body length (mask x-extent in wings-up frames f0–2, f22–27 and f47–51, thresholds 40/60/90; see
  measure2.py) is 28–30 px, so I used 29 px = 0.8 m. That gives f ≈ 3600 px, a horizontal FOV of about 15°.

## Wing
- Upstroke peak (f23–25, f48–50): the wingtip is at y=212 and the body midline at ≈247 (f24), or 224.5 vs 259
  (f48). The tip is ≈35 px above the body midline (about 35.4 px including a 5 px x offset).
- A vertical wing is foreshortened by cos δ ≈ 0.95. A wing raised to ε≈76° (the near-wing tip shows about 6 px
  lower) gives a factor sin(ε+δ) ≈ 1.0, so I used a factor of ≈0.97. That puts the wingtip about 36 px from the body
  midline.
- Wingspan ≈ 2 × 36 = 72 px. 72 / 29 × 0.8 m = **1.99 m**. The plausible range is 1.87–2.15 m (body 28–30 px,
  half-span 34.5–37 px).

## Checks
- On the downstroke (f9–12) the wing reaches ≈28 px below the body. That is consistent with a wing that is not
  fully perpendicular to the view at the bottom of the stroke, so it gives only a lower bound.
- The span/length ratio of 2.5 matches real eagles (length 0.7–1.0 m, span 1.8–2.3 m).
- Confidence: moderate (±7%). The bird is small, about 29 px long, and the wing orientation at the stroke peak is
  inferred.
