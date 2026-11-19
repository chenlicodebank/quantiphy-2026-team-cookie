# q_2493 — width of the table (cm)

Width = front-to-back depth of the table top (its shorter horizontal extent). File fps = question fps = 24.

## Method (3D, lab camera f = 0.5959*1280 = 763 px, c = (640,360))
1. Ball centres back-projected with depth_info: frame 24 (t=1.00, d=0.901 m; "0.901s" read as metres),
   frame 30 (t=1.24 → round(29.76)=30, hit board, d=1.144), frame 38 (t=1.6 → 38.4 → 38, d=1.027);
   pixel centres from scene/tracks/ball.csv (checked). Ball rolls on the table, so the table plane = ball-centre
   plane shifted 3.35 cm (radius from the 6.7 cm prior) along the normal (`plane.py`).
   The camera is only ~15-17 cm above the table top and looks almost horizontally.
2. Table edges measured in code on frame 10 (`width.py`): front top edge (top face / front face boundary) fitted line
   v = 0.0547u + 524.5 (rms 0.7 px, x 240-1050); back edge = base of the white board standing on the back edge,
   v = 0.0381u + 431.5 (rms 0.7 px, x 440-900). Side edges fitted (noisier, `width2.py`): they meet the board base
   at its corners → the board stands at the table's back edge. Check: the ball at the board-hit frame 30 has its table
   contact at v≈460, ~3 px in front of the board base at that column, as predicted for a 3.35 cm radius.
3. Width = perpendicular distance in the table plane between the front and back edge lines (`width3.py`):
   - a) plane normal from the 3 ball points: 0.557 m at the image centre (varies 0.58-0.53 across u: normal roll error)
   - b) normal from the table's vanishing points, offset from the ball points: 0.568 m (constant along the edge)
   - c) normal constrained ⊥ to the front/back-edge direction, LSQ to ball points (resid ≤ 2.6 mm): 0.578 m
   Front edge length ≈ 0.75 m (length/width ratio ≈ 0.75, plausible 80x60-type table if scale slightly larger).

## Second check / scale caveat
Apparent ball diameter (`ballsize.py`, `ballprof.py`) gives depths ~4-9 % larger than depth_info (e.g. 40-42 px at
frame 30 vs 44.7 px expected), but the measurement is unreliable (yellow-ish wood background, blur, SAM halo).
If depth_info is to the ball's front surface (+3.35 cm), the scale would be ~3 % larger.

## Answer
Mean of routes 0.557-0.578 m ≈ 0.568 m, nudged slightly up for the ball-size evidence: **57.5 cm**.
Confidence: moderate (±5 %).
