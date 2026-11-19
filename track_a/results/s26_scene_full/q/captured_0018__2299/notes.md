# q_2299 — tennis ball diameter (cm), captured_0018 (lab, 24 fps file = question_fps 24, 1280x720)

Prior: g = 9.8 m/s^2. depth_info: soccer ball 2.80 m, near person (right, holds the tennis ball) 2.002 m,
far person 3.130 m. No depth is given for the tennis ball itself, so its depth was estimated. f = 0.5959*1280 = 763 px.

## Pixel diameter (zoom.py, edge_size.py, measure_tb.py)
- Sharp frames: held (frames 0-7, hand covers its right side) vertical extent ~21-23 px (visual edges y 245-268);
  rebound apex frame 45 (nearly motionless): x 737.5-759.1 → 22.6 px (sub-pixel half-contrast), visually ~23 x 22.
- Colour-only masks underestimate (dark shadow side): 17-20 px. Adopted D_px = 22.5 ± 1 px.

## Depth of the tennis ball (three routes)
1. Rebound parabolas (accel.py, scene tracks, residual rms < 1 px): tennis a = 4.3-4.6 px/frame^2, soccer
   a = 3.26 px/frame^2. Same g → Z_tennis/Z_soccer = 3.26/4.4 ≈ 0.74 (0.71-0.76) → ≈ 2.07 m (1.99-2.14).
   (Absolute g at 24 fps gives soccer 3.98 m vs the given 2.80, i.e. the recording clock is not exactly 24 fps
   (record also notes a probable dropped frame 35→36), so g was used only as a ratio.)
2. Floor contact heights (horizon y≈342): tennis bottom 615, soccer 565 → ratio 223/273 = 0.82 → ≈ 2.29 m.
3. Back-projecting both persons (2.002 m at u≈990, 3.13 m at u≈380) and placing the ball on the line between them
   at u=771 → ≈ 2.16 m (ball held at arm's length ~0.55 m from the near person's body).
Adopted distance ≈ 2.15-2.2 m.

## Result
D = 22.5 px × 2.15-2.2 m / 763 px ≈ 6.3-6.5 cm; pixel edges are softened by blur/compression, so the true
extent is likely slightly larger. Sanity: a regulation tennis ball is 6.54-6.86 cm. Answer 6.6 cm.
Confidence: moderate (±7 %), dominated by the tennis-ball depth (no direct depth_info) and the ±1 px diameter.
