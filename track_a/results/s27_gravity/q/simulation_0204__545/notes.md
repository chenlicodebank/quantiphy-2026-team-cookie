# q545 speed of magnifying glass at t=0.333 s (frame 8 at question_fps 24 = file fps)
Method: 2D, scale from prior g=9.8 m/s^2. Quadratic fit of vertical position (frames 0-11, pure free fall, x constant)
from scene/tracks/magnifier.csv (fit.py). Mask centroid: a=12.90 px/frame^2 -> 9.8/(12.90*576)=1.319 mm/px; bbox centre a=12.93.
Speed = backward difference (p8-p7)*24*scale: centroid fit 3.091, raw 3.096; bbox-centre fit 3.094, raw 3.064.
Check: ideal release from rest at frame 0 gives g*7.5/24 = 3.0625; fitted release time -0.075 frame gives 3.093.
Bbox top/bottom edges individually are noisier (tilt changes apparent height) and bracket the value (2.9-3.3).
Answer 3.09 m/s; confidence high (~1-2%).
