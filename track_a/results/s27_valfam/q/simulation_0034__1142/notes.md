# q1142 — average speed of the person (m/s)

question_fps = file fps = 24, so frame numbers and times match.

Method (measure.py):
- The person walks right at a constant camera distance (depth 92.186 m at t=1 s, 92.196 m at t=2 s), so the motion is
  across the line of sight and one metres-per-pixel scale works.
- Pixel height: the scene track's bbox height has a median of 67 px (90th percentile 69). My own median-background mask
  (threshold 30) gives 69 px (range 68-71). The walking height is a little under the 1.75 m rest height, so I took
  ~68.5 px for 1.75 m: 0.0255 m/px, which means f ≈ 68.5·92.19/1.75 ≈ 3610 px.
- Pixel speed: a linear fit of the track's pelvis point gives 47.9 px/s. My own mask-centroid fit gives 48.1 px/s.
  The mean per-frame |dx| is 47.8 px/s. The raw 2D per-frame mean, 53 px/s, is inflated by noise in the y estimate.
- Speed ≈ 48.0 px/s × 0.0255 m/px ≈ 1.23 m/s. The true pelvis also bobs and sways a little, which adds about 1 %.
  Answer: 1.24 m/s.
- Second route: the per-second segments (48.3, 47.9, 48.5 px/s) agree. If the height were 67 px the answer would be
  1.25 m/s; at 70 px it would be 1.20 m/s.

Confidence: moderate-high (±4 %).
