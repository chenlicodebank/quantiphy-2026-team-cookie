# q_341: speed of the rocket at t = 1 s (m/s)

Prior: rocket length = 2.9 m. 2D render with a static camera. The file fps and question_fps are both 24, so t = 1 s is
frame 24. Speed = |p24 - p23| x 24.

## Method (own scripts)
- `measure.py`: takes |frame - frame0| and fits the flight axis through the centroids of frames 14-21.
  - The axis is 39.08 deg above horizontal, heading up-left. Perpendicular residuals are under 0.25 px, so the path
    is straight.
  - The along-axis profile (band ±13 px) gives 50%-of-plateau crossings for the tail and the nose.
  - Motion blur is a symmetric smear, so the 50% points sit at the true ends.
- Rocket length at 50%: median **201.0 px** over frames 13-22 (range 197-208). The scene record gives 201.8.
  - The tapered nose may put the 50% point slightly behind the tip, so I used L = 202 px.
  - Scale = 2.9 / 202 = 0.01436 m/px.
- At frames 23-24 the nose is outside the image. The rocket is rigid and its path is straight, so the centre
  displacement equals the tail displacement.

## Frame 23 → 24 advance, by route
| Route | Advance |
|---|---|
| Tail 50% crossing (0.5 px bins, `xcorr.py`) | 61.4 px |
| Tail 25% crossing | 62.0 px |
| Tail 75% crossing | 64.2 px |
| Tail-window cross-correlation | 62.0 px |
| Smooth fits of the centre track (`fit.py`), as p(24) - p(23) | 61.1-64.0 px |
| Scene record's s_axis | 61.9 px |

- Chosen advance: **62.0 px/frame**.
- Speed = 62.0 x 24 x 2.9 / 202 = **21.4 m/s**.
- The spread of the routes (61-64 px) is about ±3%.

## SAM 3 check
- **Frame 18:** the SAM mask length is 244.6 px, against my 201 px.
  - The difference is motion blur. The rocket advances about 52 px per frame and the shutter is open about 0.75 of
    the frame, which adds about 39 px of blur. The raw d>30 mask is likewise 226-240 px long.
  - SAM's extents include the blur, so I kept the 50% length.
- **Frame 13 (box prompt):** the SAM tail is at s = -320.8 against mine at -317.8, which agrees.
- **Frames 22→23:** the SAM tail advances 61.2 px against my 61.1 px, which agrees.
- **Frame 24 (box prompt):** the SAM tail gives an advance of only 42.6 px.
  - The zoomed overlay (`frames/f24_tail_check.png`) shows the SAM mask includes a spurious blob of sky below and
    behind the tail.
  - SAM is therefore wrong at frame 24, and my 50% tail point sits correctly on the blurred tail.

## Size reading
- I read the prior as the rocket's axial length (202 px).
- A world axis-aligned horizontal extent of the tilted rocket would be about 168 px, which gives 25.7 m/s.
- I rejected that reading because the 202 px scale gives realistic truck sizes: about 9.6 m long and about 3.3 m to
  the cab roof.

Confidence: good. Expect about 3-5% error, mostly from the length in pixels and from the per-frame noise in the
advance.
