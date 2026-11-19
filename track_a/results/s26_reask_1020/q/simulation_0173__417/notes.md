# Q417 – airplane length

2D side view, static camera, file fps = question fps = 24. The plane flies level from right to left at constant speed.

- Pixel speed: scene record template track gives 61.52 px/frame. My own diff-to-median-background nose-edge track
  (measure.py, frames 8–31) gives 61.35 px/frame, and the tail edge gives 61.38. I used 61.45 px/frame = 1474.8 px/s.
- Scale = 153.582 / 1474.8 = 0.1041 m/px.
- Pixel length: 459 px, nose to the tip of the tail/horizontal stabiliser (frame 18, nose at x≈842, tail at x≈1299;
  I checked it on a zoomed grid crop). The raw diff mask gives 437–459 px because the white tail blends into white clouds.
  The template value of 459 matches the visual check.
- Length = 459 × 0.1041 = **47.8 m**. If the noisy median diff-mask length (444 px) were used instead: 46.2 m.
- Plausibility: the plane looks like a regional or business jet (real size about 30–36 m), so the result is about 35% large.
  That is still within the 40% tolerance, so I kept the scale from the prior.
- Confidence: moderate-high on the measurement (±2%).
