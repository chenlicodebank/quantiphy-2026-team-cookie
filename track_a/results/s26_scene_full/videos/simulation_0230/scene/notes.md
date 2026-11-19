# simulation_0230 — measurement record (pixels, seconds)

Video: Blender render, **2D** scene, 1920x1080, 24 fps, 50 frames (t = frame/24, last frame 49 = 2.0417 s).
Front view of a classroom wall: a big green blackboard, a round wall clock at upper right, a desk/ledge under the left
half of the board, orange student chairs in the foreground, ceiling lights at the top, and bright diagonal sunbeams
across the left half. **Camera is static.** Phase correlation of the ceiling band between frame 0 and frames 10/25/49
gives shifts under 0.13 px, so no background compensation is needed.

## Moving objects
1. **paper_plane**: a white/cream paper airplane flying left→right across the blackboard with its nose pointing right.
   It is seen roughly edge-on, as a thin sliver. It can be detected in frames 10–41 and is gone from frame 42.
2. **cat**: a grey cat with its tail raised, walking left→right along the top of the desk/ledge right under the
   blackboard (paws at y≈745). It is visible in all 50 frames, but its contrast is very low (see the caveats below).

There are no other moving things. The wall-clock rim "flickers" in the frame differences because of render noise.
It is static and was masked out of the plane search.

