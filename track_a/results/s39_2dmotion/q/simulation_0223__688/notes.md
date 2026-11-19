# q_688 – acceleration of the moving red general at t = 1.5 s

- question_fps = file fps = 24, so t = 1.5 s is frame 36. 2D top-down scene; the red general slides straight down the centre file.
- Prior: piece diameter = 0.097 m.

## Scale
- My own background-difference mask (`measure.py` -> `my_track.json`): horizontal width 86–87 px, area-equivalent
  diameter 86.4–87.2 px on frames 13–39. The record says 86–87 px. I used D = 86.7 px, so the scale is 0.0011188 m/px.
- SAM 3 (segment, frame 36, box prompt) gives a 94 x 90 px box (area-equivalent diameter 90.3 px), about 4 % bigger.
  On the 5x zoom (`frames/zoom36.png`) the SAM outline is blocky and sits 2–4 px outside the disc edge all round. The
  visible disc is about x 917–1001 (≈ 85–87 px). So my mask is right and SAM over-segments. The SAM centroid
  (959.3, 849.9) matches my centroid (959.27, 849.33) to within 0.6 px.

## Motion
- Frames 9, 11, 18, 20, 28 and 34 are the first frame of duplicated image pairs, and their own position is missing.
  I left them out of every fit. This includes frame 34, which the convention's difference at frame 36 needs, so I
  used the fitted position there.
- The acceleration is not exactly constant: a global quadratic leaves 0.7 px residuals, and the local acceleration
  falls from about 1.1 to 1.0 px/frame². So I measured it locally.
- At frame 36, using the convention speed(36) − speed(35) on the fitted positions (y36 − 2·y35 + y34):
  - My track: quadratic over frames 30–39 gives 1.013 px/f²; quadratic over 25–39 gives 1.030; cubic over 25–39
    gives 1.011; cubic over 13–39 gives 1.012.
  - The record's mask_centroid_y (second route): quadratic over 30–39 gives 1.002; cubic over 13–39 gives 1.008.
  - The raw clean second differences near frame 36 are 1.065, 0.755 and 1.019.
- I took a = 1.012 px/frame² × 24² = 583 px/s² × 0.0011188 m/px = **0.652 m/s²**.

## Confidence
- The routes span 1.00–1.03 px/f², so the motion part is good to about ±2 %. The scale is good to about ±1 % (86.5–87 px).
- If the motion were really uniform acceleration, the global value would be about 1.05–1.08 px/f² (0.68–0.70 m/s²).
  The local fits are much better, so I answer with the local value.
