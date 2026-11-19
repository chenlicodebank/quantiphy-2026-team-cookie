# q1316 — height of the walking pedestrian (simulation_0064)

The file and the question both use 24 fps. t=0.58 s → frame 14 and t=1.58 s → frame 38.
The prior is the white car's (the van's) acceleration, 4 m/s².

## Focal length (main route: the pedestrian's two depths)
- The pedestrian (white T-shirt, far-left sidewalk) walks along the cross-street sidewalk. The far curb
  of the cross street is horizontal in the image: its bottom edge is at y=319 for x 20–690 and y=320
  for x 1580–2120 (measured in code). So the walking direction is parallel to the camera X axis, and the
  pedestrian keeps a constant camera Z. That gives d² = Z²(1 + ((u-cx)² + (v-cy)²)/f²), and the
  ratio d38/d14 = 38.7220/38.3473 fixes f.
- Pedestrian x: centroid track f34–71 is linear, x = 449.24 − 3.057·frame (rms 1.45 px).
  At f14 they are hidden behind the signal head, so I extrapolated u14 = 406.4. Check: the
  extrapolation at f0 gives 449, which matches the feet glimpsed at x 445–452 in f0–2.
  u38 = 333.1 and the pelvis row is ≈245.
- Result: f = 2183 px. With u14 ±3 px, f is 2134–2230 px.

## Pixel height
- Background difference against f71 for the head and f0 for the legs and feet, plus zoomed,
  contrast-stretched crops. Head top (dark hair) is at y ≈ 192 and the shoe soles at y ≈ 297.5
  (f44–52), so the height is ≈ 105.5 px. The record gave 103 px, but its head-top rows (195–200)
  pick up the face rather than the hair.

## Metric height
- Pitch comes from the horizon at y = −121: φ = atan(661/f). Pelvis depth Z = 36.34 m (camera z).
  I back-projected the head top and the soles along the world vertical through the pelvis:
  **H = 1.76 m**. Across the u14 and pixel-row uncertainties it ranges 1.71–1.82 m.
- Note: d·px/f (1.87 m) would be wrong here. The person is ~785 px off-axis, so the camera Z
  (36.3 m) is what sets the scale, not the ray distance (38.7 m).

## Second-route checks
- Van, using the prior: with the given depths, |P38 − P14| is 4.13 m at f = 2183. Uniform 4 m/s²
  from rest at frame 1 needs 4.17 m. This is consistent but only weakly sensitive to f (radial motion).
- Sanity: the van's paint width of 120 px at Z ≈ 37.75 m gives 2.07 m. A real Chevrolet Express is
  about 2.01 m wide, which implies f ≈ 2115 (within 3%).
- 1.76 m is a plausible adult male height.

Confidence: moderate-good, about ±4%. The main uncertainty is the extrapolated pedestrian x at f14
and the dark-hair head top.
