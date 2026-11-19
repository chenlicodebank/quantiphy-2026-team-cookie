# simulation_0291 – measurement record (pixels, seconds)

2D Blender render, 2560x1440, 24 fps, 72 frames (t = frame/24). An underwater side view: one koi fish swims
right to left through mid-water over a static seafloor with seaweed, a coral rock and a branching coral.
The camera is **static**: phase correlation of the seafloor/rock region gives |shift| ≤ 0.03 px in every frame.
Only the caustics and the water-surface texture move.

## Files
- `scene.json`: inventory, static object boxes, camera, events, and a summary of the fish's size and motion.
- `tracks/fish.csv`: one row per frame 0-71.
  - `cx_bbox,cy_bbox`: bbox centre. `cx_mask,cy_mask`: mask centroid.
  - `bbox_*`: bounding box (x0,y0,x1,y1 inclusive; w,h).
  - `axis_len/axis_wid/axis_angle_deg`: PCA extents along and across the main axis.
  - `area_px`, `clipped_at_frame_edge` (frames 0-4: the tail is cut at x=2559), `occluded` (always 0).
  - `dx_from_prev`: sub-pixel head shift.
  - **`ref_x, ref_y`: the recommended reference point.** It is the rigid translation of the head integrated from
    frame 0, offset so that it matches the median bbox centre over frames 5-71. It is smooth and still valid for
    the clipped frames 0-4.
- `tracks/fish_head_shift.csv`: per-frame dx, dy from template matching on the head and front body, plus their
  cumulative sums.
- `scripts/`:
  - `bg.py`: median background.
  - `camcheck.py`: camera shift check.
  - `track.py`: segmentation and track.
  - `headshift.py`: sub-pixel shift.
  - `dupcheck.py`: held-frame check.
  - `finalize.py`: adds the merged ref_x and ref_y columns.
  - `summ.py`: summary statistics.
  - Run them from scene_ws. `bg.py` must run first: it writes `scripts/bg.png`, which was deleted to save space.

## Method and reliability
- **Fish mask:** colour difference to a median background (threshold 30, open, close, fill), restricted to y 150-960.
  - Overlays (frames 7 and 49 checked) cover the full body, including the dorsal, pectoral and pelvic fins and the
    tail.
  - The thin barbels at the snout and faint translucent fin edges may be missed by a few px.
- **Fish size**, frames 5-71:
  - Snout to tail tip (bbox_w): median 582 px, range 539-627, because the tail flaps.
  - Height including fins (bbox_h): 293 px (290-294).
  - Mask main-axis length: about 579 px. Width across the axis: about 274 px.
  - For a known fish length, use bbox_w (median 582). Use a specific frame's value if the question names a time.
- **Fish motion:** almost purely along −x; y is constant at about 642 (drift < 2 px).
  - Head-template shifts are precise to about 0.1 px (match score ≥ 0.88).
  - Bbox and centroid centres jitter ±5 px per frame because of the flapping tail. **Use ref_x for speeds and
    distances.**
  - Per-frame |dx|:
    - frame 1: 0.0 (frame 1 is a duplicate of frame 0)
    - frames 2-11: about 22.0-22.4
    - rising to about 23.3-23.5 at frames 19-25
    - falling back to about 22.0 by frames 38-50
    - frames 51-70: about 22.1-22.5
    - frame 71: 0.0 (the fish is frozen while the background keeps animating, so the animation ended)
  - Net and path length, frame 0 to 71: about 1549 px (straight line, so path ≈ displacement).
  - Under the reference convention (backward difference), speed is 0 at frames 1 and 71. Note this if a question
    asks about t = 0.04 s or t = 2.96 s.
- **Fish origin:** the rig origin is unknown and is assumed near the body centre. Differences in position are
  independent of this choice because the fish only translates. Absolute positions relative to other objects carry
  about ±30 px uncertainty along x.
- **Static objects:** boxes were read from a gridded frame, ±15-20 px.
  - Seaweed stalks are thin and partly hidden behind the coral.
  - Seaweed 1 is cut by the bottom edge of the frame.

## Ambiguities
- Several similar seaweed stalks are numbered left to right (1-5).
- The coral "rock" (pale dome) is distinct from the dark branching coral in front of its left side.
- There are no shadows of the fish on the floor that matter, and no occlusion of the fish.
