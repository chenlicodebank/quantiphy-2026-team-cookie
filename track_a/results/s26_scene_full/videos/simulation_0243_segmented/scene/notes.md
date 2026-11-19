# simulation_0243_segmented – measurement record

2D scene. Segmentation video, 1080x1920, 30 fps, 75 frames (t = frame/30, 0 to 2.467 s). The camera is static:
the tree region shifts by less than 0.06 px between frames.

## Content
- **animal** (the only moving object): a dark quadruped (horse/goat-like creature) with a large curved horn/crest
  sweeping back from its head, a pale muzzle and a long tail with a tuft. Side view, facing right. It walks steadily
  to the right for the whole clip and is fully visible and never occluded in frames 0-74.
- **tree** (static): a conifer crown at the left edge, cut off by the image border, with a small trunk stub at
  x≈60-95, y≈1300-1367. Seen at frame 74: x 0-498, y 367 (spire) to 1367, so the visible height is ≈1001 px. The
  width is truncated by the edge. The tree's base sits about 180 px above the animal's hooves, so it is probably a
  more distant background object and not in the animal's plane. Do not use it for scale unless a question gives its size.
- There is no ground, no markings and no other objects. The background is white.

## Files
- `scene.json`: inventory, size summary, events and camera.
- `tracks/animal.csv`: one row per frame (0-74), all values in px:
  - `torso_cx`: midpoint of the torso's horizontal extent (`torso_x0`..`torso_x1`), taking the longest mask run
    per row over the band y = 1340-1390 (chest to rump; this leaves out the tail and legs). Most stable x reference.
  - `cx_centroid`, `cy_centroid`: mask centroid (includes horn, legs and tail).
  - `bbox_*`: mask bounding box. It runs from the tail tuft or rump at the left to the muzzle tip at the right, and
    from the horn top to the hooves.
  - `torso_len`: chest-to-rump length.
  - `muzzle_tip_x` (= bbox_x1), `top_y` (horn top), `feet_y` (lowest hoof).
  - `pca_len`, `pca_wid`: extents along and across the mask's main axis.
  - `area_px`.
  - `occluded`: 0 in every frame.
  - `torso_top_y`, `torso_bottom_y`: `torso_bottom_y` (belly, ≈1377) is fine. `torso_top_y` is unreliable, because
    the sampled column often runs up into the neck or horn.
- `scripts/measure.py` (masks + tracks + overlays), `scripts/static.py` (tree extents, camera check),
  `scripts/summarize.py` (statistics), `scripts/look_tree.py` (tree-edge montage).

## Method
The background is the last frame with the animal's pixels blanked to white. The animal mask is the set of pixels
that differ from this background by more than 22 grey levels. Near-white pixels over the tree are excluded, because
they are segmentation halo, not animal. The mask is then cleaned morphologically, the main blob kept and interior
holes filled. I checked the overlays at frames 0, 15, 30, 60 and 74: the mask covers the full animal silhouette
(horn, muzzle, legs, tail). While the animal is in front of the tree (frames 0 to about 45), a few dark patches on
the back and neck match the dark foliage and are missed. They touch the outline, so they stay unfilled. This
lowers the area and shifts the centroid by a few px in those frames, but the bbox and the torso band are unaffected.

## Key numbers (px)
- Motion: about 6.4-6.5 px/frame to the right (≈195 px/s). The linear fit of torso_cx gives 6.55 px/frame. The
  quadratic term is about 0, so the speed is essentially constant. Per-frame steps scatter by ±1-2 px (gait
  and mask noise).
- Net displacement from frame 0 to 74: torso_cx 349.5 → 826.0 (476.5 px); centroid 363.3 → 834.4 (471.1 px);
  muzzle tip 556 → 1040 (484 px). Vertical drift is negligible (centroid y 1332 → 1325, hooves at y≈1546 throughout).
- Size:

  | Measure | Median | Range |
  |---|---|---|
  | Overall height, horn top to hooves | 411 | 403-420 |
  | Overall length, tail tuft to muzzle (bbox width; changes with tail swing and stride) | 481 | 412-508 |
  | Torso length, chest to rump | 268 | 260-274 |
  | Belly line y | 1377 | – |
  | Body height, belly to hooves | ≈170 | – |

  The apparent size is constant, as expected for 2D motion.

## Events
- The animal is already walking at frame 0 and still walking at frame 74.
- There is no start, stop, contact or direction change.
- The animal overlaps the tree area during roughly frames 0-45.

## Caveats
- The rig's origin (root) is not visible. For speed or displacement, any body-fixed point gives the same answer
  within about 1 px/frame. torso_cx is the smoothest; the centroid is the closest to a centre of mass.
- Which extent a "length" question means is ambiguous: body without tail (rump at the belly band to muzzle tip) median 344 px, range 330-352 (`scripts/bodylen.py`), torso 268 px, bbox
  including tail ≈ 481 px. For height questions, use horn top to hooves (≈411 px) as the world-bbox height, and
  belly or back heights as alternatives.
- The visible tree outline changes over time; this is a segmentation artefact.
