# Round 2 addendum (Q1365, yellow-taxi average speed)

## Verified (independent code, round 2)
- **Focal length: f = 1782.**
  - Measured from Hough-fitted kerb and sidewalk lines on a median background, 8 + 7 lines.
  - vA = (-1294,-258), vB = (2686,-259). Leave-one-out gives 1779-1783.
  - This agrees with round 1's 1783-1794.
- **Ground-parallel plane model is consistent with the depths.** The sign-plane offset solved at frame 14 and at
  frame 38 agrees to 0.01 m (7.951 / 7.943).
- **Taxi speed from the roof-sign track on the plane:**
  - Mean per-frame speed is 4.12-4.18 raw and 4.02-4.07 smoothed. The lower value of each pair includes the
    duplicated frame-0 zero step.
  - f 1775-1800 and δ 0-1.5 give 4.06-4.22. The per-frame speed stays flat at about 4.1-4.2.
- **Independent chord check:** the given depths alone, placed on the frame-14 and frame-38 rays, give a 3D chord of
  4.099 m over 1 s. The plane model gives 4.094.
- **Fault reproduced:** linear-in-time depth extrapolation gives 3.50 at f 1782, 3.38 at f 1850 and 3.25 at f 1930.
  This matches C4 and C5, so B = 3.3 in the blend is faulty.
- **Closure:**
  - Van wheelbase from tyre contacts at frame 66 is 3.86-3.94 m (H 9.5-9.7 m), which fits an extended Express.
  - Scaled by length/wheelbase, that gives about 6.0-6.2 m against 6 m, about +2-3 %.
- **Plausibility:** taxi length along its heading is 5.43-5.47 m (Crown Victoria 5.39 m).

## Decision
4.1 (switch from the blend 3.696, following C2). Round 1's proposal is verified.

## Ruled out
- The KLT body-feature median-flow track drifts 91 px over the clip and is not usable.
- The van's bottom-contour length is contaminated by its shadow.

## Open
- Whether the reference counts the duplicated frame-0 zero step: about 1.5 %.
- Raw versus smoothed track: about 2 %.
- The full range is 4.02-4.18, all within 2.5 % of 4.1.
