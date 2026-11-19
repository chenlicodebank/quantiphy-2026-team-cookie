# simulation_0249: measurement record

**Video:** simulation (Blender), 2D scene, 24 fps, 50 frames (t = 0 … 2.0417 s), 1920×1080. All values are in pixels and seconds. No metric scale is assumed.

## Scene
- **View:** the camera looks straight down at a featureless light-grey ground with a radial vignette. Three animals walk toward image right (+x), each in its own horizontal lane. Motion lies in the ground plane, which faces the camera, so one m/px scale applies to the whole image. Heights cannot be observed from this view.
- **Camera:** static. There is no background texture to register against, but the vignette and the soft shadows stay put, and the lanes do not drift. No per-frame shift was applied.
- **Static objects:** none. The ground is uniform, with no markings or props.

## Objects (all visible and unoccluded in frames 0–49)
| name | how to tell it apart | lane (cy px) | length along x (px, median [min–max]) | width across (px) |
|---|---|---|---|---|
| brown_horse | dark reddish-brown horse, top lane, white muzzle at right, dark mane stripe | ~345 | 246 [232–274] | 75 [71–82] |
| tan_horse | tan/beige horse/donkey-like animal, middle lane, the largest in pixels | ~486–500 | 295 [277–316] | 87 [84–94] |
| small_brown_animal | small orange-brown rodent- or pup-like animal, bottom lane, ahead of the tan horse | ~608 | 64 [58–74] | 33 [32–36] |

All three heads point to +x. Length is measured nose-to-tail along the main axis of the mask (axis angle about 0°). Length varies with the leg and tail pose during the gait. The median is the best estimate of body length.

## Tracks (`scene/tracks/<name>.csv`, one row per frame 0–49)
**Columns:**
- `frame`, `time_s`
- `cx_bbox`, `cy_bbox`: centre of the bounding box. This is the **default proxy for the object origin**.
- `cx_mask`, `cy_mask`: centroid of the mask.
- `cx_core`, `cy_core`: centroid of the torso after a morphological opening that strips the legs, head and tail. This is the steadiest proxy for the root.
- `bbox_x0`, `bbox_y0`, `bbox_x1`, `bbox_y1`, `bbox_w`, `bbox_h`
- `len_main_axis`, `width_across`, `axis_angle_deg`, `area_px`, `n_parts`, `occluded` (always 0)

**Rough rates (bbox centre):**
- tan_horse: 984.5 → 1364.5 (+380 px over 49 frames, about 7.8 px/frame), with cy drifting 500 → 486 → 500 → 486.
- small_brown_animal: 1118.5 → 1492.5 (+374 px, about 7.6 px/frame), cy constant at 608.
- brown_horse: 626.5 → 832 by frame 48 (+206 px, about 4.3 px/frame).

Per-frame steps are noisy, about ±3–5 px, because the legs, head and tail swing during the walk cycle. Smooth the steps or use the core centroid before differencing.

## Events
- **Frame 0:** all three animals are already walking. Nobody starts or stops inside the clip.
- **brown_horse, frames 46–48:** almost stationary (cx 832, 832, 832).
- **brown_horse, frame 49:** it snaps back to exactly its frame-0 pose and position (cx 626). This is an animation-loop or root reset, not physical motion.
  - For speed or distance over the clip, use frames 0–48 for this horse and treat 48→49 with care.
  - A reference built by naive differencing would see a jump of about −206 px at frame 49.
- **No contacts or collisions:** the lanes stay separate.

## Method and reliability
- **Background** (`scripts/build_bg.py`): a degree-4 polynomial fitted to frame 0 away from the animals (residual σ ≈ 1.1 grey levels). It is saved to `frames/bg.npy` and can be regenerated.
- **Mask** (`scripts/track.py`): chroma ≥ 7, or darker than the background by more than 55, or brighter by more than 6, followed by morphological open and close and hole filling. Components are assigned to animals by lane.
  - Soft shadows are neutral grey (chroma 0), so they are excluded. This was confirmed on overlays at frames 0, 12, 24, 36 and 48 (`frames/ov/`); the masks hug the bodies.
  - **Known bias:** the white or grey muzzle tips of both horses are almost background-coloured, so the front edge can be short by about 5–20 px (worst on the tan horse, e.g. frame 24). Horse lengths may therefore be underestimated by up to about 5%. Dark tails and hooves are included.
  - The small animal is accurate to about ±2 px.
- **Origin:** the true Blender origin cannot be seen in a top-down view. For the horses, the bbox centre sits ahead (+x) of the core centroid by 13–37 px (median about 23–25 px), because the head and neck extend forward. For the small animal the two differ by about 1–2 px. Displacements over many frames are nearly identical with either choice.
- **Regenerating:** `frames/bg.npy` was deleted to keep scratch files small. Run `build_bg.py` before `track.py`.
- **Other scripts:** `summarize.py` (per-frame dumps), `strip.py` (crop strips for inspection), `probe.py` (pixel probe), `write_scene.py` (builds `scene.json`).
