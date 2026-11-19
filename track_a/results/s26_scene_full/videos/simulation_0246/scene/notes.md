# simulation_0246 — measurement record

2D simulation (Blender render), 30 fps, 75 frames (t = frame/30, frame 0 at t = 0), 1920x1080.
A top-down camera looks straight down at a flat, featureless beige floor. Two animals walk to the right (+x) in parallel rows:

- **kudu**: a large antelope with long spiral horns, big ears, an orange-brown body and a thin tufted tail. It walks along the lower-middle row (midline y ≈ 572).
- **rodent**: a small orange furry animal with a pale grey head (hamster or guinea-pig like). It walks along the upper row (y ≈ 347), ahead of the kudu and ~225 px above its midline.

Neither animal is occluded at any point. Both are visible in all 75 frames. All units are pixels and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory, summary extents and positions, camera, events and relations.
- `tracks/kudu.csv`: one row per frame. Columns:
  - `core_cx, core_cy`: recommended reference point. Centroid of the mask within ±50 px of the body midline, which covers trunk, neck, head and tail but not the horns.
  - `trunk_cx, trunk_cy, trunk_x0, trunk_x1`: columns where that core band is at least 70 px tall, i.e. rump to ears.
  - `mask_cx, mask_cy`: centroid of the whole mask, horns included.
  - Bounding box: `bbox_*`.
  - `pca_len, pca_wid, axis_deg`: main-axis extents of the mask. The axis stays horizontal (|angle| ≤ 1.4°).
  - `nose_x, tail_tip_x, midline_len`: extreme mask columns within ±25 px of the midline.
  - `area`, `occluded` (always 0).
- `tracks/rodent.csv`: one row per frame. Columns: `cx, cy` (centroid of the orange-fur mask, the recommended reference), `bbox_*`, `pca_*`, `area`, `occluded` (always 0).
- `scripts/`:
  - `bg.py`, `bg2.py`: background model. `bg2.py` builds a clean composite from frame 74 (x < 955) and frame 0 (x ≥ 955), saved as scratch `frames/bg_full.png`, outside the record. Run `bg2.py` before `track.py`.
  - `seg.py`: segmentation. It keeps pixels whose chromaticity differs from the background, pixels brighter than it, or extra texture. Shadow rejection uses a stricter chroma threshold where the floor is darkened.
  - `track.py`: makes the tracks and overlays.
  - `summary.py`: prints the summary numbers.
  - `testseg.py`, `probe.py`: debugging scripts.

## How it was measured and checked
Masks were drawn over frames 0, 15, 25, 30, 45, 60 and 74 and inspected. The kudu mask covers the full animal: horns, ears, snout, tail tuft and the visible hooves. Large soft cast shadows (light comes from the lower right, so shadows fall up and left) are excluded.

**Camera:** static. Floor intensity at the bottom corners stays constant across all frames, and the shading pattern does not move.

## Key numbers (px)
**Kudu:**
- Core position: (669.0, 572.0) at frame 0 → (1340.7, 570.8) at frame 74.
- Per-frame displacement:
  - core: mean 9.08 px/frame, range 6.2–12.0 (gait oscillation)
  - trunk: mean 9.45
  - nose: mean 9.47
  - whole-mask centroid: mean 9.36
- y stays constant within ±2 px, so the path is straight.
- The different reference points drift by ~0.4 px/frame relative to each other because the tail swings and the body stretches.

**Kudu sizes:**
- Horn-tip to horn-tip (y extent, the widest part): 289–296 px, median 293. This is the y-height of the bounding box.
- Tail tip to nose (x extent): 612–732 px, median 674. It varies with tail swing; the tail lies almost straight back late in the clip.
- Body without tail at frame 45: x ≈ 881–1375 (~495 px).
- Trunk width: ~100–115 px.
- Height cannot be observed from above.

**Rodent:**
- Position: (963.7, 347.0) at frame 0 → (1601.3, 346.3) at frame 74.
- Per-frame displacement: mean 8.62 px/frame, range 5.3–12.6. y is constant.
- Orange body length: 62–83 px, median 67. It varies with the leg stride.
- Orange body width: 39–48 px, median 43.

**Separation, rodent minus kudu core:** (+295, −225) at frame 0 and (+261, −225) at frame 74. Distances: 370.8 → 344.0 px.

## Events
- Both animals are already walking at frame 0 and still walking at frame 74.
- There are no starts, stops, turns, contacts or collisions. Both move only in +x.

## Reliability and ambiguities
- **Kudu origin:** the rig root (pelvis/hip) is not visible from above. Use `core_cx` or `trunk_cx` as the body position. Over a whole stride they agree on the mean motion to ~4%. For speed over short intervals, average over a gait cycle (~10–12 frames), since single-frame differences oscillate by ±30%.
- **Kudu length** depends on the tail. For a "length" prior, the likeliest convention is the axis-aligned bounding box. In this view that is x = 612–732 px (snout to tail tuft) and y = 289–296 px (horn span), measured at the same frame.
- **Rodent head:** the pale grey head (right end) has nearly the same colour and brightness as the floor and the shadows, so it is **not** in the rodent mask. Visual reads give a head length of ~25–32 px. Full nose-to-rear length ≈ orange `bbox_w` + ~28, which is ~90–95 px (frame 0: x 935 → ~1025). Including the head would shift the rodent centroid ~+10–14 px in x, a constant offset with no effect on speeds.
- **Rodent mask edges** are ±2–3 px. The jitter in `bbox_w` comes from leg strides and compression, not tracking errors.
- **Kudu `tail_tip_x`** jumps in a few frames (for example frames 36 and 40), where a hoof or its contact shadow merges with the tail tuft. `bbox_x0` is affected the same way.
- **Shadows:** large dark soft shadows lie up and left of each animal. They are excluded from all masks, and small contact shadows under the hooves may add ≤ 5 px.
