# q_2518 – velocity of red ball at 0.6 s (cm/s)

Lab clip, 24 fps (file and question_fps agree), 1280x720. t = 0.6 s -> frame 14. f = 0.5959*1280 = 762.8 px, c = (640,360).
Depths given: f5 0.8715, f10 1.166, f14 1.372, f19 1.315 m.

## Track
scene/tracks/ball.csv centres checked on zoomed frames 12-16 (frames/f*.png): ball at x ≈ 498, 533, 566, 602, 640
(my own edge midpoints, topedge.py, agree to ±1 px). Image motion at frame 14 is ≈ 34-36 px/frame, almost horizontal.
Frames 15-16: the table's far edge hides the bottom of the ball and the record's v is biased by a few px. I tried
v interpolated between frames 14 and 17 as well; it changes the result by < 0.5 cm/s.

## Depth per frame (main route, sinedepth.py)
The ball goes round a closed loop (period ≈ 25-26.6 frames), so I fitted d(t) = m + A cos wt + B sin wt to the 4 given
depths. It reproduces all four to within ≤ 5 mm, which supports the model. Depth keeps rising slowly after f14 (peak ≈ 1.40 m at f16).
Back-projection P = unit_ray(u,v) * d(t). Speeds near frame 14:
- forward difference 14->15: 162-164 cm/s
- mean of per-frame speeds 12-16: 167-170
- 5-frame smoothed positions, forward diff: 158 (frame 14) / 173 (frame 13)
- chord 12->16: 160
-> about 163 cm/s.

## Second routes
- PCHIP / cubic interpolation of depth (measure.py): 150-170 cm/s, depending on the radial rate at f14.
- Harmonic orbit fit to (u,v) + depths (orbit.py): 1 harmonic -> 155-166 (the depths fit to 3-9 cm);
  2 harmonics -> 187-195 (fits the depths exactly but makes the orbit strange; I treat it as overfitted).
- Chords between the given 3D points: f10->14 177 cm/s, f14->19 162 cm/s (chords run a little low on a curve).
- Sanity check: a loop of radius ≈ 0.3 m and period ≈ 1.08 s gives about 175 cm/s.

Answer: 163 cm/s. Confidence moderate (±8 %). The main uncertainty is the radial (depth) rate at frame 14.
