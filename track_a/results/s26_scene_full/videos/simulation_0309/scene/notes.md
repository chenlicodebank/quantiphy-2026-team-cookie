# simulation_0309: measurement record

The clip is a 3D Blender render: 72 frames at 24 fps, 2880x1440 px, with black pillarbox bars. The active picture is
x 160-2719 (2560x1440). The camera is static. It looks obliquely down at a snowy rock canyon, with no horizon in view.
The only moving object is a dark winged dragon. It flies right-to-left and up the image (away from the camera). For about
the first 51 frames it flaps its wings (roughly 3 strokes); from about frame 52 to the end it glides with a fixed pose.
Its shadow crosses the terrain below-left of it. All values are in pixels and seconds; no metric scale is assumed.

## Files
- `scene.json`: inventory, camera, events, wing-pose phases, apparent-size summary, active-image area.
- `tracks/dragon.csv`: one row per frame (0-71).
  - `ref_x, ref_y`: the dragon's **pelvis/hip** (top of the hind legs at the tail base). This is the reference point,
    used as the proxy for the rig origin.
  - `ref_source`: `hand` = marked on a gridded native-resolution crop (frames 0,4,...,64,71); `tracked` = template
    tracking between keyframes, run forward and backward and blended linearly; frame 1 copies frame 0 (identical image).
  - `bbox_*`: the full dragon mask (wings, tail, legs included), inclusive pixel coordinates.
  - `mask_cx, mask_cy, area_px`: centroid and area of the mask.
  - `mask_len_main_axis, mask_width_across`: mask extent along and across its principal axis.
  - `occluded_or_cut`: always 0. The dragon is never occluded and never leaves the frame.
  - `mask_quality`: notes on mask problems (see below).
- `tracks/dragon_shadow.csv`: shadow mask centroid, bbox and extents for frames 13-71 (not visible before frame 13);
  `cut_by_frame_edge` = 1 for frames 13-37, where the shadow runs off the bottom edge.
- `tracks/dragon_mask_raw.csv`, `dragon_shadow_raw.csv`: raw segmentation output (before the fixes listed here).
- `tracks/_body_keyframes.json`: the hand-marked hip points. `_body_marks.json`: all 72 points before the frame-1 fix.
- `track_overview.jpg`: hip path (red), every 8th bbox (green) and shadow-centroid path (magenta), drawn on frame 36.
  Half resolution.
- `background_median_q.jpg`: per-pixel temporal median background (half resolution, for reference).
- `scripts/`: every script used.
  - `cam.py`: camera-motion check.
  - `bg.py`: median background. It writes `scene/background_median.png`; the full-size copy was moved out to
    `frames/` to keep the record small, so put it back there before rerunning `segment.py`.
  - `classif.py`: dragon-vs-shadow pixel classifier, saved as `qda.npz`.
  - `segment.py`: masks and raw tracks.
  - `bodysheet.py`, `cropsheet.py`: gridded crops used for the hand marks.
  - `bodytrack.py`: hip tracking.
  - `assemble.py`: final CSVs.
  - `overview.py`, `checkbody.py`: visual checks.

## How it was measured
- **Camera:** phase correlation of background patches against frame 0 gives shifts under 0.3 px in every frame, so the
  camera is static and no background compensation is needed.
- **Dragon mask:**
  1. Changed pixels are those differing by more than 22 grey levels from the median background.
  2. Shadow pixels are removed. A quadratic-discriminant classifier, trained on clean dragon frames (0, 24) and clean
     shadow frames (28, 32), uses colour, the colour ratio to the background and local texture correlation with the
     background. Its output is smoothed spatially, and the filled shadow region is also removed.
  3. The dragon is the largest remaining component plus everything joined to it. The joining gap is 3 px, or 21 px when
     the 3 px version loses more than 15% of the area.
  4. In frames 60-70 the shadow on the rock face just below touches the tail tip. There the mask is cut at a hand-read
     y-limit 5-10 px below the tail tip.
- **Mask check:** overlays of all 72 frames were inspected. The bboxes cover wing tips, tail and feet in every frame.
- **Hip point:**
  - Hand-marked every 4 frames on native-resolution crops with a 50 px grid.
  - Filled in by normalised-cross-correlation template tracking at half resolution (72x72 template at half
    resolution, i.e. 144x144 px full-size, re-taken every frame), forward and backward between keyframes, blended
    linearly.
  - Over 4 frames the forward and backward tracks disagree by 5-20 px while gliding and 20-60 px during strong flapping
    (frames 8-24 and 36-44), when the body turns and is seen from behind or below.
  - All 72 points were checked visually on crops; each sits on the hip / upper thigh.
  - Expected accuracy: about ±10 px while gliding (frames 48-71), ±15-30 px while flapping. Per-frame differences of
    this point are therefore noisy at the 1-frame level, so fit or smooth over several frames for velocities.

## Reliability and ambiguities
- **Reference point:** the true rig origin of the dragon is unknown. It may sit at the hip, the body centre or the
  chest. The hip and the mid-body are about 40-80 px apart, depending on pose and depth.
  - The mask centroid (`mask_cx/cy`) is **not** a good origin proxy. It swings by 100-200 px with the wing pose
    (e.g. frame 0: centroid (2024,789) vs hip (2115,985)).
- **Frames 0 and 1 are identical images.** This looks like a duplicated first frame. Any speed at t = 1/24 s measured
  from the images is zero, although the rendered object probably moved.
- **Sizes:**
  - bbox and extents include the wings, so during flapping they show the wing pose, not depth.
  - For a wingspan question, the widest level-wing extents are: frames 13-14 (~1045-1050 px wide), 25-26 (932-956),
    37 (868) and the glide (748 at frame 52, falling to 642 at frame 71).
  - Wings are rarely exactly side-on, so the horizontal bbox width is a projected span.
- **Depth trend:** in the glide (frames 52-71) the pose is almost constant and the bbox shrinks 748 → 642 px (about
  14%), so the camera distance grows about 1.17x over those 0.83 s. During flapping, the hip moves up the image and to
  the left, i.e. away from the camera across the ground. Depth must come from the question's depth_info.
- **Mask defects:**
  - In frames 15-20 and 39-44 a wing lies over the shadow, so the mask has holes there. The area is underestimated,
    but the bbox is fine.
  - In frame 40 the lower part of the down-swept wing lies over the shadow. It is mostly kept, but its tip may be
    trimmed by up to ~30 px.
- **Shadow track:** low reliability. The shadow is soft and broken by rocks, so its centroid jumps between fragments.
  Use only for rough position or timing (it enters the bottom edge at frame 13 and is fully in view from frame 38).
- **Other objects:** there are no other moving objects, props, people or markings. The terrain is static.
