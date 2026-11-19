# Q529: speed of the droplet at t = 0.05 s

- 2D video, 60 fps (file and question_fps agree). t = 0.05 s -> frame 3. Speed = |p3 - p2| x fps.
- Scale comes from the prior a = 9.7 m/s^2 and the drop's pixel acceleration.
- `measure.py` re-measures the drop: background subtraction against frame 13, then the sharp top tip and the centroid
  of the top 45 rows, frames 0-11. I fitted a quadratic to frames 2-11 (frames 0-1 sit next to the pipette).
  - Tip: a = 28.83 px/frame^2, p3 - p2 = 74.0 px (fit gives 74.5).
  - Top-45 centroid: a = 28.81 px/frame^2, p3 - p2 = 74.3 px (fit gives 74.6).
  - The scene record's centre track gives the same: 73.5 px, a of about 29.
- Speed = (dy / a_px) x 9.7 / 60 = 0.415-0.419 m/s. Second route: a drop falling from rest at about frame 0
  (the fit puts the rest time at frame -0.09) has v = a x 2.5/60 = 0.404-0.41 m/s, which agrees.
- Answer: 0.417 m/s. Confidence: high (about 2%).
