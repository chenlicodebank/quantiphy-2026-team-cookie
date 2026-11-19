# simulation_0025_segmented — measurement record

3D Blender scene, segmentation version: the background is pure white (RGB 255), so only the two moving
objects are visible. 960x960 px, 25 fps, 75 frames (t = frame/25, 0 to 2.96 s). Pixel coords: x right, y down.

## Objects
- **bird** — the only animal: dark brown/black raptor-like bird, flapping, flying left -> right across the upper
  middle (y ≈ 355–410). Visible frames 0–66; fully in frame 0–62; cut by the right edge 63–66; gone 67–74.
- **human** — the only person: white top, almost-white head, grey trousers, below the image centre (x ≈ 515–568,
  y ≈ 527–594). Walks slowly to the left and slightly down the image (toward the camera) during all 75 frames.
- No static objects, ground, markings or horizon (everything else was replaced by white).

## Files
- `scene.json` — inventory, camera, apparent sizes, flap cycle, events.
- `tracks/bird.csv`, `tracks/human.csv` — one row per visible frame: `frame, t, cx, cy` (mask centroid),
  `x0,y0,x1,y1` (inclusive bbox), `bw, bh` (bbox width/height), `major, minor` (mask extent along/across its
  principal axis), `angle` (deg of principal axis), `area` (px), `ncomp`, `occluded_or_cut` (1 = touches image
  edge). Human extra: `pelvis_x` (= cx), `pelvis_y` (= y0 + 0.47·bh, hip level), `feet_y` (= y1).
- `scripts/track.py` (segmentation + tracks), `scripts/overlay.py` (check images), `scripts/summarize.py`
  (window summaries -> `summary_tmp.json`).

## Method
Foreground = pixels with 255 − min(R,G,B) > 10 (2×2 opening), split into bird (component centroid y < 470)
and human (y > 470). The human's head/shirt are nearly white, so the human mask is regrown with a looser
threshold (> 5, 3×3 close, largest blob near the strict mask). Overlays at frames 0, 4, 24, 49, 66 were
checked visually: boxes cover the full bird (incl. wing tips) and the human from feet to (faint) head.

## Key numbers (pixels)
- Bird path: cx 234 -> 916 over frames 0–62 (≈11.0 px/frame mean); per-window mean x step 9.6 (0–20),
  11.0 (21–41), 12.2 (42–62) px/frame. cy oscillates 371–398 with the flaps; net path ~horizontal.
- Bird flap: period ≈ 25 frames (1.0 s). Wings raised (V, bbox_h max ≈ 27–33): frames ≈ 0, 24, 49. Wings flat
  (thin, bbox_h ≈ 9–14): ≈ 6, 32, 57. Max horizontal span (bbox_w) per cycle: 46 (f14), 48–52 (f31, f42),
  55 (f58); min width with wings raised ≈ 22–24 (f23–25). Spread-wing width and pixel speed both grow ~20–25%
  left -> right, so the bird gets closer to the camera (depth not constant) — use given depths to scale.
- Human: centroid x 560 -> 521 (≈ −0.53 px/frame), feet_y 583 -> 591; height bbox_h ≈ 53–57 (frame 0 = 57,
  y 527–583; overall 51–62 due to faint head and stride), width 16–27 (median 20). Apparent height roughly
  constant -> depth roughly constant.
- Camera: static (nothing in the background to measure; no common jitter). No perspective cues; take image
  centre (480,480) as principal point; focal length must come from given depth_info + a known size.

## Reliability / ambiguities
- Bird centroid is a proxy for the body origin; the wing pose moves it a few px (vertical ±5–10 px with the
  flap) — smooth over a flap period (25 frames) for speed. Bird extents vary strongly with the flap phase;
  "wingspan" questions should use the max bbox_w / major per cycle (±2 px).
- Human head blends into the white background: top edge uncertain by 3–5 px, so height and the pelvis_y
  estimate are noisy (±3 px frame to frame); feet/x are more stable. The human moves only ~40 px total, so
  per-frame speeds are dominated by noise — fit over many frames.
- Bird frames 63–66 are truncated by the right edge (centroid biased left); exclude them for sizes.
- No shadows, no occlusion between the two objects, little motion blur.
