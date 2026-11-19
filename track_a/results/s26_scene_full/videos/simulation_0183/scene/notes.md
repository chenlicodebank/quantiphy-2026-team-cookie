# simulation_0183 – measurement record

2D Blender scene at 24 fps, 45 frames (t = 0 … 1.833 s), 1920×1080. The camera is static. One object moves: a **crate**, a black hard case with a green lid, a red light and "DS" labels on its front. It starts at rest in mid-air at upper left (centre at (571.0, 329.5) px) and falls straight down. It hits the blue ramp, tips onto it and slides down to the right. At the last frame it is still on the ramp and still moving.

## Files
- `scene.json`: the inventory (moving and static objects), events, camera notes and static pixel extents.
- `tracks/crate.csv`: the **main track**, one row per frame 0–44. Columns:
  - `x, y`: centre of the crate's projected rectangle. Use this as the crate origin.
  - `angle_deg`: in-plane angle of the long axis, measured clockwise on screen.
  - `bbox_*`: axis-aligned image box of the rotated 335×190 rectangle.
  - `length_px, width_px`: the nominal rectangle, 335 × 190.
  - `fit_ncc`: fit quality.
  - `template`: which template produced the row.
  - `occluded`: 1 means the lower edge is hidden by or merges with the ramp.
- `tracks/crate_mask.csv`: visible-mask measurements from background differencing (centroid, minAreaRect, bbox, area) plus the per-frame camera shift (≈0).
- `tracks/crate_phase1.csv`: intermediate fit using the frame-0 template. Only valid for frames 0–12, because it loses the crate after frame 34.
- `static_auto.json`: ramp edge line fits and the colour-threshold boxes for the sign and the orange frame.
- `background.jpg`: median background at half resolution.
- `scripts/`, in run order:
  1. `track.py`: background, mask and camera check.
  2. `fit_template.py`: phase-1 fit.
  3. `fit_slide.py`: phase-2 fit, then merges both into crate.csv.
  4. `static.py`: static objects and per-frame step printout.

## Method and reliability
- **Crate track.** The track is a rigid template fit: masked normalized cross-correlation over translation and in-plane rotation, with sub-pixel peak refinement. Two templates are used:
  - **Frames 0–11** use the frame-0 appearance (NCC 0.73–1.0).
  - **Frames 12–44** use a template cut from frame 24 on the ramp (NCC 0.74–1.0). The crate looks different on the ramp: it tips slightly toward the camera, shows more of its green lid and is shaded.
  - **Shared reference point.** The frame-24 template is anchored to the frame-24 centre found by the phase-1 fit, so both phases use the same point. Over frames 10–34 the two fits agree to within about 1 px.
  - **Precision.** Expected accuracy is about 1 px frame-to-frame. The absolute centre on the ramp is good to about 3–5 px, because the bottom edge is hidden.
  - **Checks.** Overlays of the rectangle and track were inspected at frames 13, 24/28 and 44, and they sit on the crate.
- **Crate size.** At frame 0 the crate is axis-aligned against the plain wall, so its size is clean there: 335 px long (horizontal) × 190 px high, bbox x 404–738, y 235–424. A looser threshold gives 341 × 191, because the right edge is soft. Size questions should use frame 0.
  - On the ramp, the visible-mask extents in crate_mask.csv come out too small (about 327 × 165, area 38k vs 59k px²). The dark underside blends into the dark-blue ramp, so those values understate the crate's size.
  - Frames 0–7 of crate_mask.csv are reliable (length 337–340, height 184–190).
- **Static objects.** The ramp edges are line fits to blue pixels in frame 0. Over x 760–1280 the top back edge gives slope 0.568 (29.6°), with a residual of 6 px. The crate slides along 28.4°, a direction between the ramp's back edge and its front face; the extra slope of the back edge comes from the slight top-down view. The sign, vent, shelf, post and cardboard boxes are bounding boxes read by eye from a 100-px grid (±5–10 px).

## Events (frame / time)
| Event | Frame | Time | Evidence |
|---|---|---|---|
| Release from rest | 0 | 0.000 s | First vertical step is 2.4 px, then 6.7, 11.1, 15.5, 19.6, 24.0, 28.4: a uniform increase of about 4.4 px per frame, with the first step about half of it. |
| Free fall | 0–7 | 0–0.292 s | x stays at 571.0 and the angle at 0. |
| First contact with the ramp | 7→8 | 0.333 s | The lower-right corner hits the ramp. |
| Tipping onto the ramp | 8–13 | 0.333–0.542 s | The angle goes from 0° to 27.5°. |
| Full face lands | 13→14 | 0.583 s | The vertical step collapses from 24.8 to 5.0 px. |
| Rocking | 14–22 | 0.583–0.917 s | The angle peaks at 32.7° around frames 17–18. |
| Steady slide | 22–44 | 0.917–1.833 s | The crate slides along 28.4° and keeps speeding up (step about 20 → 33 px per frame). It does not reach the floor. |

## Ambiguities
- **Only one moving object.** The crate is the only thing that moves; the cardboard boxes are static props.
- **Reference point.** The rectangle centre is a 2D proxy for the 3D origin.
- **Size depends on the frame.** On the ramp the crate's apparent shape changes slightly, because it tips toward the camera.
- **Shadow.** There is no separate shadow on the wall. Shading makes the crate darker on the ramp.
- **Motion blur.** It is mild in frames 7 and 13.
