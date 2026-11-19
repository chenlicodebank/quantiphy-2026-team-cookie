# Q1297: length of the turning yellow car (taxi), in metres. Answer: 5.38 m

The file and the question both use 24 fps, so frame = round(t*24): t=0.58 s is f14 and t=1.58 s is f38.
The camera is static. Principal point is taken as (1080, 540); the horizon is at row 532.3 (from the scene record, via the man's feet/height relation).

## 1. Focal length from the prior (white van, a = 4 m/s²)
- `wheel_tm.py`: multi-scale template match of the van's near rear wheel (+ arch), using a template from f34. Hub track
  covers f26-42 and f46-56 (NCC > 0.8; f43-45 are hidden by the man). Output: `wheel_tm.csv`.
- `van_fit.py`: the tracked body point moves along a straight ground line with s(t) = v0·(t−t38) + ½·4·t², at a fixed
  height k below a level camera: u = cx + fX/Z, v = vh + fk/Z. Rms is 0.27 px for every f. The image alone cannot fix f,
  and a = 4 fixes the metric scale (v38 = 6.42 m/s; fitted start time ≈ t=0, which fits a start from rest).
- The van origin (box centre, offset from the hub by typical van dimensions) must reproduce the given distances:
  D38 = 29.809 → f = 2196 px; D14 = 29.244 (extrapolated back to f14) → f = 2219 px. These are two independent depth checks.
- Sensitivity (`van_sens.py`, `van_rest.py`): van length/width/overhang ±0.3 m → ±15 px. Forcing a start from rest
  at t=0 → f = 2248-2288. Fitting f26-42 only → 2100. Adopted value: **f ≈ 2210 px** (horizontal FOV ≈ 52°).
- Camera height implied by the fit is ≈ 2.09 m (the man is then ≈ 1.80 m tall, which is plausible).

## 2. Check of the camera model against the other depths (`check_depths.py`)
Ground-plane depths with f = 2210 and Hc = 2.087 m, against the given values:
- man at f14: 16.73 (given 16.67)
- man at f38: 15.26 (given 15.50)
- cyclist at f38: 29.49 (given 29.41)

All are within 1.5%. Read the other way, each given depth implies a camera height of 2.08-2.12 m.

## 3. Taxi length
- At f6-26 the taxi is seen side-on: wheel contacts and the line of sight give a heading of ≈17°, perpendicular to the
  line of sight (16.6°).
- `taxi_edge.py`: sub-pixel half-max edges of the (R−B) yellowness profile at the bumper ends. At f14: rear 159.8,
  front 681.1, extent **521.3 px**. A visual zoom gave 158.4 / 682.4.
- The scene record's bbox width (543 px) includes shadow and ~20 px of margin, so it is too wide and was not used.
- `taxi_len.py`: origin = D14 (24.8414 m) along the ray of the silhouette centre. The rays through the two bumper
  extremes are intersected with the vertical plane through the origin along the heading. **L = 5.376 m** at f = 2210.
  - Heading ±6° changes this by <0.7%.
  - Focal length: f = 2150 → 5.50, 2250 → 5.30, 2300 → 5.20.
- Second route (`taxi_len_frames.py`): the same construction on f6-21, with depth scaled from f14 by the rear-tyre ground row.
  Median 5.377, sd 0.04 (range 5.32-5.47).
- Sanity check: a Ford Crown Victoria taxi is 5.39 m long in real life.

## Confidence
The main uncertainty is f, estimated at ±3%, so L ≈ 5.38 ± 0.17 m. The length was measured in the side view, where
the bumper-to-bumper extent is the car's long horizontal extent.
