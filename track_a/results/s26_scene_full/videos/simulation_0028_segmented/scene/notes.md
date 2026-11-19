# simulation_0028_segmented: measurement record

960x960 px, 25 fps, 75 frames (t = frame/25, 0 to 2.96 s). The source is "segmentation": a Blender 3D render with the
background replaced by white. All values are in pixels (x right, y down, origin at the top left) and in frames/seconds.
No metric scale is assumed.

## Scene
- **bird**: the only moving object. A dark-brown bird of prey flapping its wings and flying left to right.
  - It is visible in frames 0–47 (t 0–1.88 s). From frame 48 on the segmentation removes it completely (frame 48
    shows a white notch in the rock edge where it was). It is not hidden behind anything and it does not land or
    hit anything.
  - It is already flying at frame 0, so its motion starts before the clip.
- **rock**: a static, snow-covered rocky mountain block in the upper right. It has a white snowy top, brown cliffs
  on its right and a striped brown base.
  - bbox x 328–959, y 24–310 (632 x 287 px). Centroid (636.7, 167.0).
  - PCA main axis 631 px at about 4° from horizontal; width across it 278 px.
  - Its right tip reaches the image edge (x=959), so it may be slightly cut off.
  - Silhouette top/bottom every 50 px are in scene.json.
- **No ground plane, horizon or vanishing points** are visible because the background is white. The only depth cue
  is that the bird passes in front of the rock from frame 21 on.
- **Camera**: static. Phase correlation of the rock region against frame 0 gives a shift of at most 0.16 px. The
  rock's segmentation boundary flickers by a few px near its right and lower edges.

## Files
- `scene.json`: inventory, rock extents, camera, events and summaries.
- `tracks/bird.csv`: one row per frame, 0–74 (visible=0 from 48 on). Columns:
  - `cx, cy`: centroid of the mask.
  - `ref_x, ref_y`: **the reference point to use**. It equals the centroid on good and fair frames. On the
    unreliable frames 21, 23 and 39–43 it is interpolated linearly between neighbouring good frames; on frame 47
    it is extrapolated from frames 44–46.
  - `bbox_*`: bounding box; `bbox_cx, bbox_cy` is its centre.
  - `area_px`: mask area.
  - `axis_len, axis_wid, axis_angle_deg`: PCA extents of the mask (along and across its main axis).
  - `over_rock`: 1 when the bird is in front of the rock.
  - `occluded`: always 0.
  - `quality`: good, fair or poor.
- `scripts/`:
  - `bg.py`: median background (`bg_median.png`).
  - `track_bird.py`: coarse pass.
  - `track_bird2.py`: refined masks. Run it after `track_bird.py`.
  - `finalize.py`: reference points, rock, camera check, scene.json.
  - `overlay.py`, `crops.py`, `explore.py`: visual checks.

## Method and reliability
- **Bird mask**:
  - Over the white background: pixels with min channel < 232.
  - Over the rock: |frame − median background| > 30, inside a ±45 px window around the coarse track.
  - Masks were drawn on every frame and checked by eye.
- **Mask quality**:
  - Good on white (frames 0–20). Fair over the light rock (frames 22–38, 44–46).
  - Frames 21 and 23 pick up rock-edge flicker.
  - Frames 39–43: the bird crosses the dark brown cliff texture and the mask is fragmentary.
  - Frame 47 picks up edge bits.
  - **Do not use** bbox or extents from frames 21, 23, 39–43 or 47.
- **Reference point**: in simulation, positions refer to the bird's origin (pelvis/body), but the mask centroid
  swings by a few px with the wingbeat because the wings change the mask shape.
  - x moves very steadily, about 16.5–17 px/frame (frame-to-frame jitter about ±1 px).
  - y moves in a slow wave between about 222 and 261 px. Part of this is real path curvature and part is wing pose.
    Treat per-frame y with about ±3 px uncertainty.
  - Path from frame 0 to 47: (59, 223) → (848, 247).
- **Apparent size**: changes only with the wingbeat (period about 12 frames, ≈0.48 s). There is no trend over the
  clip, so the bird is at roughly constant depth and flies roughly parallel to the image plane.
  - bbox_h minima (wings level or edge-on) near frames 6, 18, 32 and 43; maxima (wings raised) near 0–1, 10, 24–25
    and 47.
  - Largest reliable horizontal spread: about 35–38 px at frames 30–38, when the wings are spread sideways (e.g.
    frame 36–38 bbox_w 37–38).
  - Largest reliable vertical extent: about 37–41 px at frames 0–1 and 24–27.
  - Body-plus-wing mask main axis: 25–43 px.
  - Thin, light wingtips can be 1–3 px under-segmented.
- **Ambiguity**: a question asking about the bird after t = 1.88 s refers to a time when it is not shown. Its steady
  motion would have to be extrapolated.

## Events
| Frame | t (s) | Event |
|---|---|---|
| 0 | 0.00 | Bird already in flight |
| 21 | 0.84 | Bird starts to overlap the rock |
| 47 | 1.88 | Last frame with the bird visible |
| 48 | 1.92 | Bird vanishes (segmentation artefact) |

There are no bounces, impacts or contacts. There is no sharp change of direction; only a gentle wave in y.
