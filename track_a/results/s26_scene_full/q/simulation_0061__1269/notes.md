# Q1269: speed of the yellow car (taxi) at t = 2.5 s, frame 60 at 24 fps (file fps = question fps = 24)

Answer: **4.25 m/s**

## Method (3D ground-plane geometry)
1. **Focal length from the prior** (`van_f.py`, `solve_f.py`). The white van's image x track fits a
   start-from-rest parabola with start frame k ≈ 0 (rms 0.5 px). So at a = 4 m/s² the van travels
   0.5·4·((38/24)² − (14/24)²) = 4.333 m between f14 and f38. I back-projected the van's bbox centres
   (811.8 → 1020.0 px) with the given depths (45.52 / 43.95 m), and |P38 − P14| = 4.333 m gives
   **f ≈ 2290 px** (±70 px for ±3 px of centre error; HFOV ≈ 50°). Sanity sizes: pedestrian 1.81–1.84 m,
   taxi side length ≈ 5.0 m, van ≈ 5.6 m.
2. **Horizon and camera height** (`calib.py`).
   - Three identical double-lantern lamp posts (A, C, far-left) satisfy (base − v_h) ∝ pole pixel height,
     which gives **horizon v_h ≈ 478 ± 4** (camera pitched about 1.5° down). The record's 535 is wrong.
   - Camera height H comes from ground-contact rows plus the given depths: pedestrian feet f14/f38,
     cyclist wheels f38, taxi tyres f14/f38 (with offsets from the contact to the car centre), and van
     wheel f38.
   - With v_h = 478, H = 2.68 m and the depth residuals are under 3% (van −4.6%). A joint fit gives
     H = 2.60 at v_h = 483. A taxi-only fit gives H = 2.70, with residuals ±1.5%.
3. **Taxi tyre contacts at f44–71** (`contacts.py`).
   - Dark (max channel < 80) connected components below y = 640 give two blobs: the image-left front
     tyre and the image-right rear tyre. Their lowest pixels are the ground contacts.
   - These are diagonal wheels, so the midpoint of their ground points is the car's footprint centre
     (the origin's horizontal position). The diagonal length stays at 3.3–3.45 m, so the pair is rigid
     and the geometry holds.
4. **Speed** (`speed.py`).
   - Fitted the centre's ground X and Z with a quadratic over f50–70 and evaluated it at f59.5 (the f59→60
     backward difference): **4.18 m/s**.
   - A linear fit over f55–64 gives 4.25. The raw |p60 − p59|·24 gives 4.22.
   - Across calibrations (H, v_h) from (2.73, 475) to (2.55, 486), the result spans 4.13–4.39.
   - The car decelerates slowly through the turn: about 4.6 m/s at f48, 4.0 at f70.
   - The axles differ because the car is turning: front-left contact ≈ 4.0 m/s, rear-right ≈ 4.4–4.5 m/s.
     The centre is used because the origin is the car centre.

## Second route (`scale_check.py`)
- An ECC affine fit on the taxi's front fascia between symmetric frame pairs around f60 gives the
  vertical scale change sy = Z_a / Z_b.
- The five pairs give 1.051, 1.073, 1.031, 1.074 and 1.089. The ground model gives 1.043, 1.057, 1.032,
  1.070 and 1.085, so the two agree to within about 1%.
- The mean d ln Z/dt is 0.142 /s. With the front-plane depth (≈ 30.2 m) that gives Ż ≈ 4.3 m/s. Adding
  the lateral rate (≈ 1.2 m/s) gives ≈ 4.45 m/s, about 5% above the ground route.
- The taxi's depth at f38, propagated with this track, comes out about 1% short of the given value. Both
  checks point slightly upward, so I answer 4.25 rather than 4.18.

## Confidence
About ±5%. The main uncertainty is the ground-plane scale (H and horizon) and the centre-offset
assumptions used in the calibration.
