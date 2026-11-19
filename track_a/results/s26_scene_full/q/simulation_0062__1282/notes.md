# q1282 – height of the white car (white cargo van)

Prior: acceleration of the white car = 4 m/s^2. question_fps = file fps = 24.

## Method
The white car is the van in scene/ (`tracks/van.csv`). Its image size and top row stay the same through the clip, so it
translates parallel to the image plane at constant depth. Its pixel acceleration and its pixel height are therefore
on the same depth plane (the near side face), which gives:
H = h_px x a_world / a_px. The focal length and depth cancel out.

- a_px (fit.py): quadratic fit of the tracked x against t = frame/24.
  f1–71: 307.2 px/s^2 (rms 0.53 px); f22–71: 307.4; f35–71: 308.2; f1–35: 310.8; mean of the per-frame second differences: 309.
  The short window f54–71 gives 322 (less reliable). Value used: 308 px/s^2.
- h_px (profile.py, vanh.py): in f57 and f62, the roof edge is at y ≈ 453–454 (faint, white on white sky) and the tyre bottom
  is at y ≈ 617–618 (rear and front wheels). That gives about 164 px. The record gives 162.5 (452.5–615). Value used: 163.5 px.
- H = 163.5 x 4 / 308 = 2.12 m.

## Second route (depth_info)
With the van's u at f14 (516) and f38 (860), v ≈ 534, a principal point of (1080, 540), and the given distances
30.065 m and 29.307 m, solving D^2 = Z^2 (1 + r^2/f^2) gives f ≈ 2256 px and Z ≈ 29.17 m.
The acceleration then comes out as 308 x 29.17 / 2256 = 3.98 m/s^2, which matches the prior.
The height comes out as 163.5 x 29.17 / 2256 = 2.11 m at the origin depth, or about 2.04 m using the near-face depth Z − 1 m.
The focal length is very sensitive to the depth ratio, so the prior route is preferred.

Confidence: about ±3–4 %.
