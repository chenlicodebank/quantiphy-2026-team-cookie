# q_2794 — diameter of the yoga ball (cm)

File fps = question_fps = 24; t = 1.0 s -> frame 24. depth_info: yoga ball centre 2.612 m at t = 1.0 s.
Lab method card: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Pixel diameter at frame 24 (measure.py)
- Foreground mask (per-row background median, threshold 40), left/right edge per row, least-squares circle fitted on
  the free left arc and the right arc below the hand (excludes the hand at top right and the SAM shadow tail at the
  bottom). Overlay f24_fit.png: circle follows the outline all round, incl. top (y~466) and bottom (y~613).
- Circle fit d = 145.7 px, centre (571, 540); widest chord 148 px (scene record); visual edges x 498 -> 644 (147 px),
  vertical top->bottom ~147 px. Adopted 147 px (+-1.5).
- Neighbouring frames consistent: 23 -> 140.6/152 (fit/chord), 25 -> 150.3/151, growth smooth as the ball approaches.

## Size
D = 2.612 x 147 / 762.8 = 0.5034 m -> 50.3 cm (range 49.9-50.6 for 145.7-148 px).
Off-axis note: the ball is 14 deg off-axis; exact sphere projection would give ~48.6 cm; the card formula (used by the
reference) gives 50.3 cm.

## Second route / check
- Prior velocity 2.19 m/s at 1.0 s: with depth from apparent size (Z ~ 1/d, anchored at 2.612 m at frame 24) and
  back-projected circle centres, speed around frame 24 = 1.92 m/s (steady 1.9-1.96 over frames 21-28). That is 12 pct
  below the prior; if 2.612 m were the front-surface depth (centre at ~2.86 m) the speed would be 2.11 m/s and the
  diameter ~55 cm. The annotators' velocity came from their own per-frame clicked depths, so this is a weak check;
  the answer follows the method card with the given centre depth.

Confidence: moderate (pixel size +-1 pct; main uncertainty is the depth convention, possibly ~+10 pct).
