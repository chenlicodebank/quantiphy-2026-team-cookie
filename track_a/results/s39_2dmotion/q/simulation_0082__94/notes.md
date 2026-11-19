# Q94 – speed of the black-and-white car at t = 1.0 s (m/s)

Prior: yellow car (pickup) length = 5.67 m. 2D top-down render, 24 fps (file rate = question rate). t = 1.0 s → frame 24.
The black-and-white car is the lower truck (white hood/roof rails, black bed). This matches the scene/ record.

## Measurements (my scripts: measure.py, yellow_len.py)
- Yellow length (sub-pixel front/rear edges of a colour/brightness mask, rows 375–430): it shrinks steadily from
  313 px at the right edge (frame 0) to about 304 px near and left of the image centre (frames 54–71). At frame 24 it is 308–310 px.
  Median over the clip is about 308 px.
- White car pixel speed around frame 24: 1D cross-correlation of the column profile (rows 489–590) gives
  15.95–15.99 px/frame for frames 18–30. The box-centre differences for frames 20–28 average 15.88. The front edge moves 15.76 and the
  rear edge 16.00 px/frame (perspective: features at different heights move at slightly different rates). Motion is
  constant from frame 2 onward, pure −x. At frame 24 I take 15.9 px/frame.
- SAM 3 check: the yellow box at f24 is 1174.1–1481.2 (307.1 px; mine 308.1). At f55 it is 824.2–1127.5 (303.3; mine 303.9).
  The white box centre is 1237.95 at f23 and 1222.4 at f24 (mine 1238.6 and 1222.75). All agree to within 1%, so no conflict.
  SAM's own frame-to-frame centre difference (15.55) is noisier than the cross-correlation.

## Scale and answer
Scale = 5.67 m / L_px. Perspective makes L range from 304 px (centre) to 309 px (at the frame-24 position).
I used L = 306 px, the middle of that range.
v = 15.9 px/frame × 24 fps × 5.67 / 306 = 7.07 m/s.
Range of readings: with L = 304 and 15.98 px/frame, 7.15 m/s; with L = 309 and 15.88 px/frame, 6.99 m/s.

## Second route
The same scale gives the yellow car 11.40 px/frame × 24 × 5.67/306 = 5.07 m/s. The white/yellow pixel-rate ratio
is 1.40 on every method, so the result is consistent. The (5, 7) m/s design pair would correspond to L ≈ 309 px.
That is within 1% of my answer.

Confidence: high (±2%).
