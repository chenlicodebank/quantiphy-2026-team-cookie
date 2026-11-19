# Q1194: height of the moving bicycle (handlebar top to ground), in metres. Answer: 1.00 m

The file and the question both run at 33 fps, so t = 1 s is frame 33 and t = 2 s is frame 66.

## Task this round
Round 1 proposed switching from 1.49 (C1) to 1.00 (C2's method family). Its fault proof was that f ≈ 1185 (from the walker's given depth) contradicts the horizon set by the level building lines. I re-measured that fault with my own code.

**Crux:** the focal length and which given depth to trust. C1 and C3 used f ≈ 1185 from the walker's depth and then applied the bike's 16.49 m, giving 1.49–1.6. C2, C4–C6 and round 1 used f ≈ 1870–1980 from vanishing points or the walker's ground plane, giving 0.96–1.06.

## Measurements (my own code)
**`vp.py`: LSD segments on frame 0, RANSAC, then a weighted least-squares fit.**
- Vertical VP: (958, 8023) from 65 segments (kiosk edges, building columns, wall planks).
- Street VP: (1793, −76.5) from 14 cornice/siding segments on the stoop building (x 1100–1500, y < 300). Bootstrap y (16/50/84 %): −80 / −77 / −73. The overlay is `frames/vp_lines.png`.
- From orthogonality, **f = 1874 px** with a pitch of 13.8°. Round 1 found VP y = −82 and f = 1887–1958, so the two agree.
- f = 1185 would need the horizon at y ≈ 213, inside the building's level lines, which all rise to the right. So it is ruled out.

**`geom.py`: ground-plane model from the walker.**
- Camera height above the sidewalk from the 1.8 m walker over 86 unoccluded frames: 4.61 m (sd 0.024).
- The road is 0.10 m lower (curb; I varied this from 0 to 0.15).
- Bike pixels (contact / grip top): f0 416.5/312, f20 492.5/374.5, f33 559.5/424, f56 727/552, f60 761/579. All sessions agree on these.
- H at f = 1874, for grip set-back r behind the front contact (frames 0, 20, 33, 56, 60):

  | r | H per frame |
  |---|---|
  | 0 | 1.05, 1.03, 1.07, 1.11, 1.11 |
  | 0.15 | 1.02, 1.00, 1.03, 1.07, 1.06 |
  | 0.3 | 0.99, 0.97, 1.00, 1.02, 1.02 (mean 1.00) |
  | 0.4 | 0.97, 0.95, 0.97, 0.99, 0.98 |

  - Swapping f for 1950 changes H by under 0.3 %, so this route barely depends on f.
  - The curb (0 to 0.15 m) moves H by ±2 %.
  - Bike geometry: the steering axis at about 70° puts the stem about 0.3 m behind the contact, and swept-back grips add more. So r ≈ 0.3–0.45 and **H ≈ 0.97–1.00**.

**Route B: the bike's own given depth (`plaus.py`).**
- The model puts the bike origin (mid-wheelbase, about 0.55 m behind the contact) at 15.9–16.0 m, against 16.49 m given. That is 3 % at f = 1874 and about 0 % at f = 1950.
- Scaling by the bike depth instead of the walker raises H by 0–3 %, to about 1.00–1.03.

**Human-size cross-check (new route, independent of f):**
- At f33 the rider's head is about 20 px wide and the walker's about 17 px.
- At the given depths (16.49 vs 11.93 m, with the bike's larger off-axis angle on top), the rider's head would be about 1.6× the walker's real size, which is impossible.
- In the vanishing-point camera the walker's body is at 17.4 m, so the sizes are consistent.

## Rechecks
- **a. Closure.**
  - Route A uses the walker's 1.8 m for its scale.
  - Independently, the bike's given depth predicts the walker at 1.8 × 16.49/15.98 = 1.86 m, so **closure is 3 %** (0 % at f = 1950).
  - The walker's own given depth (11.93 m) is not reproduced (the body is at 17.4 m): the character's origin is offset from its body.
- **b. Plausibility.**
  - The handlebar at 1.0 m is a normal city bike.
  - The rider's head is 1.65–1.69 m above the road, which fits a seated adult.
  - The bike moves at 4.66 m/s and the walker at 1.24 m/s.
  - In C1's world the bike would be 1.5 m, the rider's head about 2.6 m and the road 2.7 m below the sidewalk.
- **c. Units and time base.** The answer is in metres. Frame = round(t × 33), and question_fps equals the file rate.
- **d. Fault proof.**
  - **C1 (1.49) and C3 (1.6):** f ≈ 1185 from the walker's offset origin. My facade-line horizon is at y = −77 (f = 1874), against the y ≈ 213 that f = 1185 needs. The head-size ratio also contradicts their geometry.
  - **C6 (1.06):** r = 0, with the grips directly over the contact. That inflates H by about 6 %.
  - **C2 (0.97) and C4/C5 (0.96):** no fault found; they are within 3–4 %.

## Decision
I verified round 1's switch: I reproduced the fault, and my value (1.00, range 0.97–1.03) agrees with round 1's 1.00. **Answer: 1.00 m.**
