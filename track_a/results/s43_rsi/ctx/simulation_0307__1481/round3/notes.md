# Q1481: length of the plane (m), investigation round 2

Prior: speed 22.16 m/s. depth_info: 102.6664 m at t = 1 s (frame 24) and 121.8263 m at t = 2 s (frame 48).
question_fps = file fps = 24. This is a 3D Blender scene with a static camera. A VTOL aircraft flies away from the camera, up-left in the image, with a constant attitude.
Its parts: twin pods, a central fuselage with the canopy and a ventral fin under its rear end, wings with ducted fans, and wingtip fins.

## What the answer depends on
The nose-to-tail extent along the flight direction, from the frontmost point to the rearmost point.
The scale comes from |V| = 22.16 and the two origin depths, through a constant-velocity pinhole fit.

## Crux
Where the length ends at the rear:
- C2/C3/C6 (10.6–10.8) ended it at the pod rear tips.
- Round 1 (14.8) ended it at the central fuselage end and the ventral-fin trailing edge, which it found 4.9 m further aft.

## Verifying round 1 (own code, own clicks)
1. **Scale (`fitf.py`).** Constant-velocity fit over frames 2–71, with |V| = 22.16 and both depths:
   - hull centroid: f = 3390, V = (-10.61, -6.35, 18.39), rms 2.3 px;
   - bbox centre: f = 3240.
2. **Tracking (`track.py`).** Chain NCC from frame-2 clicks (`feat2.json`), refined against a scaled frame-2 template. The points:
   - LR: left pod tip
   - RR: right pod tip
   - RC: lower corner of the fuselage rear end
   - VB: ventral-fin bottom tip
   - VF: fin top front
   - AN: antenna tip
   - FLt: left fin top

   The pod-front corner LF drifts along its edge in the automatic track (9 px at frame 24). I therefore clicked it by hand on 8–10x CLAHE zooms at frames 2, 6, 12, 18, 24, 30, 36, 42, 48 and 60 (`manual.json`, LFm).
   Overlays are in frames/ov_2/24/48/71.png.
3. **Triangulation (`tri.py`, `world.py`).** Each point is triangulated as a fixed point translating with V. I used a level-flight world frame: up is perpendicular to V, which puts the camera pitch at 19°.

   Coordinates relative to LFm (hull f), in m:

   | point | aft | lat | up | rms (px) |
   |---|---|---|---|---|
   | LR | 9.45 | -0.40 | -1.86 | 2.0 |
   | RR | 9.37 | -9.36 | -1.89 | 1.4 |
   | RC | 14.43 | -4.93 | 0.52 | 1.5 |
   | VB | 14.32 | -4.69 | -1.06 | 1.5 |
   | AN | 1.52 | | | 1.6 |
   | FLt | 5.45 | | | |

   - The pod tips are symmetric: aft 9.45 vs 9.37, and their lateral midpoint -4.88 is the centreline.
   - RC and VB lie on the centreline, 4.9–5.1 m aft of both pod tips, in every frame window: 0–36, 12–48, 24–71 and 0–71.
   - VB is 1.6 m below RC. The trailing edge is near vertical (the aft offset is 0.1 m).
   - Model-light check: from frame 2 to frame 71, RC and VB both move 1155 px and RR moves 1099 px. So RC and VB are nearer the camera. Being lower would put a point farther from this downward-looking camera, so they are aft.
   - `depthscan.py`: putting VB 1 m off its fitted depth raises its rms from 1.8 to about 3 px; at the ~5 m shift that would bring it level with the pod tips, the rms passes 10 px. So round 1's fault is **reproduced**.
   - Note: RR (the right pod tip) and RC overlap in frame 2 (10 px apart), but by frame 24 they are 37 px apart. They are different parts.
4. **Front end.**
   - LF (pod front top corner) is the frontmost point. The antenna is 1.5 m behind it, the fin tops 5.4 m behind and the canopy further back.
   - A bootstrap with ±1.5 px click noise gives an LF→RC sd of 0.18 m.
   - C3's three LF clicks (its frame-48 click is 6 px lower on the edge) put LF 0.9 m further forward, with rms 3.05 px against 2.0 px for my 10 clicks.

## Results: length LF → RC/VB along the flight direction
| route | f | LF→RC | LF→VB |
|---|---|---|---|
| hull origin, frames 0–71 | 3390 | 14.43 | 14.32 |
| bbox origin, frames 0–71 | 3240 | 14.67 | 14.60 |
| hull, frames 0–36 | 3390 | 14.45 | 14.37 |
| hull, frames 12–48 | 3390 | 14.22 | 14.21 |
| hull, frames 24–71 (4 LF clicks) | 3390 | 13.98 | 13.78 |

- Answer: **14.5 m**, with a range of 14.0–14.7.
- The rounded fuselage tail cap may reach about 0.1–0.3 m beyond RC. Ending at the ventral-fin edge point VM gives 15.0 m, but VM is a sliding edge point (rms 4.5 px), so I did not use it.

## Rechecks
- a. **Closure.**
  - At f = 3390, the hull-centroid rays at frames 24 and 48 with the given depths imply a speed of 22.22 m/s (+0.3 %).
  - At f = 3240 (bbox), they imply 22.38 m/s (+1.0 %).
  - The fit reproduces the depth at frame 48 to 0.04 m.
- b. **Plausibility.**
  - The aircraft comes out 14.5 m long and 18.2 m across the fin tops (FLt lat +4.18, with the centreline at -4.9). The pods are 9 m apart.
  - The speed is 22 m/s. All of this is plausible for a V-22-class VTOL.
  - I did not re-measure the tanks: no depth is given for the ground. An earlier session put them at 7.6–8.7 m at f ≈ 3400, which is plausible.
- c. **Units and time base.** The answer is in metres. question_fps = 24 = file fps; the depths are at frames 24 and 48.
- d. **Fault proof.**
  - C2/C3/C6 (10.6–10.8): they missed the fuselage end and fin, which lie 4.9–5.1 m aft of the pod tips (shown above). Their pod length (10.5–11) is itself about 10 % above mine (9.4–9.5), because of their LF clicks and joint fit.
  - C1 (17.4), C5 (19.3), C7 (20) and C8 (17.8): these are the span or a silhouette long axis. My span is 18.2, and a wingspan is never the length.
  - C4 (15.9): a PCA box mixing span and length.
  - Round 1 (14.8): it is the right reading. Its value is 2 % above mine, because some of its variants used C3's LF clicks (giving 15.4).

## Decision
The fault in the submitted 10.7 is reproduced, and round 1's proposed 14.8 is confirmed within 3 %. Since I have my own value, the decision is **new: 14.5 m**, confidence medium.
Uncertainty: the LF corner depth (±0.3 m), and whether the reference box is aligned with the flight direction.
