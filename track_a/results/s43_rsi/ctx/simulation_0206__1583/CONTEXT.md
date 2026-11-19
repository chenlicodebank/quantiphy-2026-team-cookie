# Context of question 1583 (organised record; every round adds to it)

## Question
- Text: What is the length of the letter placed under the gun in meters?
- Its own prior: acceleration of the typewriter before 0.45s = 9.8m/s^2
- Its own depth_info: t=0s, distance_typewriter_camera = 4.32m  
t=0.5s, distance_typewriter_camera = 4.501m  
distance_gun_camera = 4.704m  
distance_desktop_corner_far_right_camera = 5.009m  
distance_desktop_corner_closest_to_camera = 3.593m
- question_fps: 24
- Video: simulation_0206.mp4 (simulation, A3MC)

## The answer currently submitted
0.148 - the Claude line's answer 0.148, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.11 | 0.743 |
| C2 | Claude Opus 5.5 (Claude Code agent), 27_9 gravity-prior re-ask | 0.148 | 1.000 |
| C3 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_9b D3 adjudication batch 2 (DeepSeek+SAM 3 differs >25 pct) | 0.13 | 0.878 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.2 | 1.351 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.29 | 1.959 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 0.28 | 1.892 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 0.3 | 2.027 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 0.12 | 0.811 |

DeepSeek median over its 5 runs: 0.28.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v2; files in context/round1/)
- Answer: 0.139 (new, confidence medium, follows None)
- Where the answers part: camera pitch (desk-plane tilt) that sets the foreshortening of the slip's receding front-to-back side; secondarily the blurred acute tip position
- Fault proven: C2's 11.6 deg pitch (from treating the 5.009 m point as the front-right desk-top corner) contradicts the leg verticals (VPy y~11967), the receding-edge horizon (y -66..-113), slip rectangularity (84 deg) and gun height (+5.7 cm); measured pitch 13.3 deg gives 0.139
- Closure on the prior: 0.1 pct

# Round 1 addendum for Q1583 (letter under the gun, length)

Proposed answer: **0.139 m (new)**. Submitted was 0.148 (C2). Confidence: medium.

## Established, and by which measurement
- **The slip and its corners.** The slip lies under the revolver, aligned with the desk.
  - F = (1362.9, 643.2) and R = (1413, 634); R is the real corner (Lab b* falls to desk level at x 1412–1414).
  - L lies on the L–F edge line at x = 1316.5 ± 1.5. The line intersection gives 1315, integrated intensity gives 1316–1318, and the visible blurred tip is at 1320.
  - The length is the receding front-to-back side L–F; the width F–R is about 0.106 m.
- **Roll ≈ 0.** The vertical vanishing point from a sub-pixel fit of 12 desk-leg edges is (1046, 11967), with x ≈ cx.
- **Horizon from receding desk lines.** VP2 ≈ (−486, −113) from the inset left edge and outer right edge (rms ≈ 1 px), and (−423..−476, −66..−110) from the other pairs.
- **Focal length.**
  - VP orthogonality gives f ≈ 2690–2715 and pitch ≈ 13.3°.
  - The typewriter fall with g = 9.8 at 4.32 m gives f = 2700 (initial velocity free) or 2830 (from rest).
- **Desk-plane back-projection** (near corner 3.593 m): at f = 2710 / 13.3°, L–F = 0.139, F–R = 0.106 and the corner angle is 90.3°. The gun-depth plane gives the same value.
- **Closure.** At f = 2700–2710 the fall fit returns g = 9.79 (−0.1%) with the initial velocity free, or 10.2 (+4%) from rest.

## Ruled out
- **C2's pitch of 11.6°.** It reproduces 0.146, but predicts leg slopes 12% too shallow and a horizon at y = −29 (measured −66..−113). It also makes the slip 84° skewed and puts the gun origin 5.7 cm above the desk.
- **C1's 3.4° roll.** The verticals put the VP at x = cx.
- **DeepSeek runs.** They measured the wrong sheet (0.28–0.30) or used planar extents with no foreshortening (0.20).

