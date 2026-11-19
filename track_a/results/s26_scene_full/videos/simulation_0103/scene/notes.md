# simulation_0103 — measurement record

The video is a 2D Blender render, 1920x1080 px at 24 fps with 54 frames (t = frame/24, 0 to 2.2083 s). It is a side view of the sea with three bands: grey sky (y 0–565), a grey-violet distant-sea strip (y 566–672) and a uniform blue underwater area (y 673–1079). **The camera is static.** The horizon and band edges stay at the same rows in every frame, and the background matches a frame-0/53 composite everywhere except where the objects are.

## Files
- `scene.json`: the object inventory, static features, pixel extents, camera notes and events.
- `tracks/boat.csv`: one row per frame (0–53).
  - `x0, x1, y0_visible, y1`: the difference-mask bbox. The water reflection below the keel is cut off at y = 637.
  - `bow_x`: the integer bow tip.
  - `shift_dx_vs_f53, dy_vs_f53, pc_resp`: the subpixel shift from template matching against a frame-53 patch of the wheelhouse and bow (normalised correlation 0.94–1.0).
  - `bow_x_sub`: the subpixel bow tip.
  - `ref_x`: the reference point, = bow_x_sub − 429. It is the centre of the full 858-px-long bbox.
  - `ref_y`: fixed at 436.5. This is only a nominal midpoint between the wheelhouse roof (236) and the keel (637), because the true origin height is unknown and the boat does not move vertically.
  - `stern_visible` / `occluded`: `occluded` = 1 means the stern is cut by the left image border (frames 0–20).
- `tracks/shark.csv`: one row per frame (0–53).
  - `cx, cy`: the mask centroid, which is the reference point.
  - Bbox centre, bbox, `bbox_w` (nose-to-tail length), `bbox_h` (dorsal-fin-to-pectoral-fin height).
  - Principal-axis length, width and angle (about 0°, horizontal), and the area.
  - `occluded` is always 0.
- `scripts/`:
  - `segment.py`: background plate and masks.
  - `tracks.py`: writes the CSVs.
  - `static_measure.py`: band rows and boat parts.
  - `build_scene.py`: writes scene.json and draws a check image.
  - `check_diffs.py`: per-frame displacements.
  - `overlay.py`, `probe*.py`: visual and pixel checks.

## Objects
- **boat**: a red fishing boat with yellow lettering "AH805", a white wheelhouse and a tall mast. It sits on the sea strip and moves right (+x) in pure horizontal translation.
  - The bow moves from x = 520.3 at frame 0 to 1451.5 at frame 53.
  - Its per-frame step is a constant 17.9 ± 0.2 px from frame 2 on. Frame 0→1 has zero motion, so motion starts after frame 1. One template outlier at frame 42 (15.8 px) is followed by a normal step.
  - Vertical drift is under 2.5 px. This is a template/perspective artefact, not real motion.
  - Full length is 858 px (stern-to-bow bbox, frames 21–53).
  - The keel/rudder bottom is at y = 637, the wheelhouse roof at y = 236, and the bow tip at y ≈ 351.
  - Keel to wheelhouse roof is 401 px; keel to bow sheer is 286 px.
  - **The mast is always cut by the top image border, so the total height including the mast is over 637 px and cannot be measured.**
  - `y0_visible` in the CSV jumps between 0, 96 and 231. This is because the thin grey mast is only partly detected; ignore it for heights.
  - The thin white rails and rigging are partly missed by the mask, which does not affect the x extents.
- **shark**: grey back, white belly, head pointing left, in the blue underwater area. It swims left (−x) along a horizontal line (cy = 903.6 ± 0.3).
  - Centroid x goes from about 1665 at frame 0 to 1080 at frame 53.
  - The per-frame step speeds up smoothly from about 7.5 px (frames 2–5) to about 14.7 px (frames 48–53).
  - Frame 0→1 shows no bbox motion.
  - Length is 260 px median (254–264, because the tail fin swings). Height is 105 px (104–106).
  - Centroid steps are noisy by about ±1 px from tail and fin animation. Bbox-edge steps are noisier (integer edges plus tail swing), so prefer the centroid or a smoothed fit.
- **Static features**: horizon at y = 566; the sea strip from y 566 to 672 (107 px); the underwater area from y 673 to the bottom. The boat's reflection lies in the sea strip at y 638–670. There are no other objects.

## Events (see scene.json)
- Both objects start moving after frame 1 (t = 0.042 s).
- The boat's stern enters the view at frame 21 (0.875 s).
- Horizontal alignments only, since the two objects are at different heights. Fractional frames come from linear interpolation:
  - bow over shark nose: frame 37.56 (1.565 s)
  - bow over shark centroid: frame 40.88 (1.703 s)
  - bow over shark tail tip: frame 45.88 (1.912 s)
- The boat centre never passes the shark centroid: at frame 53 they are at x ≈ 1022 and 1080.
- Both objects are still moving in the last frame.

## Reliability and ambiguities
- **Boat x positions:** reliable to about ±0.3 px.
- **Shark centroid:** reliable to about ±1 px per frame.
- **Extents:** reliable to about ±2 px.
- **Boat origin:** the boat's Blender origin is not visible. I used the bbox centre; its vertical position is nominal.
- **Different depths:** the boat (surface, upper half) and the shark (underwater, lower half) may sit at different depths even though the scene is labelled 2D. The record assumes one px scale; a session should note this if its prior comes from the other object.
- **Blur, shadows, occlusion:** no motion blur of note and no shadows, apart from the boat's reflection, which is excluded. Nothing is occluded apart from the image borders (the boat's stern in frames 0–20 and its mast top in all frames).
