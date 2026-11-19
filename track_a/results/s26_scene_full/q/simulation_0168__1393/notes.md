# q_1393 – length of the police car (van), simulation_0168

Prior: bike speed 5.52 m/s. depth_info: bike–camera 28.219 m (t=0, frame 0), 25.554 m (t=0.5 s, frame 12).
question_fps = file fps = 24.

## Camera geometry
* No roll / no pitch: long vertical edges tilt −0.05° (`roll.py`). The common vanishing point of six rigid-point
  tracks (van FR/RR tyre contacts, plate, light-bar top; cyclist ground point, helmet top) is (2640 ± 7, 540)
  (`vp_tracks.py`). So the bike and the van move parallel, along the horizontal direction D ∝ (1680/f, 0, 1).
* Focal length: with constant speed, the triangle camera–P(0)–P(12) (sides 28.219, 25.554, 2.76 m) puts the heading
  at 14.33° from the t=0 ray. I fitted f and the bike origin pixel to the bike hub midpoints read at frames 40, 50,
  60, 70 and 79 (`focal6.py`): **f = 2532 px** (HFOV 41.5°), residuals ≈ 2–3 px. Sensitivity: VP ±30 px → f ±80;
  hub readings ±5 px → f ±17. A model with the bike origin at the hip pixel instead gives about 2450.
  Independent check from the van wheel rim ellipses at frame 79 (wheel plane ⊥ lateral axis): measured axis
  ratios 0.395 (rear) and 0.46 (front); predicted 0.396 and 0.48 at f = 2532, but 0.28 and 0.34 at f = 4000, so
  this supports f ≈ 2530–2600.
* Camera height: bike hub height 0.887 m below the camera, plus a bike wheel radius of 0.375 m, gives
  h = 1.26 m. The bike's front-wheel contact rows give 1.23–1.29 m, which agrees.

## Van
* Pose: FR tyre contacts (scene record, hand-anchored at frames 40–79) on the ground plane, z = f h/(y − 540).
  Wheelbase = 3.09 m (3.0 m from the hubs at frame 79, 3.12 m at frame 70); FR/RR line parallel to D within 1°.
  Wheel radius from the hubs is 0.388 m at both wheels (consistent).
* Front end = licence plate (on the front bumper, centred under the VW logo). Rear end = rear-right silhouette
  corner. Body edge columns: frame 40 → 1903, 50 → 1820, 60 → 1721.5, 70 → 1595, 79 → 1450. The rear bumper
  sticks out a little further: 60 → 1726, 70 → 1604, 79 → 1457. Rear edges were checked on zoomed crops and
  intensity profiles (`edges.py`).
* The flank is seen at a grazing angle (13–23°), so the rear position depends strongly on the body-side lateral
  offset (≈ 2.4 m of length error per metre of lateral error). Two ways of fixing the lateral positions:
  * **Set B** (`triang.py`, `final2.py`): plate offset triangulated across frames 40–79 (rms 1.5 px), and the
    body side at +0.07…+0.13 m from the contact line (hubs are +0.075 m outboard of the contacts; the free fit
    gives +0.09). Result: L ≈ 4.10 m to the body edge, 4.22 m to the bumper. Spread over VP 2630–2650 and
    f 2480–2580: 3.9–4.4 m.
  * **Set A** (`final3.py`): centreline = FR contact − track/2 (FL–FR track 1.66 m); body side from the
    front-face width (1.90 m). Result: L ≈ 4.20–4.35 m to the body edge, 4.38–4.43 m to the bumper. This set is
    stable across VP and f.
  * Set B puts the plate 0.94 m from the right contact line, while the front-face width implies about 0.83 m. The
    two sets bracket the answer.
* Bumper to bumper (rear-most point = rear bumper): about 4.2–4.4 m. **Answer 4.3 m.**
* If the reference AABB is aligned with the road (VP 2777) rather than the van's heading, the length would rise
  by about +0.07 m. Not applied.

## Confidence
Moderate: about ±6 % from the lateral-offset ambiguity at the grazing flank view, plus about ±3 % from f, the VP
and the camera height. Scripts in this folder: focal*.py, vp_tracks.py, roll.py, van3d.py, length*.py,
triang.py, pipeline.py, final*.py, crops.py.
