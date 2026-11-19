# Q85: speed of the bike at 0.5 s (m/s)

- The video is 24 fps and question_fps is also 24, so t = 0.5 s is frame 12. The scene is a top-down 2D scene, so one metres-per-pixel scale comes from the prior (bike length = 1.7 m).
- I re-measured the bike in `measure.py`, using an HSV cyan mask in the bike band. The overlay `frames/ov12.png` shows the mask runs from the front wheel tip to the rear rack.
  - Bike pixel length at frame 12: 381 px (376–386 over frames 2–28, matching the record). Scale = 1.7/381 = 0.004462 m/px.
  - Bike bbox centre: x 1710.5 at frame 2 and 477.5 at frame 28, a constant −47.42 px/frame. The per-frame steps of 46–48 px are pixel quantisation.
  - Around frame 12: the step from frame 11 to 12 is 46.5 px (front tip 46, rear 47). The mean step over frames 10–14 is 47.5 px.
- Speed = 47.42 × 24 × 0.004462 = **5.08 m/s**. The raw single-frame step gives 4.98, and the frames 10–14 window gives 5.09. The motion is constant (Blender linear motion), so I answer **5.07**.
- Second route: the front-tip step alone (−47.23 px/frame) and the rear-tip step alone (−47.62 px/frame) give 5.06 and 5.10 m/s. Grey-level SSD on the whole band gives 49 px/frame, but that band includes the raised rider, who shows about 4% parallax, so I rejected it for the ground-level bike.
- Confidence: high, within about 2–3%.
