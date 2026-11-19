# q_3170 – ball displacement 2.00 s → 4.00 s

- Time base: fps = question_fps = 30, so t = 2.00 s is frame 60 and t = 4.00 s is frame 120. Frame 60 is in the shot's flight;
  frame 120 is just after the apex of the first bounce (apex at 116, bounce 1 at frame 97).
- Scale from the prior g = 9.8 m/s². I fit a parabola to the ball's bg-fixed y in each free-flight arc (`measure.py`):
  shot (55–95, without the degraded frames 73–77) 1854.6 px/s²; bounce 1 arc (99–134) 1890.3; arc 2 (137–163) 1828.6;
  arc 3 (166–186) 1869.6. Mean 1860.8 px/s², so the scale is 0.005267 m/px (the arcs spread by ±1.7 %).
- Positions (bg-fixed, camera drift removed): frame 60 (739.6, 333.9), frame 120 (1429.9, 527.6), so the ball moved 716.8 px
  (from the parabola/line fits: 716.6 px). I checked both positions by eye on zoomed crops: raw centres ≈ (730, 330) and
  (1418, 518), which match the track.
- Displacement = 716.8 × 0.005267 = **3.775 m**.
- Second-route checks: using raw frame pixels without drift compensation gives 713.0 px → 3.755 m. Using each arc's own g
  alone gives 3.72–3.84 m. Sanity checks with the same scale: the ball's diameter of 45 px comes out at 0.237 m (a real
  basketball is 0.24 m) and the rim's 90 px at 0.47 m (real 0.46 m), so the scale is consistent.
- Confidence: high, about ±2 %.
