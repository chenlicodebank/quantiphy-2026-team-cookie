# q_144 – body length of the big bird (eagle)

2D simulation, static camera, both birds flying horizontally at the same image row (y ≈ 600), so one metres-per-pixel scale is used.
fps = question_fps = 24.

## Scale from the prior (small bird = crow, speed 11 m/s)
- Re-segmented with my own script (`measure.py`: |frame − median(frames 24–29)| > 20, 5x5 close, connected components).
- Crow x0: 1507 (f3) → 72 (f18) = 1435 px / 15 frames = 95.67 px/frame; x1 and bbox centre give the same 95.67 px/frame.
  Motion is uniform (per-frame steps 94–96 px).
- 95.67 px/frame × 24 = 2296 px/s → scale = 11 / 2296 = 0.004791 m/px.

## Eagle length
- Horizontal bbox extent (beak to tail, the flight axis) = 181–182 px in every unclipped frame 2–10 (my segmentation agrees with scene/ record). Mean 181.5 px.
- Checked on zoomed frame 3: the mask spans the pale head through the tail/feet; the wings do not extend past it horizontally.
- Length = 181.5 × 0.004791 = 0.870 m.

## Check
- Second route: the crow's speed from the bbox centre (1562.5→127.5 over 15 frames) and from its trailing edge x1 (1618→183) both give 95.67 px/frame, the same as from x0. Frame-to-frame spread of eagle width (181–182 px) is ±0.3%.
- Sanity: 0.87 m is a plausible bald-eagle body length; crow 112 px → 0.54 m (slightly large but consistent scale).

Confidence: high (≈ ±2%).
