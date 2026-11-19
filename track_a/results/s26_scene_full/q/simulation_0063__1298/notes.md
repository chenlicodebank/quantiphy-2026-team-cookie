# q1298 — height of the turning yellow car (taxi), metres

Answer: **1.69 m** (vertical world extent of the taxi = tyre contact to top of the roof "TAXI" sign).
question_fps = file fps = 24, so the frame numbers below are t × 24 (t=0.58 → f14, t=1.58 → f38).

## Focal length (the main scale driver)
- Left street: a row of identical lamp posts recedes to a vanishing point. Measured in code from pole tops and bases at f70
  (`lamps*.py`): poles at x 162/85/42 (15). Tops 460/480/492 and bases ~642/608/588 give VP ≈ (-92, 528). If the far 4th
  lamp is included, VP ≈ -72.
- Crossing road: the far road edge and sidewalk/sky edge on the right (`curbs.py`) vanish at u ≈ 4835 / 4740. The white
  van's path, fitted as straight-line constant-acceleration ground motion (`van_fit.py`), has VP u ≈ 4793. That VP does not
  depend on f. I used u ≈ 4790.
- The two streets are perpendicular, so f² = (4790-1080)(1080-u_left), which gives f ≈ 2067–2085 px (HFOV ≈ 55°).
- Checks with the van only: the van's depths at f14/f38 are consistent (|P14|/|P38| ratio matches) at f ≈ 2000–2100.
  The prior (van acceleration 4 m/s²) gives a = 4.04 at f = 2000 and 3.93 at f = 2085. The van started from rest
  (fitted v0 ≈ 0). This agrees within about 2–4 %.

## Camera height and taxi height
- Horizon at row 528–532: the lamp VP is at 528, and the scene record's man feet/height fit gives 532.3. The result barely
  depends on which (see `height.py`).
- Tyre contacts measured in code (`wheels.py`, `tyres.py`): at f14 the rear near wheel is at 737 and the front near wheel
  ≈ 730.5 (interpolated between f7 = 728 and f18 = 732; the front wheel is hidden by the bin at f14). At f38 the rear near
  wheel is at 738 and the front near wheel at 755.
- Taxi depth Z_c = d × f / sqrt(f² + du² + dv²), with d = 24.84 (f14) and 22.95 (f38).
- Near-side tyre outer edge assumed at half-width b = 0.92 m (±0.1 m changes H by about ±0.01 m).
- Camera height above the road, h_c: 2.22 from f14 (both wheels) and 2.27 from f38 (both wheels, solving the yaw).
  Independent checks: the cyclist's wheels plus its depth at f38 give 2.22, and the man gives 2.21 (on the sidewalk).
- Roof-sign top at f38, from a paint-colour mask (`sign.py`): row 581.5. The sign is hidden behind the man's head at f14.
- H = h_c + (vh − 581.5) × Z_c38 / f:
  - f14 wheel route: 1.66–1.67
  - f38 wheel route: 1.71–1.72
  - f14 rear wheel only (ignores yaw, biased high): 1.70
  - Mean ≈ 1.69. For f = 2000 it would be about 1.75.

## Notes
- If "height" were meant without the roof sign it would be smaller (about 1.45–1.5). The question asks for the car's
  bounding-box height, so I included the sign.
- The van-based h_c (2.03–2.10) is lower than the others. It depends on assumed van length, width and wheel geometry,
  so I did not use it for h_c.
- Confidence: medium-high, about ±4 %.
