# Q331 – total length of the bird's flight path (m)

Prior: speed of the bird = 9.146 m/s. 2D simulation, 60 fps (file and question_fps agree), 100 frames (0–99).

## Method
- Used scene/tracks/bird.csv (eroded-mask centroid of the bird, checked in the record on crops). `measure.py`
  recomputes the per-frame pixel displacements and a polynomial-smoothed path (frames 17–99, after the sun/edge frames).
- Pixel speed is almost constant along the arc: mean per-frame displacement 20.1 px (frames 4–40), 19.6 (40–70),
  19.7 (70–99); smoothed speed 19.46–19.95 px/frame (within about ±1.3 %). So the bird flies at constant speed and
  the prior speed holds over the whole clip.
- Scale: 9.146 m/s / (19.68 px/frame × 60) = 0.00774 m/px.
- Path length = sum of the per-frame displacements over the 99 frame intervals (frames 0→99; the bird moves in
  every frame, entering from the left edge at frame 1):
  9.146 × 99 / 60 = **15.09 m**.

## Second route
- Measured pixel path (smoothed speed 19.68 px/frame × 99 intervals) × 0.00774 m/px also gives 15.09 m. Since the scale
  comes from the same speed, this mostly confirms that the speed is constant (no speeding up or slowing down along the
  arc), so speed × time is valid.
- If only the visible frames 1–99 counted (98 intervals): 14.94 m (−1 %).

Confidence: high (about ±2 %).
