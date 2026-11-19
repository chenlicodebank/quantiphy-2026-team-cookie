# Q77: speed of the bike at 1.0 s (m/s); prior: bike length = 1.7 m

Top-down 2D clip, 24 fps (the file and question_fps match). t = 1.0 s -> frame 24. The bike rides right -> left at constant velocity.

## Method (measure.py)
- Cyan bike pixels (HSV hue 75-100, sat > 50, val > 100) in the axis band y 625-672. Front and rear tips = the extreme
  columns (the rider hides the middle of the bike, so gaps of up to 200 px are bridged). Frames 4-32 show the whole bike.
- Bike length in pixels (tip to tip): 409 px at frame 24 (mean 409.0 over frames 21-27); 412 px median over the whole
  frame (it shrinks slowly from 416 at the right to 408 at the left, a ~2% scale drift).
- SAM 3 "bicycle" mask at frame 24: box x 443.0-852.4, length 411 px. My value is 409 px (0.5% off) and matches the scene record (409).
  The overlay covers the whole bike from the front wheel tip to the rear rack tip.
- Motion: centre 698.5 -> 647.0 between frames 23 and 24 = 51.5 px (front tip 51 px, rear tip 52 px). A linear fit over frames 4-32
  gives 51.24 px/frame. The per-frame diffs are 50-52 px (±1 px of quantisation), and the scene record also has 51.3 px/frame.

## Result
Local scale = 1.7 / 409.5 px = 4.151e-3 m/px.
v = 51.24 px/frame x 24 x 4.151e-3 = 5.10 m/s.
Cross-checks: the raw one-frame diff (51.5 px) gives 5.13; the whole-clip median length (412 px) gives 5.07. All are within 1%.
Answer: 5.10 m/s. Confidence high (about ±1-2%).
