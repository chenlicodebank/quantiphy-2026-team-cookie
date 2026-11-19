# q_2885: speed of the white ball at 1.0 s (frame 24, question_fps 24 = file fps)

**Answer: 2.22 m/s**

## Identification
- The white ball is the record's `grey_object`, a light-grey/white tennis-sized ball.
- The "green ball" is the record's `yellow_object`, a tennis ball.
- Both are thrown up and to the right from the left edge, and both are motion-blurred during frames 18–29.

## Scale and depth
- Lab camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360).
- At frame 24 the white ball is 1.235 m away (depth_info).
- I measured the width across the motion direction myself (`sizes2.py`): background difference, colour mask, then the median chord perpendicular to the blob's major axis. This width is not affected by blur along the motion.
  - White ball at frame 24: 41.5 px → diameter 6.7 cm.
  - Green ball at frame 24: 38.0 px at its given depth of 1.331 m → 6.6 cm.
  - Both are tennis-ball sizes, so the depths and the widths agree.
- Both balls shrink quickly after frame 24 (white 41.5 → about 34 px by frame 27), so they move away from the camera fast. Depth makes up a large share of the speed.

## Route 1: depth from apparent size (`sizeroute.py`), chosen
- Depth R(t) ∝ 1/width, using a linear fit of 1/w over the window, anchored at R(24) = 1.235 m.
- The 3D centre is the ray through the track centre scaled to length R.
- Velocity is the mean of the forward differences, or a linear fit, over a 5–9 frame window around frame 24.
- White ball: 2.12–2.28 m/s (windows 20–28 … 22–26). Example: V ≈ (0.80, −1.25, 1.65) m/s, |V| ≈ 2.25.
- **Prior check** with the same method on the orange basketball at frame 12, depth 2.24 m: 2.06–2.20 m/s against the prior of 2.21. That reproduces it within 0–7 %, slightly low.

## Route 2: ballistic fits (`fit2.py`, `joint.py`)
- Projectile fits to the pixel track with a free gravity vector, plus optionally the size data.
- White ball: 1.89–2.23 m/s.
  - Using pixel positions alone gives 1.9. The depth rate is then poorly constrained, and the size data rejects that fit: it predicts too little shrinking.
  - Weighting the sizes more moves the result up to 2.1–2.2.
- The same fits applied to the basketball reproduce its prior badly (1.8 m/s, and a non-physical g). So route 1 is preferred.

## Final value
- 2.22 m/s: the route-1 central value (about 2.2–2.25), allowing for that method's slight underestimate on the prior.
- Confidence: moderate, about ±8 %. The depth rate comes from size change and is the main uncertainty.

## Caveats
- The orange ball's given depth at 1.0 s (1.81 m) contradicts its apparent size, which implies about 2.8 m because the ball shrinks from 75.8 to 60.4 px. That value was not used.
- One source frame is missing between frames 35 and 36 (from the record). It is handled in the fits and lies outside the frame-24 windows.