## Files
- `scene.json`: inventory (moving and static objects with pixel sizes and positions), camera, events, size summaries.
- `tracks/paper_plane.csv`: one row per frame from 10 to 41.
  - `ref_x, ref_y`: the reference point (taken as the plane's origin, i.e. its centre). Normally it is the midpoint of
    the nose and tail along the main axis. Column `ref_source` gives the fallback used in partial frames: frames 34–37
    use nose − 70.5 px along the axis; frames 38–41 (nose beyond the right edge) use tail + 70.5 px. Frame 10 has
    no reference point because only a fragment is visible.
  - `cx, cy`: mask centroid. Also: bbox (`x0..y1`, `bbox_w/h`), `length_main_axis`, `width_across`, main-axis angle
    (degrees, positive = nose down), nose and tail points, area, `quality`, `occluded_or_partial`.
- `tracks/cat.csv`: one row per frame from 0 to 49.
  - `ref_x`: estimated body centre. `ref_y` = 677, the torso centre, held constant because the cat walks on a level
    surface; its body showed no vertical motion.
  - `nose_x`: front edge of the head blob, frames 11–49. `rump_x`: rear of the torso without the tail, frames 0–15.
  - Also: head-blob centroid, approximate full-mask bbox and centroid, `occluded` flag and a `note`.
- `scripts/`: every script used. `bg2.py` builds the clean background, `frames/bg_clean.png`: frame 0, with the cat's
  frame-0 area taken from frame 49. `plane.py` tracks the plane. `cat2.py`, `cat_rear.py` and `cat_torso.py` handle the
  cat. `finalize.py` adds the reference points. `static.py` measures the blackboard and clock. `check_overlay.py`,
  `view.py` and `diffview.py` make the visual checks. Scratch images are in `../frames/` and are not part of the record.

## Method
- Segmentation is by background difference: the maximum channel |frame − clean background|, blurred with a 5x5 Gaussian
  (9x9 for the cat body), then thresholded and cleaned with morphology. Render noise is about 1 grey level (median)
  and 9 grey levels (99.9th percentile).
- Plane: threshold 6, or 4 plus a brightness test in the faint frames 10–11. Fragments must lie on the plane's line.
  The overlays (`frames/plane_overlay.png`) were checked by eye: the contours fit the plane in frames 11–33.
- Cat: only parts of it are separable from the haze.
  - Rear half: high contrast while it is left of x≈340, which covers frames 0–15. Here the rump x is measured from the
    torso rows 665–695.
  - Head: a light blob that can be found from frame 11 on.
  - Nose-to-rump length, measured in frames 11–15 where both ends are visible: **163 px** (range 162–165).
  - `ref_x` is rump + 81.5 for frames 0–10, the mean of the two estimates for frames 11–15, and nose − 81.5 for
    frames 16–49.
  - The overlay (`frames/check.png`) confirms that the reference point sits mid-body.

## Key pixel sizes (clear frames)
- Paper plane, frames 13–33: nose-to-tail length **≈142 px** (median 141.8, range 137–150). The mask includes about
  2 px of blur at each end, so the true length is about 138–140. Thickness across the axis is ≈22 px, and the bbox is
  141 x 28 px.
  - Its pitch in the image goes from −9.5° (nose up, frame 13) through 0° (frames 23–24) to +11° (frame 33) and about
    +19° (frame 38).
  - Because it is seen edge-on, no wingspan can be measured.
- Cat:
  - Nose-to-rump length: 163 px.
  - Horizontal length including the raised tail: about 194 px.
  - Height from paws to ear tips: about 110 px. Paws to back: about 93 px. Paws to tail tip: about 148 px.
- Static objects:
  - Blackboard green surface: x 342–1670, y 315–717, so 1328 x 402 px. Outer frame: x 320–1692, y 298–738, so
    1372 x 440 px.
  - Clock: centre (1763.5, 292.5), outer diameter about 112 px.
  - Chair, desk and light bounding boxes are in `scene.json`. They are approximate (±10 px), read from a grid overlay.

## Events (frame / time)
- Frame 0 (0 s): the cat is already walking. It keeps walking for the whole clip with no stop or turn, moving about
  9 px/frame in x.
- Frame 10 (0.417 s): the plane is first detectable. It is already in flight, at the lower left near x≈150, y≈630.
- Frame 11 (0.458 s): the cat's head is first detectable.
- Frame 23 (0.958 s): the plane reaches its highest point (`ref_y`≈342.7, x≈1028) and turns from climbing to
  descending.
- Frame 34 (1.417 s): the plane leaves the blackboard area and passes over the pink wall.
- Frame 38 (1.583 s): the plane's nose reaches the right image edge.
- Frame 41 (1.708 s): the plane is last seen. Frame 42: it is gone.
- There are no contacts, bounces or impacts.

## Reliability and ambiguities
- **Plane, frames 12–33:** good, about ±2 px on the reference point.
- **Plane, frames 10–11:** faint against the light wall and inside the sunbeam. Frame 11 has two fragments whose span
  (139 px) matches the plane, so it is usable at about ±5 px. Frame 10 is a fragment only.
- **Plane, frames 34–37:** low contrast over the pink wall, so only part of the mask is found. The reference point is
  extrapolated from the nose, ±10–15 px.
  - Frame 37 looks too short a step: Δx = 28 px against ~47 px for its neighbours.
- **Plane, frames 38–41:** cut by the right edge, so the reference point is extrapolated from the tail (±10 px). Treat
  any speeds from frames 34–41 with care, and prefer frames 12–33.
- **Cat:** low contrast throughout because it is seen through the volumetric sunbeams.
  - Frames 0–10: the front of the cat (head) cannot be seen at all, so the reference point rests on the rump alone.
  - Frames 16–49: the middle and rear of the body are washed out, so the reference point rests on the nose alone.
  - Nose x jitters by about ±5 px from frame to frame.
  - Frame 25: the head was lost and the nose was interpolated.
  - Frames 26–33: the head blob locks onto the ear or forehead.
  - Smooth over a few frames before differencing; a single-frame difference of the cat's position is noisy.
  - The mask bbox columns in `cat.csv` are approximate: the full-mask bbox picks up haze edges and the blackboard frame
    edge near x≈334 in frames 21–32.
- Sizes of a single object can be trusted more than the distance between the two objects. The cat's `ref_y` (677) is
  a constant estimate, not a per-frame measurement.
- The light shafts and the blackboard-frame edges are not objects. There are no shadows of the moving objects.
