# Q1888: astronaut speed at t = 3 s (m/s)

Prior: the astronaut is 2.2 m tall. depth_info: the camera-to-astronaut distance is 18.147 m at t = 1 s (frame 24).
The file and the question both use 24 fps, so t = 3 s is frame 72. This is a 3D scene, and the camera is assumed
fixed.

## Scale
- Focal length: f = h_px(f24) x D / H = 380 x 18.147 / 2.2 = 3134 px (horizontal FOV about 40°). If the walking-pose
  bounding-box height is about 2.1 m, f = 3284 px. This only affects the lateral term, and only by about 3%.
- Depth at f72: D72 = 18.147 x 380 / 421 = 16.4 m. This uses the bbox-height ratio. ECC registration of the upper
  body gives a ratio of 1.093 to 1.106, which means 16.4 to 16.6 m.

## Why bbox height was not used for the depth rate
Near f72, bbox_h rises quickly (406 → 437 px over f66 to f78). Taken as depth, that would mean about 2.5 m/s of
approach. The crops show that this comes from pose: at f60 to f66 the astronaut leans forward and crouches, and at
f72 to f78 they stand more upright. Over the same frames the feet's image row stays at 1055 px. The rigid
backpack's vertical extent (`backpack.py`, overlays in `frames/bp*.png`) grows only 0.14 to 0.15 % per frame, so the
radial speed is about 0.55 to 0.6 m/s.

## Measurement (final.py)
- Pelvis image velocity from linear fits over f66 to f78: (+7.9, -0.9) px/frame. The backpack's rear edge gives
  7.6 px/frame.
- Back-projection: P = unit ray(u, v, f) x D(t), with D(t) = D72 x bp_h(72) / bp_h(t). Speed = |P72 - P71| x 24.
- Result: 1.07 to 1.16 m/s across fit windows (66-78, 64-79, 68-76) and H_eff of 2.2 or 2.1 m. Lateral part about
  0.95 m/s, radial part about 0.58 m/s.

## Second route (plane.py)
I fitted a plane to the pelvis 3D track over the whole clip, using bbox-height depths, and re-derived each depth by
intersecting the pixel ray with that plane. The speed at f72 comes out at 1.05 to 1.13 m/s, with a mean over f68-76
of 1.10 to 1.18 m/s. This agrees with the first route.

## Answer
**1.11 m/s.** Confidence is moderate. The main uncertainty is the depth rate (pose against scale), and the true
per-frame root speed also wobbles with the gait.
