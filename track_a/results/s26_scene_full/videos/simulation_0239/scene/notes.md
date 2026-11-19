# simulation_0239 – measurement record

Video: 1920x1080, 24 fps, 50 frames (t = frame/24, 0–2.042 s). Source: simulation, labelled **2D**.
View: overhead (bird's-eye) camera looking down at a house with a cross-shaped tiled roof and two horses
walking on the lawn just south (below, image +y) of it. Image axes: +x right, +y down. All values are in pixels and seconds.

## Files
- `scene.json`: inventory, static extents, camera, events, per-horse summaries (net displacement, path length, sizes).
- `tracks/brown_horse_mask.csv`, `tracks/white_horse_mask.csv`: one row per frame (0–49). Columns:
  `cx,cy` = centroid of the colour mask (body + head where detected); `torso_cx,torso_cy` = centroid after a 13x13
  erosion (drops thin legs/neck/tail; steadier, but sits slightly toward the rump: for the brown horse ~6 px behind `cx`);
  bbox (inclusive pixel coords) and `bbox_w,bbox_h`; `mask_length_main_axis`/`mask_width_across` = PCA extents of the
  mask (main axis is ~2° from horizontal, i.e. along +x); `mask_area_px`; `occluded` (always 0).
- `scripts/`: `track.py` (masks, tracks, overlays), `house.py` (roof outline), `strip.py` (frame strips + background
  shift check), `zoom.py` (gridded zooms), `probe.py` (colour probe), `write_scene.py` (builds scene.json).

## Objects
1. **brown_horse** – chestnut horse with a white face blaze, the upper one (y≈776), right under the roof edge. It walks
   toward +x, head at its right end. Visible in all frames. About 2.6 px/frame (noisy step to step, -2 to +5 px, because of the
   gait and mask). Torso goes from x 745.9 (frame 0) to 863.9 (frame 48): net 118 px, framewise path 124 px. y is almost
   constant (776→778).
   **Event: at frame 49 the animation loops and the horse jumps back to its frame-0 position** (Δx ≈ −125 px). This is
   not real motion: use frames 0–48 for any kinematics.
   Size: nose-to-rump ≈ 143 px at frame 0 (zoom check: x 695–838), width (top-down) ≈ 40 px (y 755–795). Median mask
   length is 144 px. It grows to 150–164 px when a hind leg is stretched back (frames 27–32, 46–48).
2. **white_horse** – cream/white horse, the lower one (y≈865). It is larger, moves faster and has a dark tail at its left (rear) end
   and a greyish muzzle at its right end. Moves toward +x, head right. Visible and inside the frame in all frames. Steady speed:
   about 4.6 px/frame (3.6–5.9 per step). Torso x 969.4 → 1192.8 (frames 0–49): net 223 px, path 225 px. y sways
   ±3.5 px (868→861→868→861) with the gait.
   Size: tail-tip to muzzle ≈ 175 px at frame 0 (x 892–1067). Body without the tail starts at x≈903 (≈165 px). Width ≈ 50 px (y
   843–893). The colour mask misses the dark tail and the grey muzzle, so mask length (median 138 px, 131–159) is
   shorter than the full body. Use the zoom value for "length" questions.
3. **house** (static) – roof outline at frame 0: bbox x 616–1427, y 19–745 (centroid 1024,394). Main block (runs
   top-bottom): x 660–1363 (703 px wide), y 19–745 (726 px). Cross gable (runs left-right): x 616–1427 (811 px), y ≈270–520
   (250 px). The roof is far above the ground, so it is closer to the camera and its outline shows perspective (top eave corners at
   y≈90 rise to the ridge apex at y≈19, x≈1025). **Its pixel sizes are not on the horses' ground-plane scale.**
4. **lawn / tree shadows** (static): bright yellow-green grass on the right and dark tree shadows on the left and bottom. There are no
   markings, other props or animals.

## Events
- Frames 0–48: both horses move steadily toward +x the whole time. No start, stop, contact or direction change.
- Frame 49 (t = 2.042 s): the brown horse resets (teleports) to its start position. The white horse continues normally.
- Relative distance between the torso centres: 241.8 px at frame 0 and 335.1 px at frame 48.

## Camera
Static. Phase correlation of the roof and lawn against frame 0 gives <0.02 px of shift in every frame. Both horses are on
the same flat ground at nearly the same depth, so one m/px scale (from the prior's horse) should hold for both. The roof is
at a different depth, so its scale differs.

## Reliability and caveats
- Centroids are ±1–2 px per frame. The legs, head bobbing and mask edges add noise to each step (the brown horse especially), so
  per-frame speeds of the brown horse are noisy. Averages over several frames are reliable to a few %.
- The rig origin (pelvis/root) is not directly visible. The torso centroid is the best proxy, and `cx` (full mask) sits a
  few px further forward. The difference is a constant offset, so it does not affect displacements.
- There are no shadows in the masks: the horses stand in tree shade. The white horse's own soft shadow lies along its lower edge and is
  excluded by the brightness threshold.
- Masks and tracks were checked visually on overlays (frames 0, 12, 24, 30, 36, 47, 49).
