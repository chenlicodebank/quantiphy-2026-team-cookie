# simulation_0030_segmented — measurement record

3D scene, segmentation video (Blender render, background replaced by plain white), 960x960, 25 fps, 75 frames
(t = frame/25, frame 0 at t = 0). All values are pixels / frames; no metric scale assumed.

## Files
- `scene.json` — inventory, camera, events, bird apparent-size summary, terrain extents.
- `tracks/bird.csv` — one row per frame 0-74. `visible`=0 for frames 40-74 (bird gone). Columns: `ref_x, ref_y` =
  mask centroid (reference point); `bbox_*` axis-aligned box (inclusive pixel coords, `bbox_w/h` = extents);
  `mask_len_main_axis` / `mask_width_across` = PCA-axis extents of the mask, `main_axis_deg` its angle (image
  coords, 0 = horizontal); `area_px`; `occluded_or_cut`=1 when the mask touches the image edge (frames 37-39);
  `ref_x_flapavg, ref_y_flapavg` = centroid averaged over a centred 14-frame window (one wing-beat), only where the
  whole window is uncut (frames 7-29).
- `terrain_static.json`, `terrain_mask.png` — static mound mask (from frame 74) and its extents.
- `scripts/track.py` (segmentation + track), `scripts/overlay.py` (check montage), `scripts/finalize.py`
  (flap-averaged columns, camera check, scene.json).

## Objects
1. **bird** (only moving object): small dark grey/black-brown flapping flyer, upper half of image. Visible frames
   0-39; fully in frame 0-36; leaves across the right edge at frames 37-39 (cut, centroid biased left), absent 40-74.
   Already in flight at frame 0. Moves left→right almost horizontally: centroid x ≈ 381.2 + 15.33·frame,
   y ≈ 281.2 + 0.13·frame (frames 0-36); per-frame centroid Δx varies ~14-17 px and y oscillates ±~12 px with the
   wing beat (wings up: frames ~0, 10-12, 23-25; wings level/spread: ~5, 17-18, 31-32; period ~12-14 frames ≈ 0.5 s).
   Apparent size: bbox width 20-35 px (max 35 at f31, wings spread), height 9-35 px (max 35 at f23-24 wings up),
   mask main-axis length 24.6-39.1 px. Same-phase sizes grow only ~5-10% over the clip → depth roughly constant,
   maybe slightly approaching the camera. Bird is seen roughly from behind/side, wings sweeping up and down.
2. **terrain_mound** (static): pale pink/cream rock/sand landform in the image centre, darker eroded texture on its
   right end. bbox x 228-813 (586 px wide), y 382-511 (130 px tall); mask centroid (501.7, 448.7). Long axis nearly
   horizontal; bottom edge from (231,478) to (812,505). Viewed obliquely from slightly above, so its image height mixes
   true height and depth.

## Camera
Static: terrain region shift vs frame 0 ≤ 0.15 px over all frames (phase correlation). No ground plane, horizon or
vanishing lines (white background); the only perspective cue is the mound's top surface being visible (camera slightly
above it). Focal length unknown — must come from a question's depth_info + known size.

## Events
f0 (0.00 s) bird already flying; f37 (1.48 s) bird starts to be cut by the right edge; f39 (1.56 s) last visible
sliver; f40 (1.60 s) onward nothing moves. No contacts, bounces or direction changes (steady horizontal flight).

## Reliability / ambiguities
- Bird mask: threshold on non-white pixels above y=380, verified visually on every frame (montage) — covers full
  body and wings, small antialiased fringes excluded (±1 px on extents).
- The simulation origin (body/pelvis) is not directly visible; the mask centroid moves with the wings (vertical
  ±~12 px, horizontal ±~2 px). For speeds, prefer the flap-averaged columns or a fit over whole wing-beats; frame-to-frame
  centroid differences are noisy. Frames 37-39 centroids are biased by edge cut — do not use for motion.
- Wingspan/width questions: use bbox_w (max 35 px at f31 / ~33-34 px at f5, f32) and min (20 px at f12).
- Terrain mask threshold is low (pale object); edges ±2 px.
