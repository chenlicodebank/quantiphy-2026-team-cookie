# q1148 – eagle body length (m)

File fps 24 = question_fps 24. Scripts: geom.py, body.py, rows.py, crops.py.

## Scale
- Person (prior 1.75 m) is 41 px tall (median over 72 frames, ±1 px), and its distance is 139.10 m -> f ≈ 41·139.1/1.75 ≈ 3259 px
  (range 3180-3340 for ±1 px). Check: the person's walking speed comes out at 1.09 m/s (plausible). Their distance stays constant,
  so they walk across the view.
- Eagle m/px = depth/f: 0.0429 at t=1 s (139.70 m) and 0.0452 at t=2 s (147.16 m). Linear in time between these.

## Eagle orientation
- 3D origin positions from back-projection at t=1 and t=2 give v ≈ (8.5, 0.4, 7.9) m/s, 11.6 m/s, at about 50° to the line of sight.
  The bird is seen from behind and to the left: the wings spread horizontally across the image, and the body is foreshortened by sin θ.
- Check: the wings-level span of 30-31 px gives 1.33 m projected, so the true wingspan = 1.33/cos50 ≈ 2.07 m (a realistic eagle).
  An independent estimate from the raised-wing V geometry gives θ ≈ 32-45°, which is rough.

## Body length
- Projected horizontal extent of the body: measured with a 50 % darkness threshold plus anti-aliased edge fractions, on the bottom
  rows of the wings-raised frames (20-26, 44-49, 68-71). Result 10-12 px = 0.46-0.54 m (median 0.49). The body under the wings in
  wings-level frames 5 and 30 gives 13-13.5 px, about 0.55 m.
- L ≈ 0.52 / sin θ: θ=50° gives 0.68 m, θ=44° gives 0.75 m. A typical eagle length/wingspan ratio of about 0.4 suggests θ ≈ 44°
  and L ≈ 0.78 m. The thin beak and tail tips are partly lost at this resolution, which biases the measurement low. The body's
  cross-section width adds to it, which biases it high.
- Answer: 0.75 m. Confidence is moderate (about ±15 %). The main uncertainty is the body yaw relative to the line of sight.
