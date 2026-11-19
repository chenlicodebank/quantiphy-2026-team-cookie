# q_1778: height of the purple car (m)

Answer: **1.45 m** (estimated uncertainty about ±6%).

## Setup
- 3D Blender scene, segmentation video, 2160x1080, 24 fps. The file rate equals question_fps, so t = 0.58 s is frame 14 and t = 1.58 s is frame 38.
- The purple car is the parked sedan at the lower left. It is static and no depth is given for it.
- Prior: the white car (van) has a constant acceleration of 4 m/s².
- Depths are given at frames 14 and 38 for the human, the taxi, the van and the bike.
- The camera is static (scene record), and the principal point is taken at the image centre.

## Focal length (f ≈ 900 px), from four routes
1. **Van kinematics.** The van starts at rest (t0 ≈ 0–0.04 s) and moves s = 2(t − t0)².
   - Its displacement from frame 14 to 38 should be 4.17–4.33 m.
   - Matching |O38 − O14| (from depths plus centroid rays) gives f ≈ 845–980. At f = 900 the displacement is 4.256 m, which fits t0 ≈ 0.018 s.
2. **Purple car's wheel ellipses** (`wheels2.py`, `circpose.py`).
   - Each rim edge was fitted with an ellipse, and the circle's pose was solved for each f.
   - The two wheel normals agree to about 1°, and the wheelbase vector is perpendicular to the normal only at f ≈ 900 (0.3° there, compared with 3.6° at 800 and 4.9° at 1000).
3. **Pedestrian path.** The 3D angle between the pedestrian's and the van's displacements reaches its maximum of 89.6° at f ≈ 900, consistent with perpendicular paths.
4. **Van front wheel at frame 71.** Its axle is perpendicular to the van's direction at f ≈ 950.

## Ground plane and camera height
The fits are in `hyp.py`, `joint.py` and `fixedup.py`.
- **Up vector.** It was fitted under two hypotheses: vehicle origins at ground level (rig root) or at the vehicle's centre.
  - Constraints: the depth points' heights, the van's front-tyre ground contacts at frames 38 and 71 (translated 12.39 m along the van's direction, from a = 4), and the pedestrian.
  - Result: up ≈ (−0.01, −0.867, −0.50). This agrees within about 2° with the up vector from the purple car's own wheels, (0.007, −0.855, −0.519).
- **Camera height.** It comes out at 7.2–8.2 m depending on the route.
- The pedestrian then comes out about 2.2 m tall with a pelvis at about 1.2 m, so the scene is not at real-world scale.

## Purple car height (`height.py`)
- The tyre bottoms (157.8, 896.5) and (506.8, 800.5) were intersected with the ground plane to give the near-side contact line.
- A vertical plane through that line, moved about 0.1 m inward for the roof's inward lean, was intersected with the rays to the near-side roof rail, at pixels (191.4, 761.4) and (272.9, 740.0).
- Roof-rail heights over all the camera variants: 1.35–1.54 m. The central routes give 1.42–1.47 m; at f = 900 they give 1.42–1.47 m.
- Adding about 0.03 m for the roof crown gives about 1.45 m.

## Checks
- **Car-internal consistency.** Rail height divided by wheelbase is about 0.46–0.47 for every camera variant (wheelbase 2.95–3.25 m).
  - The far roof edge sits about 1.45 m laterally from the near contact line, giving a roof about 1.35 m wide.
  - These proportions are typical for a sedan of this shape (a Mercedes W126-like model). That model is about 1.44 m tall with a wheelbase of 2.9–3.1 m, consistent with 1.45 m.
- **Van-tyre route with the car's own up vector.** This gives a rail height of 1.41–1.42 m for every f from 850 to 950, the most stable route.

## Confidence
Medium. The main uncertainties are:
- the focal length (±5% in f gives about ±5% in height);
- the ground tilt and camera height;
- the rail inset and roof crown (±0.05 m).
