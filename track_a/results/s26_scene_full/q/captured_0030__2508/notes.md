# Q2508 — red ball velocity at t=0.2 s (cm/s)

Lab video at 24 fps (the file and question_fps match), so t = 0.2 s is frame 5. Focal length f = 0.5959·1280 = 763 px, principal point (640, 360).
Prior: the ball is 7 cm across. depth_info gives distances at frames 5, 10, 14 and 19 (0.8715, 1.166, 1.372 and 1.315 m).

## What happens
Around frame 5 the ball reaches the left end of its loop over the table. Its image motion slows (u steps 38 → 27 → 12 px/frame) as it turns
to move away from the camera. So most of the speed at frame 5 is change in depth, and the answer depends on how the depth changes from frame to frame.

## Method
- `diam.py`: I measured the ball diameter myself as the half-maximum width of a redness profile (R − (G+B)/2), vertical and horizontal,
  through the refined centre, for frames 0–22. On the sharp frames 6–10 this is much tighter than the scene/ mask: the mask was inflated by
  blur, e.g. 64 vs 57 px at frame 6.
- Check against the given distances: a 7 cm ball with these widths (√(v·h)) reproduces the given distance to within 1.8% at frame 5 and
  0.5% at frame 10. At frames 14 and 19 the error is about 5% (small far-side images).
- Per-frame depth: Z = f·0.07/d_px. I tried this as is, anchored to the frame 5 distance, and with a linear scale anchored at both frames 5
  and 10. Each 3D centre is the back-projection ((u−cx)/f, (v−cy)/f, 1)·Z.
- Speed: one-frame forward differences of the 3D centre. I smoothed it over 5 frames in three ways: the mean of the forward-difference speeds
  over frames 3–7, a forward difference after a 5-frame moving average of position, and a central difference P7−P3.
- Results (`measure4.py`): 134–161 cm/s across the diameter choices and smoothings. The cluster is about 140–150, and the depth rate is about
  +1.3 m/s.

## Second routes
- `measure.py`: depth interpolated linearly between the given values, with the start extrapolated from the ball's size: 122–150 cm/s.
- `measure2.py`: ball on a plane fitted to the 4 given distances: 154–190 cm/s. The fit is poor (residuals up to 7 cm), so I gave it less weight.
- `measure3.py`: a polynomial depth curve fitted to the scene/ mask sizes: 80–145 cm/s. The mask diameters are inflated by blur, so this
  route is less reliable.
- Sanity check: on the near side the image speed is about 65 px/frame at about 0.83 m depth, which is about 160 cm/s. That fits a loop
  swung at a roughly constant ~150 cm/s.

## Answer
**145 cm/s**. Confidence: moderate, about ±10–15%. The main uncertainty is how fast the depth changes at the turn.
