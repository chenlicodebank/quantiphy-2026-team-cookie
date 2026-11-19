# simulation_0194 — measurement record

2D simulation (Blender render), 1920x1080, 30 fps, 100 frames (t = frame/30, 0 to 3.300 s).
The scene shows a large tan planet (static) and a small grey moon orbiting it. The camera is static.
All values are in pixels and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory, static extents, events, camera, and a summary of the moon's motion.
- `tracks/planet.csv`: one row per frame (0-99). `circ_cx, circ_cy, circ_diam` come from a least-squares circle fitted to the disk outline; this is the reference point and size. `cx, cy` is the mask centroid. Also: bbox `x0 y0 x1 y1 bw bh`, PCA `length`/`width`, `area`, equal-area diameter `eq_diam`, and `occluded` (always 0).
- `tracks/moon.csv`: one row per frame (0-99). `cx_w, cy_w` is the intensity-weighted centroid (the reference point / origin). `cx, cy` is the plain mask centroid. The other columns are the same as for the planet.
- `scripts/track.py` builds both tracks and the overlays `frames/ov_{0,50,99}.png`. `scripts/analyze.py` prints the moon's path diagnostics (radius, angle, steps, circle fit). `scripts/probe.py` measures planet brightness/sharpness and background stability per frame.

## Method
- Planet: grey > 20 inside a window around the disk (the background there is 12-17). Take the component at the centre, fill it, and fit a circle to its outer contour. The disk's top is shaded dark, but it is still above the threshold, which I checked with intensity profiles: top edge y≈459, bottom ≈628, left ≈875, right ≈1041.
- Moon: subtract a 101-px median-blur background from the grey image, threshold at > 12, ignore anything inside the planet disk, and take the largest blob (about 120 px area).
- I checked the overlays visually: the circle sits on the planet rim, and the box sits on the moon in frames 0, 50 and 99.

## Results and reliability
- **Planet**: static at (958.3, 544.6) ± 0.1 px. Diameter 167.5 px (circle fit 167.3-167.9). The mask bbox is 170-172 x 167-168 because it includes the anti-aliased rim. Use about 167.5 ± 1 px.
- **Moon**: diameter ≈ 12.5 px (equal-area 12.3-12.9; bbox 13x12). Its size is constant. Because it is small, the relative size error is about ±5%. Do not use it as a scale reference if a better one is available.
- **Moon motion**:
  - It moves on a circle around the planet centre: distance 412.5-413.2 px (mean 412.7). The polar angle in image coordinates (y down) goes from 65.24° to 37.30°. On screen it moves counter-clockwise, up and to the right, from (1131.1, 919.2) at frame 0 to (1286.8, 794.9) at frame 99.
  - The angular rate is steady at about 0.282°/frame.
  - Per-frame step is 1.81-2.30 px (mean 2.036 px/frame ≈ 61 px/s). The scatter is centroid noise of about ±0.15 px; the motion looks uniform.
  - Path length over frames 0-99 is 201.5 px; net displacement is 199.3 px.
  - The tangential speed is constant, so the change in scalar speed is about 0. For reference only, the centripetal value v²/r is ≈ 0.0100 px/frame² ≈ 9.0 px/s².
  - Single-frame differences are noisy (±0.2 px/frame). Average over several frames, or use the arc length (radius × angle), to get a speed.
- **Events**:
  - The moon is already moving at frame 0 and still moving at frame 99. There are no bounces, contacts, releases or reversals.
  - At frame 87 (t = 2.900 s) the planet's texture/shading switches abruptly (mean brightness 77 → 55, looks blurrier). Its position and size do not change, so this is a render artifact. It does not affect the moon's track.
- **Camera**: static. Background patches stay constant to 0.01 grey levels.
- **Ambiguities**:
  - The planet's darker upper rim could be mistaken for background at a high threshold.
  - The moon is never occluded and never overlaps the planet.
  - There is no ground, horizon or other objects.
  - It is a 2D scene, so one scale applies to all distances (no perspective change: the moon's apparent size is constant).
