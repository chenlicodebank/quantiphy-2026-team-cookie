# Q80 – walker speed at 0.5 s (simulation_0080)

- 2D top-down Blender render, 24 fps (file fps = question_fps = 24), static camera. t = 0.5 s -> frame 12.
- Scale from prior: bike length 1.7 m. Re-measured cyan bike x-extent in code (measure.py): 378 px (frames 0, 5),
  380 (frame 10); scene record also 378. -> 1.7/378 = 0.004497 m/px.
- Walker reference point: torso (shirt) – my own bright-shirt mask (walker.py), bbox centre and centroid, plus the
  record's pelvis_x (shirt bbox centre).
  Step 11->12: record 13.0 px, my bbox 14.0, my centroid 13.35. Steps 10..13 average ≈ 13.2 px/frame;
  whole-clip average (frames 2–28) ≈ 12.9–13.0 px/frame, so motion is near uniform.
- Speed = 13.2 px/frame x 24 x 0.004497 = 1.42 m/s (plausible walking speed).
- Second route: whole-clip mean 348 px / 27 frames = 12.89 px/frame -> 1.39 m/s; agrees within 2.5 %.
- Confidence: good (±4 %); main uncertainty is the per-frame pelvis proxy jitter (±1 px/frame).
