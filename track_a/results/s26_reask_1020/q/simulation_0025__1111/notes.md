# q1111 — eagle wingspan (simulation_0025)

The file runs at 25 fps and question_fps is 24. I used frame numbers, so depth times t=1 s and t=2 s are frames 24 and 48.

## Scale (focal length)
- Person (person.py): mask height is 54.5–55 px in every frame, with almost no trend (-0.6 px over 74 frames). The depth to their origin is 114.83 m.
- If the 1.3 m/s walk were all across the view (38.7 px lateral over 74 frames), f would be about 1110 px and the person 5.4 m tall. That is impossible, so I rejected it.
- I took the scale from a standard adult instead, H ≈ 1.75 m, which gives f = 54.8 × 114.83 / 1.75 ≈ 3600 px.
  - At this scale the person's lateral speed is only about 0.4 m/s. The rest of the 1.3 m/s would have to be along the line of sight, and the nearly constant pixel height does not clearly show that. This is not fully resolved.
- Independent check (birdfit.py): a constant-velocity perspective fit of the bird's image x-track gives a depth ratio Z48/Z24 = 0.940 ± 0.002.
  - Given depths: 108.28 / 116.05 = 0.933.
  - Predicted at f = 1100: 0.966, which is rejected.
  - Predicted at f ≥ 3000: 0.94, which is consistent. So f ≈ 3600 is supported.

## Bird
- 3D velocity (span.py), from the given depths and the fitted track with f = 3596: V ≈ (8.15, 0.09, -8.06) m/s, i.e. 11.5 m/s. The bird flies about 45° toward the camera.
- Wing axis: I assumed it is horizontal and perpendicular to the direction of flight. Its projection factor onto the image is 0.74 (early frames) to 0.62 (late frames).
  - The asymmetric silhouettes support an oblique wing axis: the near (left) wing looks foreshortened and blobby, while the far wing is long (frames 59–62; frames/birdmask_b.png).
- Mask extent, taken as the PCA main axis, at the frames where the wings are level and spread. Depth is interpolated linearly from the given values.
  - Without the foreshortening correction, the per-cycle maxima are 1.35–1.52 m.
  - With the correction, the per-cycle maxima are 2.05, 1.99, 2.13, 2.21, 2.12 and 2.42 m (median about 2.13).
  - I took the fully spread value near the upper middle: about 2.2 m.
- This is plausible for a bald eagle: the white head and tail are visible, and real wingspans are about 1.8–2.3 m.

## Caveats
- Without the correction, the per-cycle values stay flat over time, while the heading model predicts they should fall by about 17%. This hints that the bird yaws or that the wing pose varies.
- An alternative raised-wing (V-shape) estimate gave a projection factor of about 0.88, which would mean a wingspan of about 1.65 m.
- The answer is 2.2 m. Confidence is moderate, about ±15%.
