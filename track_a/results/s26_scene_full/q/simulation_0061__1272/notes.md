# Q1272: length of the turning yellow car (taxi)

Answer: **5.0 m**, likely range 4.8–5.15 m.

The file rate equals question_fps (24 fps), so frame = round(t·24): t=0.58 → f14, t=1.58 → f38.

## Focal length (van_fit.py)
- The prior is the white van's acceleration, 4 m/s². I modelled the van as moving on a straight 3D line from P0 with s(t) = v0·t + 2t².
- The fit uses the van's pixel track (scene/tracks/van.csv, bbox centre) and the two given van depths (45.5234 m at f14, 43.9499 m at f38).
- Free parameters: f, P0, heading and v0. Principal point is (1080, 540).
- Result: f = 2157 (f0–71), 2179 (f0–48), 2154 (f10–71), 2207 (f0–40). **I used f ≈ 2180 px** (HFOV ≈ 53°).
- The fitted van heading is about 17° toward the camera.
- Sanity checks at f = 2180:
  - Pedestrian: 124 px at Z 32.4 → 1.84 m tall.
  - Bike: 86 px at Z 41.9 → 1.65 m.
  - Taxi head-on at f38: 128 px wide → W ≈ 2.0 m; about 107 px tall → about 1.75 m with the roof sign.
  - Van: about 6.2 × 2.4 m.

## Taxi measurements (crop.py, ends.py: zoomed frames with pixel ticks)
- **f6:** rear bumper at u = 664.5 and front bumper end at u = 948.7, so the bbox extent is **284 px**. f0 gives the same (634.5 → 919, 284.5 px).
  - Near wheel centres at 720 and 864 (near wheelbase 144 px).
  - Far wheels are shifted about 43 px to the right, so the car is not side-on: it is turned about 27–32° toward the camera, measured against the line of sight.
  - The grille is 23.75 px wide, against 52 px when head-on at f38.
- **f14** (depth given exactly, 40.1 m): extent 716 → 995 = **279 px**.
  - Near wheelbase 133 px, far-wheel shift about 56 px, grille 26 px. These give a heading about 35° from side-on, measured against the line of sight.
- The f6 depth is 40.1 m plus the motion along the line of sight over 8 frames: 5 px/frame across the view at a heading of about 27° gives about 0.047 m/frame, so d6 ≈ 40.45 m.

## Length (box_fit.py, box_f14.py)
- I modelled the car footprint as a rounded rectangle (L × W, corner radius r), placed at depth d on the ray through the bbox centre with the measured heading. L was solved so the projected extent matches the measured one (full perspective).
- With f = 2180 and W = 1.95–2.05 m:
  - Sharp box corners (r = 0): f14 gives 4.76–4.84 m; f6 gives 4.79–4.85 m.
  - r = 0.2: f14 gives 4.95–5.04 m; f6 gives 4.96–5.01 m.
  - r = 0.35: f14 gives 5.10–5.17 m; f6 gives 5.08–5.13 m.
- The two frames are independent routes. f14 uses the given depth directly; f6 uses a different heading. They agree within 1%.
- A real car's bumpers are rounded in plan view, so I take r ≈ 0.2–0.3 m, giving **L ≈ 5.0 m**.
- Changing f by ±1.5% changes L by about ∓1.6%.

## Caveats / confidence
- Medium confidence; I expect the answer to be within about 5%.
- The main uncertainties are the corner rounding (±3%) and f (±1.5%).
- The car looks like a Crown Victoria taxi, whose real length is 5.39 m. The measured proportions are wheelbase about 3.0 m and L/W about 2.5, so the asset is likely shorter than 5.39 m.
- Ground-plane checks were not consistent: the horizon fits disagreed (about 535 vs about 480). I did not use them.
- The record's taxi bbox at f0 is clipped (637–910). The true extent is 634.5–919.
