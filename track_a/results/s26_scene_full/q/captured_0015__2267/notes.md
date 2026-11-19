# q2267 - velocity of the toy at 0.6 s (cm/s); prior g = 9.8 m/s^2, no depth_info

t = 0.6 s -> frame round(0.6*24) = 14 (question_fps = file fps = 24). At frame 14 the toy is rising during toss 1
(the hands are still near it, but its path is already ballistic, see below).

## Method
- `tmatch.py`: the scene/ toy track had a noisy centre (rotation/white parts give g between 2200 and 3700 px/s^2
  depending on the column and frames), so I re-tracked the toy by template matching (NCC, template from a clear
  free-flight frame, rotations -30..30 deg, sub-pixel peak). Templates from f19 and f17 (toss 1) and f55 (toss 2).
- Parabola fits of y(frame): toss 1 frames 15-21: g = 4.78-4.80 px/frame^2, residuals < 0.4 px; toss 2 frames
  52-58: 4.76 px/frame^2. Range across windows/templates 4.66-4.94 -> ~2740 px/s^2 -> scale 9.8/2740 = 3.58 mm/px.
- The toss-1 parabola (template f17) also fits frames 12-14 within 1.7 px, so the toy is effectively in free flight
  from ~frame 12; frame 14 is on the parabola. Apex at frame 18.85-18.90.
- Since the scale comes from g, v_y(frame) = 9.8 * (apex - frame)/24 directly (pixel scale cancels).
  Horizontal velocity is small (~7 cm/s).

## Results (vel.py)
- instantaneous at frame 14: 198-200 cm/s
- forward difference 14->15 (the lab reference convention; symmetric smoothing of a parabola keeps it at
  the t=14.5 value): 177-180 cm/s
- backward difference 13->14: ~219 cm/s
Answer 183 cm/s: leaning to the forward-difference convention (~178) and allowing for the instantaneous value (~199).

## Second-route check
Independent toss-2 g (4.76 px/f^2) agrees with toss-1 g (4.72-4.80) within 1%. The scale 3.58 mm/px makes the toy
~37 cm tall and the person ~1.8 m tall (at a slightly greater depth), which is plausible.
Confidence: moderate; the main uncertainty is the convention (forward vs instantaneous, ~11% apart).
