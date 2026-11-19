# Q1409: astronaut speed at t = 1 s (m/s), round 2

**Inputs**
- Prior: astronaut height 2.2 m.
- depth_info: 18.147 m at t = 1 s.
- question_fps = 24, the same as the file rate, so t = 1 s is frame 24.
- Speed = |P24 - P23| x 24, using the 3D pelvis/root.

**Crux:** whether the astronaut approaches the camera (the depth term, and depth-correcting the rest pixel height), and then the rest height in pixels at frame 24's depth: 388 px (C1/C2) against 400 px (round 1).

## Measurements (my own code, a different method from round 1's ECC)

### `sift_track.py`: pelvis step
- Method: SIFT keypoints on the rigid upper body (helmet, backpack and torso), fitted with a RANSAC similarity transform.
- Template from frame 24: the pelvis point (1080, 795) moves from (1050.34, 809.28) at frame 23, a step of (+29.7, -14.3) px = 32.9 px.
  - Round 1 found 33.3 px with ECC; the mask centroid step is 33.3 px.

### Depth step at frame 24: s24/s23
| Template frame | s24/s23 |
|---|---|
| 21 | 1.0056 |
| 27 | 1.0051 |
| 24 | 1.0058 |
| 23 | 1.0065 |

- With the template at frame 23 or 24 the result is biased: s(template) = 1 exactly, and matches to neighbouring frames come out about 0.001 low.
- The unbiased templates (frames 21 and 27) give 1.0054, so dZ ≈ 18.13 x 0.0054 ≈ 0.098 m per frame (round 1: 0.095).

### `chain.py` and `flight.py`: chained scale through the clip
- The chained similarity scale relative to frame 24 is:

  | Frame | Scale |
  |---|---|
  | 0 | 0.925 |
  | 17 | 0.96 |
  | 36 | 1.05 |
  | 42 | 1.072 |
  | 60 | 1.13-1.14 |
  | 79 | 1.16 |

- At frame 42 the direct SIFT match gives 1.068 and round 1's ECC gave 1.052.
- **Ground-row check.** Take foot-contact rows 1023 (frame 17) and about 1060 (frame 79) with these scales, in a level-camera ground model. The horizon comes out at about row 842. That model predicts a contact row of 1054 at frame 60; the observed row is 1053. So the depth growth is consistent.
- **The astronaut clearly approaches the camera.** C3/C4's constant-depth premise is false (reproduced).

### Rest height H in pixels at frame 24's depth (bbox height / scale)
- **Flight, frames 34-40** (legs spread, rear foot pointed toe-down, slight lean): 393-394 px with the chained scale, or about 399 px with the ECC scale.
  - The pointed toe overstates the rest height.
- **Upright walking, frames 74-79** (rear stance leg nearly straight, front knee bent, slight forward lean): 377-380 px.
  - Adding about 1-2 % for the lean and the stance-knee bend gives about 383-387 px.
- **Adopted:** H = 390 ± 8 px, so f = 390 x 18.147 / 2.2 ≈ 3217 px (hfov about 39°).
- Gravity check (`flight.py`): the hop parabola gives g ≈ 2.4 m/s² rather than the lunar 1.62. The animation is not ballistic, so this gives no usable focal length.

### Speed (`speed.py`): 3D back-projection
P = Z((u-cx)/f, (v-cy)/f, 1), with Z23 = Z24/s23.

| H (px) | s23 = 0.9942 (raw) | s23 = 0.9946 (unbiased) | s23 = 0.9950 |
|---|---|---|---|
| 388 | 5.26 | 5.17 | 5.08 |
| 394 | 5.20 | 5.10 | 5.02 |
| 400 | 5.14 | 5.04 | 4.96 |
| 405 | 5.09 | 5.00 | 4.91 |

All speeds are in m/s.
- At H = 390 and s23 = 0.9946 the speed is **about 5.14 m/s**.
- Components per frame: dx 0.170, dy -0.085, dz -0.098 m.
- Plausible range: 5.0-5.25.

## Rechecks
**a. Closure.**
- f comes from the prior itself, so closure is by construction.
- Independent bracketing at this f:
  - The upright walking frames (knees slightly bent) give a height of 379-383 px, which is 2.14-2.16 m.
  - The flight bbox with a pointed toe gives 394 px, which is 2.22 m.
- Rest height 2.2 m lies between the two. Closure is within about 2 %.

**b. Plausibility.**
- Walking phase, frames 70-79: about 7.5 px per frame lateral at Z ≈ 15.8 m, which is about 0.9 m/s lateral, or about 1 m/s with the depth part. That is a slow walk, plausible.
- Hop flight: lateral speed about 2 m/s.
- Push-off at frame 24: about 5 m/s (lateral 4.1, vertical 2.0, depth 2.35). That is high, but it is what the animation shows.

**c. Units and time base.** The answer is in m/s. Frame 24 = 1 s x 24 fps, and the file rate equals question_fps.

**d. Fault proof.**
- **C3 (4.12) and C4 (4.25).** They assume constant depth. My measured scale is 1.07 at frame 42 and 1.16 at frame 79, and the ground rows agree, so:
  - they omit dz ≈ 0.098 m per frame (about +10 % on the speed);
  - they use H = 418-420 px at frame 42 without dividing by 1.05-1.07 (about -5 %).
- **Round 1 (4.95).** Its method is right. It is about 4 % low because:
  - it uses H = 400 px from the frame-42 flight pose (pointed toe) divided by the lower ECC scale of 1.052;
  - upright walking frames bound the rest height at about 383-387 px;
  - its smoothed dz of 0.095 is slightly low.

  The difference is within tolerance. It is not a gross fault.
- **C1 (5.2) and C2 (5.15).** No fault found. C2's value equals my own.

## Decision
- **Verification of round 1:** the fault it claimed (C3/C4's constant depth, and the blend inheriting it) is real. My value of 5.14 agrees with round 1's 4.95 within 4 %, so the change stands.
- **Final answer:** I answer with my own measured value, which is C2's 5.15 (switch, following C2).
- **Confidence:** medium, about ±4 %. H is the main uncertainty.
