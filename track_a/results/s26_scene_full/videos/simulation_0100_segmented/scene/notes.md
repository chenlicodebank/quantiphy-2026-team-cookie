# simulation_0100_segmented — measurement record

2D segmentation video (Blender render, background replaced by plain white). 1920x1080, 24 fps, 58 frames (t = frame/24, 0 to 2.375 s).
All values are in pixels and seconds. No metric scale is assumed.

## Scene
- **boat**: red fishing boat ("AH805" on the bow, white wheelhouse, tall mast, purple lower hull) in the upper half of the frame, with its bow pointing right. It moves **right**.
- **shark**: grey-blue shark with a white belly in the lower part of the frame (y 853–955), with its head pointing left. It moves **left**.
- There are no other objects, no ground and no markings. The camera is static: the background is plain white, and both objects move at a steady speed with no shared jitter.
- There are no perspective cues. Both objects keep a constant pixel size, so they behave as a planar scene and one m/px scale applies.

## Files
- `scene.json`: inventory, sizes, positions at frame 57, events and camera.
- `tracks/boat.csv`, `tracks/shark.csv`: one row per frame (0–57). Columns:
  - `ref_x`, `ref_y`: the reference point.
  - `full_bbox_*`: the full object box, including any part off-screen, obtained by shifting the frame-57 box.
  - `vis_bbox_*`: the visible mask box.
  - `length_px_main_axis`, `width_or_hull_height_px`, `visible_height_px`: mask extents.
  - `mask_centroid_*`: the visible mask centroid.
  - `match_score`: template-match quality.
  - `truncated_by_frame_edge`: which frame edge cuts the object (the occlusion flag).
- `tracks/*_raw.csv`: raw mask statistics per frame (threshold mask, PCA length/width, area).
- `tracks/shifts.json`: sub-pixel shift of each object relative to frame 57, per frame.
- `scripts/`, run from scene_ws in this order:
  - `track.py`: masks.
  - `refine.py`: template-match shifts.
  - `parts.py`: part extents at frame 57.
  - `final_tracks.py`: final CSVs and overlay checks.

## Method
- **Masks**: non-white pixels (min channel < 225 or saturation > 40), split at y = 740 into boat (above) and shark (below).
- **Positions**: normalized cross-correlation of rigid frame-57 templates with sub-pixel peak refinement. The boat template covers the wheelhouse to the bow; the shark template covers the whole body. Match scores are ≥ 0.93.
- **Reference point**: the origin is not visible, so I used the centre of the full bounding box.
  - Boat: x is the midpoint of stern (666) and bow tip (1521) at frame 57; y is the hull centre (498.5).
  - Shark: the box centre.
  - Both motions are pure translation (vertical drift < 1 px, no rotation), so any rigid point gives the same displacements and speeds. Only the absolute boat–shark distance depends on this choice.
- **Checks**: I drew boxes and reference points on frames 2, 30 and 57 and looked at them; they sit on the right object and cover its full extent.

## Key numbers (px)
- **Boat**
  - Length, stern to bow tip: 856.
  - Hull height: 294 at the bow (bow top to keel), about 190 at the stern.
  - Visible height, keel (y=645) to frame top: 646. The mast top is cut off, so the full height is unknown.
  - Wheelhouse: about 174 × 214. Mast: about 22 wide.
- **Shark**
  - Length, nose to tail tip: 277–278. This is constant over all frames (± 2 px of mask noise).
  - Height including fins: 103.
- **Motion**: both are at rest in frames 0–1 (identical frames) and start moving between frames 1 and 2 (t = 0.083 s). After that the per-frame shift is constant to within noise:
  - Boat: +17.86 px/frame to the right (per frame 17.1–18.5).
  - Shark: −10.76 px/frame to the left (per frame 10.1–11.3).
  - Neither object shows acceleration.
- **Ref points at frame 0**: boat (92.8, 498.4), shark (1658.9, 903.7). At frame 57: boat (1093.5, 498.5), shark (1056.5, 904.0).
- **Crossing**: the ref-point x positions cross between frames 55 and 56 (t ≈ 2.31 s). The vertical gap between ref points is a constant ≈ 405.5 px.

## Reliability and ambiguities
- Per-frame positions are good to about 0.3–0.5 px; sizes to about ±2 px.
- **Boat truncation**:
  - The stern is off the left edge in frames 0–20, so the visible bbox and mask centroid are biased there. Use `ref_x` or `full_bbox`, which are derived from the rigid shift.
  - The mast always leaves the top edge.
- **Segmentation artifacts**:
  - The grey aft cargo rail is missing from the mask before frame 30, so the mask centroid jumps about 7 px at frame 30. That jump is not motion.
  - Small detached fragments (a thin vertical line near the stern, the rudder) are included in the boat bbox. The stern edge at 666 is the hull/rudder extent.
- **Boat origin height**: the true Blender origin height is unknown. I used the hull centre; the wheelhouse/keel and the mast-inclusive centre are alternatives. The x motion is unaffected.
- **Shark**: no visible tail beat, so its extents are stable.
- **Shadows and blur**: no shadows and no notable motion blur.
