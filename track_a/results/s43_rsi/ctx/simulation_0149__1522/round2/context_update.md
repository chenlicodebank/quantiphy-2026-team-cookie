# Round 2 addendum – Q1522 (speed of the car at t = 0.5 s)

Round 1's switch to **6.8 m/s** was verified with independent code. Decision: switch (to 6.8), confidence medium.

## Newly established
- Camera geometry: the vertical lines in f49 have zero tilt up to |u−cx| = 500 px. So there is no pitch, and the horizon v≈829 comes from a lens shift (principal point ≈ (960, 829)). With this principal point the VPs give f = 2370 (round 1 had 2353 with the image centre). The effect on speed is about 1%.
- Rim vertical extent, from two of my own estimators:
  - Column half-max: f0 87.25, f11 97.25, f12 99.29.
  - Radial-edge conic fit: f0 86.35, f11 97.03, f12 99.47.
  - Both agree with round 1 within about 0.6 px.
- Speed at f12 with long-window local fits (cubic to quintic or quadratic, windows 0-23, 0-20, 2-22, 6-18): 6.50–6.97, centre ≈ 6.8. Short windows (8-16, 6-18 cubic) give 5.95–6.35 and are noise-dominated. Raw single-frame differences (6.3–8.3) are unusable.
- C4's fault reproduced: a linear 1/H fit over f8-23 gives a rate −2.27e-4 vs −2.0e-4 locally (+13%), which gives 7.8 m/s.
- Closure: tyre about 137–140 px at f0 (top edge about 759, floor contact about 899) → 0.771–0.788 m vs 0.764 (+1 to +3%).

## Ruled out
- 8.2 (constant-rate fit plus far-tyre offset) and 9.0 (a guess from the speed-limit sign).
- A pitched-camera model is not needed. It also does not change the result materially.

## Open
- Derivative noise of about ±4% (6.5–7.0). The tyre-size closure being +1 to 3% high hints that f might be slightly larger (about 2450). That would lower the speed by about 0.1 m/s. This is within the noise.
