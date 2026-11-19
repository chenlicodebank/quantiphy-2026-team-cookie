# q_2559 — velocity of the ping pong ball at 1.4 s (cm/s)

t = 1.4 s -> frame round(1.4 x 24) = 34 (the file is also 24 fps). Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
Depth at f34 = 0.738 m (Euclidean) -> optical-axis Zc = 0.712 m.

## What happens around f34
After the 2nd bounce (f25) and a small hop (f26–28), the ball rolls across the table toward the camera and to the left
(f29–34). It reaches the front edge at f35 and falls off at f36–37. At f34 it is still on the table, about 5 cm behind the
front edge. A check at f34: the ball's crisp top edge to its half-intensity bottom is about 41 px, so D = 0.712 x 41 / 763 = 3.8 cm,
which matches the 40 mm prior.

## Method (scripts in this folder)
- `measure.py` / `measureB.py`: ball mask from background subtraction, keeping pixels brighter than the background (this keeps
  more of the shaded underside than the scene record did), giving centre, extents and overlays (frames/masksB_95_12.png).
  Centres agree with scene/tracks/ball.csv to within about 2 px.
- Table-plane model: the table's side edges meet at a vanishing point (624, 328.7), so the horizon of the table plane is
  row 328.7. Any point at a fixed height above the plane satisfies (v - vh) x Zc = const.
- `fit_roll.py`: fits constant 3D velocity on that plane to the ball centre and top-edge tracks, with Zc(34) fixed by the
  depth_info.
  - Frames 29–35, 30–35, 31–35 and 30–34 give 89–101 cm/s (centre or top edge).
  - The fitted motion is Vx ≈ -0.30, Vz ≈ -0.90, Vy ≈ -0.04 m/s.
  - Residuals are about 2 px.
- Second route, `fit_free.py`: no horizon assumed. Constant 3D velocity makes the image path projective,
  u = u_vp + A/(1 + w t) and the same form for v. Fitting it leaves the vanishing point free. It lands near the
  table horizon (v_vp 270–373), and the speed comes out 64–134 cm/s, mostly 80–100.
- Third check, `fwhm.py`: the half-maximum width of the brightest ball row grows 33.5 -> 45.8 px from f25 to f32, a ratio of
  1.37. The plane model's depth ratio Z25/Z32 is 1.35, so the depth rate is confirmed. From f33 on, this width is inflated
  by motion blur.
- Raw frame-to-frame differences of the per-frame depths are too noisy to use directly (50–140 cm/s), so the answer
  comes from the fits.

## Result
The 3D speed at f34 is about 95 cm/s (rolling). A reference smoothed over 5 frames centred on f34 would include the start of
the drop off the edge (f35–36), which pushes it a few percent higher. Answer: **97 cm/s**.

## Caveats
- The given depth at 0.9 s (1.457 m, f22) does not fit the table geometry or the ball's apparent size. Both put the ball at
  about 1.0–1.15 m at f22, while 1.457 m matches the ball's size at f0–3. It was not used for the velocity. If the
  reference's own depth series falls that steeply, its velocity would be higher (around 150 cm/s).
- Confidence: moderate, about ±15%.
