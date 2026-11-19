# simulation_0143 — measurement record (pixels, seconds)

3D Blender render, 1920x1080, 24 fps, 100 frames (t = frame/24, 0 … 4.125 s). It shows a futuristic corridor
(white arch ribs, a glossy tiled floor, a bright opening at the far end) and **one moving object: a man in black clothes**
who walks away from the camera. His face is a light/white patch. There are no other people, vehicles, balls or props.

## Files
- `scene.json`: inventory, camera, perspective cues, per-object summary, events.
- `tracks/person.csv`: one row for every frame 0–99. Columns: frame, time, bbox_x0/y0/x1/y1 (inclusive px), height_px
  (top of hair to bottom of sole), width_px, area_px, centroid_x/y (mask centroid), pelvis_x_est/pelvis_y_est
  (estimated pelvis = simulation origin), torso_x (mean x of rows 20–45 % of height), feet_x/feet_y (ground contact:
  lowest sole row, mean x of the bottom 6 rows), occluded (always 0), at_edge (always 0).
- `camera_shift.csv`: per-frame global shift against frame 0 (phase correlation of the top 300 rows).
- `bg_median.jpg`: median background.
- `scripts/`: `bg_and_camera.py` (background and camera check), `probe.py` (writes the 80th-percentile background
  `bg80.npz`; `bg80.npy` is an emptied leftover), `track_person.py` (segmentation and track, writes the overlays to `frames/ov_*.png`), `events.py`
  (extremes, reversals, step timing, horizon fit), `vanishing.py` (corridor vanishing point from hand-picked points).

## Method
- **Camera:** static. The largest shift over the whole clip is 0.009 px. No pan, no shake.
- **Person mask:** I subtracted each frame from the 80th-percentile background (diff > 40) and kept the largest
  component. The glossy floor shows a dark reflection under his feet. His body is near black (V < 15), while the
  reflection is grey (V ~ 40–90). So the mask is cut at the row where the run of near-black rows ends below the
  body. A closing step fills in the light face. I checked overlays at frames 0, 5, 10, 20, 30, 32, 40, 50 … 93, 99: the
  contour hugs the full body, including hair, hands and soles, and leaves out the reflection.
- **Pelvis (reference point):** this is an estimate, not seen directly. pelvis_y = bbox_y0 + 0.48·height_px (a
  standing adult's hip joint is ~0.52 H above the floor). pelvis_x = middle of the silhouette at that row. Expect about
  ±5 px error, more during long strides. For depth or ground-plane work, `feet_y` (ground contact) and `torso_x` are
  steadier lateral and depth cues.
- **Extents:** height_px changes with the gait (stride lowers the head). width_px is mostly the stride width in side
  view, or the shoulders and arms when seen from behind. It is not a body dimension.

## Motion (descriptive)
- At frame 0 he is already walking, mid-stride, facing left in profile. He recedes along the corridor the whole time,
  zig-zagging sideways:
  - drifts left until ~frame 34–35 (torso_x ~658–662, t ≈ 1.42 s);
  - turns to drift right until ~frame 74 (torso_x ~812, t ≈ 3.08 s);
  - drifts left again until the end.
- Apparent height: 429 px (f0) → 278 (f50) → ~185–192 (f94–99). So his depth grows about 2.3x, and the decrease is
  steady.
- Ground contact row feet_y: 843 (f0) → 674 (f95).
- Step timing from the silhouette width (approximate): legs apart at ~5, 17, 27, 34, 43, 54, 65, 72, 81, 94; legs
  together at ~0, 11, 25, 30, 38, 48, 63, 69, 76, 85, 99.

## Perspective
- Corridor vanishing point ≈ (954, 532). It is the intersection of two lines through hand-picked points, so allow
  ±10 px:
  - the right pillar bases: y = 0.409x + 141.9;
  - the left floor/wall edge: y = −0.285x + 804.1.
- The person's height fits H = 1.365·(feet_y − 537.8), giving a horizon at row ~538. This agrees with the vanishing
  point, so the camera is about level, with the horizon near the image centre row.
- The focal length is unknown. Get it from depth_info plus a known size, e.g. f ≈ height_px·depth/H_m, with the
  pelvis depth ≈ the body depth. Check it on a second given depth.

## Static objects (frame 99, approximate)
- Right pillar bases (bottom-centre, from near to far), with widths:

  | base point | width |
  |---|---|
  | (1690, 834) | ~140 px |
  | (1435, 728) | ~70 px |
  | (1316, 678) | ~45 px |
  | (1244, 650) | ~35 px |
  | (1190, 630) | ~30 px |
  | (1157, 616) | — |

- The nearest arch rib spans the frame; its right leg is at x ≈ 1600–1760.
- The bright end opening is about x 800–1050, y 440–600.
- Floor tiles have seams converging to the vanishing point.

## Reliability and ambiguities
- Bbox and heights: ±2 px. Feet row: ±3 px. At frames 20–21 there is a 12 px jump while a foot lifts or plants.
- The light face could be mistaken for background, but it is filled in by the closing step.
- The arm sometimes widens the bbox by a few px.
- Nothing occludes the person.
