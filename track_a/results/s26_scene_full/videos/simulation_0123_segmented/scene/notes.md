# simulation_0123_segmented — measurement record

2D scene (top-down view), 1920x1080, 24 fps, 72 frames (t = frame/24). White, segmented background. Camera static.

## Files
- `scene.json` — inventory (5 objects), static object pixel sizes/positions, events, camera.
- `tracks/teal_block.csv` — the only moving object, all 72 frames: frame, time, bbox centre (cx, cy),
  mask centroid (centroid_x, centroid_y; **use this as the reference point/origin**), bbox x0/y0/x1/y1, bbox_w/h,
  min-area-rect length/width/angle, mask area, occluded flag (always 0).
- `scripts/measure.py` — HSV teal segmentation + tracking, static-object segmentation (non-white pixels, frame 0),
  drain holes, static-region change check -> `scripts/measure_out.json`.
- `scripts/check.py` — per-frame dx, static-object jitter check.

## Objects
- **teal_block** (moving): small teal rectangle, 78 px tall (y) x 42 px wide (x, motion direction) at rest.
  At rest frames 0–1 (dx = −0.1 px), then moves straight right with constant velocity: linear fit of centroid x over
  frames 1–71 gives 14.536 px/frame (≈348.9 px/s), residual 0.27 px rms; quadratic term ≈ 0 (−1.2e-4 px/frame²);
  first half 14.53 vs second half 14.54 px/frame. y constant 586.6–587.4. x goes 412.45 (f0) → 1429.64 (f71).
  Per-frame dx scatters 13.9–15.3 px (mask edge noise) — use fits/averages rather than single differences.
  Moving width reads 42–46 px (motion-blur fringe; the mask slightly misses a faint grey trailing edge), so
  take the size from frame 0–1 (42 x 78 px). Length along motion = 42 px; the longer side (78 px) is perpendicular.
- **left_sink / right_sink** (static): identical beige basin panels 479 x 315 px, notch at top, dark drain
  hole ∅ ≈ 36 px. Centres (411, 357) and (1451, 357); centre-to-centre 1040 px.
- **tray** (static): grey foam-like rectangle, rotated ~26°, own-axis 375 x 189 px, centre (911, 199).
- **pen** (static): thin yellow-green stick, ~114 x 16 px along its diagonal axis, centre (794, 446).

## Events
- Motion start: between frame 1 and 2 (t ≈ 0.04–0.083 s). No release/bounce/contact; block passes below the
  left sink's right edge around frame 17–18 without touching anything; still moving at the last frame.

## Reliability / ambiguity
- Centroid positions ±0.5 px; static extents ±1–2 px (anti-aliased, segmentation edges flicker by <1 px per frame,
  ~1500 changed pixels/frame only at edges — not camera motion).
- Scale: one metres-per-pixel factor for the whole plane (no perspective). If the prior is the block's
  size, note which side: 42 px (along motion/x) vs 78 px (across/y). If the prior is speed, 14.536 px/frame.
- The two sinks are identical — distinguish by left/right. Object identities (sink, tray, pen) are visual guesses.
