# q_1946 — speed of the red general chess piece at t = 1 s

- The moving "block" in scene/ is the Chinese chess piece (a disc lying flat, sliding down the ramp trough; seen
  obliquely, so it looks like a rounded bar). It is the asked object and the prior's object.
- Time base: fps = question_fps = 24, so t = 1 s -> frame 24. A uniform acceleration of 1.00 px/frame^2 along a
  straight path is physically plausible for sliding down a slope, so I kept 24 fps.
- Scale (2D, planar): diameter 0.097 m <-> extent of the piece along the ramp direction. My own masks (difference
  to a frame where the piece is elsewhere, `mask_diam.py`) give 77-82 px depending on threshold (82.0 at the
  loose threshold that includes the shaded edge, ~79 at a medium one); scene record PCA length 81.3 px (median).
  Used 81 px -> 1.198e-3 m/px.
- Motion (`speed.py`): the scene track (template-matched centre, ±1 px) has repeated frames (6, 13, 25, 28, 35, 38)
  and double steps (5, 10, 23, 27, 34, 37). Mapping file frames to true render indices makes the per-frame step
  grow linearly; a quadratic fit of the path coordinate vs render index (rms 0.4 px) gives a = 1.00 px/frame^2.
  - backward-difference speed at render frame 24: 23.3 px/frame -> 0.670 m/s
  - at file frame 24 (= render 25): 24.3 px/frame -> 0.700 m/s
  - Second route, raw local steps: render 22->24 mean 23.1 px/frame (0.665 m/s); render 24->25 24.7 px (0.710 m/s).
    The raw backward difference at file frame 24 (s24 - s23) is 24.7 px because frame 23 was already shifted forward
    (frame 25 is the repeat), so the raw value is about right here.
- Answer: midpoint of the two index conventions, 0.685 m/s (both within ~2.2 %).
- Confidence: moderate-high. Scale ±2-3 % (edge definition of the piece), index convention ±2 %.
