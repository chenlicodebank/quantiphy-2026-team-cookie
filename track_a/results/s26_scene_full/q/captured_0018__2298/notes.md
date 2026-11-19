# q_2298 — soccer ball diameter (cm)

File fps = question_fps = 24. Lab video, f = 0.5959 x 1280 = 762.8 px; depth to ball = 2.800 m (depth_info).
The gravity prior isn't needed for a size question.

## Measurement (measure2.py)
Per frame: background subtraction (frame 48 as background for the held frames, frame 0 for the late frames), then
mask, outer contour and a robust least-squares circle fit. In the held frames the lower-left quadrant (the hand) is
left out. The contour runs through boundary-pixel centres, so edge-to-edge diameter = fit + ~1 px.
- Held frames 0–28 (sharp, at rest): fit D = 42.5–43.1 → 43.5–44.1 px
- Frames 40, 46, 47, 48 (after the bounce, little blur): 43.6, 42.5, 41.9, 43.3 → 42.9–44.6 px
- The scene record gives about 44 px (bbox width 45 on frame 0, sharp frames 43–46). This agrees.
Fit circles were drawn on frames 0 and 48 (frames/fit_*.png) and follow the silhouette.

Adopted D_px = 43.8 ± 0.6 px → D = 2.80 x 43.8 / 762.8 = 0.161 m = **16.1 cm** (range 15.8–16.4).

## Second route
The late frames (a different position, background and time) give the same value within 1 px. Their depth may
differ slightly, but the apparent size is constant, which matches the record's note that the depth stays the same.

## Caveats
The ball is about 10° off-axis. A strict sphere-projection correction would make it 1.5–3% smaller (about 15.7 cm).
I followed the method card (depth x px / f) without that correction. 16 cm is small for a soccer ball (a size-1
or mini ball), but the scale comes from depth_info. Confidence: good (±3%).
