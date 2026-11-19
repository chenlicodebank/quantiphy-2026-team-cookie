# q_2282 – soccer ball diameter (cm)

Lab video, 1280x720, 24 fps (the file and the question use the same rate). The depth_info gives the ball at t = 1.5 s, which is frame 36: D = 1.402 m.
Method card: f = 0.5959 x 1280 = 763 px, and diameter = D x pixel diameter / f.
The gravity prior does not affect the size.

## Pixel diameter near frame 36
- Frame 36 is just after the large 35→36 image step (93 px) and is strongly motion-blurred.
  - Measured across the motion, its extent is only about 84 px. Blur lowers the edge contrast where the chord is short, so this value is biased low.
  - Measured along the motion, it is about 110–116 px, which includes the blur.
  - So frame 36 cannot be measured directly.
- Frames 37–39 have mild blur. Extent across the motion, at half-maximum of |frame − median background| with the outermost crossings (`perp_size.py`, `vprof.py`):
  - 37: 98.7 (motion is horizontal, so this is the vertical extent)
  - 38: 96.6
  - 39: 92.8
- The ball recedes, so its apparent size shrinks about 2–3 % per frame. Extrapolating back to frame 36 gives about 100–102 px.
- `cropsheet.py` (`frames/cropsheet.png`) is a visual check: a 96 px reference circle roughly fits frames 36–40.
- Adopted value: 100 px (±4).

## Result
1.402 x 100 / 763 = 0.184 m, so the answer is **18.4 cm**.
- Using frame 37 alone (98.7 px at roughly the same depth) gives 18.1 cm.
- A real size-3 football is 18.5–19 cm across, which agrees.

## Caveats
- The ball is about 24° off the camera axis. A strict pinhole sphere model, with D as the Euclidean distance, would multiply the result by cos θ ≈ 0.92, giving about 16.9 cm. This answer follows the method card instead (no off-axis factor).
- The size record in `scene/` (89 px tall at frame 36, shrinking to about 85 px by frame 41) is too small: its masks dropped the blurred black panels at the edges.

Confidence: moderate (about ±5–8 %).
