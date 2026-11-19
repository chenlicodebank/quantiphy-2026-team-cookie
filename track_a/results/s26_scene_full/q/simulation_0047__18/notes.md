# Q18: speed of moving bicycle at t = 1.0 s (frame 33), fps 33 (file = question fps)

Scene: 2D top-down render with a static camera. The walking person (upper sidewalk) and the cyclist (road) are both on the ground plane, so one m/px scale comes from the prior.

Prior: walking person's speed = 1.236 m/s, read as the person's average speed. Their per-frame speed oscillates with the gait (2.6–4.0 px/frame).
- Scene record: mean step 3.350 px/frame; net displacement over f0–98 gives 3.333 px/frame.
- My own template tracking (measure.py, templates from f33 and f60): mean step 3.355 / 3.358, net 3.332 / 3.344, f3–71 (4 steps) 3.32–3.34.
- Adopted value: 3.34 px/frame, so the scale is 1.236 / (3.34 × 33) = 0.01121 m/px.

Cyclist: moves uniformly with no acceleration.
- Scene record linear fit (f14–98): 12.85 px/frame.
- My own template track (f20–49): fit 12.81 px/frame; the step at f33 is 12.94 (per-frame jitter ±0.2).
- Adopted value: 12.83 px/frame, i.e. 423 px/s.

Speed = 1.236 × 12.83 / 3.34 = 4.75 m/s. The range is 4.73–4.76 depending on which pedestrian average is used.

Second route: independent re-tracking agrees with the scene record within 0.5 %.

Caveats: the tracked points are head/torso proxies, not the exact origins. Both are elevated by a similar amount, so the perspective effect largely cancels. If the prior were an instantaneous gait speed rather than an average, the answer could be off by about 10 %.

Confidence: good (about ±3 %).
