# q1782 – width of the white car (m)

2D top-down simulation, 24 fps (file fps = question_fps, no retiming). White car = scene's `white_van` (straight up, uniformly accelerating).

## Scale from prior (a = 4 m/s^2)
measure.py: quadratic fit of the van centroid y(frame) from scene/tracks/white_van.csv.
- frames 0-71: 0.2792 px/frame^2 = 160.8 px/s^2 (rms residual 0.42 px)
- windows 5-71 / 10-60 / 0-35 / 36-71: 160.9 / 160.3 / 160.9 / 161.6 px/s^2
- bbox top / bottom edges: 161.9 / 159.0 px/s^2
=> 160.8 px/s^2, scale = 4 / 160.8 = 0.02487 m/px.

## Width (horizontal extent across the van, x direction)
width.py: darkness profiles across the body (several rows, frames 12/24/36/48). The left body edge is a sharp step at x≈787.5,
and the right edge is at x≈875–876 (half-contrast). Width ≈ 87.5–88.8 px, taken as 88 px. The mask/rotated rectangle in scene/
gives 91 px because it includes the faint 1–3 px soft shadow/anti-alias fringe (values 3–5 out of 255).
Width = 88 × 0.02487 = 2.19 m (using 91 px instead would give 2.26 m).

Check: length 240 px → 5.97 m; length/width = 2.73, which fits a minivan. The acceleration is consistent across independent frame windows.
Confidence: moderate-high (±3%).
