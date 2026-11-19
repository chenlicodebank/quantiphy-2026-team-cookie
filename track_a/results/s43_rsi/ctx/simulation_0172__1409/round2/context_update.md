# Round 2 addendum, Q1409 (astronaut speed at t = 1 s)

**Answer: 5.15 m/s** (switch, following C2). Confidence medium, about ±4 %.

## Round 1 verification
- **Its fault claim holds.** SIFT + RANSAC similarity tracking of the upper body (a route independent of round 1's ECC) gives a scale relative to frame 24 of:

  | Frame | Scale |
  |---|---|
  | 0 | 0.925 |
  | 17 | 0.96 |
  | 42 | 1.07 |
  | 60 | 1.13-1.14 |
  | 79 | 1.16 |

  - Foot-contact rows check this. Rows 1023 at frame 17 and 1060 at frame 79 put the horizon at about row 842, and that predicts a row of 1054 at frame 60; the observed row is 1053.
  - So C3/C4's constant-depth premise is false.
- **Round 1's value (4.95) is about 4 % low, but within tolerance.**

## Established
- **Pelvis image step, frames 23 to 24:** (+29.7, -14.3) px = 32.9 px (round 1: 33.3).
- **Depth step:** s24/s23 = 1.0054 from templates at frames 21 and 27, so dZ ≈ 0.098 m per frame.
  - With the template at frame 23 or 24 the result is biased: about 1.0058-1.0065 backward, with the forward step correspondingly low.
- **Rest height at frame 24's depth:**
  - Upright walking frames 74-79: bbox / scale = 377-380 px, about 383-387 px after correcting for lean and knee bend.
  - Flight frames 34-40 with a pointed toe: 393-394 px (chained scale) or about 399 px (ECC scale). This overstates the rest height.
  - Adopted H = 390 ± 8 px, so f ≈ 3217 px.
- **Speed:** at H = 390 it is 5.14 m/s, with per-frame components dx 0.170, dy -0.085, dz -0.098 m.
  - Over H 388-400 and the scale choices, the range is 5.0-5.25.

## Ruled out
- **C3/C4 (4.12 / 4.25):** they assume constant depth.
- **Submitted blend 4.665:** it inherits that bias.
- **Hop gravity as a focal-length route:** the parabola gives about 2.4 m/s² rather than the lunar 1.62, so the animation is not ballistic.

## Open
- **Rest pixel height, ±2 %:** a skeleton or segment-length fit would settle it.
- **The frame 42 scale:** chained/direct SIFT gives 1.068-1.072 and ECC gives 1.052. This affects only the flight-pose height route.
