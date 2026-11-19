# simulation_0236 — measurement record (pixels, seconds)

2D simulation (Blender), 1080x1920 portrait, 24 fps, 50 frames (t = frame/24, 0 to 2.042 s).
Scene: one chestnut horse walking left to right, side-on, in front of a two-storey half-timbered house on a grass
field. **The camera is static**: frames 0 and 49 differ by only 2–4 grey levels (compression noise) in the sky, house
and grass. Pixel coordinates are image coordinates (x to the right, y down).

## Files
- `scene.json`: inventory, static extents, horse size summary, events and camera.
- `tracks/horse.csv`: one row per frame (0–49):
  - `ref_x, ref_y`: **recommended reference point**, the horse's trunk midpoint (between buttock and breast, about
    mid-depth of the body). Measured by chaining frame-to-frame template matches of an interior torso patch
    (correlation 0.94–0.998, sub-pixel), anchored at (225, 958) in frame 0. Total shift is 154.2 px in x and +0.15 px
    in y.
  - `rump_edge_x`: sub-pixel buttock edge (saturation crossing, median over rows 940–965). This is a second,
    independent x track: 155.2 px over frames 0→49. `back_line_y` is the top edge of the mid-back.
  - `rump_mask_x`: left-most mask pixel; this includes the tail, so it sits a few px further left: 164 px over frames 0→49.
  - `mask_cx, mask_cy, bbox_*, mask_length_px, mask_height_px, area_px`: from the segmentation mask. The bbox and
    lengths are **not reliable**: the pale grey face is often missed, and from frame 29 on stray brick blobs or holes
    appear. Use the keyframes for size.
  - `occluded`: always 0. The horse is fully visible in every frame and nothing passes in front of it.
- `tracks/horse_keyframes.csv`: extremities read by hand on 3x zoomed crops with a 10 px grid (±2–3 px) at frames
  0, 12, 25, 37 and 49: rear x (tail/buttock), nose x, ear-top y, hoof-bottom y.
- `scripts/`: track_horse.py (mask + background model), trunk.py, rump_subpix.py, torso_match.py, check_rump.py,
  zoom.py, draw_check.py, build_record.py (writes horse.csv, the keyframes and scene.json).

## Horse (the only moving object)
- Size in px:
  - Length nose-to-rear ≈ **182 ± 3** (keyframes 182, 182, 181, 182, 185).
  - Height ear top to hoof ≈ **162 ± 3** (ears ≈ 880–885, hooves ≈ 1043–1047).
  - Withers/back height ≈ 120–125.
  - Trunk (buttock to breast) ≈ 123.
  - Body depth ≈ 50–55.
  - The horse walks across the image plane, so its apparent size stays constant.
  - In some strides a hind hoof reaches slightly behind the buttock, and the pose changes the head position by a few px.
- Motion: walks to the right for the whole clip. It is already moving at frame 0 and still moving at frame 49, with
  no stop, start or turn.
  - Mean horizontal step is ≈ 3.15 px/frame (torso track) or 3.17 (buttock edge). The two tracks agree to about 1 px
    over the clip.
  - Per-frame torso steps oscillate between about 1.3 and 5 px with the gait. Frames 14–17 and 38–43 are the
    extremes, and part of that may be template noise; correlation dips to 0.89 at frame 17.
  - Vertical motion is under ±2 px, so treat it as horizontal.
- Rig origin: where the rig's origin sits is unknown. The trunk midpoint is the best guess for a quadruped's root or
  pelvis region. Any trunk point gives the same displacement up to the gait wobble.

## Static objects (frame 0, ±5 px)
- **House**:
  - Overall x 180–900 (720 px wide) and y 270 (roof apex) to 1040 (base), 770 px tall.
  - Roof eaves x 218–866, bottom edge y 478. Upper storey x 200–880, y 630–830.
  - Brick ground floor x 250–830 (580 wide), y 845–1040 (195 tall).
  - Three arched windows, each 64x105 px, at y 845–950: x 272–338, 508–572 and 744–808. The horse walks in front
    of the left and part of the middle-left facade.
  - Upper central wooden door x 462–620, y 632–790.
- **Red flowers** in the grass: centroids (325, 1247), (975, 1662) and a small blob at (1018, 1709).
- Grass field from y ≈ 990 down. The grass/sky line is at y ≈ 988–995 left of the house. Cloudy sky.

## Reliability and ambiguities
- **Horse x displacement and track:** good, about ±1–2 px per frame and ±1 px cumulative.
- **Horse length and height:** ±3 px, from manual reads.
- **Pale face:** the face looks pale and semi-transparent, and its nose tip is fuzzy (±3 px).
- **Tail:** the tail hangs at the rump and makes the rear edge ambiguous by ~5 px. The buttock edge excludes the
  tail; the mask and keyframe rear include it.
- **Shadows:** no strong cast shadow on the ground.
- **Motion blur:** slight, mainly on the legs.
- **Scale:** no metric scale was assumed.
