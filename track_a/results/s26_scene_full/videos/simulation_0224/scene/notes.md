# simulation_0224 — measurement record

2D simulation (Blender render), 1920x1080, 24 fps, 45 frames (t = frame/24, frame 0 at t = 0). Static camera.

## Scene
A small white/cream rounded rectangular block (looks like a bar of soap) starts at rest near the upper-right end
of a large inclined reddish-brown wooden ramp, which has a grey channel along its top. The block slides
down-left along the channel, passes behind the raised lip at the lower-left end (frames 40-41), drops off
(frame 42), falls past the ramp's lower-left end (frame 43) and leaves the frame at the bottom (frame 44).
Static: the ramp, a light beige stand/box with a black open top under the ramp, a calligraphy hanging scroll on
the back wall, the tan wall, and a tatami floor (the wall/floor line is at y ≈ 900).
**The block is the only moving object.**

## Files
- `scene.json`: the inventory (pixel extents and positions of static objects), the block's pixel size, events,
  camera, and the duplicate-frame list.
- `tracks/block.csv`: one row per frame (0-44). Columns:
  - `cx, cy`: centroid of the mask, used as the reference point (for a rigid block the visible centre is about the origin).
  - `bbox_*`: bounding box.
  - `len_main_axis, width_across`: mask extent along and across its principal axis.
  - `bbox_w, bbox_h`, `axis_angle_deg`, `area_px`.
  - `occluded`, `quality` (good/fair/poor), `duplicate_of_prev`, `phase`.
  - `s_along_ramp_px`: signed distance from the frame-0 position, measured along the fitted down-slope line.
  - `source_frame_est`: see the duplicate-frame section below.
- `scripts/`:
  - `track_block.py`: background subtraction against the median of all frames inside the ramp area, then the largest blob nearest the previous position. It also writes overlay images, which I checked.
  - `finalize.py`: adds the flags, the along-ramp distance and `scene.json`.
  - `check_quadratic.py`: a sanity check only.
  - `sheet_end.py`: a montage of the end frames.

## Key numbers (pixels)
- **Block size** (frames 0-38, sliding):
  - Length along the slope: 81.5 px (range 80.2-82.7). This is the most reliable dimension.
  - Thickness across the slope: 32.3 px (range 31.2-33.6). The lower edge may be slightly hidden by the channel wall.
  - Axis-aligned bbox: about 77 x 55 px.
  - In free fall (frame 43): 84.6 x 34.1 px.
- **Block path:** a straight line at 25.9° below horizontal in the image (fit residual rms 0.2 px). The ramp's top
  edge runs from (1378, 488) to (424, 962): about 1065 px long, at 26.4°.
- **Displacement from frame 0:** `s_along_ramp_px` is 0 at frame 0, 305 px at frame 24, 710 px at frame 38 and
  754 px at frame 39 (where the block reaches the lip).
- **Events:**
  - At rest: frames 0-1.
  - Motion starts: about frames 1-2 (s = 0.9 px at frame 2, 2.6 px at frame 3).
  - Reaches the lip and passes behind it: frame 40.
  - Leaves the ramp and falls: frame 42.
  - Exits the frame: frame 44.

## Duplicate / skipped frames (important for speeds)
- **Duplicates:** frames 6, 13, 25, 28, 35, 38 and 41 are pixel-identical to the frame before. Frame 1 is also
  flagged, but that is the real rest at the start.
- **Skipped frames:** the step into frames 5, 10, 23, 27, 34, 37 and 40 is about twice as large as the steps
  around it, so a source frame was skipped there. Each skip is paired with a nearby duplicate.
- **Effect:** naive per-frame differences show zeros and spikes at these frames.
- **`source_frame_est`** re-indexes the frames: +2 at a skipped step, 0 at a duplicate. With this index the
  along-ramp distance is a smooth quadratic (rms 1.0 px), compared with rms 9.6 px against the raw frame index.
  So the render frames are most likely `source_frame_est`, and the totals agree (both end at 44).
- **Recommendation:** fit s against `source_frame_est`/24 s, or against time using only the non-duplicate
  frames, rather than taking single-frame differences.

## Reliability
- Centroids for frames 0-38: about ±0.5 px. Frame 39: fair (a little shadow is included).
- Frames 40-41: poor, because the block is hidden behind the lip and only a sliver is visible.
- Frame 42: fair (only partly visible). Frame 43: good. Frame 44: poor (mostly out of frame).
- Static extents were read from gridded zooms: about ±3 px.
- No metric scale is assumed. Use the prior from the question (for example the block's length, which is
  81.5 px) to set one m/px scale. This is a 2D scene, so the motion is in a plane facing the camera.
