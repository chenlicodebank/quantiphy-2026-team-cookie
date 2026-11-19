# Q3231 – velocity of the ball at 1.90 s (internet_0066)

The video and the question both run at 30 fps, so t = 1.90 s is frame 57.

## Scale
The prior (g = 9.8 m/s²) can't set the scale here. The camera looks straight down at the gym floor and the basketball rolls horizontally across the view. Its apparent size stays the same, so it doesn't fall, and there is no vertical motion to calibrate against. The scale comes from the ball itself instead: a regulation size-7 basketball, diameter about 0.239 m (circumference 0.749 m).
- The ball's diameter across the motion (no blur) is 256 px in the scene record (range 250–261). My own re-measurement gave 258–262 px (`remeasure.py`).
- I use 257 px, so the scale is 0.239 / 257 = 9.30e-4 m/px.
- The ball's centre and its diameter lie in the same plane, so perspective doesn't bias this scale.

## Pixel velocity (vel.py, scene/tracks/ball.csv cx_stab/cy_stab, frames 53–69 with the ball fully in view)
- Linear fit: 90.4 px/frame (vx -90.4, vy +0.94). The motion is uniform: a quadratic term is negligible and the slope at frame 57 is 91.9.
- Centred differences: 52–62: 90.9; 54–60: 91.3; 55–59: 89.4.
- Single steps: 57→58 (forward): 89.0; 56→57 (backward): 82.5. These are noisy at about ±5 px.
- Camera drift during the pass is under 1 px/frame. The cx_stab values have it removed.

## Answer
90.4 px/frame × 30 = 2711 px/s, × 9.30e-4 m/px = **2.52 m/s**.

Second route: the forward difference at frame 57 (89.0 px) gives 2.48 m/s. With the record's 256 px diameter it is 2.53 m/s. A size-6 ball (0.232 m) would give 2.45 m/s.

My independent difference mask (`remeasure.py`) picked up the shadow along with the ball, so its centre slope (83.7 px/frame) is biased. I used it only for the diameter.

Confidence: moderate. The main uncertainty is the assumed ball size (±3%) and which difference scheme the annotators used (±2%).
