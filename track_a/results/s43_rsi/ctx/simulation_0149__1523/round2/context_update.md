# Round 2 addendum, q1523 (car acceleration at t = 0.5 s, frame 12)

## Verified (independent route)
- Round 1's switch to 10.4 is verified. My own value is 10.5 ± 0.15 m/s^2, so the answer is 10.4 (C5).
- **No yaw.** The heading comes from the near-front rim ellipse aspect ratio, corrected for azimuth (`traj.py`), and
  uses no size cue. It stays at 37–38.5° from the camera-ward axis in every frame 0–28. The path is a straight line
  in the hub-height horizontal plane, with the hub row at 829–831 = horizon.
- Positions come from the ray–line intersection anchored at the frame-0 point, which is set by 14.244 m and u0. The
  camera pitch (about 7°) is included.
- **Focal length.**
  - A joint fit (rim-size ratios against ray depths, plus aspect headings) gives f = 2264–2316 (±25).
  - The tyre/rim ratio of 1.515 with the prior gives about 2262.
  - The vanishing-point route (round 1 / C2) gives 2410.
- **a(12)** by the convention (s12 − 2 s11 + s10)·576:
  - Cubic: 10.60 / 10.52 / 10.32 at f = 2260 / 2300 / 2410.
  - Smoothstep: 10.58 / 10.30, with ease start i0 = 0.0, T ≈ 52–56 frames, rms 2 mm.
  - Windows and degree change the result by ≤ 0.1.
- **Closure:** the tyre comes out at 0.741–0.778 m against 0.764 at f ≈ 2290. At f = 2410 with my tyre ratio it is
  −4 to −8 %.

## Ruled out (reproduced)
- Quadratic fits: frames 10–28 give 5.1, which matches C9/C10 at 4.3. Frames 0–28 give 8.5, which matches C6 and C4.
- The 8.81 blend.

## Open
- The only point left open is the centring of the convention. The short-window instantaneous a(12) is about 9.9,
  while the backward second difference centred at frame 11 is about 10.5. The task's stated convention was followed.
- f is 2290 vs 2410, which is worth about 2 % in a.
