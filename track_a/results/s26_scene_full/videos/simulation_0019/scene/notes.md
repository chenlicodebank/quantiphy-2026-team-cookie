# simulation_0019 — measurement record

**Video:** Blender simulation, 3D scene, 1080x1080, 97 frames at 33.264746 fps (t = frame / fps).
**Orientation:** the render is rotated 90°. World up points to image −x: the person's head is at the left and the feet are at the right.
- World-vertical sizes (heights) are measured along image x.
- The walking direction is image +y (downward), parallel to the back wall.

**Camera:** static. Phase correlation on the wall shows less than 0.03 px drift, so no per-frame background shift is needed.

## Files
- `scene.json`: inventory of all objects with image bounding boxes and pixel extents, camera and perspective cues, events.
- `tracks/person.csv`: the only moving object. One row per frame (0–96):
  - `pelvis_x, pelvis_y`: the reference point.
  - `ref_source`:
    - `measured`
    - `measured_torso_legs_hidden`
    - `linear_fit` (an estimate while occluded)
  - Mask bounding box.
  - `height_px`: head top to lowest foot, along x.
  - `stride_extent_px`: mask extent along the walking direction.
  - `torso_width_px`: shoulder band.
  - `mask_area`.
  - `lead_y` / `trail_y`: visible front and back edges along the walk.
  - `occluded`: none, partial, full or feet_maybe_hidden.
- `scripts/`:
  - `bg.py`: camera-motion check.
  - `track_person.py hybrid`: median-background subtraction with shadow suppression. It writes the masks `_person_masks_hybrid.npz`, which were deleted to save space; rerunning recreates them.
  - `person_csv.py`: builds the CSV.
  - `check_pelvis.py` / `inspect_mask.py`: visual overlays.
  - `wall_grid.py`: wall beam positions.
  - `cleanup.py`.

## How it was measured and how reliable it is
**Person mask**
- Method: difference from a full-resolution median background (the person never covers the same pixel for more than half the clip). Morphological cleanup, then the largest connected group is kept.
- Shadow: the person's shadow is a thin streak on the floor just right of the feet (x ≈ 785–815). It was removed by a darker-but-same-colour test plus a rule for x ≥ 770 that keeps only near-black shoe pixels.
- Visual checks of overlays: the mask covers head to shoes. Small holes appear in the white shirt where it matches the background. The white soles at the far right are sometimes lost, so foot x may be 2–5 px short.

**Pelvis (reference point)**
- x = head_x + 0.5 × (feet_x − head_x), which is ≈ 646–657 and fairly constant.
- y = mean mask y in the band from 30% to 50% of the body length below the head top, which is the hip region including the arms hanging alongside.
- Uncertainty:
  - About ±10 px along the body axis, because the 0.5 fraction is anatomical, not measured.
  - About ±3 px along the walk, from gait and arm swing.
- Frames 89–93: only the leading part of the torso is visible, so pelvis_y may be biased by +3 to +7 px.
- Frames 51–88: pelvis comes from a linear fit of all measured frames:
  - pelvis_y = 198.08 + 5.601 × frame px, rms residual 3.3 px.
  - Frames 0–50 alone give 5.51 px/frame.
  - The jump from frame 50 to 94 implies 5.75 px/frame.
  - Treat the walk as approximately constant speed with a gait ripple.
- Person depth looks constant: they walk parallel to the wall and the image plane, and apparent height shows no trend (median 255 px, range 243–261; lower values occur at mid-stride when the legs are spread).
- Any depth_info for the person should therefore be nearly constant through the clip.

**Static objects**
- Bounding boxes were read from grid crops (frame 67, background frame). Accuracy is about ±3 px.
- Main sculpture: its left tip (x ≈ 393) blends into the grey wall, so expect about ±8 px there.
- The middle painting is mostly hidden behind the sculpture.
- The top sculpture and the bottom dark object are cut off by the image edges.

**Perspective**
- The wall's horizontal beams sit at constant x for every y, and the wall columns are spaced evenly (≈ 214 px).
- So the wall and the walking direction are almost parallel to the image plane, and no usable vanishing point exists.
- The camera looks slightly down (the floor is visible at image x > ~650).
- The person (feet at x ≈ 780) is behind the main sculpture and pedestal: they hide the person, and the pedestal's floor edge at x ≈ 895 is closer to the camera.
- One px/m scale cannot be applied across the person and the sculpture or pedestal, because they are at different depths.

## Events
- The person walks through the whole clip: already moving at frame 0 and still walking at frame 96. There is no start, stop or turn.
- Occlusion:
  - Starts at frame 51.
  - Fully hidden in frames 59–77.
  - Head glimpsed in frames 78–83, legs in 84–88.
  - Head and torso back from frame 89, nearly complete in 94–96.
- Gait, from `stride_extent_px`:
  - Widest stride at frames ≈ 0, 15, 30, 47.
  - Feet together at frames ≈ 6, 22, 40.
  - Step period ≈ 16–17 frames.

## Ambiguities
- The sunlight patches and shadows on the floor are static and are not objects.
- There are three paintings on stands (upper, middle, lower), told apart by position.
- There are two sculptures: the large grey one in the centre and the small bronze one at the top edge.
- No other object moves.
