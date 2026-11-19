# q_3232: ball velocity at 2.00 s

- The camera looks straight down at a gym floor. A basketball rolls from right to left between frames 49 and 72. There is no fall, bounce or vertical motion, so the prior (gravity = 9.8 m/s^2) describes a motion the clip never shows and gives no usable scale.
- **Scale:** from a regulation size-7 basketball, diameter 0.239 m. The ball's blur-free vertical diameter is 256 px (median over frames 53–69, range 250–261, from scene/tracks/ball.csv), so the scale is 0.000934 m/px.
- **Time:** question_fps = file fps = 30, so t = 2.00 s is frame 60.
- **Pixel speed** (measure.py, cx_stab/cy_stab, which are relative to the background):
  - Local fits around frame 60 give 90.3–90.8 px/frame. The motion is nearly uniform and the vertical drift is about 1 px/frame.
  - The raw one-frame differences are noisy (±5 px of centre noise): forward 60→61 is 96.6 px, backward 59→60 is 89.5 px. I used the smoothed value, 90.5 px/frame = 2715 px/s.
- **Velocity:** 2715 px/s × 0.000934 m/px = **2.53 m/s**.
- **Second check:** the court lines are about 50 px wide and are taken as the standard 2 in (0.0508 m) width. That gives 0.00102 m/px at the floor plane and a speed of 2.76 m/s there. The ball's centre is about 0.12 m above the floor, so closer to the camera, and its true scale should be somewhat smaller. The size ratio implies a camera about 1.8 m above the floor, which is plausible for a hand-held phone with the holder's shoes in view. The two routes agree.
- **Confidence:** moderate.
  - If a size-6 ball (0.232 m) was used, the answer would be 2.46 m/s.
  - The single raw forward difference would give 2.70 m/s.
