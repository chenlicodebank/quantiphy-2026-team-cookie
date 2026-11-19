# Q51: distance between the white car and the bicycle at 2.0 s

- 2D top-down scene with a static camera, 24 fps (question_fps is also 24). t = 2.0 s is frame 48.
- Scale comes from the prior (bicycle speed 5.33 m/s). The cyclist moves at a constant speed from frame 1→2 onward.
  A linear fit of cy over frames 2–71 gives 8.916 px/frame = 213.98 px/s (rms 0.45 px), so the scale is
  0.024909 m/px.
- Positions at frame 48 come from the scene/tracks centroids. I re-checked them on a zoomed frame
  (frames/f48.png): the van spans y ≈ 470–708 with its centre near 589, at x ≈ 833. The bike spans y ≈ 375–440
  with its centre near 409, at x ≈ 917.
  - Smoothed: van y from a quadratic fit = 590.3, bike y from a linear fit = 409.5, dx = 84.6, giving 199.7 px.
  - Raw centroids at frame 48: 200.4 px.
- Distance: 199.7 px × 0.024909 = **4.97 m**. The raw-centroid route gives 4.99 m. As a sanity check, the bike is
  64 px long, which is 1.6 m.
- Confidence: high. The main uncertainties are where each origin sits relative to its mask centroid (±1–2 px,
  under 1%) and the scale (under 0.5%).
