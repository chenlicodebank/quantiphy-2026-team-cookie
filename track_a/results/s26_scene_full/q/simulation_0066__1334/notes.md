# q1334 — height of the white car (the white Chevrolet-style van), simulation_0066

The file and question_fps are both 24, so frame = round(t*24): t = 0.58 → f14 and t = 1.58 → f38.
Answer: **2.10 m**

## Camera calibration (3D scene, static camera)
- Vertical vanishing point: centre lines of 6 poles (`poles.py`, `vvp.py`) meet at (1077, 2102). All 15 pairwise
  intersections fall between y = 2008 and 2128, and x ≈ cx, so roll ≈ 0.
- Road A vanishing point: (627, 79.5) from refined curbs (`curbs.py`), and (642, 81) from the van's own image track
  (1D projective fit in `kin.py`). Road B vanishing point: (3135–3148, 70–75).
- The three vanishing points agree, with the principal point at the image centre:
  f = 846 px (from vertical + road A, and from road A ⟂ road B: 846.6). Horizon y ≈ 78–82, pitch ≈ 28.5°, HFOV ≈ 104°.
  (`cam.py`)
- Camera height above the ground: the pedestrian's pelvis (given depth 21.35 m at f38) plus the vertical through the
  feet gives Hc = 7.00 ± 0.06 m (pelvis 0.98 m above ground). The pedestrian's height stays constant between f14 and
  f38 (−6.020 vs −6.023 m), which checks the pitch.

## Van height
- `boxfit.py`: a box standing on the ground plane, heading toward road A's vanishing point, fitted to the van's silhouette
  (convex hull; cyclist box excluded) by IoU. Size is shared across frames; position is free per frame.
  * f38,46,54,60,66,71: L 5.67, W 1.91, **H 2.114**
  * f38–50: H 2.100;  f62–71: H 2.095;  first run (bad windshield mask): H 2.054
- Scale check against depth_info: the fitted box centre is 19.97 m from the camera at f38 (given 19.99 m, 0.1 % off).
  At f14 the van is small and the fit is poor (1−IoU 0.20); it gives 24.7 m vs the given 23.59 m.
  Centroid ray to the plane at half height gives 23.8 m at f14.
- Prior check (a = 4 m/s²): the van centres from depth_info + f = 846 move 4.25 m from f14 to f38. Uniform a = 4 from
  rest at t = 0 gives 4.33 m (2 % apart). The fixed-box track f14–71 (`boxtrack.py`) gives a = 4.02 m/s².
  Later windows give 4.3–4.7 (box/shape bias when the van is close).
- Second route: the centroid points at the given depths sit 0.97 m (f38) and 1.12 m (f14) above the ground. If the origin
  is the box centre, that means H ≈ 1.9–2.2 (mean 2.08), which agrees.
- Sanity: a real Chevy Express is about 2.08–2.11 m tall and 5.7 m long, consistent with the fit.

## Confidence
Estimate 2.10 m, about ±4 %. The main error sources are box-versus-rounded-body shape bias and Hc (±1 %).
