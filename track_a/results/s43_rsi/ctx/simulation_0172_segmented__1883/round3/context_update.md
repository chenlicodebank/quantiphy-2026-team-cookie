# Round 3 addendum: Q1883 (answer 0.40, switch to C6, verified round 2; confidence medium)

## Established
- Round 2's fault proof was reproduced with a different tracker: dense DIS and Farneback flow, not chained ECC
  (`c1check.py`).
  - C1's landmark x drifts 9.5 px against the rigid backpack track over f0-14.
  - C1's own fits (quadratic, windows 2/4/6-14) on its landmarks give exactly -0.24/-0.26/-0.06.
  - The same fits give -0.31 to -0.36 on the backpack flow and -0.41 to -0.47 on the waist-band flow.
- The derivative depends on the body part tracked, because the torso turns about 0.7 deg/frame in the image:
  - head: -0.10 to -0.26
  - upper body / backpack: median -0.28
  - waist band at pelvis level: median -0.43, range -0.25 to -0.51 over quadratic/cubic/speed-series fits in
    f0-14
  - all-track median: -0.36
  Value for the pelvis origin: about 0.42.
- Scale confirmed:
  - The rigid helmet-top to backpack-bottom size is 176.8 px at f12 and 180.4 at f24, so Z12 = 18.5 m and
    m/px = 0.0059 (f = 3134).
  - Speed at f12 is 1.45-1.65 m/s.
- The flow-divergence vertical scale grows 0.5-0.9 %/frame in both segments. bbox_h and the backpack height are flat,
  so this is an estimator bias, not approach. Size-scale depth trends (C12, C9) are rejected again.

## Ruled out
- C1 (0.25): landmark drift (reproduced twice now, ECC and flow).
- C3, C4, C11: fits cross the f14→15 step.
- C9, C12: biased depth trends.

## Open
- Which body point the true origin follows: the upper body gives about 0.28, the waist about 0.43. The answer 0.40
  assumes the waist and pelvis.
- Gait oscillation of the true pelvis, and camera motion, cannot be checked on the white background.
