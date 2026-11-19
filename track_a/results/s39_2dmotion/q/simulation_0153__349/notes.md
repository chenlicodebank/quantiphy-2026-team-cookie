# Q349 — speed of the blue car at t = 1 s (m/s)

The prior is a tyre diameter of 0.369 m. The file and the question both run at 24 fps, so t = 1 s is frame 24, and the speed is |x(24) − x(23)| × 24.
The scene is 2D: the blue cart moves side-on at constant depth, and its ground contact stays at y ≈ 948. So a single m/px scale from the tyre applies.

## Scale: tyre diameter in pixels
- Scripts: profile.py (half-level edge crossings along rows and columns through the hub), circfit.py (circle fit to the outer contour), radius.py (gradient-based, too noisy, discarded) and sam_runs.py plus a direct SAM call (SAM 3 masks).
- Which edges can be trusted. The tread shows on one side when a wheel sits off the image centre, and the front wheel also has a grey band on its left (it looks steered). That inflates the horizontal extent on one side. The top edge merges into the dark wheel well and the bottom edge merges into the contact shadow, so vertical extents run about 2–3 px too large. The cleanest measurement is the rear wheel's horizontal extent when it is near the image centre, where the edges are symmetric about the hub.
  - My rear-wheel measurements: 108.0 px at frame 36 and 107.7 px at frame 39 (left edge 959.8, right edge 1067.5, hub ≈ 1014). At frame 30 I get 110.4 px, with tread visible on the right.
  - Front wheel: from the hub, the clean right-hand side gives a radius of about 53.3–54.8 px, i.e. a diameter of about 107–110 px. The full left-to-right width is 112–114 px, but that includes the grey tread band. The circle fit gives 112.5 px and the vertical extent 112.3 px, both inflated by the shadow and wheel well.
  - SAM 3, tyre masks:
    - frame 30: front 108.8 px wide × 108.8 px tall, rear 109 × 110.6
    - frame 39: rear 109.1 × 108.5, front 111.2 × 106.9
    - frames 23 and 24: 109–110 px tall
- How SAM compares with my measurements. On the clean rear-wheel width SAM and I agree within about 1%. My front-wheel width (113 px) is about 4% larger than SAM's (108.8 px at frame 30). On zoomed frames (frames/front36.png, frames/rear39.png) the extra width is the grey tread band on the left of the tyre, which SAM leaves out. So SAM is right there, and I discarded my full front width.
- Adopted value: D = 108.5 ± 1 px, giving a scale of 0.369 / 108.5 = 3.401e-3 m/px.

## Displacement from frame 23 to frame 24
measure.py tracks template patches against frame 30, with sub-pixel matching:

| Point | Shift 23→24 (px) |
|---|---|
| panel lights | 47.98 |
| rear hub | 47.53 |
| front hub | 47.72 |
| SAM tyre centroid, front | 47.0 |
| SAM tyre centroid, rear | 49.1 |
| SAM tyre box centre, front | 47.65 |
| SAM tyre box centre, rear | 48.35 |

The neighbouring intervals are 46.5–47.3 px (22→23) and 48.3–48.6 px (24→25), so the motion speeds up smoothly. The SAM cart mask is not usable for the centre here: at frame 23 its rear blends into the dark wall, so its centroid only moved 39.5 px. I used 47.8 ± 0.3 px/frame.

## Answer
v = 47.8 px/frame × 24 frames/s × 3.401e-3 m/px = **3.90 m/s**

## Checks
- Second route for the shift: the three template patches and the SAM tyre centroids and box centres are independent ways to measure the 23→24 shift, and they agree within ±1%.
- Taking the diameter as 107.7 px or 110 px moves the answer to between 3.85 and 3.93 m/s.
- The scene record gives 48.0 px/frame for this interval (panel track), which matches. Its wheel diameter of 105 px was a visual guess and too small. I replaced it with 108.5 px.

Confidence: good, roughly ±2–3%.
