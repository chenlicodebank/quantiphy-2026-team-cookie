# simulation_0274 – measurement record (pixels, seconds)

2D simulation (Blender), 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).

## Scene
- **Camera**: static, looking straight down at a uniform light-grey floor with a soft vignette. Background
  phase-correlation shifts are < 0.3 px for every frame (`tracks/camera_bg_shift.csv`). There are no perspective cues
  and no static objects, markings or furniture. Motion lies in the ground plane facing the camera, so one px→m scale
  from the prior applies everywhere.
- **raccoon**: this is the only object that moves. It is a grey raccoon seen from above, with a ringed tail pointing
  left and a light-grey face/head patch on the right. It walks in a straight line toward +x (image right) at y ≈ 729
  and is visible and unoccluded in all frames 0–71.
- **raccoon_shadow**: a dark (grey ≈ 60) side-profile silhouette of the raccoon, cast just above it (smaller y). It
  moves rigidly with the animal. Its head carries a light-grey patch that looks like a render artefact. It is a shadow,
  not a second animal, and should not be confused with the raccoon.

## Files
- `scene.json`: inventory, extents, events and a summary of the pixel motion.
- `tracks/raccoon.csv`, one row per frame:
  - **Reference point** `root_x, root_y`: the body centre (tail excluded). It is anchored as the median over all
    frames of (raw body centroid − registration shift), then carried to every frame by subpixel template matching of
    the raccoon band (y 712–764) against frame 36. Its frame-to-frame jitter is about ±1–2 px,
    caused by leg and gait deformation.
  - `body_cx/cy`: the raw per-frame centroid of the body without the tail. It is noisier (it jumps by up to ±15 px when
    the legs merge into or split from the mask). Prefer `root_*`.
  - `mask_cx/cy`: the full-mask centroid.
  - Bounding box `bbox_*`: covers nose to tail tip, raccoon only. `mask_len_main_axis` and `mask_width_across` are PCA
    extents. The main axis is about 0° (horizontal).
  - `occluded` = 0 in every frame.
  - `reg_dx/dy/score`: the registration output.
- `tracks/raccoon_shadow.csv`: centroid, bounding box and area of the shadow.
- `scripts/`:
  - `track.py`: median-background segmentation and raccoon/shadow separation.
  - `register.py`: template registration and camera check.
  - `write_scene.py`, `check_overlay.py`, `strip.py`, `summ.py`, `probe.py`: assembly, visual checks and diagnostics.

## Key numbers (px)
- **Length nose to tail tip**: median 296 (range 282–304, varies with gait and tail swing). Without the tail (tail base
  to nose) it is about 189; the tail is about 102. These two values were read off frame 24 and are good to ±5 px.
- **Body width across** (top view, flank to flank): about 60–62. The bottom edge is clean at y ≈ 757–758. The top edge
  touches the dark shadow, so it is less certain (±3 px). In frames 61, 62 and 68–71 `mask_width_across` and `bbox_y0`
  are inflated (68–77) by shadow leaking into the mask; ignore width in those frames.
- **Height**: cannot be seen in a top-down view.
- **Motion**:
  - The raccoon is stationary at frames 0–1 (the two frames are almost identical).
  - Motion starts between frames 1 and 2 (t ≈ 0.083 s).
  - From then on it walks at a steady 20.58 px/frame mean root step (std 1.2, with no trend, so speed is essentially
    constant). The nose (bbox_x1) also advances about 20.6 px/frame.
  - Root goes from (772.4, 729.7) at frames 0–1 to (2212.6, 729.1) at frame 71: net 1440.2 px, path length
    1440.5 px. Vertical drift is under 1 px.
  - There is no stop, turn, bounce or contact event. The raccoon is still in view at the end.
  - Gait period is about 15 frames.

## Reliability
- **Raccoon x position and steps**: good, ±1 px per frame. **Lengths**: ±3–5 px.
- **Root definition**: the true rig origin is not visible. The body centre is the best proxy, and any constant offset
  cancels out in speeds and displacements.
- **Shadow separation**: uses grey-level thresholds (shadow < 75, raccoon fur 85–160, face patch 165–185). The dark
  rings of the tail and the dark rump fur are sometimes mislabelled as shadow, which affects body_cx and the mask top
  but not root_x.
