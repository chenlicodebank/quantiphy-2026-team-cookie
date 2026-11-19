# q1185: width of the telephone booth (simulation_0046)

Answer: **1.12 m**. This is the booth's extent along the street (its front face, roof cap included), which is its shorter horizontal side.

## Time base
The file and the question both use 33 fps, so t=1 s is frame 33 and t=2 s is frame 66. The booth is static.

## Focal length (from the moving bicycle wheel, 0.65 m)
- **Wheel size in pixels.** I measured the outer tyre extent along the hub row (`wheel_ext.py`, several frames around each time):
  - t=1: front 100.9 px, rear 101.5 px
  - t=2: front 93.3 px, rear 94.8 px
- **Model (`focal.py`).** Each wheel is a 3D circle in the bike's heading-vertical plane. The bike is placed at its given distances (12.6215 m, 13.2055 m) and its heading comes from those positions, about 6.6° away from the camera. The model therefore includes the yaw foreshortening at t=2.
- **Result.** f = 1887–1928 px over the wheel/time combinations. I use **f = 1912 px** (horizontal FOV ≈ 53°).

## Camera pose (vanishing points)
- **Yaw.** Lines along the facade (booth roof edge, PHOTO LAB sign, near kerb) converge to a vanishing point at u ≈ −16000 on the horizon. So the camera is yawed about 6.4° to the street.
- **Independent check of the yaw.** The predicted depth-direction vanishing point is at (1175, 341). The line from it reproduces the booth's side roof-edge slope: 0.199 predicted vs 0.198 measured.
- **Horizon.** Three estimates agree:
  - booth side edge combined with the orthogonality of the two vanishing points: y ≈ 340
  - convergence of vertical lines (camera pitch about 1.3° down): y ≈ 339
  - the bike's ground contact at the two times: y ≈ 344

  I use y = 341.
- **Check against the bike.** The bike's 3D motion between t=1 and t=2, computed from the given distances, runs parallel to this street axis within 0.16°. That is strong confirmation of the pose and of the bike distances.

## Ground planes and booth depth (`geom.py`)
- **Street.** Camera height above the street is 1.656 m. It comes from the wheel centres at the given distances plus the 0.325 m wheel radius, and the two times agree (1.655 and 1.658 m).
- **Kerb.** The kerb face spans v = 562.5–584 at u = 1050, which gives a height of 0.147 m. The sidewalk plane is therefore 1.509 m below the camera.
- **Booth base.** The bottom edge of the booth's front base runs from v = 549.4 at u = 83 to v = 551.2 at u = 225; its slope matches the yaw. Back-projected onto the sidewalk plane, the booth's front is about 15.3 m from the camera.
- **Front face in pixels (frame 0, row profiles):**
  - roof cap: u = 76.7 → 223.5 (146.8 px)
  - body posts: u = 82.5 → 220.5
- **Widths:** roof cap (the bounding-box extent) **1.118 m**; body 1.051 m.
- **Other dimensions:** front-to-back depth 1.20 m (side face out to u = 297); height 2.86 m.
- **Reading of "width".** The shorter horizontal extent and the width across the front face are the same edge here, about 1.12 m. The front-to-back depth is about 1.20 m.

## Robustness / second route
Varying each input over its range (`sens.py`) changes the roof-cap width as follows:

| Input varied | Range tested | Roof-cap width (m) |
|---|---|---|
| Focal length f | 1887–1928 px | 1.111–1.129 |
| Horizon | 336–346 | 1.114–1.122 |
| Yaw vanishing point u | −15000 to −17500 | 1.118 |
| Horizon at the image centre (zero pitch, rejected) | y = 383 | 1.157 |

The street-plane height is consistent at both bike times, and the bike's motion matches the street axis independently.

## Caveat: walker distances
The given walker distances (14.77 m, 15.18 m) do not fit the image:
- **Image size.** The walker's height (≈244 px) and foot row (y = 558–559) are almost constant, while the distances imply he recedes about 5%.
- **Ground plane.** Placing his feet on the sidewalk plane gives a pelvis distance of 13.6–13.8 m, and a walker height of 1.69 m.

So I did not use them. Taking the booth depth from the walker's given distance instead would give about 1.20–1.23 m.

Confidence: moderate-good, about ±4%.
