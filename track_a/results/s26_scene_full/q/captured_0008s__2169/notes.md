# q_2169 — basketball velocity at t = 1.2 s

The question and the file both run at 24 fps, so t = 1.2 s is frame 29. That is the last falling frame: the first impact is at about frame 30.

## Method
- I used the camera from the method card: f = 0.5959·1280 = 762.8 px, principal point (640, 360).
- Ball centres come from scene/tracks/ball.csv (circle fit). I checked frames 26–31 on a crop (frames/fall.png). In frames 28–29 the tracked centre sits on the solid part of the ball, slightly below the middle of the blur streak.
- The given distances match the measured diameters with a ball diameter D of about 0.225 m:
  - frame 24: 0.228 m
  - frame 29: 0.220 m
  - frame 36: 0.228 m
- 3D positions are back-projected along the unit ray times the distance: the given depth where there is one, otherwise D·f/diam.

## Routes (speed at frame 29)
- **A. Anchored chord, frames 24→29.** Uses the given depths 1.401 and 1.564 m. The 3D displacement is 0.517 m over 5/24 s, so the average is 2.48 m/s. With a = 9.8 that gives v29 = 2.48 + 9.8·(5/24)/2 = **3.50 m/s**.
- **B. Quadratic fit of 3D positions, frames 22–29.** With acceleration free, |a| comes out 12.8–15.6 (inflated by blur on the late frames) and v29 = 3.9–4.2. With |a| fixed at 9.8: **3.52–3.64 m/s**.
- **C. Drop from release.** Measured from release, the drop to frame 29 is 0.632 m, so v = sqrt(2·9.8·0.632) = **3.52 m/s**. If instead I take the release time as t ≈ 0.875 s (frame 21) and use v = g·Δt, I get 3.27 m/s. That would mean release at about frame 20.5, or a slight push from the hand: frame 22 has already moved 11 px, twice what free fall predicts.

## Answer
**3.45 m/s.** This weights the distance-based routes (about 3.5) over the release-time route (3.27).

Confidence: moderate, about ±7%. The main uncertainties are the release time, the blurred centres in frames 26–29, and how the reference smoothing treats a frame right next to the impact.
