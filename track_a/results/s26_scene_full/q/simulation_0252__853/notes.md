# Q853: speed of the soccer ball at t = 1.5 s

The clip is a 2D Blender render with a static camera, 24 fps. The file and question frame rates agree, so t = 1.5 s is
frame 36. The ball moves horizontally at a constant depth (its apparent size is constant), so one metres-per-pixel
scale comes from the prior: diameter = 0.344 m.

## Pixel speed at frame 36 (backward difference 35→36)
- From the scene track (left-limb ellipse fit, `cx`):
  - The raw step 35→36 is 46.0 px.
  - A quadratic fit over frames 25–40 gives a slope of 45.93 px/frame at 35.5.
  - A cubic fit over all frames gives 45.96.
  - The mean step over frames 31–40 is 45.88.
- My own limb measurement (`limbs.py`, |frame − background| > 10 on rows 380–390 and 395–405):
  - The edge midpoints give 45.8–45.9 px/frame.
  - The left limb alone gives 45.85–46.1.
- Texture cross-correlation (`measure.py`) gives 46.7 px/frame. The steps are very smooth and decelerate linearly.
  It reads about 1.5–2% high over the whole clip, consistently. I attribute that to the ball's surface rotation
  moving the star pattern relative to the origin, so I did not use it.
- Adopted value: 45.9 px/frame.

## Pixel diameter
The ball body is about the same brightness as the background, and a soft shadow sits above it, so edges are faint.
- `edgefit.py` fits circles to the top and bottom limbs, using the strongest vertical gradients per column:
  - frames 5–22: R ≈ 32.3–33.2 (D ≈ 65–66);
  - frames 23–40: R ≈ 31.2–32 (the shadow affects these);
  - median D = 64.4.
- A ball-centred stack of frames 6–40 (`stack.py`) puts the top edge near −33 and the bottom near +31 (D ≈ 64).
- A zoom of frame 16 by eye: top ≈ 350.7, bottom ≈ 414.5 (D ≈ 64).
- The scene record says 66 ± 1.5.
- The horizontal width (68–72) includes a little motion blur, so I did not use it.
- Adopted D = 65 ± 1.5 px, which gives a scale of 0.344 / 65 = 5.29e-3 m/px.

## Answer
v = 45.9 px/frame × 24 × 0.344 / 65 = 5.83 m/s. With D anywhere in 64–66, v = 5.75–5.92. Answer: **5.85 m/s**.

The check by a second route is above: two independent limb trackers agree on 45.9 px/frame. Confidence: about ±3%,
and the diameter is the main source of uncertainty.