## Open
- **Left-tip position.** Between 1315 and 1318 the length ranges from 0.144 to 0.135.
- **Focal length.** Between 2700 and 2830 the length ranges from 0.140 to 0.129. The fall fit depends on whether the release is from rest at t = 0.
- **The 5.009 m "far right corner" is not consistent with the desk-top surface.** At my geometry it is 2–4 cm below it, so it is probably not the top-surface corner.

### Round 3 (harness v3; files in context/round3/)
- Answer: 0.139 (new, confidence medium, follows None)
- Where the answers part: camera pitch (desk-plane tilt), which sets the foreshortening of the slip's receding L-F side; with the pitch tied to f by the measured vertical VP, what remains is f (2650-2840)
- Fault proven: C2 solved the pitch (11.6 deg) by putting the 5.009 m point at desk-top height; that implies VPy y~14020, which the LSD verticals reject (residual 0.39 vs 0.14 deg, measured VPy 11981); at C2's own f with the measured pitch its corners give 0.128-0.134, not 0.147
- Closure on the prior: -0.7 pct

# Round 2 addendum for Q1583 (letter under the gun, length)

Answer: **0.139 m (new; verifies round 1's proposal)**. Submitted before this round: 0.148 (C2). Confidence: medium.

## Verified this round (independent code)
- **Vertical VP.** LSD over 65 segments gives VPy = (1066, 11981), and (1064, 12058) from desk legs only. Roll ≈ 0. This agrees with round 1 (11967) and C3 (11966).
- **C2's fault is real.** Its geometry (f 2770, pitch 11.6°) implies VPy y ≈ 14020, and the verticals reject it (median residual 0.39° vs 0.14°).
  - I reproduce C2's 0.147 at that pitch.
  - With the measured pitch at C2's own f, its corners give 0.128.
- **Slip corners** (Lab L*, clean edge parts, rms ~0.1 px):
  - F = (1362.6, 643.1); L, the line intersection, = (1315.8, 624.4); R x ≈ 1413.5 (from b*).
  - Image edge directions: L–F 21.8°, F–R 170.7°, back edge 171.9°.
  - F–R points beyond x ≈ 1394 are in the gun's shadow and bend, so they must be excluded.
- **Length vs f** (pitch = atan(f/11441), desk plane through the near corner at 3.593 m, or the gun at 4.704 m minus 2 cm):

  | f | 2650 | 2700 | 2720 | 2750 | 2800 | 2840 |
  |---|---|---|---|---|---|---|
  | length (m) | 0.147 | 0.141 | 0.140 | 0.137 | 0.133 | 0.130 |

  The two planes agree to within 2%.
- **Typewriter key-template fall fit**, g = 9.8, |P0| = 4.32:
  - initial velocity free: f = 2690–2700, with the initial velocity at 0.081–0.090 m/s;
  - from rest: f = 2820–2840.
  - The fitted initial velocity equals 0.5·g/60 (a 60 Hz Bullet step), which favours the free-velocity fit.
  - If the keys are about 7 cm closer than the origin, f drops by about 2.5%.
- **Closure:** at f = 2720, g comes back at 9.74 (−0.7%); the variants range from −2.3% to +4.1%.

## Ruled out / not usable
- **Desk-rectangle and slip-rectangle orthogonality as f routes.** The angle peaks at about 89–90° over f 2700–3000 and never crosses 90°, so it is ill-conditioned. My LSD desk orthogonality's f ≈ 3000 is therefore not evidence.
- **The typewriter depth pair (4.32 → 4.501) as a test of f.** A tumble or slide of a few cm dominates it.

## Open
- **f between 2650 and 2840** gives 0.147–0.130. The routes are:
  - the free-velocity fall fit, about 2700;
  - round 1's horizon, 2690–2735;
  - a gun origin about 2 cm above the desk, which needs 2750–2850.
- **The 5.009 m point** gives f 2550–2620 if it is the top-surface front-right corner. Its identity is unresolved.
- **The left tip at 1315–1318** gives ±3.5%.
