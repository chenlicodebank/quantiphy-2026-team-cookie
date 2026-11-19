# q1294 — width of the lane (road curb to curb), simulation_0063

Answer: **12.7 m**. Confidence: moderate, roughly ±0.4 m (about 3 pct).

## Scene reading
- The file and question_fps are both 24. The camera is static.
- The main road (taxi, van and cyclist drive on it) is one straight road crossing the view and receding to the right.
  Both of its curb lines meet at the vanishing point (≈4900, 530) on the horizon.
  - Far curb: road edge at v≈625 at x=1800.
  - Near curb: the far edge of the right traffic island at v≈672 at x=1800. The same line continues as the edge of
    the man's sidewalk at v≈740 on the left.
- There is no lane marking, so "lane" means the road surface curb to curb, as the instructions say.
- The width is measured on the right part of the image (x 1460-2160, frame 0, no movers there).

## Camera model
- The camera is level. The horizon is at v0=532, from the man's feet-vs-height relation and from the vanishing point
  at 530. The principal point x is 1080.
- Ground points: Z = f·h/(v−v0), X = (u−cx)·h/(v−v0).
- **f·h = 4610 px·m.** Each source pairs a road contact row with the given distance (fh.py, taxi_fh.py):
  - taxi, frame 14: near tyre contacts (rear 295/736, front 580/728.5), centre 0.8 m across → 4604-4623.
  - cyclist, frame 38 → 4608.
  - man (sidewalk flush with road), frames 14 and 38 → 4598 and 4686.
  - van → 4440. It is an outlier, because its centre x is an estimate.
- **f ≈ 2200-2300 px**, from three checks:
  - Man height (h/1.16) = 1.81 m at f=2200.
  - Taxi wheelbase 2.87 m at f=2200 (a real Crown Victoria's is 2.91 m).
  - **Prior check:** the van's rear corner, tracked along a road-parallel image line (vanacc.py), gives 4.11 m/s² at
    f=2200 and 3.97 at f=2300. The prior is 4 m/s², which gives f≈2270, h≈2.03 m.
- Plausibility: the van's height ≈ h + 0.08 ≈ 2.1 m, which is realistic.

## Curb correction
- The curb is a raised stone about 0.09 m tall (curb.py). Its tan face at the sidewalk corner has a pixel height
  proportional to (v−v0), which means a vertical face, with c = 0.085-0.096 m. The island's visible curb face gives
  0.085-0.09 m.
- The near boundary seen at v≈672 is the curb's top far edge, so it is projected at height c=0.09.
- The far boundary is the bottom of the far curb face, at road level.
- Without this correction the width would be 11.75 m. The correction is the largest sensitivity in the answer.

## Result (width2.py)
- Both curb lines are fitted with sub-pixel half-max edges over 114 columns: rms 0.17 px for the far line and 0.59 px
  for the near line.
- The curb points are converted to ground coordinates, and the width is taken perpendicular to their common
  direction (≈30°).
- f=2200: 12.75 m. f=2300: 12.66 m. f·h ±30 changes the width by ±0.08 m. c=0.08-0.10 m gives 12.64-12.87 m.
- If the bright island-top edge is taken instead of the road→curb edge: 13.1 m.
- Final value: f≈2250, fh=4610, c=0.09 → **12.7 m**.

## Second-route checks
- The near curb line from the island extrapolates to the man's sidewalk edge on the left (v≈739 at x=300), which
  confirms it is one straight curb.
- The scale is confirmed independently by the prior (van acceleration 4.0-4.1 m/s²) and by the taxi wheelbase.
- Caveat: the man's origin moves less than his body between frames 14 and 38, so he was not used for the scale.
