# q_1903 — length of the box (m); prior: speed of the box = 0.094 m/s

2D side view, 120 fps (file and question rates agree), static camera. "The box" = brown cardboard box on the truck's roof
(the prior's object and the asked object are the same).

## Speed of the box in pixels
- The box rises at a CONSTANT speed (the cargo body underneath accelerates; the box does not follow it exactly).
  So the prior speed is a single well-defined value.
- Route 1 (texture.py): template match of the printed icon block on the box face, all 401 frames:
  linear slope 19.19 px/s, residual rms 0.05 px, quadratic term ~0; 40-frame chunks 18.7-19.7 px/s.
- Route 2 (measure.py): sub-pixel top edge of the box at 6 columns: 18.93 px/s (rms 0.26 px, noisier, top edge
  slightly affected by flap/edge shading). Agrees within 1.4 %.
- Used 19.19 px/s -> scale = 0.094 / 19.19 = 0.004898 m/px.
- (scene/ record's box ref_y is contaminated by the bottom edge, which follows the accelerating roof; not used.)

## Length of the box in pixels
- Left/right edges (threshold crossing, 3 rows, all frames): 410.1 ± 0.4 px; scene record mask width 408 px.
  Take 409.5 px.

## Answer
409.5 × 0.004898 = 2.006 m -> 2.0 m. (With the top-edge speed: 2.03 m.)
Confidence: good (~2-3 %).
