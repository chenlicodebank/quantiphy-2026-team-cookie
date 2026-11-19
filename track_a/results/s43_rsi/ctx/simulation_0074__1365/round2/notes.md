# Q1365: average speed of the yellow taxi, start to end (m/s). Round-2 investigation

**Answer: 4.1 m/s.** Decision: switch from the submitted blend 3.696 to C2's 4.1. This confirms round 1's proposal.

## Inputs
- Blender 3D render, 2160x1080, 72 frames. The file is 24 fps and question_fps is 24, so frame = round(t*24).
- Depth frames: t=0.58 s is frame 14 and t=1.58 s is frame 38. Given taxi depths: 31.0495 and 30.4267 m.
- Prior: white van (Chevy Express) length = 6 m.
- Frame 0 duplicates frame 1. My own grey differences are 0.019 for 0→1 against 0.318 and 0.341 for the next two steps.

## Crux
The answers part at the taxi's 3D path. One reading puts the taxi on a ground-parallel plane fitted through the two
given depths (4.1). The other extrapolates its depth linearly in time from the two given values (3.2-3.3, plus a long f).

## Measurements (all my own code)
1. **Focal length** (`v1_bg_lines.py`, `v2_vp.py`):
   - Hough kerb and sidewalk lines on a median background: 8 lines go to vA and 7 to vB.
   - vA = (-1294,-258), vB = (2686,-259); line residuals are mostly 0-6 px.
   - f from orthogonal road directions = **1782**, and leave-one-line-out gives 1779-1783.
   - Round 1 got 1783-1794 by the same idea plus pole verticals.
   - The depth data confirm the plane: the plane offset solved from frame 14 and from frame 38 agrees to 0.01 m
     (7.951 / 7.943).
2. **Taxi track** (`v3_track.py`):
   - I track the roof sign, the most saturated orange blob on the foreground, in all 72 frames.
   - Frame 55 is an outlier (another blob) and is interpolated. Frame 0 is set equal to frame 1 (duplicate).
3. **3D path** (`v4_speed.py`):
   - Each sign ray is intersected with the ground-parallel plane. The origin sits δ below the sign, and the plane
     offset is solved so that the origin reproduces both given depths.
   - Mean of the per-frame speeds, steps 2..71 (in brackets: steps 1..71, which includes the duplicate zero step):

     | f | δ = 0 | δ = 0.8 | δ = 1.5 |
     |---|---|---|---|
     | 1782 | 4.21 (4.15) | 4.18 (4.12) | 4.15 (4.09) |
     | 1775-1800 | 4.11-4.22 overall | | |

   - A 5-frame smoothed track (less pixel-noise inflation of the path) gives 4.07 (4.02).
   - The per-frame speed is constant at about 4.1-4.2 with no trend, so there is no deceleration.
   - Origin depth is 32.2, 31.0, 30.3, 30.4, 33.9 m at frames 0, 14, 30, 38, 71: the taxi approaches, then recedes.
4. **Second route, a chord from the given depths alone** (`v6_route2.py`):
   - The given depths are placed directly on the frame-14 and frame-38 rays. The 3D chord is 4.099 m over 1 s.
   - The plane model gives a chord of 4.094 and a path of 4.21 over the same frames.
   - This independently confirms the scale and the speed level.
   - A KLT body-feature track was tried too. It drifted 91 px from the sign by frame 71 and is unreliable, so I
     discarded it.
5. **Value:** the range is 4.02-4.18, depending on smoothing and whether the zero step counts. The central value is
   **4.1**.

## Rechecks
a. **Closure (van length 6 m)** (`v5_van.py`, `v5b_vanlen.py`, frame 66):
   - Camera height is 9.5-9.7 m (sign plane 7.95 m + sign height 1.55-1.75 m).
   - Tyre contacts on the ground give a wheelbase of 3.86-3.94 m, which is the extended Express (3.94 m wheelbase,
     6.2 m long).
   - Scaling the length by the length/wheelbase ratio of 1.54-1.58 gives 5.95-6.2 m, about +2 % against 6 m.
   - The bumper-corner to rear-corner extent is 5.3 m. It is a lower bound, because the rounded bumper corners sit
     behind the bumper front.
   - The bottom-contour route was contaminated by the shadow and is discarded.
   - The speed scale rests mainly on the exact given depths. f enters only weakly: ±10 px moves the speed by 0.5 %.
   - closure ≈ 2-3 %.
b. **Plausibility:**
   - Taxi length along its heading (`v7_taxilen.py`, frames 26/30/34) is 5.43-5.47 m. A Crown Victoria is 5.39 m.
   - Taxi speed 4.1 m/s = 15 km/h in a junction turn.
   - Round 1's pedestrian estimate is about 1.82 m.
c. **Units and time base:** m/s; question_fps 24 = file fps; depth frames 14 and 38.
d. **Fault proof:**
   - **C4 (3.3) and C5 (3.2):** linear-in-time depth extrapolation. It gives D = 31.41 → 29.57 m, while the
     plane-consistent depth goes 32.2 → 30.3 → 33.9 m.
     - My reproduction gives 3.50 at f 1782, 3.38 at f 1850 and 3.25 at f 1930, matching their 3.32 / 3.20.
     - Their f of 1850-1930 is also about 4-8 % above the VP value of 1782.
   - **C3 (3.9):** f = 1659 contradicts the VPs, and it averaged in a biased mask-centroid route. Its own tyre route
     (4.12) agrees with mine.
   - **Submitted blend 3.696:** its B input (the DeepSeek median, 3.3) carries the fault above.
   - **C1 (4.14) and C2 (4.1):** no fault found.

## Decision
I switch to 4.1 and follow C2. Round 1's fault proof is reproduced with independent code, and my own value of 4.02-4.18
agrees with 4.1 within 2 %.
