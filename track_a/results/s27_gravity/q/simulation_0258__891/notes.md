# Q891: diameter (width) of the plant

- This is a 2D video with a static camera. The file plays at 24 fps; question_fps is 30, and the time base follows question_fps.
- **Scale from the prior** (the pen falls at 9.8 m/s²):
  - I fit a quadratic to the pen centre `cy` over frames 3–15, the free fall before the bounce, taken from `scene/tracks/pen.csv`.
  - The fit gives a pixel acceleration of 6.868 px/frame², and the residual is tiny (0.98 px² total).
  - The one-frame differences rise steadily by 6.5–7.5 px per frame.
  - At 30 fps that is 6181 px/s², so the scale is 9.8 / 6181 = 1.586e-3 m/px.
- **Plant width** (`plantw.py`, frame 36):
  - The white cup has half-max brightness edges at x ≈ 1085 and 1127 at y = 845, so it is about 42–43 px wide.
  - The succulent's leaves span x ≈ 1084–1131, about 46–48 px.
  - I took the plant's horizontal extent as ≈ 45 px (range 42–48), which gives 45 × 1.586e-3 = 0.071 m (range 0.067–0.076 m).
- **Checks:**
  - The pen is 65.3 px long, which is 0.104 m at this scale: a plausible pen.
  - A plant about 7 cm across is a plausible small potted succulent.
  - If I had used the file's 24 fps instead, the result would be 0.111 m and the pen would be 0.16 m long. I rejected that because the rules say to use question_fps.
- **Confidence:** moderate. The main uncertainty is whether the asked width means the pot or the leaves (about ±7%).
