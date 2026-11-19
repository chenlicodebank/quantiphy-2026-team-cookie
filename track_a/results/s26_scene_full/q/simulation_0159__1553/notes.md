# Q1553 — shark speed at t = 1.5 s (frame 36 at 24 fps; the file is also 24 fps)

## Method
- 3D scene, static camera, principal point (960, 540). Origin proxies are the core centroids from scene/tracks. I checked them against the contact sheet: the shark is fully in view f20–f37, and the turtle core is noisy (±6 px) because of the flippers.
- Model for each animal: a straight-line path with uniform acceleration from rest, P(t) = P0 + ½·a·t²·d. P0 is the back-projection of the fitted image position at t = 0 with the given depth. The depth at t = 0.5 s (frame 12) is a hard constraint. The image track is fitted by least squares for each fixed focal length f (fit.py, fit2.py, scan.py, scan2.py).
- Turtle (prior a = 2.639 m/s²): the best fit is at **f ≈ 2500 px** (rms 6.4 px). With v0 left free, the fitted v0 is about 0 near f = 2400–2600, which supports the from-rest model.
- Shark (a free, frames 20–37 where it is fully visible): the best fit is at **f ≈ 2770 px** (rms 1.07 px). Using frames 24–37 gives f ≈ 2650. The free v0 is about 0 near f = 2600–2800.
- Shark speed at frame 36 (backward difference ×24 of the fitted 3D path) against f: 2500 → 10.91, 2600 → 10.73, 2700 → 10.57, 2800 → 10.43 m/s. The fitted shark acceleration is about 7.2 m/s² (speed ≈ a·71/48).
- Third check (sizecheck.py): if the shark's image height scales as 1/Z, the bbox height growth points to f ≈ 3000–3200 (speed ≈ 10.0–10.2). This check is weaker because the shark turns and rolls as it approaches, which changes its apparent height.

## Answer
f ≈ 2650 px (between the turtle and shark track routes) → **10.6 m/s**. All three routes give 10.0–10.9 m/s, so I expect the error to be about ±5%.
