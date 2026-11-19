# simulation_0251 — measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 51 frames (t = frame/24, frame 0 at t = 0, last frame 50 at t = 2.0833 s).
Source: simulation (Blender), **2D** scene. No metric scale is assumed anywhere.

## Scene content
- **ball** (only object): white/light-grey sphere with black five-pointed stars. Rolls left to right along
  the floor, almost exactly horizontally, slowing down gradually. It is already moving when it enters at the left
  edge in frame 0 and is still moving at frame 50 (cx ~1453 px). It has a soft contact shadow underneath.
- **backdrop_wall / floor**: plain grey studio backdrop; wall above, floor below, with a soft horizontal
  wall/floor boundary band at y ~544-556 px. No markings, furniture or other props.
- **Camera**: static (no pan, zoom or shake; differencing against the median background leaves nothing but the
  ball). The apparent ball size is constant, so all motion is in a plane facing the camera.

## Files
- `scene.json`: inventory, camera, events, summary numbers.
- `tracks/ball.csv`: one row per frame 0-50, with: frame, time_s, cx_px, cy_px (centre = sphere origin),
  radius_px / diameter_px (fixed 25 / 50), bbox (circle box clipped to the image), visible_frac,
  partial_at_edge, fit_score, occluded (always 0).
- `scripts/`: `track_ball4.py` is the final tracker. `track_ball.py`, `track_ball2.py` and `track_ball3.py` are
  superseded earlier attempts kept for provenance (track_ball4 reads `_fit_v3.npy`, the output of v3).
  `check_vertical.py` checks the vertical position, `write_scene.py` writes scene.json, `cleanup.py` removes scratch.

## Method
- Background = per-pixel median over all 51 frames (band y 380-720); d = |blurred frame - background|.
- A circle is fitted to the ball's **outer silhouette**. Score = mean contrast d(r-2.5) - d(r+2.5) around the
  circle (clipped so the internal star edges do not dominate), leaving out the bottom 80 deg because the shadow
  touches the ball there.
- A free-radius fit over frames 5-36 gave a median radius of **25.0 px (diameter 50 px)**. The final track fixes
  R = 25 and fits only the centre, to 0.125 px resolution.
- Overlays drawn on every frame were inspected: the circle matches the ball outline in all frames 1-50.

## Results (for later sessions)
- Ball diameter: **50 px (±2)**, constant. Use this for a size prior (metres per pixel = D_world / 50).
- Horizontal steps per frame (event detection only): ~33 px/frame near frames 2-8, falling steadily to
  ~25.5 px/frame near frames 46-50. A quadratic fits cx(frame) over frames 2-50 with 0.47 px rms
  (cx ≈ -21.7 + 33.78·f - 0.0859·f²), i.e. close to uniform deceleration.
- cx: 46.5 px (frame 2) → 1452.6 px (frame 50); net displacement 1406.1 px over frames 2-50.
- Events: frame 0 ball enters at the left edge (centre still off-screen, cx ≈ -17); frame 2 first fully
  visible; no bounce, impact, contact or change of direction; frame 50 the video ends with the ball still rolling.

## Reliability / ambiguities
- cx is reliable to about ±0.5 px per frame in frames 2-50. Frames 0-1 are partial (centre near or outside the
  left edge), so their cx is less certain (±2-3 px).
- cy is less certain (±3 px). The fitted cy is about 562 in frames 2-38 and about 557.5 in frames 39-50; that
  4 px jump is probably a fit artefact (shadow below, wall/floor band and a faint compression arc above the ball),
  not real motion. The raw mask's top/bottom midpoint stays ~557-558 throughout. Treat the motion as horizontal
  and use cx for distances and speeds (cy contributes at most ~0.5 px per frame at the jump only).
- The dark stars rotate with the ball (rolling); they are texture, not separate objects.
- No occlusion. There is mild motion blur (~30 px/frame at the start), but the silhouette stays sharp enough.
