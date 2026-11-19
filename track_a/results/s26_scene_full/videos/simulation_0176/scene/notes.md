# simulation_0176 — measurement record (pixels, seconds)

3D Blender render, 1920x1080, 24 fps, 40 frames (t = frame/24, 0–1.625 s). Tropical sea scene: a tall tree-topped
rock sea-stack on a pale sandbar (centre-left), a turquoise sea, and a blue sky. A white twin-engine jet with its landing gear down
flies right to left across the upper sky. It is the only moving object. Its shadow also moves across the sea at lower right.

## Files
- `scene.json`: inventory, static extents, camera, horizon and events.
- `tracks/airplane.csv`: one row per frame from 0 to 38 (the plane is not visible in frame 39). Columns:
  - `cx_centroid, cy_centroid`: mask centroid.
  - `cx_bbox, cy_bbox`: bbox centre.
  - `x0, y0, x1, y1, bbox_w, bbox_h`: mask bbox.
  - `axis_len, axis_wid, axis_angle_deg`: PCA main-axis length (nose to tail), width across it, and tilt (+ means the right/tail end is higher).
  - `area_px`, `cut_by_frame_edge`, `occluded` (always 0, because nothing occludes the plane).
- `tracks/airplane_shadow.csv`: centroid, bbox and area of the plane's dark shadow on the water, with a `reliable` flag
  (1 for frames 16–25 only).
- `scripts/track_plane.py`: does the background subtraction (per-pixel median of all frames) and the tracking.
  `scripts/static_objs.py` measures the horizon and the static boxes. `scripts/finalize.py` writes scene.json.

## Method and reliability
- **Camera: static.** Phase correlation of the rock region against frame 0 gives shifts of at most 0.01 px over all frames.
- **Airplane mask:** pixels that differ from the median sky by more than 18 (max over BGR channels), followed by a morphological close.
  The largest blob is kept, plus nearby small blobs such as the landing-gear wheels. I checked the overlays at frames 0, 8 and 28
  (they are in `frames/`, which is scratch). The mask covers the fuselage, the T-tail fin, the engines and the gear.
  - The nose glazing is slightly translucent, and the horizontal stabiliser tip is faint, so the extents may be
    under by a few px at the ends.
  - The plane is fully in frame only for **frames 7–30**. In frames 0–6 it is entering at the right edge (the tail fin enters at frame 6/7).
    In frames 31–38 it is leaving at the left edge (the nose reaches x = 0 at frame 31). In cut frames the bbox and centroid are biased, so do not use them as the origin.
  - Origin proxy: use the bbox centre or the centroid in frames 7–30. They differ by up to about 7 px vertically because of the tail fin and gear.
    The Blender origin is probably close to the fuselage middle, roughly the bbox centre in x and slightly below the bbox centre in y.
  - Motion is steady to the left and slightly downward in the image. The centroid moves about 64 px/frame near frame 8 and about 54 px/frame near frame 28,
    and its y rises from about 127 to 166 px. These are image measurements only; I did not fit any motion model.
  - Motion blur is strong in the early frames (frame 8 looks ghosted), which slightly inflates the length along the motion direction.
- **Apparent size vs time (3D cue):** the nose-to-tail length (`axis_len`) falls steadily from 501 px (frame 7) through 456 (frame 16)
  to 425 px (frame 30), a ratio of about 0.85. The height (`bbox_h`, fin top to gear bottom) falls from 107 to 95 px.
  So the plane is moving away from the camera as it crosses (its depth grows by about 18% if the size is inversely proportional to depth).
  Part of the early length comes from blur. The best "clean" sizes are around frame 16, where the plane is near the image centre: length 456 px, bbox 453 x 100 px.
  The plane is seen side-on, so its wingspan cannot be measured.
- **Shadow:** dark core that is more than 25 grey levels below the median water. Over open water (frames 16–25) it moves about 60 px/frame
  leftward at y ≈ 980–995. From frame 26 on it runs into the rock's shadow and the beach, so those rows are unreliable. The waves add noise.
- **Static objects** (frame 16 grid, ±10 px):
  - Rock island including trees: x 510–1075, y 522 (treetop) to about 1020 (base on the sand), so about 565 x 498 px.
    The bare rock tower spans x 695–1050 and y 600–1020.
  - Sandbar: x about 344–1300, y 956 to the bottom edge (it is cut by the frame).
  - Horizon (sea/sky boundary): y = 0.0244·x + 867, which is y 867 at the left edge and 914 at the right. It tilts by 1.4°, so the camera is slightly rolled. The horizon sits well below the image
    centre (y 540), so the camera pitches up slightly. The plane, at y ≈ 120–170, is far above the horizon.
- **Events:**
  - Frame 0: the nose enters at the right edge.
  - Frame 7 (t = 0.292 s): the plane is fully visible.
  - Frame 31 (1.292 s): the nose reaches the left edge.
  - Frame 38 (1.583 s): last partial view.
  - Frame 39: the plane is gone.
  - There is no bounce, contact or direction change.
- **Ambiguities:** the plane is the only vehicle, and there are no people, animals or birds. Its shadow could be mistaken for a second object.
  The median background contains a faint shadow trail on the water. The early frames are motion-blurred.
