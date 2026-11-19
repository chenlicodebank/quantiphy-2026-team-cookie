# q_1725 – eagle length (m)

File fps = question fps = 24. 3D Blender render, segmented, 1080x1080, principal point assumed (540,540).

## Scale
- Human height 40 px (median over frames 0-64, scene/tracks/human.csv; 39-42 range) at depth 139.10 m, prior 1.75 m
  -> f = 40*139.1/1.75 = 3179 px (range 3100-3260 for ±1 px).
- Check: human walks 1.04 px/frame -> 1.09 m/s at constant depth (plausible).

## Eagle 3D motion (geom.py)
- Back-projecting bird ref point at f24 (depth 139.70) and f48 (147.16): velocity (8.8, 0.4, 7.9) m/s, |v| = 11.8 m/s,
  heading ~42 deg out of the image plane, ~52 deg from the line of sight (flying away to the right).
- Projection factors: body axis (heading) 0.79, wing axis (horizontal, perpendicular) 0.60.
- Camera sees the bird almost edge-on in elevation (bird ~2 m below the optical axis at 140 m), so body and flat
  wings both project onto a horizontal image line.

## Measurements (rows.py, 50 pct coverage)
- Route 1, body directly: body blob below the flat wings / at the V bottom is 11-12 px (f6, f24, f30, f48, f54);
  thin head/beak and edge-on tail are partly sub-threshold, faint pixels add ~2-4 px. f30 (Z = 141.6 m):
  12 px -> 0.68 m, 15 px -> 0.85 m (divide by 0.79 foreshortening).
- Route 2, wingspan: flat-wing frames span 30 px (f6, Z 134), 29 px (f30, Z 141.6), 26 px (f54, Z 149)
  -> 2.03-2.15 m after the 0.60 foreshortening; golden-eagle length/span ~0.42 -> ~0.88 m.
- Answer 0.85 m (both routes; real-size golden eagle, consistent with real-world scale).

## Confidence
Low-moderate: the bird is ~12-30 px, the body is not cleanly separable from the wings, and the foreshortening
assumes the eagle faces its direction of motion. Plausible range 0.7-1.0 m.
