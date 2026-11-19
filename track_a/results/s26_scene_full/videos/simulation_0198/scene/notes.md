# simulation_0198 — measurement record

The video is a 2D Blender simulation: 2560×2560 px, 60 fps, 14 frames (t = frame/60, so 0–0.2167 s). One drop of serum
falls from a glass pipette, which is held tilted above a serum bottle ("SKYNOVA RADIANT VITAMIN B", orange). The bottle
stands on a grey plinth in front of a beige wall with light stripes cast by venetian blinds.
**Camera: static.** Phase correlation against frame 0 gives a shift below 0.001 px in every frame. All values are in
pixels, with image x to the right and y downward. No metric scale is assumed.

## Files
- `scene.json`: inventory, static extents, per-frame displacements of the drop, events and camera.
- `tracks/drop.csv`: the drop in frames 0–10. Columns:
  - mask centroid `cx_mask, cy_mask`. This is the reference point and stands in for the rigid object's origin.
  - bbox centre and corners, `bbox_w`/`bbox_h`.
  - length along the main axis (PCA) and width across it, plus the axis angle (about 90° = vertical).
  - mask area, `render_index_est` (see the timing note below), occlusion flag, note.
- `scripts/`:
  - `diff.py`, `track_drop.py`: background difference against frame 13 (drop absent), threshold 18, hole-filled mask.
  - `framediff.py`: camera and duplicate-frame check.
  - `check_timing.py`: test of the frame-index mapping.
  - `write_scene.py`: writes `scene.json`.
- `../frames/drop_overlay.png`: mask contour, bbox and centroid for every frame. I looked at it: the masks hug the whole
  teardrop.

## Objects
- **drop** (the only moving object): a clear amber teardrop, point up. It is rigid, and its shape stays the same across frames.
  - Visible in frames 0–10, never occluded. It leaves through the bottom edge between frames 10 and 11.
  - Size: 59–60 px wide × 91–92 px tall (medians 59 × 91). In frame 10 the width reads 54 because the drop is on a dark
    background, so that value is underestimated; in frame 8 the height reads 94 (slight blur).
  - Path: almost vertical with a small leftward drift. x goes from 1449 to 1426 while y goes from 748 to 2346.
  - Centroids are accurate to about ±0.5 px.
- **dropper / pipette** (static): the open glass tip is at (1455, 700) and the white cap's bulb end is at about (2244, 178).
  - Overall length about 946 px, tilted 33.5° above horizontal.
  - Cap opening: centre about (1900, 389), diameter about 255 px. Glass tube width about 40 px.
  - Accuracy about ±15 px, because the parts are transparent.
- **serum bottle** (static):
  - Body bbox (1702, 678)–(2133, 1250): width 431 px, height 572 px.
  - Threaded neck bbox (1772, 500)–(2067, 656): width 295 px.
  - Height from neck top to base about 750 px.
  - Accuracy about ±10 px.
- **plinth** (static): top edge at y ≈ 1240, left edge at x ≈ 1670. It runs to the right and bottom borders of the image.
- **wall**: blind-stripe light pattern, with a dark band at the far left. Nothing on the wall moves.

## Events
- Frame 0 (t = 0): the drop hangs at the pipette tip, centroid (1449.0, 747.6), and its top touches the tip. A quadratic
  fit of frames 1–6 passes through the frame-0 position (residual < 0.4 px), so the drop starts from rest at frame 0.
  Release is therefore at frame 0.
- Frames 1–10: free fall. The per-frame vertical step grows by about 31.6 px each frame.
- There is no bounce or impact in view.

## Timing anomaly (important)
- Video frame 7 is an almost exact duplicate of frame 6: the drop does not move, and the whole-image difference is 0.005.
- The step from frame 8 to 9 is 510 px, which equals two normal steps (≈240 + 272).
- My reading is that the video shows render steps 0–6, 6, 7, 9, 10: frame 7 is a duplicate and render step 8 is missing.
- With that mapping (`render_index_est`), one quadratic fits all of frames 1–10 to within 0.4 px. With the raw video
  index the misfit reaches 166 px.
- An answer that uses one-frame differences at frames 7, 8 or 9 should consider which index the reference used.
  - Reference answers come from the Blender data, so they probably follow the uniform render steps.
  - Raw video differences at those frames are 0, 208 and 510 px; the uniform steps there would be about 208, 240 and 272 px.

## Reliability and ambiguity
- There is only one moving object, and nothing in the scene looks like it.
- The drop is transparent, but the background difference outlines it clearly. No shadow of the drop is visible and there
  is no motion blur to speak of.
- Static extents were read by eye from grid images of frame 12 (`frames/top.png`, `frames/static.png`).
