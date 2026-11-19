# simulation_0099_segmented — measurement notes

2D segmentation video, 1920x1080, 24 fps, 73 frames (t = frame/24, 0 … 3.0 s). Background is pure white.
Static camera. There are only two objects, and both move horizontally at constant pixel velocity.

## Objects
- **boat**: a red fishing boat with a dark-purple lower hull, a white wheelhouse, the hull number "AH805" and a mast.
  It is in the upper half of the image (keel bottom at y≈644) and moves **right** (+x).
  - Full stern-to-bow length: **857 px** (range 856–860 over frames 0–47, when the whole length is in frame).
  - The bow touches the right image edge from frame 48 (t = 2.0 s). After that the visible length shrinks, down to 421 px at f72.
  - The mast is cut off by the top of the frame in every frame, so the boat's true total height is not measurable.
    Visible height is 645 px (y 0–644). Sub-heights at f0: hull from bow top (y 352) to keel (y 644) = 292 px; wheelhouse roof y≈237.
  - Small segmentation fragments (rudder piece at x≈255–285 at f0, bits of the mast rigging) are part of the boat.
- **shark**: a blue-grey shark with a pale snout. It is in the lower part of the image (y 853–955) and swims **left** (−x).
  - Full length snout tip to tail tip: **278 px** (range 276–280; the tail beat is small).
  - Height from dorsal-fin tip to fin bottom: **103 px**.
  - The snout touches the left edge from frame 63 (t = 2.625 s).
- Static objects: none (no ground, water line or markings).

## Motion and events
- Frames 0 and 1 are identical: both objects are at rest, so the backward-difference speed at frame 1 is 0.
- From frame 1 to frame 72 the motion is uniform:
  - Boat: **+17.886 px/frame (429.3 px/s)**. This is a linear fit to the stern edge; the max residual is 1.6 px.
  - Shark: **−10.75 px/frame (258 px/s)**. The snout fit gives −10.76 and the tail fit −10.74; the max residual is about 2 px.
- No bounce, no direction change and no vertical motion (bbox y is constant within 1 px).
- The two objects pass each other horizontally (equal ref_x) at about frame 6.2.
- If a prior gives a speed or acceleration that is constant from t = 0, note this jump: speed goes from 0 to constant between frames 1 and 2.

## Files
- `scene.json`: inventory, extents, velocities, events.
- `tracks/boat.csv` and `tracks/shark.csv` hold the final per-frame tracks. Columns:
  - `ref_x`, `ref_y`/`ref_y_hull`: estimated origin = horizontal centre of the full-length bbox.
    - Boat: `ref_x` = stern_x + 428, so it stays valid while the bow is clipped.
    - Shark: `ref_x` = bbox centre, or tail_x − 138.5 when clipped.
  - `bbox_*`: visible mask box.
  - `visible_length_px`, `full_length_px`, height.
  - Mask centroid and area.
  - `clipped` (which frame edge cuts the object). `occluded` is always 0: there is no occlusion, and the objects never overlap.
- `tracks/*_raw.csv`: raw per-frame mask statistics (stern/bow/hull columns for the boat, snout/tail columns for the shark).
- `scripts/`:
  - `measure.py`: segmentation (non-white pixels: min RGB < 238 or saturation > 25, 3x3 opening; image split at y = 740 into boat above and shark below).
  - `finalize.py`: reference points and fits.
  - `overlay.py`: check images in `frames/` (`check.png`, `shark_zoom.png`); these were inspected and the boxes cover each full object.

## Reliability and ambiguity
- Lengths and positions are good to about ±2 px.
  - A first threshold missed the shark's pale snout (about 18 px). It was fixed, and the shark length is now 278 px, not 260.
- The boat's vertical origin is unknown, because the mast is clipped at the top. Its true bbox height and centre y cannot be measured.
  - Use `ref_y_hull` (498) only as a hull-centre proxy.
  - Vertical or 3D boat–shark distances are therefore uncertain. The horizontal offset is reliable.
- Treat this as a single plane: one metres-per-pixel scale from whichever prior is given (boat length 857 px, shark length 278 px, or a pixel speed above).
