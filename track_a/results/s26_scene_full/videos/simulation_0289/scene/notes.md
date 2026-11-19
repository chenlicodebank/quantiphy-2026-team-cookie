# simulation_0289 — measurement record

Video: Blender render, 2D scene, 2560x1440, 24 fps, 72 frames (t = frame/24, frame 0 at t = 0). All values are in
pixels (x to the right, y downward) and seconds. No metric scale is assumed.

## Scene
- **koi_fish**: the only moving object. A single white/grey koi with orange-red patches, a pinkish (flat-shaded) head
  and long pale fins, seen side-on. It swims right to left, parallel to the image plane, at a constant height
  (bbox centre y ≈ 642, trunk y ≈ 639). There are no other animals or props.
- **fish_shadow**: a dark, elongated soft shadow on the floor at y ≈ 1330–1370. It follows the fish about 40–60 px to
  its right. Do not confuse it with the fish.
- **backdrop_floor**: a seamless light-grey cyclorama with a vignette and no markings. There are no static objects
  with measurable extents.
- **Camera**: static. The per-pixel median background is clean and shows no shift.

## Files
- `scene.json`: inventory, extents summary, motion summary in px, events, camera.
- `tracks/koi_fish.csv`: one row per frame (0–71). Columns:
  - `cx_bbox, cy_bbox`: centre of the mask bounding box. This is the proxy for the object origin.
  - `cx_mask, cy_mask`: mask centroid.
  - `x0 y0 x1 y1, bbox_w, bbox_h`: bounding box. `x0` is the snout tip, `x1` the tail-fin tip, `y0` the dorsal-fin
    top, `y1` the lowest fin tip.
  - `axis_len, axis_wid, axis_angle_deg`: PCA extents of the mask.
  - `area_px`.
  - `truncated_by_frame_edge`: 1 in frames 0–3, when the tail is cut by the right edge.
  - `occluded`: always 0.
  - `body_x, body_y, body_match`: a subpixel template-match track of a rigid trunk texture patch (scales and red spots
    under the dorsal fin), with match score ≥ 0.82.
- `tracks/fish_shadow.csv`: same columns except the body columns. Truncated at the right edge in frames 0–17.
- `scripts/track.py` (threshold 14), `scripts/body_patch.py`, `scripts/summarize.py`: these regenerate everything.

## Method
Each frame is segmented by subtracting a background: the per-pixel median of every 4th frame, using the max-channel
difference > 14, followed by morphological open/close. Components with centre y < 1150 are the fish; the rest is the
shadow. I checked the overlays at frames 0, 12, 36, 60 and 71. The mask covers the whole fish, including the fins.
A few very pale fin-edge pixels may be missed, so the bbox could be ≈ 1–3 px too small.

## Key numbers (px)
- **Fish size, fully visible (frames 4–71)**:
  - Height (bbox_h) is 290–292 and constant.
  - Snout-to-tail-tip length (bbox_w) grows steadily from ≈ 590 (frames 4–12) through 613 (frame 36) to ≈ 643
    (frames 60–71). This is most likely the tail fin extending or animating. Mean 617, median 613.5.
  - The body axis tilts about 5.5° (head slightly higher than tail, in image coordinates).
  - If a question gives the fish's length, use bbox_w at the time it names. If no time is named, the median ≈ 613
    (frame 36) is a reasonable default; note the ±5% variation.
- **Motion**:
  - Frames 0 and 1 are identical (static), motion starts at frame 2, the last motion is at frame 70, and frame 71
    duplicates frame 70.
  - The motion is purely horizontal and leftward. Trunk x goes from 2269.4 (frame 1) to 707.5 (frame 70); bbox centre
    x goes from 2293.5 to 779.5.
  - Trunk per-frame step: ≈ 22.0 px (frames 2–17), rising to ≈ 23.4 (peak ≈ 24.1 around frames 20–28), then
    ≈ 22.3 (frames 41–70). Mean over frames 2–70 is 22.64 px/frame.
  - The bbox-centre step averages 22.33 px/frame. It is lower because the box grows toward the tail, so its centre
    drifts about −0.7 px/frame relative to the trunk.
  - Trunk path length over frames 1–70 is 1561.9 px.
- **Shadow**: length 735–824 px (its faint thin tip is unstable), height ≈ 37–45, cy ≈ 1347.

## Events
| Event | Frame | t (s) |
|---|---|---|
| Static start | 0–1 | 0–0.042 |
| Motion start | 2 | 0.083 |
| Tail fully in frame | 4 | 0.167 |
| Speed peak | ~25 | ~1.04 |
| Motion end | 70 | 2.917 |
| Duplicate of frame 70 | 71 | 2.958 |

There are no bounces, impacts or contacts.

## Reliability and ambiguities
- **Positions**: ±0.5 px for the trunk track; ±1–2 px for the bbox.
- **Which reference point**: the true origin of the fish rig is unknown.
  - The bbox centre is the best match to "origin = centre". It mixes in the fin animation, though, and in frames 0–3
    it is biased by the truncation.
  - The trunk track is the best estimate of rigid-body motion.
  - For speeds, the two differ by about 1.5% on average.
- **Duplicate frames**: because frames 0–1 and 70–71 are duplicates, the speed at t = 0.042 s and at t = 2.958 s is
  0 by the backward-difference convention.
- **Scale**: one scale for the whole scene is appropriate, since this is a 2D scene and the fish stays at a constant
  depth (its height is constant).
