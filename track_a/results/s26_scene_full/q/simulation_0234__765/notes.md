# Q765 – acceleration of the basketball at t = 0.5 s (frame 12)

- 2D simulation, static camera, fps 24 (the file and the question agree). t = 0.5 s is frame 12, during the free fall (frames 0-23; the bounce is at frame 24).
- Scale from the prior: ball diameter 0.282 m. The ball diameter in pixels is 74.8 px (circle fit to the HSV mask contour, mean over frames 0-22). The mask width is 74.6 px and the record's circle fit is 74.75 px. The mask height of 76.2 px includes slight vertical motion blur, so I did not use it. That gives 0.003770 m/px.
- The fall is uniformly accelerated, so the acceleration is the constant from a quadratic fit of the centre y over frames 0-22:
  - my own HSV mask (meas.py): 2.051 m/s² (circle-fit centre) and 2.050 m/s² (centroid);
  - scene record track (acc.py): 2.056 (frames 0-22), 2.048 (0-19) and 2.035 (local window 6-18).
- Convention route (one-frame differences of speed at frame 12): 2.21 m/s². Frames 11-13 average 2.28. Frames 9-15 give 0.7 to 3.0, which is pixel noise from double differencing. The underlying value is the constant from the fit.
- The diameter choice (74.6-75.8 px) moves the answer by about ±1 %.
- Answer: **2.05 m/s²**. Confidence: high, about ±3 %.
- The ascent fit gives about 1.89, about 8 % lower. It does not apply, because frame 12 is in the descent.
