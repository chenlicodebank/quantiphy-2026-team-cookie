# q_1252: height of the streetlight (simulation_0059, 3D Blender scene)

Answer: **3.17 m**. File fps = question_fps = 24.

## Object
"Streetlight" = the ornate double-lantern lamp posts. All of them are the same model. The four nearest were measured on
frame 24 with half-contrast edges in code (`lamp_row.py`). Height runs from the finial tip to the bottom of the base:
L1 (x 431) 541.3 to 897.0; L2 (x 654) 586.2 to 844.5; R1 (x 1932) 530.6 to 908.8; R2 (x 1742) 579.8 to 851.1 px.
In world units the four come out the same height to within 0.4 %.

## Camera
- Horizon: lamp tops and bases on each side converge at y = 704.7 (right pair) and 705.2 (left pair). The scene record's
  curb vanishing point gives 702. I used **705**.
- Vertical vanishing point: the near lamp-pole axes were fitted to sub-pixel precision (`poles.py`) and meet at about
  (1084, -27850). That x matches the principal point at the image centre.
- Focal length, from three routes:
  1. f^2 = (horizon - cy)(cy - vertical vanishing point) gives f = 2164 (2179 if pole R2 is included).
  2. The prior: back-project the van ("white car") from its depths at t = 0.58 s and 1.58 s, put the per-frame pixel
     track onto that 3D line and fit a quadratic. Acceleration = 4 m/s^2 when f = 2163 (bbox centre) or 2220
     (side-panel centre) (`solve_f.py`, `solve_f2.py`).
  3. The cross-street directions of the van and the bike are within 1 degree of perpendicular to the main road
     (vanishing point x 1258) for f between 2100 and 2250.
  
  I used **f = 2170 ± 30**. The pitch is 4.4 degrees up.

## Scale
- Camera height above the road: from the bike, using its depth at both times (40.87 m and 40.40 m) and its wheel
  contact at y 800.6 and 801.5. The origin's horizontal distance comes from the depth, and the ground ray at the contact
  row gives h_road = 1.778 m. The van gives about the same value once its near-side tyres are allowed for.
- Curb: on the near-right curb face, the road edge and sidewalk edge rows give h_road / h_sidewalk = 1.0435
  (`curb.py`). So the camera is 1.704 m above the sidewalk.
- Lamp: intersect the base ray with the sidewalk plane, then find the height of the vertical point that projects to the
  top row (`height3d.py`, `final.py`). This gives **H = 3.174 m**, with H / h_sidewalk = 1.863.

## Checks and uncertainty
- All four lamps agree (3.18 to 3.19 m at f = 2160).
- Pedestrian on the same sidewalk, pelvis depth 30.97 m: the soles are hidden behind the top of the garbage bag
  (y ≥ 813 to 821). This gives camera height ≥ 1.61 m above the sidewalk and H ≥ 3.0 m, which is consistent.
- Sensitivity: horizon ±3 px changes H by ∓1.4 %; f ±30 px by ∓1.4 %. Without the curb correction H would be 3.31 m.
  Overall range is about 3.09 to 3.26 m. Confidence: moderate to good, about ±4 %.
- Correction to scene/: the pedestrian's "soles at y ~815" are actually the top edge of the garbage bag that hides the
  feet, so the real foot line is lower (y ≥ 821).
