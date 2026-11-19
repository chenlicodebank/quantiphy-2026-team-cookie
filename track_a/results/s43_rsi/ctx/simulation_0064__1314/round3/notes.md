# q1314: height of the traffic light (simulation_0064), round 2 (verification of round 1's switch to 4.97)

The file and question_fps are both 24, so frame = round(24 t). Frames 14 and 38 are the depth_info times.
Asked object: the signal asset on each corner (pole, 3-lamp head, pedestrian box, triangular crossing sign on top). Its height is the AABB vertical extent from the pole base to the sign apex.

## Crux
H_light = k(horizon, vertical VP) × camera height Hc. The answers part ways on:
- the camera geometry: f and pitch, and where Hc comes from;
- the top point: sign apex (row ≈65) vs head top (row ≈150).

## My measurements (own code)
- **curbs.py:** sub-pixel gradient fits of the two long near curb edges.
  - Left: x = −0.6526 y + 1004.2 (n=212, rms 0.94).
  - Right: x = 1.0547 y + 1212.4 (n=147, rms 0.37).
  - Street VP (1084, −122), so the horizon is at y = −122 (overlay frames/curbs_ov.png).
- **poles.py:** dark-ridge axis fits of both near poles (rms 0.46–0.50 px). Vertical VP: (1068, 7877) at f0/f14 and (1080, 7794) at f60, so yv = 7850 ± 50.
- **Sign apex:** row 65 on the left light, from a zoom (frames/signL.png); 64 on the right light (round-1 value). Base rows: L 571, R 565.4.
- **scan.py:** pinhole model, principal point at the centre, f² = (cy − yh)(yv − cy). Camera height comes from four independent routes:
  - pedestrian f38: pelvis at D = 38.722, then down the vertical to the feet ray;
  - cyclist f14 and f38: wheel contact with the origin 0.45 m up, absolute D;
  - van f14 and f38: front contact with the origin 1.95 m behind, absolute D;
  - van ground track fitted with the prior a = 4 from rest at frame 1. This route is new and does not use depth.

| yh | f | Hc ped / cyc14 / cyc38 / van14 / van38 | Hc(prior kin.) | light/Hc | light L / R | head-only |
|---|---|---|---|---|---|---|
| −60 | 2094 | 5.98 / 6.09 / 6.48 / 6.16 / 6.12 | 6.04 | 0.815 | ≈4.9–5.1 | |
| −75 | 2120 | 6.16 / 6.24 / 6.59 / 6.32 / 6.26 | — | — | 4.988 / 4.986 | 4.20 |
| −90 | 2146 | 6.33 / 6.38 / 6.70 / 6.48 / 6.39 | 6.66 | 0.781 | 4.989 / 4.986 | 4.20 |
| −122 | 2200 | 6.69 / 6.69 / 6.92 / 6.82 / 6.67 | 7.34 | 0.748 | 5.002 / 4.997 | 4.21 |
| −190 | 2310 | 7.41 / 7.30 / 7.37 / 7.48 / 7.23 | 8.83 | 0.687 | ≈5.05 | |

With depth-based Hc, the light height is 4.99–5.00 m and almost independent of the horizon: the ratio and Hc move in opposite directions. The prior-only route agrees best at yh ≈ −75 to −90.

## Rechecks
- **a. Closure:** with the depth-based Hc, the van's ground-track acceleration (bottom rows, from rest at f1, f2–71) comes out as:
  - 3.94 m/s² at yh = −75 (1.5 pct off the prior);
  - 3.84 at yh = −90 (4 pct);
  - 3.65 at yh = −122 (9 pct).

  The depth drop of the van from f14 to f38 (4.09 m) matches the prior's 4.17 m from rest. Round 1's paint-width closure gave 3.99. Closure is about 1.5–4 pct. The answer moves by less than 0.3 pct across these geometries.
- **b. Plausibility:**
  - Pedestrian stature: 1.75 / 1.73 / 1.68 m at yh −75 / −90 / −122.
  - Van paint width: 2.00–2.03 / 1.97–2.01 / 1.91–1.97 m.
  - Pelvis: 0.86–0.91 m.

  All are realistic.
- **c. Units and time base:** metres. Frames 14 = round(0.58·24) and 38 = round(1.58·24); file fps = question fps = 24.
- **d. Fault proof:**
  - **C3 (3.4):** f = 2727 with the measured vertical VP implies a horizon at y ≈ −477. That contradicts the curb VP at −122 (rms < 1 px fits). C3 also measures to the head top. With the correct geometry the head-only height is 4.20, not 3.4.
  - **C4 (3.85) and C5 (2.9):** they also use the head top, with the same f ≈ 2700–3000 geometry family that round 1 showed makes the van 1.55 m wide and the pedestrian 1.41 m tall.
  - **Submitted 4.435:** a 0.7/0.3 blend whose B input (DeepSeek median 3.4) carries those faults.
  - **C1 (4.97), C2 (5.05):** consistent with my 4.99–5.00.

## Decision
Round 1's switch is verified: its claimed fault is reproduced, and my value (4.99–5.00) is within 1 pct of the proposed 4.97. I follow C1, **4.97 m**. Confidence is high on the geometry. The only remaining risk is the reading: if the reference stops at the head top, the answer would be 4.20.
