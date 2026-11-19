# q1342 — width of the green car (simulation_0066)

The question asks for the width of the parked green coupe (BMW E24 style), which is static on the far side of road B with its
nose pointing left. Width means the horizontal extent across the car. The car is parked along road B, so its width runs along
road A, which in this view points mostly away from the camera. The file fps (24) equals question_fps (24).
Depth frames: t=0.58 s → f14, t=1.58 s → f38.

## Camera model (scripts: curbs.py, vpA.py, vert.py, ped.py, vanacc.py, geom.py)
- Curb lines were extracted in code from scene/bg.png (sidewalk/road colour boundary).
  - VP_A (road A) ≈ (620, 75): clean lines A_right_far × A_left_near give (623, 80); lsq gives (636, 81).
  - VP_B (road B) ≈ (3125, 78): the far curb is one straight line (rms 0.6 px), intersected with the near-right curb.
  - Horizon y ≈ 76, roll ≈ 0. Perpendicular roads with the principal point at the centre give **f ≈ 835–855 px**.
  - Check from the vertical VP of the pole lines, ≈ (1030, 2008): f ≈ 825.
- Checks with the question's depth_info at f = 850 (pitch 28.6°, roll 0):
  - Pedestrian, from pelvis depth plus head and feet pixels: height 1.80 m, pelvis 0.93 m above the feet,
    camera height **H = 6.96 m**. At f = 1200 the height would be 1.50 m and the pelvis 0.78 m, which is implausible.
  - The f14→f38 displacements from the depths are parallel to the ground plane within ±0.15 m for all four objects.
  - Van displacement f14→f38 is 4.25–4.36 m. With the prior a = 4 m/s² this means the van starts from rest at t ≈ 0,
    which fits the record (the van is nearly still in the first frames). The prior does not constrain f strongly here,
    because the van moves mostly along the line of sight.
  - Rough van ground points (3/4 down the box) sit 6.9–7.1 m below the camera, in line with H = 6.96.

## Width measurement (green4.py, green5.py, gmask.py)
- The car pixels come from bg.png, using the teal mask G − R > 12.
- **Near front-bottom corner** (end of the front spoiler, near side): (1504.5, 409.5).
- **Far front corner** is the car's leftmost column, x = 1442.
- These were back-projected onto planes h = 0.15–0.3 m. The front lower edge runs along road A (perpendicular to road B,
  horizontal). The width is the length along that line from the near corner until its projection reaches x = 1442.
  - Result: **W = 1.82–1.90 m**, for f 830–1000, horizon 66–86 and corner pixel ±1.5 px.
  - The predicted far-corner y (386) matches the top of the observed leftmost teal rows (386–393).
- A direct two-point reading is very sensitive to the far corner's y (≈ 0.05 m/px), because the width axis is close to the
  depth direction. The reading (1442, 386)/(1501, 409) satisfies the flat-front-face check (ΔB ≈ 0) and gives 1.82 m.
- The box overlay (frames/box.png) with W = 1.83 matches the front face, near sill line and hood edge.

## Second route
- The near-side tyre contacts (1516.7, 414) and (1596.7, 397) give a wheelbase of 2.79 m. The car is aligned with road B
  to within 0.01 m over the wheelbase.
- Using the real E24 width/wheelbase ratio (1.725/2.626 = 0.657) gives 1.83 m. This assumes the model has real proportions,
  so it is a sanity check only.

## Answer
**1.85 m**, roughly the middle of 1.82–1.90.
- Small door mirrors are visible at the A-pillar base and do not stick out noticeably. They could add a few cm to the
  bounding box.
- Confidence: moderate, about ±5–8%. The main uncertainties are which pixels mark the far corner, and f / H (the pedestrian
  height check depends on human proportions).
