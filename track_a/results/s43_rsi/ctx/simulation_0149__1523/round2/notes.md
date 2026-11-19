# q1523 — acceleration of the yellow car at t = 0.5 s (m/s^2), round 2 verification

Answer: **10.4 m/s^2**. Decision: switch from the submitted 8.81 blend to C5 = 10.4, which confirms round 1's proposal.
My own value is 10.5 ± 0.15.

## Data
- Prior: tyre diameter 0.764 m. depth_info: frame 0, camera to the right-front tyre = 14.244 m.
- question_fps = file fps = 24. t = 0.5 s is frame 12.
- Convention: a = (s12 − 2 s11 + s10)·576 on a smooth fit of the path length s.
- The visible near-front wheel is the car's right-front wheel: the car faces the camera at frame 0 and heads to the
  camera's right.

## Crux
The answers part on the motion model and fit window used for the second difference:
- Local cubic or ease fit on a straight 3D line: 10.1–10.4.
- Long constant-acceleration fits, or noisy size rulers: 4.3–9.0.

## My measurements (own code, different route from round 1)
- `rim.py`: white-rim mask (low S, V above an adaptive threshold), largest component, ellipse fit. Overlays
  `frames/rim_0.png` and `frames/rim_12.png` were checked: the fit is tight.
  - Hub row v = 828.7–830.8 for frames 0–28. The hub stays on the horizon (829), so it moves in the camera's
    horizontal plane.
  - Rim height: 86 (f0), 99 (f12), 121 (f20) px. This agrees with round 1 (87.2 / 99.5 / 121.9).
- `traj.py`, route A (new): the heading comes from each frame's rim ellipse aspect ratio,
  sin α = (w/h)·cos φ, and uses no rim size.
  - The per-frame heading is constant at 37–38.5° (f = 2300) over frames 0–28, so there is **no yaw** and the path
    is a straight line. This confirms round 1's line by an independent cue.
  - Positions are the ray–line intersections from the frame-0 point, which comes from depth 14.244 m and u0. The
    geometry includes the camera pitch: the horizon at 829 against cy = 540 gives about 7°.
- Focal length:
  - `tyre.py`: tyre/rim ratio is 1.515 (median, frames 14–28). Closure on the prior then gives f ≈ 2262.
  - `ffit.py`: a joint fit of f and heading, in which the rim-size ratios must match the ray depths and the aspect
    headings must agree, gives f = 2264 ± 28 (hv) and 2316 ± 20 (hcol).
  - Round 1 / C2 found f = 2410 by vanishing points.
- a(12):
  - Cubic fits: 10.60 (f 2260), 10.52 (f 2300), 10.42 (f 2350), 10.32 (f 2410).
  - The window (0–24, 0–20, 4–20, 2–22, 0–28) or a quartic changes the result by ≤ 0.1.
  - Smoothstep (Blender Bezier ease), frames 0–28: i0 = 0.0, T ≈ 52–56 frames, rms 2 mm.
    a12 = 10.58 / 10.40 / 10.30 at f 2260 / 2350 / 2410.
  - v12 is about 6.6–6.8 m/s.
- Second route: rays on the TLS line of the size-based positions (round-1 style, my data) give 10.35–10.72.
  The pure size route (no rays) is far too noisy for a second difference (8–18).

## Rechecks
- a. Closure: at f = 2264–2316, the tyre diameter at frame 0 is ratio·rim·Zh0·cosθ/f'. This gives 0.741–0.778 m
  against the prior 0.764 m (−3 to +2 %; about 0 % at ratio 1.54 / hcol). At round 1's f = 2410 it would be −4 to
  −8 % with my tyre ratio, so I prefer the lower f. a differs by only 2 % between the two, which is 10.5 vs 10.3.
- b. Plausibility: v12 = 6.7 m/s, and the speed reaches about 10 m/s by frame 28 (36 km/h), a brisk launch from
  rest. Peak acceleration is about 17 m/s^2 at frame 0, then falls linearly (ease-in). These are animation values,
  but fine for a staged clip. Round 1 found the wheelbase at 3.1–3.3 m. There are no people or other standard
  objects.
- c. Units: m/s^2. Time base: frame 12 = 0.5·24, and the file fps equals question_fps (24).
- d. Fault proof (`quad.py`, f = 2300):
  - A quadratic over frames 10–28 gives a = 5.09. This reproduces C9/C10 (4.3, quadratic over 10–31) and the low
    DeepSeek runs C7/C8 (6.0 / 5.5, constant-acceleration models).
  - A quadratic over 0–28 gives 8.49, near C6 (9.0) and C4 (7.2).
  - A short quadratic window centred on 12 gives about 9.9. It estimates a(12), not the convention's backward
    second difference centred on frame 11. Under a linearly decaying acceleration, that one-frame offset is worth
    about 0.6 m/s^2.
  - The submitted 8.81 is a blend with the DeepSeek median (5.5), which comes from these faulty fits.

## Decision
- Round 1's proposed switch is verified. The fault reproduces (long constant-acceleration fits read 5.1–8.5 against
  10.5 on the local model).
- My value, 10.5 (range 10.3–10.6 over f 2260–2410), agrees with the proposed 10.4 within 1 %.
- I answer 10.4 (C5). It is within my measurement band.
