# q737 – width of the orange chair next to the blackboard (simulation_0231), round 2

Prior: black cat speed 0.714 m/s. No depth_info. File fps 24 = question_fps 24, so no re-timing is needed.

## Task this round
Round 1 proposed switching from C2's 0.455 to 0.476 (C1-type geometry). Its fault proof rests on one claim: the
teacher's desk is not flush with the wall, because its front leg reaches lower in the image than a flush desk allows.
I verified that claim with my own code and closed its main open point (the hidden floor contact of the desk leg) by a
route round 1 did not use: an upper bound from the desk's back leg.

**Crux:** how deep the cat (on the desk top) sits relative to the chair, i.e. where the desk is in depth. Either its
rear edge is flush with the wall (C2), or it is placed from its leg floor contact (C1, round 1).

## Geometry
- The camera is level: horizon at y = 540, wall–floor line at y = 951.5 (taken from the earlier record; the
  ceiling vanishing point was measured by both C1 and C2).
- For a point on the floor at row y, depth Z = 411.5/(y−540) in units of the wall depth Z_w.
- Width W = backrest px × s_cat × Z_backrest / Z_cat.

## Measurements (my scripts)
- **Cat speed** (`cat_check.py`, scene track): linear slopes of 8.913 / 8.998 / 8.987 / 8.904 px/frame
  (torso_cx / cx_dark / cx_mask / nose). I used 8.93 px/frame, so s_cat = 0.714/(8.93×24) = 0.003332 m/px.
- **Cat paw contact** (`paws.py`, frames/paws2.png): the planted white paws end at y 740–742. I took the midline at
  740 ± 1.
- **Desk top** (`desktop_rows.py`): the rear edge is at y 733 (end of the board frame) and the top surface's front
  edge at 762 (rounded highlight; the front face below it runs 763–766). Ratio = 222/193 = 1.150.
- **Desk legs** (`desk_geom.py`; half-level edges over rows 790–860):
  - front-right leg x 752.6–767.2 (centre 759.9);
  - back-right leg x 778.8–790.3 (centre 784.5);
  - depth ratio from the centres (960−759.9)/(960−784.5) = 1.140 (outer edges 1.136, inner edges 1.144). Round 1 had
    1.130.
  - So the legs are inset only 0.5% of their depth.
- **Desk front leg floor contact** (`leg_check.py`, `backleg.py`; frames/leg_enh.png, frames/mid.png):
  - Below the foreground chair back, the front leg is crisp and dark (grey 28 against floor 65) down to y 1026–1027,
    where the foreground chair's seat edge hides it. So the contact is at **≥ 1027**.
  - NEW upper bound: below the foreground chair back's lower edge (y 977.5), the back-right desk leg does **not**
    show as a crisp bar (expected grey ≈ 25). There is only a soft smear (55 against 70) that fades by about 1005.
    It looks like the blurred floor reflection seen under the orange chair's leg contact (frames/smear.png vs
    frames/chair_contact.png).
  - So the back leg meets the floor at ≤ 978, which puts the front leg at ≤ 540 + 438×1.140 = **1039**.
  - The front contact therefore lies in [1027, 1039]. The reflection is strongest just below 978, which favours
    the lower half of that range. I used 1033 ± 6.
- **Chair** (`final_calc.py`, `chair_legs2.py`; frames/chair_overlay.png):
  - Backrest, half-saturation mask over rows 750–795: x 1603.1–1751.9 = **148.8 px**. Round 1 had 149.4; C2 150.5.
  - Front-left leg contrast drops at 1027–1028. The right legs' x-ratio is 832/792 = 1.0505, so the back legs meet
    the floor at 1004. This matches the back-right leg's crisp end on the enhanced crop (≈1003; below that only the
    reflection shows).
  - Z_back = 0.887 Z_w and the backrest 0.889 Z_w. The front-right leg's outer edge gives the same right-hand
    extreme to within 0.1% (round 1).

## Result
- Z_cat = Z_tf × 222/200. Z_tf follows from the front leg contact and the 0.5% inset.
- **W = 0.4784 m** at a contact row of 1033. Over the bounded range 1027 → 1039 the result runs 0.4725 → 0.4842.
- Other sensitivities, each about ±0.5%:
  - paw row 739 / 741 → 0.476 / 0.481;
  - leg ratio 1.13 / 1.15 → 0.481 / 0.476;
  - cat speed 8.90 / 9.00 → 0.480 / 0.475;
  - chair back row 1002 / 1006 → 0.480 / 0.476;
  - no backrest lean → 0.477.
- Second route, the flush-desk model with the same edges: 0.457. That model is ruled out (see 4d).
- **Answer: 0.478 m.**

## Rechecks
- **a. Closure.** The prior is the only metric input; the measured 214.3 px/s returns 0.714 m/s (0%, by
  construction). Non-trivial consistency checks:
  - chair right-leg x-ratio 1.0505 vs floor-row ratio 487.5/464 = 1.0506;
  - desk top corner x-ratio 1.147 (round 1) vs row ratio 1.150.
- **b. Plausibility** (s_wall = 0.00361 m/px): camera height 1.49 m, teacher's desk height 0.82 m, chair height
  0.86 m, chair width 0.478 m (classroom chairs are 0.40–0.50 m), cat torso 146 px × 0.00333 = 0.49 m. All are
  realistic.
- **c. Units and time base.** Answer in metres. No time stamps are involved; the cat speed uses frame steps at
  24 fps = question_fps.
- **d. Fault proof.**
  - **C2 (0.455, submitted)** assumed the desk's rear edge touches the wall. That makes the top's front edge
    Z_w/1.150 = 0.870 Z_w, so a leg under it would meet the floor at y ≤ 540 + 411.5×1.150 = 1013. But the desk's
    front leg is visible, crisp, down to 1026–1027 (my profile: grey 28 against 65 at rows 1000–1026, x 753–766). The
    leg would stand in front of the desk top, which is impossible.
    - With the measured contact range, the desk's rear edge lies at 0.944–0.967 Z_w, not at the wall.
    - C2's model with my edges gives 0.457, matching its 0.455. The model is the fault, not C2's pixels.
    - I reproduced round 1's fault proof.
  - **C3/C5 (0.67)**: one 2D scale applied to the full 199 px extent. That includes the front-to-back perspective
    spread and ignores the depth difference between chair and cat (round 1; not re-litigated). 0.67 m is
    implausible for this chair.
  - **C4 (0.50)**: a blend of readings without depth correction.
  - **C1 (0.485)**: the same method; within 1.5% of my value.
  - **Round 1 (0.476)**: the same method. It took the leg contact at 1029.5, which is really only the occluder
    edge, a lower bound. My bounded central value of 1033 moves the answer +0.5%.

## Decision
Switch to the C1 / round-1 geometry with my own value of 0.478 m. Round 1's proposed 0.476 is verified: the fault
is reproduced, and my value agrees with it within 0.5%. Confidence: high. The answer is bounded to
0.472–0.484 by the desk-leg contact limits.
