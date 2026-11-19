# Q1196: diameter of the moving bicycle's wheel. Answer: 0.59 m

The file and question_fps are both 33 fps. The bike is head-on to the camera for the whole clip, so its wheel is seen
edge-on. The wheel's vertical image extent equals D·f/R; this holds for orthographic projection of a circle whose plane
contains the line of sight.

## Depth consistency check (important)
- Given: bike at 16.49 m (t=1) and 11.93 m (t=2); human at 11.93 m (t=1) and 10.82 m (t=2).
- Assume the walker really is at 11.93 m, so f = 198 px · 11.93 / 1.8 ≈ 1310. The cyclist (229 px at 16.49 m) would
  then be 2.9 m tall, and the wheel about 1.1 m across. That is implausible.
- The image ordering also disagrees: the bike's ground contact (y=559) sits below the walker's feet (y≈445), so the bike
  is nearer than the walker, not 4.5 m farther away.
- The walker's growth in apparent size, at its given rate of 1.1 m/s, puts its body at about 17 m.
- Conclusion: the walker's distance values belong to an origin that is offset from its body. I did not use them as
  absolute depths. The bike's distances are consistent with its size growth: 1/h slope 1.28e-3/s against the 1.21e-3/s
  implied by the depths.

## Camera model (scripts: vvp.py, groundcal2.py)
- Vertical vanishing point from 73 LSD line segments (kiosk, building, sign edges): (948, 7875). This gives roll ≈ 0
  and pitch = atan(f / 7492).
- Ground-plane model with pitch θ and focal length f. The camera height comes from the walker's measured head-top and
  foot rows with H = 1.8 m.
- Best consistent solution: f ≈ 2050 px, θ ≈ 13°, camera height ≈ 4.8 m. It reproduces the following:
  - bike contact distance at t=1: 16.50 m (given 16.49);
  - bike distance rate: 4.62 m/s (given 4.56);
  - walker distance rate: 1.21 m/s (given 1.11);
  - cyclist head-top height: 1.78 m (plausible).

## Wheel pixel extent (bluelight.py, montage.py, profile.py)
- The front tire is a dark vertical line running from ground contact up to the fork crown, where a blue front light
  sits. The tire's top is taken at the bottom of the blue light.
- Measured for frames 40–60: D_px = contact − blue-light bottom = 77 → 97 px, about 0.32 × the cyclist's head-to-contact
  height.
- The fork-leg end (hub) sits about 45 px above contact at f49–f56, consistent with D_px ≈ 90 there.

## Metric conversion, two routes
1. **Single-view metrology** relative to the walker (1.8 m) on the ground-plane model: D = 0.585 m, sd 0.009 over 21
   frames. This is nearly independent of f: 0.584–0.606 for f = 1900–2200 and θ = 12.5–15°.
2. **Pinhole**: D = D_px · R / f, with R = the bike's given distance (linearly interpolated) minus 0.5 m to the front
   axle, and f = 2050. This gives D = 0.584 m. The result is sensitive to f: 0.63 at f=1900, 0.55 at f=2200.

At the self-consistent calibration both routes agree at 0.584.

## Answer and uncertainty
The answer is about 0.59 m. I rounded up slightly because the extreme top of the projected tire may hide behind the
light. Uncertainty is about ±7%. The main error sources are the exact tire-top row and walking height versus standing
height.
