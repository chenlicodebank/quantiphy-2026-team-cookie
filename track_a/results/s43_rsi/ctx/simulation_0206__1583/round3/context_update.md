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
