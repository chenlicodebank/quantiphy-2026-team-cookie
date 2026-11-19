# q_343: speed of the train at t = 1 s (m/s)

Prior: side window width (not the door windows) = 1.8 m. depth_info: none. question_fps = file fps = 24, so t = 1 s is frame 24.

## The catch
The train is visible only in frames 2-20 and has left the view by frame 21. So the speed at frame 24 has to be
extrapolated. Within the visible span it accelerates steadily (no stops or impacts), so I used a linear fit.

## Measurements (all done in code, scripts in this folder)
- `winedges.py`: glass width of each fully visible big side window (near layer), using half-level edges of the
  row profile at y 560-680. The values were 346.8 (f6), 346.2 (f8), 349.3 (f9), 348.2 (f11), 352.9 (f12), 351.6 (f14), 353.8 (f15) and
  353.3 (f17) px. `winheight.py`: the glass height grows the same way, from 278 to 283 px (+1.8%, against +2.0% for the width).
  So the train approaches the camera slightly and the pixel scale grows about 0.72 px of window width per frame.
  The growth is not motion blur, because half-level edges are unaffected by blur.
- SAM 3 "train window" masks: f8 is 348 px wide (mine 346.2, 0.5% apart) and f17 is 356 px (mine 353.3, 0.9% apart). Both are within 3%,
  and the overlay outlines the glass correctly.
- `shift.py`: per-frame near-layer shift from NCC of x-gradient profiles in three bands. Frames 7-18 agree with the scene
  record to within 0.5 px (for example 355.7, 359.7, 363.7 ... 391.0). Frames 3-6, 19 and 20 lock onto a spurious 379-380 px value and were
  not used (I used the record's 353.4 for f6). Linear fit d(i) = 333.98 + 3.192 i, rms 0.7 px.
- The shifts and the window are both on the train's near side, so their ratio is scale-free. Speed v(i) = d(i)/w(i) x 1.8 m x 24.

## Result (`speed.py`)
- Route A: extrapolate d and w separately to frame 24 (d = 410.6, w = 359.2), giving v = 49.38 m/s.
- Route B: per-frame speeds 44.1 m/s (f6) up to 47.6 m/s (f18), linear fit (about 7.2 m/s^2), extrapolated to frame 24, giving 49.45 m/s.
- Check: the direct per-frame ratios at frames with measured windows (44.0 to 47.4 m/s) follow the same line.
- If the scale growth is ignored (constant mean width of 350.3 px), the result is 50.6 m/s, so that is a 2.5% sensitivity.
- Answer: **49.4 m/s**.

## Confidence
Moderate to good. The main uncertainties are these:
- Whether the 1.8 m width means the glass opening (used here) or the glass plus its dark rim, which would be 2-4% wider in pixels and give a lower speed.
- The 6-frame extrapolation beyond the last visible frame (±1%).
