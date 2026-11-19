# Q1567 – width of the table (m)

Width = the desk top's front-to-back depth (its short horizontal side). File fps = question fps = 24.

## Focal length and camera tilt from the fall (fall_fit.py)
- Magnifier ref track, frames 0–11 (free fall before impact at about frame 11.3). Model: P(t) = 4.2401·ray(u0,v0) + (v0·t + 4.9·t²)·d,
  where d is world-down in camera coordinates, and f, roll, pitch and v0 are free; principal point at the image centre.
- Best fit: f = 2633 px (hfov 44°), pitch 0.232 rad, roll 0, v0 ≈ 0.02 m/s, rms 0.30 px. The cost profile has a sharp minimum
  (rms 1.2 px at f = 2400, 0.6 px at f = 2800).
- Check: the predicted depth at contact (frame 11 to 11.3) is 4.40–4.43 m, against the given 4.4097 m at t = 0.5 s.
  Magnifier length 183 px × 4.24 / 2633 = 0.295 m and revolver 153 px × 4.704 / 2633 = 0.27 m, both plausible.

## Desk top (plane2.py, joint.py)
- Corners on the last frame (silhouette and line fits): left-back (460,695), back-right (1601,522), front-right (1996,652),
  near (697,875).
- Desk plane: normal = the fitted down direction, anchored at the near corner (depth 3.593). The magnifier at rest and the
  gun give the same plane height (1.25 / 1.25 / 1.23 m).
- "far_right" corner: the front-right corner fits (plane depth 4.87 m before refinement, 5.006 m after). Back-right would be
  5.7 m, and making it 5.009 m forces 10–15 px corner moves and large rectangle residuals, so that reading was rejected.
- Joint least squares: fall pixels, near depth 3.593, front-right depth 5.009, magnifier resting on the plane, and a
  rectangle constraint, with each corner pixel allowed to move by σ = 3 px. Result: f = 2625, desk 2.48 × 1.06 m.
  With σ = 1 px: sides 1.03 / 1.07. With σ = 10 px: 1.05.
- Second route (plane2.py): the plane from the fall tilt only, with the raw corners and no rectangle constraint. Left side
  0.965 m, right side 1.144 m, mean 1.05 m.

**Answer: width ≈ 1.05 m (length ≈ 2.48 m).** Confidence: moderate, about ±5%. The view grazes the desk top (camera about
1.25 m above it), so corner pixel errors are amplified.
