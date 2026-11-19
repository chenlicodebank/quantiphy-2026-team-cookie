# captured_0052x — measurement record (pixels, seconds)

Lab clip (24 fps, 49 frames, 1280x720, 3D). The copy given is a SAM2 segmentation: the background is flat green,
the face is masked green, and there is a watermark at the bottom right. A crouching person in black pushes a large dark-grey
**exercise ball** toward the camera. The ball rolls down and to the left, gets bigger as it comes closer, and leaves
through the bottom-left edge (last seen at frame 44). Static objects: blue **recycling bin**, **basketball**, white **shoe**.
The camera is static.

## Files
- `scene.json`: inventory, static extents, events, camera notes.
- `tracks/exercise_ball.csv`, one row per frame 0-44:
  - `cx, cy, diam`: circle fitted to the ball's free silhouette edge. This is the reference point (the visible centre).
  - `bbox_*`, `mask_w/h/area`: foreground pixels inside 1.04 x the circle.
  - `n_fit_pts`, `arc_coverage_deg`: how much edge supports the fit.
  - `cut_by_frame_edge`.
  - `occluded_or_touching`: 1 for frames 0-26 (ball against the person) and for frames cut by the image edge
    (33-44).
- `tracks/person.csv`, frames 0-48: centroid and bbox of the visible person mask, head-top y, and a touching-ball flag
  (a loose dilation test, so it is too generous). `occluded` = 1 throughout, because the bin always hides the lower legs.
- `static_objects_raw.json`: per-object median bbox, centre and stability over all frames.
- `scripts/`:
  - `common.py`: decoding and green-screen mask.
  - `track_ball.py`: circle tracking.
  - `statics_person.py`
  - `contact.py`: gap test. Its result was not informative; release was timed visually.
  - `montage.py`: viewing crops.

## Method
The foreground is every non-green pixel. For the ball, I took the outer contour points that border the green screen
(not the image edge), kept those within a tolerance of the circle predicted from the last frame, and fitted a
least-squares circle with tolerances tightening from 25% to 4% of r. I checked overlays at frames 0-44: the circle
lies on the ball's outline.

## Reliability
- **Ball, frames 0-32:** good. Centre ±2 px, diameter ±3 px.
  - Frames 0-19: the right/top edge is hidden by the person's arms and body. The fit uses the left and bottom arcs.
  - Rest diameter is about 132 px (129-134).
  - Frames 10-17 show ±4 px of centre/diameter wobble while the person shifts their grip. This is not real motion.
- **Ball, frames 33-44:** cut by the bottom edge. The fit uses only the upper arc, and the SAM mask there is uneven and
  flattened, so `diam` (and cy) are rough, roughly 10-30%. Frame 44 (diam 465) is unreliable. Prefer bbox top
  `bbox_y0`, `bbox_x0/x1` and the arc fit only as a guide.
- **Converting to metres:** with given depths, use f = 762.8 px, principal point (640,360). Ball size from apparent
  diameter: D ≈ diam·Z/f. 3D centre: X = (cx-640)·Z/f, Y = (cy-360)·Z/f (Z ≈ depth for rays near the axis; use
  depth/√(1+((u-640)²+(v-360)²)/f²) for the exact Z).
- **Events:**
  - Push starts about frame 18 (±1).
  - Release (hands off) about frame 21 (±1).
  - The ball touches the person's knees until about frame 26.
  - The ball is out of view from frame 45.
- **Person:** the mask centroid moves with the arms. The lower body is hidden by the ball (frames 0-28) and the bin, so
  the bbox bottom (585) is not the feet. The person crouches the whole clip; no standing height is visible.
- **Statics** (bbox, px):
  - Bin: 98 w x 104 h, centre (729,534).
  - Basketball: 92 px wide (bottom touches the frame edge), centre (802,672).
  - Shoe: bbox 69x62, about 78 px heel-to-toe along its diagonal, centre (286,658). Hidden behind the ball in frames
    36-41.

## Ambiguities
- The ball's dark lower half and the person's black clothes have similar colours. This is why I fitted a circle to
  the free edge instead of using colour.
- There are no shadows (background removed). Mild motion blur at frames 36-44.
