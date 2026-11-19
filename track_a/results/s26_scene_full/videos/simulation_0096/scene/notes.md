# simulation_0096 — measurement record (pixels, seconds)

2D simulation, 41 frames at 24 fps (t = frame/24), 1920x1080. Static camera, plain uniform grey background,
no ground/horizon/props. Two moving objects, both in side view:

- **plane** — white Air China airliner (red phoenix tail logo), upper half (y 284-510). Moves RIGHT at constant
  ~50.5 px/frame, constant y. Fully visible frames 0-10, cut by the right edge in frames 11-25, gone from frame 26.
  Full size: length (stabiliser tip to nose) 750.5 px (749-753), height (fin top to engine bottom) 226.8 px.
- **car** — silver Cybertruck-style pickup, y 585-622 under the plane. Starts at rest and drives LEFT with steadily
  increasing speed (per-frame steps 0,1,1,2,2,2,3,... up to ~14 px/frame at frame 40). Visible in all 41 frames,
  never occluded. Length 113.5 px (113-114 while slow; 115-117 late, motion blur), height ~36.5 px (35/38 jitter).
- Frames 0 and 1 are identical for both objects; the first motion is between frames 1 and 2.

## Files
- `scene.json` — inventory, sizes, reference-point definitions, events, camera.
- `tracks/plane.csv`, `tracks/car.csv` — per frame: t, ref_x/ref_y (reference point), ref_method, bbox
  (x0,y0,x1,y1 inclusive), visible length/height, mask area and centroid, truncated_by_frame_edge, occluded.
- `scripts/measure.py` — segmentation: |frame − background| > 18 (max over RGB), open/close, connected components;
  background = frame 40 with the car area patched from frame 0. `scripts/raw_rows.json` its raw output.
  `scripts/tracks.py` — writes the CSVs and an overlay check image (frames/overlay.png, inspected: boxes hit the full
  objects).

## Reference points and reliability
- Car: bbox centre. x is reliable to ~±0.5 px (both bumpers clear); the y centre jitters by 1.5 px (roof edge
  threshold), the bottom edge y1 = 622 is constant — the car moves purely horizontally.
- Plane: bbox centre in frames 0-10 (x ±0.5 px). In frames 11-25 the nose is out of frame, so ref_x = tail edge x0 +
  374.77 px (half-length measured in frames 0-10) and ref_y = 397.09 (constant); this assumes the rigid plane keeps
  its shape, which the constant 50-51 px/frame steps of x0 confirm. Visible length/height in those frames are
  truncated values, not object sizes. The plane's origin is assumed at its bbox centre (Blender origin unknown);
  for speed questions the choice does not matter since it is a pure translation.
- No perspective; one metres-per-pixel scale applies to both objects (their pixel length ratio 6.6 matches an
  A320/Cybertruck ratio, so they look rendered at the same depth).
- Ambiguities: none between objects (only two, very different). Faint wisp just behind the plane's tail cone is
  ignored (below threshold, present in all frames). No shadows.
