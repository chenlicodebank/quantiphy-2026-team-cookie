# q_1352 — length of the turning yellow car (taxi), simulation_0067

Answer: **4.88 m**. The file rate and question_fps are both 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Objects
- Yellow car = the taxi (scene/tracks/taxi.csv). It drives away from the camera, then turns right into the east-west
  road. Its yaw goes from about -28° (frame 11) to 53° (frames 56-68).
- White car = the van. Prior: a = 4 m/s².

## Camera (3D scene, static)
- Focal length from vanishing points, with the principal point at the image centre:
  - Two orthogonal road vanishing points, (2697,-43) and (110,-47): f = 1107.
  - Horizon plus a vertical vanishing point fitted in code (poles.py) on 9 poles, giving (1083, 2672): f = 1117.
  - I used **f = 1110 px** (horizontal FOV ≈ 88°). Pitch = atan(585/f) ≈ 27.8°, horizon at y = -45.
  - Checks: the van's 3D heading comes out at -37.1°, matching the diagonal road (-37.7°). The fitted taxi yaw at
    frames 56-68 (51-54°) matches the east-west road (52.2°).
- Camera height above ground from the pedestrian (ped.py): the pelvis is placed in 3D from depth_info, and the
  foot-pixel ray is intersected with the vertical line through it. This gives 7.13 / 7.06 m, so H = 7.09 m (the
  pedestrian comes out 1.85 m tall).

## Measurement: silhouette fit (carfit.py, runfit*.py, occfit.py, gridfit.py)
- The car model is a sedan template with Crown-Victoria proportions: 5.39 m long at scale 1, with lower body, cabin,
  roof sign and 4 wheels.
- Fitted on the ground plane: separate scales kL / kW / kH (length / width / height), plus a position and yaw for
  each frame.
- Cost: IoU against the taxi mask (background difference + orange colour, holes filled). Pixels covered by the van
  are excluded from the cost.
- Side-on frames 13, 15, 17, 19, grid over (kL, kW, kH): the length profile has its minimum at **kL ≈ 0.933**
  (template L ≈ 5.03 m), with kW ≈ 0.88-0.94 and kH ≈ 0.92.
- Depth check: I also fitted frames 14 and 38 and took the box centre at half the box height.
  - Centre depths came out 15.27 / 18.88 m, against the given 14.787 / 18.379 m.
  - That is a uniform factor of 0.969 / 0.973 at two very different yaws, so the ratio matches the given depths
    within 0.5%.
  - I therefore rescaled the scene by **0.971** (camera height 6.88 m). This makes the taxi's own depth_info set the
    scale. The 3% probably comes from the pedestrian foot/pelvis pixels.
- **L = 5.03 × 0.971 ≈ 4.88 m.**

## Second routes and disagreements
- Single-frame optima: frames 13-19 give kL ≈ 0.93. Frame 22 gives 0.90. The rear views (frames 46-68) give
  0.86-0.88, which is ≈ 4.6 m after the 0.971 correction.
  - In rear views the length is foreshortened (it lies 30° off the line of sight), and the far front outline depends
    on the template's hood/bumper shape. So I trust the side-on frames more.
  - Fitting all 8 frames together gives kL ≈ 0.89, i.e. ≈ 4.65 m corrected.
- Bumper-tip check at frame 17 (tipcheck.py): tip pixels projected along the fitted heading, assuming the hood
  front is at 0.9 m and the rear bumper at 0.35-0.45 m. This gives 4.9-5.0 m, but it is very sensitive to the
  assumed heights (±0.3 m per 0.1 m of height).
- Van prior check, where the methods do not agree:
  - The van's centroid track shows uniform acceleration from rest. But with the depth-based scale it gives
    a ≈ 4.4 m/s² (≈ 4.3 after the 0.971 correction), not 4.
  - No plausible van-origin offset fixes this, so the van prior and depths disagree by about 7-10%.
  - I let the taxi's own depths set its scale. If the van prior were used for the scale instead, L would be about
    4.55 m.
- The wheelbase from wheel contacts at frame 60 comes out at 2.9 m (Crown Victoria: 2.91 m), but this is very
  sensitive to the pixels picked.
- Named size: length is the longer horizontal extent, bumper to bumper.

Confidence: moderate, about ±6%. The main uncertainty is the template shape: the side-on and rear views differ by
6-7%.
