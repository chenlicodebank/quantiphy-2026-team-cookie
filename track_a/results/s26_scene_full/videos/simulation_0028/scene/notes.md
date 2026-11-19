# simulation_0028 – measurement record

3D Blender render, 960x960 px, 25 fps, 75 frames (t = frame/25). Static camera on a high oblique aerial view: pink sand
beach, a big white rock plateau with brown cliffs (top centre/right), and green sea (lower ~45%). No horizon or sky.

## Files
- `scene.json`: inventory (bird, bird_shadow, rock_plateau, sand_beach, sea), camera, events, pixel extents.
- `tracks/bird.csv`: the bird, frames 0–54. Columns: frame, t, cx, cy (centroid of the dark mask; this stands in for
  the bird's origin), bbox x0/y0/x1/y1/w/h, area_px, axis_len/axis_wid (PCA main-axis extent of the mask and the
  extent across it), axis_angle_deg (0 = image +x, measured clockwise because y points down), and the flags occluded,
  edge_clipped and low_contrast.
- `tracks/bird_shadow.csv`: the bird's shadow on the sand, frames 0–33, same columns.
- `scripts/`: `bg.py` builds the median background and checks for camera shift. `detect.py` lists the blobs.
  `track.py` does the tracking and writes `frames/raw_tracks.json`. `finalize.py` writes the CSVs, applies the flags
  and measures the static objects. `overlay.py` and `show.py` are for checking.

## Method
- Background is the per-pixel median of every 3rd frame. The mask is every pixel more than 60 (sum over RGB) darker
  than the background, closed with a 3x3 kernel. The tracker takes the nearest connected component and adds fragments
  within 12 px.
- I drew the overlays on frames and looked at them. Both tracks hit the right object and its full visible extent.
- Camera: phase correlation on the rock region gives a shift under 0.03 px over the whole clip, so the camera is static.

## Reliability and ambiguities
- **Only one animal.** The grey-blue winged shape about 300 px right of and 130–145 px below the bird is its **shadow**
  on the sand, not a second bird. Its length grows and shrinks in step with the wing beats. It disappears at f34 near
  the beach edge (≈(900,393)).
- Bird centroid: good to about ±1–2 px on sand (f0–36 and f46–51). It is a flapping bird, so the mask centroid moves a
  few px with wing phase compared with the true body/pelvis origin. Over the dark brown cliffs (f37–45,
  low_contrast=1) the mask can be incomplete or merge with rock, so expect ±3–5 px there. At f52–54 the bird is partly
  past the right edge (edge_clipped=1): sizes and centroid there are biased, and f52's bbox is inflated.
- Bird apparent size depends on wing phase: bbox_h 19–40 px, bbox_w 25–43 px. Maxima at the same wing phase (≈37,
  40, 39 px at f0, f25, f50) show no trend, so the bird's camera depth is roughly constant along its path. For a
  wingspan or size question, use the largest extent over a flap cycle (axis_len up to ~43 px in clean frames).
  Shadow axis_len reaches ~57–60 px with wings spread.
- Path: the bird moves left to right at a steady ≈16.9 px/frame in the image (x 59 → 952 over f0–53), with a small
  image-y undulation (223 → 250 → 233 → 261 → 248).
- Static extents are from the median background and the gridded frame 72. They are approximate (±5 px) because the
  rock and beach edges are soft. Rock plateau: x 328–950, y 25–310 (622 × 285 px); it runs to the right edge.
- No depth or focal information is in the video. Answering sessions must get the scale from their prior or depth_info.
