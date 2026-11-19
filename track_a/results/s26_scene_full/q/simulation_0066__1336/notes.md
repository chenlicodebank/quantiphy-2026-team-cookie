# Q1336: height of the turning yellow car (taxi), in metres

The file and the question both run at 24 fps (frame = round(t*24); f14 = 0.58 s, f38 = 1.58 s).

## Camera calibration (curbs.py, poles.py, geom.py)
- Vertical vanishing point from 4 poles (sub-pixel row centroids, line fit rms < 0.2 px): (1082, 2112). It lies at
  x = cx, so roll is about 0 and the principal point sits on the vertical centre line.
- Road vanishing points from curb edges (gradient fits): road A (621.5, 78.0), road B (3130–3137, 73–76).
- Focal length from three independent pairs: A+vertical 852.8, B+vertical 852.6–854.9, A+B (orthogonal) 851.8–852.9
  → **f = 853 px** (HFOV ≈ 104°, a strong wide angle; leaning poles confirm it). Horizon y ≈ 77 → pitch 28.5° down.
  Check: the model reproduces the vertical VP at y = 2111.5 (measured 2112.5).
- Check against the prior: with f = 853 the white van's 3D displacement f14→f38 (from depths) is about 4.25 m.
  Uniform 4 m/s² from rest gives 4.33 − 4·t0, so t0 ≈ 0.02 s. That fits the van starting at the clip start.

## Camera height H (sets the scale; given depths)
- Pedestrian f38: feet ground point plus pelvis ray at the given depth 21.3488 → H = 7.05–7.17 (insensitive to the
  pelvis pixel; ±3 px in the feet row gives ±0.06). At f14 the given depth with a 0.95–1.05 m pelvis gives H = 7.01–7.11.
- Taxi f38: plan centre from the near-side tyre contacts plus a lateral offset, at the given depth 16.549 →
  H = 6.88–7.04, depending on the origin height (0–0.8 m) and centre placement.
- Adopted **H = 7.03 m** (±0.08).

## Taxi top height in units of H (signfit.py, signfit2.py)
- In 8 frames (f38–f71, relative heading varying by 48°) I read three points from gridded 3–4x crops: the near-side
  front and rear tyre ground contacts, and the top of the roof light bar.
- For a trial height hs, the roof-light-top ray is cut with the plane z = hs, and the point is expressed in car-body
  coordinates (from the tyre contacts). hs is chosen so that this body point stays fixed across frames.
- Result: hs = 0.237 (all frames). Leave-one-out gives 0.234–0.240; dropping the pole-occluded f38/f46 gives 0.230.
  So hs = 0.236 ± 0.005.
- Consistency check: the fitted lateral position (0.155 H ≈ 1.09 m beyond the near tyre line) is the far end of a
  transverse roof light bar. The bar is about 0.45 m wide, seen in the front views f6/f26. That puts the car centre
  about 0.87 m from the near outer tyre line, which is a normal half track. The fitted wheelbase is 0.441 H ≈ 3.1 m.

## Answer
Height = top of the roof light above the ground (AABB vertical extent) = 0.236 × 7.03 ≈ **1.66 m**.
Sanity check: a Crown-Victoria-style taxi is 1.47 m without the light, so 1.6–1.75 m with a roof light. The model here
is slightly larger than real (wheelbase 3.1 m vs 2.91 m). Using the taxi-only H (6.95) gives 1.64; using the
pedestrian-only H (7.11) gives 1.68.
Confidence: moderate, roughly ±5%. The main uncertainties are the hand-read tyre and light-top points and the choice
of H.
