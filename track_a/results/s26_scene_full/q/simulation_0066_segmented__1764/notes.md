# q_1764 — width of the white car (van), simulation_0066_segmented

**Answer: 1.93 m**

## Setup
- 3D Blender scene, static camera, 2160x1080, 24 fps (same as question_fps). t=0.58 → frame 14, t=1.58 → frame 38.
- White car = the white cargo van (`scene/tracks/van.csv`). Prior: the van's acceleration is 4 m/s².
- depth_info: van 23.5892 m at frame 14 and 19.9903 m at frame 38. Depths are also given for the pedestrian, the taxi (yellow car) and the cyclist (bike).
- Width = the van's shorter horizontal extent (side to side).
- No side mirror sticks out of the silhouette (checked on frame-71 zooms), so the bounding-box width is taken as the body width.

## Method
1. **Rigid feature tracks** (`track_feats.py`): LK tracks on the van, about 80 kept, all frames.
2. **Pure-translation fit** (`trans_fit.py`): p_k(i) = VP + A_k / (z_k + (i − i0)²).
   - Travel vanishing point VP = (624, 79.5) ± 0.5 px. i0 = −1.06 ± 0.1. Median residual 0.36 px on frames 2–50.
   - So the van moves in a straight line with constant acceleration (with a small initial speed).
   - Frames 0 and 1 of the video are identical.
3. **Kinematic scale**: s = ½·4·((i − i0)/24)² metres. Given f, this places every feature in 3D (camera z ∝ 1/ρ from VP).
4. **Focal length** (independent of scale):
   - Pedestrian body axis (head–hip line) over all 72 frames, compared with the vertical vanishing point of a zero-roll camera whose horizon passes through VP (`vertical_scan.py`): f ≈ 870–910.
   - Purple parked sedan's long-axis VP (3279, 50), assumed perpendicular to the van's path (`vp_lines.py`): f ≈ 882 (785–1013). Both VPs lie near the same horizon height, which supports a level camera.
   - A depth-plus-kinematics match at frame 14, with the origin at the fitted box centre: f ≈ 928.
   - Adopted f = 900 (hFOV about 100°; equals a 15 mm lens on a 36 mm sensor).
5. **Footprint** (`footprint.py`): for each frame 20–71, the two vertical tangent planes of the van silhouette (lines through the vertical VP), expressed in the van's plan frame (travel direction e, lateral, up).
   - Solved by linear least squares for the plan rectangle (centre, L, W).
   - At f = 900: L = 5.645 m, W = 1.918 m, rms 1.6 cm over 104 constraints. The tangents touch the rear corner on the near side and the front corner on the far side (body corners, not mirrors).

## Scale routes and check
| scale source (f = 900) | W (m) |
|---|---|
| a = 4 m/s² kinematics | 1.918 |
| depth_info at t = 0.58 (origin = fitted box centre) | 1.937 |
| depth_info at t = 1.58 | 1.981 |

- With the box centre as origin, the kinematic distances match depth_info to 1% at frame 14 and 3% at frame 38.
- **Inconsistency found:** the given depth ratio d14/d38 = 1.180 cannot be reproduced by any point on the van for any f (the image gives about 1.20).
  - At frame 38 the gap is about 0.4 m whatever f is.
  - A uniform time offset of about 2.5 frames in depth_info, with f ≈ 897, would reconcile both depths with the kinematics. That gives W ≈ 1.92.
- Sensitivity to f: W(850) = 1.965, W(950) = 1.870 (kinematic route).
- Frame-window check (f = 900): frames 10–45 → 2.01, 30–65 → 1.93, 45–71 → 1.85, so the window choice adds about ±4%.

## Confidence
Moderate: about ±5%. The main uncertainties are f (±30 px gives ±3%), the box model of a rounded van, and the depth/prior inconsistency (1–3%). Reported value: 1.93 m.
