# simulation_0172: measurement notes

**Scene.** A 3D Blender render, 80 frames at 24 fps, 2304x1296 px, with a black letterbox from row 1195 down. One astronaut in a white suit with a backpack hops and walks from left to right across a grey lunar plain under a black, starry sky. The camera is static: a ground strip shifts (-0.08, +0.03) px between frame 0 and frame 79. There are no other moving objects and no props. The only other things a question could name are the ground plane, the terrain ridge where sky meets ground, the stars, and the astronaut's own cast shadow.

## Files
- `scene.json`: inventory, camera, perspective cues, events, size examples.
- `tracks/astronaut.csv`: all 80 frames. Columns:
  - `cx, cy`: mask centroid.
  - `x0 y0 x1 y1`: bounding box (inclusive). `y0` is the helmet top and `y1` is the lowest foot.
  - `bbox_w`, `bbox_h`, `area`.
  - `main_axis_len`, `across_width`, `main_axis_deg`: PCA extents of the mask. The main axis is close to vertical, about 76-81°.
  - `occluded`: always 0.
- `tracks/astronaut_shadow.csv`: the cast-shadow core per frame, with `gap_feet_to_shadow_top_px` = shadow `y0` minus astronaut `y1`. Use it as a ground-contact indicator.
- `scripts/`:
  - `bg.py`: median background from every 4th frame, plus the camera check.
  - `track.py`: segmentation and tracks; writes overlays to `frames/ov_XX.png`.
  - `static_and_overlay.py`: ridge line and the `frames/track_overlay.png` check image.
  - `probe.py`: pixel probes and a table printer.

## Method
- **Astronaut mask.** Each frame is compared with the median background.
  - Against the sky, a pixel counts if grey > 40 and it differs from the background by more than 30. The suit has a bloom halo that fades smoothly from about 50 grey to 0; the threshold removes it but keeps the shaded far leg, which is 41-65 grey.
  - Against the ground, a pixel counts if it differs from the background by more than 30 and is either not darker than the ground or 45-85 grey (shaded suit).
  - The cast shadow (grey ≤ 45) is excluded, along with a 4 px rim around it.
  - Interior holes, such as the dark visor, are filled.
- **Checks.** Overlays were inspected at frames 0, 10, 11, 20, 30, 42, 50, 51, 53, 60, 66, 70 and 79. The mask covers the whole suit, including the backpack, hands and boots, without the halo or the shadow.

## Reliability
- **Centroid.** Smooth to about 1-2 px per frame, and the path in `frames/track_overlay.png` is clean.
  - The centroid is a proxy for the pelvis/root. The backpack, at the rear on the left, pulls it slightly up and back, so the true pelvis is probably a few tens of px lower and/or to the right.
  - The mask centroid tracks the body well, but the absolute pelvis offset is uncertain by about ±30 px.
- **Bounding box.** Good to about ±3 px.
  - In a few frames the dark far boot is partly lost where it is very dark against the sky (about 30 grey, e.g. frame 42 lower-left boot), so `x0`/`y1` can be a few px short.
  - Against the ground, a sliver of the darkest boot sole adjacent to the shadow can be lost.
- **Heights change with pose.** The suit is never in a rest standing pose:
  - frames 0-14 (knees bent in the air): about 340 px
  - frames 15-18 (crouched landing): 345-355 px
  - frames 30-50 (legs spread): 405-418 px
  - frames 60-79 (upright walking): 400-440 px. The most upright frames are 76-79, at about 438 px.
- **Apparent size grows** about 1.2x from start to end (sqrt of the area ratio for f79/f0 is 1.205) because the astronaut also comes toward the camera. The feet/shadow ground rows move from y ≈ 1024 to about 1047-1060.
- **Shadow track.** Fine, except at frame 66, where `y0` = 1008 because a dark boot touches the shadow (gap -43 there is spurious).

## Events
See `scene.json` for the full list.
- Frame 0: the astronaut is already in the air, descending.
- Frames 15/16-18: ground contact (crouch). The lowest centroid is at frame 15.
- Frame 19: take-off.
- Frames 35-37: apex. The helmet top is at y = 507 and the feet are 102 px above the shadow.
- Frame 58: landing.
- Frames 59-79: on the ground, stepping and decelerating.
- The astronaut moves only in +x.

## Ambiguities
- The sky/ground edge is a nearby curved ridge, not the true horizon.
- The shadow is offset to the left of the feet, so it is not directly under the body.
- The focal length is unknown; use depth_info plus a known size to set the scale.
