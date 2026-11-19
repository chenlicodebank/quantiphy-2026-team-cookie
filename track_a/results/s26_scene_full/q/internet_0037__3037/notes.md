# q_3037 — average speed of the swimming woman, 2.07–5.20 s

**Answer: 0.40 m/s**

## Time base
The file is 22.52 fps, but the question gives 24 fps. 22.52 is not a native drone rate (drones record at 23.976, 24, 25 or 30), so the clip was probably re-timed when it was cut. Both rates give a plausible slow breaststroke (a ~2 s cycle, 0.37–0.40 m/s), so physics cannot pick between them. I used question_fps = 24 because the reference answers follow the original footage. That gives t = 2.07 s → frame 50 and t = 5.20 s → frame 125 (75 frames).

## Scale (from the prior)
The prior is height = 1.63 m. I took the pixel height as head top to toes in stretched glide frames, read on gridded crops (`view.py`, `frames/`):
- f123: about 1720 → 2447, so ~727 px
- f125: about 1749 → 2453, so ~704 px
- f29: about 1020 → 1713–1753, so ~700–730 px

The scene record gives 690–730 px for glide frames. I used H = 720 px, so the scale is 1.63 / 720 = 2.264 mm/px. One planar scale, as in the internet-video convention.

## Motion
I used the scene/ tracks, which are corrected for camera drift (the drift is small, ~1.5% of the travel). I checked the positions at f50 and f125 on the crops. `speed.py` computes the speed for each reference point:

| Point | Displacement f50→f125 | Speed | Linear-fit slope | Speed from fit |
|---|---|---|---|---|
| head (hair) | 583 px | 0.42 m/s | 7.27 px/f | 0.395 m/s |
| trunk | 538 px | 0.39 m/s | 7.23 px/f | 0.393 m/s |
| head front | 551 px | 0.40 m/s | 7.23 px/f | 0.393 m/s |
| mask centroid | 553 px | 0.40 m/s | — | — |
| toes | 505 px | 0.37 m/s | — | — |

The endpoint values differ between points because each sits at a different phase of the stroke. The window-fit slopes agree at 7.2–7.3 px/frame. The full-clip average is also 7.3–7.4 px/frame, giving 0.40 m/s.

At 7.3 px/f × 24 fps × 2.264 mm/px the speed is ≈ 0.40 m/s.

## Second route and sensitivity
- The full-clip slope, which covers whole stroke cycles, gives 0.40 m/s, the same as the window.
- Using the file's 22.52 fps instead would give ~0.37 m/s (frames 47–117).
- A smaller pixel height (e.g. 680 px) would raise the answer by ~6%.

Confidence: moderate, about ±8%. The fps choice and the reference point are the main uncertainties.
