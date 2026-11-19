# simulation_0155 – measurement record

2D simulation (Blender), 1920x1080, 24 fps, 48 frames (t = frame/24). It's an underwater scene. **One moving object: a single
grey-blue shark** swimming horizontally right to left, parallel to the image plane, at constant height. Static
background: blue water with faint light rays, and undulating sand dunes along the bottom with animated caustic light
patches. **The camera is static** (sea-floor phase correlation shift ≤ 0.1 px). All values are pixels / seconds; no metric scale.

## Files
- `scene.json` – inventory, sizes, events, camera, summary.
- `tracks/shark.csv` – one row per frame 0-47 (`visible`=0 at frame 47). Columns:
  - `cx_centroid, cy_centroid`: mask centroid. This is biased whenever the shark is cut by an image edge.
  - `bbox_x0..y1, bbox_cx, bbox_cy, bbox_w, bbox_h, area_px`: mask bbox. `truncated_left/right`, `occluded`=cut by image edge.
  - `axis_len, axis_width, axis_angle_deg`: PCA main-axis extents of the mask. The axis is about horizontal.
  - `nose_x`: refined snout-tip x (frames 0-30). `tail_x`: tail-fin tip x (frames 15-46). `silhouette_len_x`: tail_x − nose_x + 1 where both are reliable.
  - `dorsal_apex_x`: x of the dorsal-fin apex (top rows of the mask, y≈161), frames 6-38.
  - `step_dx, step_dy`: frame-to-frame body displacement from template matching (frame i minus i−1, frames 1-42).
  - `origin_x_chain`: an alternative origin path from cumulating `step_dx`, anchored at 1114.5 at frame 20. Frames 43-46 come from the tail tip.
    `check_origin_from_tail` = tail_x − 462.5 (the frame-20 offset), for comparison.
  - **`origin_x_est, origin_y_est`: recommended reference point**, the estimated centre of the full silhouette bbox
    (proxy for the rig origin). `origin_src` says how each frame was obtained.
- `scripts/`: `bg.py` (median background, camera check), `track.py` (mask track), `snout.py`, `chain.py`, `features.py`,
  `origin.py` (merge), `finalize.py`, `overlay.py` (overlay check images), `floor.py`, `probe.py`, `diffview.py`, `match.py` (abandoned global matching).
  Pipeline order: bg → track → snout → chain → finalize → features → origin.

## How it was measured
Mask = |frame − per-pixel median background| summed over BGR > 18, for rows y < 760 (the sand below has animated caustics).
Background noise is ≤ 14 and the faint snout is ≈ 23. Then: open 5x5, take the largest component, close 7x7, fill the contour. I checked overlays
(frames 0, 2, 3, 6, 7, 10, 14, 20, 27, 31, 35, 38, 40, 42, 44-46) and they cover the full shark including the fins. Exceptions:
- the pale snout tip (~10-30 px) is often missed. `nose_x` was refined with a lower, smoothed threshold, but frames 21, 22, 25 and 27 are still ±15 px.
- frame 46 covers only the upper tail lobe.

## Sizes (full view, frames 15-30)
- Length (snout tip to tail tip, horizontal) is **926 px at frame 20** (652→1577). It is 926-929 at frames 15-23 and 914-919 at frames 24-30. The tail beats and the body flexes, so expect ±1 %.
- Height of the bbox (dorsal apex y=161/162 to lowest fin y=431-433) is **≈270-272 px**. It is constant all clip, so there's no depth change.
- The shark's apparent size is constant, so its depth is constant. Use one m/px scale (2D scene).

## Motion
- The shark is moving at frame 0, with no start or stop in the clip. The direction is −x only. The vertical motion is 0 ± 1 px: the dorsal apex row and the bbox bottom are constant.
  (The template-chain `step_dy` adds up to a +4.7 px drift. I treat that as matching bias.)
- Positions of `origin_x_est`: 2236.6 at frame 0, 1114.5 at frame 20, 54.0 at frame 38, −392.2 at frame 46. The origin is off-screen for frames 0-5 and 39-46.
- The dorsal-apex step is 58.6 px/frame on average over frames 7-38. Individual steps are 56-61 (feature noise about ±1.5 px).
  The snout steps over frames 1-5 are 37, 51, 55, 52, 56. The tail-tip steps over frames 39-46 are about 54-58 (mean 56).
- **Ambiguity:** different body points give slightly different speeds because the swimming animation flexes the body.
  The template chain (head and front body) gives 38→50→…→61 (frames 21-30)→56 (frame 42). The dorsal apex (near the body centre) gives about a constant 58.6.
  The tail tip gives about 60 at frames 15-30 and about 56 later. `origin_x_est` uses the dorsal apex as the best proxy for the root.
  Frames 0-5 and 39-46 use the snout or tail tip, with offsets calibrated in overlapping frames, so they carry the flex error of those points (±5 px).
  The low first steps (37 at frame 1) are seen by both the snout and the chain. They may be real (ease-in) or head motion. Reliability is lower there.
  The chain fails for frames 0-1 because the template is small.

## Events
- Frame 0: the snout is entering at the right edge (x≈1777).
- Frame 15 (0.625 s): the shark is fully in view.
- Frame 31 (1.29 s): the snout reaches the left edge.
- Frame 39 (1.625 s): the dorsal fin is out.
- Frame 46 (1.917 s): only the tail fin is visible.
- Frame 47: the shark is gone.
- There are no bounces, contacts or direction changes.

## Static objects
- Sea floor (sand): its top edge is at y≈795-1030 depending on x. Sample points are x=0:832, 600:989, 1080:795 and 1440:1031. The edge is fuzzy (±20 px).
- There are no other props, animals or markings.
