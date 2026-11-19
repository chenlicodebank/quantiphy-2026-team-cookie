# q37 – length of the white car (simulation_0068)

2D top-down Blender scene, 24 fps (file fps = question_fps = 24, no re-timing issue). The "white car" is the white
van/minibus driving straight north (up) in the west lane, x ≈ 831 px; it accelerates from rest all clip.
Prior: its acceleration = 4 m/s² → one metres-per-pixel scale from its pixel acceleration.

## Pixel acceleration (quadratic fits of y(t), frames 4-71 and sub-windows)
- tmpl.py: template match of the frame-0 van patch, subpixel peak: a = 164.8 px/s² (rms 0.14 px; windows 4-40: 164.3, 20-60: 164.3, 40-71: 166.7).
- edges.py: subpixel top/bottom edges of the white roof region: a = 165.0-165.4 px/s² (rms 0.15-0.25 px).
- scene record tracks (min-area rect / bbox of colour mask): 157-163 px/s², noisier (rms 0.3-0.7, window-dependent) → not used.
- Adopted a = 165 px/s² → scale = 4 / 165 = 0.02424 m/px. Per-frame steps grow linearly (0.69 → 20.4 px), i.e. constant acceleration confirmed.

## Pixel length (frame 0, at rest, no blur)
- Full extent, front bumper outer edge (y ≈ 801, grey bumper visible on 5x crop) to rear edge (y ≈ 1046.5): ≈ 246 px
  (background-difference mask length 247 px agrees).
- White painted body only (excluding grey front bumper): 234 px.
- Bounding-box length includes the bumper → 246 px.

## Answer
L = 246 px × 0.02424 m/px = 5.96 m → 5.95 m.
(Body-only reading: 234 px → 5.67 m; with the scene-record acceleration 160 px/s² it would be 6.15 m.)
Confidence: moderate-high; main uncertainty the bumper edge (±2 px, ~1%) and acceleration (±1%).
