# q_2145 – ball velocity at the end of the slope (cm/s)

Prior: a = 3.0 m/s^2 at t = 1.6 s (frame 38). The depths given are ball 1.1075 m at f0 and 0.912 m at f36; slope far end 1.136 m, near end 0.884 m.
The file runs at 24 fps, the same as question_fps. f = 0.5959*1280 = 763 px, principal point (640,360).

## Method (measure.py, fit.py)
- I back-projected the ball centre at f0 (664.1,332.9; range 1.1075) and f36 (661.6,423.6; range 0.912) to get two 3D points.
  The ball path is the straight 3D line through them. Its direction matches the slope direction from the back-projected
  board edges (top (644.5,353) at 1.136 m, bottom (638,496) at 0.884 m; slope length 0.313 m, about 32 deg).
- For each frame I took the point on this line closest to the ball's pixel ray, which gives the path coordinate s.
- The ball reaches the bottom of the slope at about frame 38, where s = 0.305-0.316 m (crop sheet frames/seq.png).
- The track is irregular: frames 17-19 are duplicates, 38/39 and 41/42 are near-duplicates, and 35->36 has a large jump with blur.
  Because of this, frame differences after f35 are unreliable (they give 216, 123, 86, -16 cm/s). The answer uses the
  sharp frames 28-35 instead.

## Results
- Quadratic fit to s(t) over frames 29-35 (rms 1 mm): a = 3.8 m/s^2, v(f35) = 1.02 m/s. Extrapolated to the end of the
  slope (frame 38.2): v = 1.52-1.56 m/s.
- Using the measured v35 and the prior a = 3.0 for the last 0.17-0.18 m: v = 1.43-1.45 m/s.
- Second route, pure physics from rest with the prior: v = sqrt(2*3.0*L), with L = 0.305-0.316 m, gives 1.35-1.38 m/s.
- Answer: 145 cm/s, in the middle of the three routes (137-155). Every route lands within about 7% of it.

Confidence: moderate. The irregular frame timing near the end of the slope makes a direct frame-difference speed unreliable.
