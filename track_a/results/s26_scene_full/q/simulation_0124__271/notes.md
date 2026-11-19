# Q271 – speed of the grey/red car at 1.0 s

- 2D top-down render at 24 fps (question_fps is also 24), so frame 24 is t = 1.0 s. The camera is static.
- Grey/red car = `silver_car` (silver with red stripes). Black car = `dark_car`. I confirmed both on frame 24 (frames/f24.png).
- Scale: one metres-per-pixel factor from the prior (the black car at 26.085 m/s).
- Per-frame steps, from scene/tracks (steps.py): both cars move at a constant speed from frame 2 to their exits.
  - silver: 22.27 ± 0.18 px/frame (22.34 around frames 20–28; 21.91 at frame 24 itself, which is noise)
  - dark: 27.01 ± 0.33 px/frame
- Ratio 0.8246 → 26.085 × 0.8246 = 21.51 m/s.
- Second route (check.py): 2-, 3- and 4-frame chord speeds give ratios of 0.8253, 0.8260 and 0.8265 → 21.53, 21.55 and 21.56 m/s. The local window around frame 24 gives 21.57.
- Answer: 21.53 m/s. Confidence is high (about ±1 %), because both speeds are constant and the scale is a pure ratio.
