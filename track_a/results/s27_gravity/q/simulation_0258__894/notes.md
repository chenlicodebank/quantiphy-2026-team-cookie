# q894 phone width (right of plant)
2D scene; scale from pen free-fall prior (9.8 m/s^2). File is 24 fps; question_fps = 30 used as time base (per rules).
- Pen cy (scene/tracks/pen.csv, frames 3-15) quadratic fit: a = 6.87 px/frame^2 (from frame 5: 6.84; second diffs 6-8, mean ~6.9). Fit rms 0.27 px.
- Scale = 9.8 / (6.87*30^2) = 1.585 mm/px.
- Phone (black, x~1142-1189, y 866-871 at frame 36) edge-crossing on row-averaged profile: 1141.5 -> 1189.2 = 47.8 px (dark-pixel row extents 44-49 px; scene record 50 px visual).
- Width = 47.8 * 1.585 mm = 0.0757 m -> answer 0.076 m.
Check: at 30 fps, AC unit 506 px = 0.80 m, table 1.62 m, pen 0.10 m, cup 7.3 cm (all plausible); with 24 fps they would be 1.25 m, 2.53 m, 0.16 m (AC and table too large) -> 30 fps scale consistent.
Confidence: moderate-good (edge of phone +-2 px ~ 4 pct).
