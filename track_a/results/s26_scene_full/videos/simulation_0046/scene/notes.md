# simulation_0046: measurement record

This is a Blender render of a 3D street scene. It runs at 33 fps, has 99 frames (t = i/33, 0 to 2.97 s) and is 1920x766 px.
All values are in image pixels (x right, y down) and seconds. No metric scale is assumed.

## Scene
- **Camera: static.** I phase-correlated the facade against the median background and the shift is below 0.01 px in every frame. The camera looks roughly perpendicular to a street. Facade and curb lines are horizontal in the image. The horizon is above the frame.
- **Depth order, near to far:** pink parked bicycle (ground contact y≈680), then the cyclist (wheel bottoms y≈610→590), then the walker (feet y≈557), then the house fronts (base y≈545).
- **Two moving objects.** Both move right→left the whole clip.
  1. **walker**: man in a white T-shirt and light jeans with grey hair, on the far sidewalk. Visible in all frames 0-98. His reference x goes from 1685 to 1185 px, about 5 px/frame.
  2. **cyclist**: rider in a dark navy jacket and jeans on a dark-blue bicycle with a rear rack. The front wheel enters at the right edge at f2. The rider is fully in frame from f13 to f89. The front wheel reaches the left edge at f90, and the rider is still partly visible (x 0-62) at f98. Speed is about 24 px/frame at entry and about 20.5 px/frame near the end.
- **Static objects** (pixel boxes are in scene.json): pink parked bicycle at lower left (bbox 70-422 x 452-682, length 352, height 230, rear wheel diameter 120), telephone booth, two "PHOTO LAB" signs, blue shop door, trash can, "JUICE UP" box, green-house wooden door (125x265) and steps, lace-curtain window, iron fence with hedge, stone-house arched door (125x300) and gate posts with finials, and a small iron fence at lower left. These were read off a gridded median-background image and are good to about ±3 px.

## Files
- `scene.json`: inventory, camera and perspective cues, static extents, apparent-size summaries and events.
- `tracks/walker.csv`, one row per frame:
  - `ref_x, ref_y` is the pelvis estimate. x is the median x of the mask rows 20-45% of the body height from the top (the torso). y is top + 0.47·height.
  - `ref_method`, `head_x`, `head_top`, `head_top_fine` (low-threshold hair top).
  - Mask bbox, `length_px` (horizontal extent; it changes with stride), `height_px` / `height_fine_px` (head top to lowest shoe pixel), and `occluded`.
- `tracks/cyclist.csv`, one row per frame:
  - `ref_x, ref_y` is the midpoint between the two wheel hubs (≈ the bicycle root at mid-wheelbase). `ref_method` says how it was obtained.
  - `tm_scale` is the apparent size relative to frame 35.
  - Hough-circle wheel hubs and radii (`front_*`, `rear_*`).
  - Mask bbox, `wheels_x0/x1` (extent of rows y≥480), `length_px`, `height_px`, `rider_top_fine` (rider head top) and `flags`.
- `scripts/`, run in this order: `bg.py` (median background, camera check), `fg.py` (foreground mask with a shadow filter), `wheels.py`, `bike_tm.py`, `rider_tm.py`, `build_tracks.py`, `postfill.py`, `headtop.py`, `draw_tracks.py`, `write_scene.py`. `write_scene.py` deletes the 4 MB `bg.npy`, so re-run `bg.py` before re-running anything else. The `*.json` files next to the scripts are their intermediate outputs.

## Methods and reliability
- **Foreground and shadows.** Foreground is the colour difference from the median background. The sun casts shadows up and to the left; the cyclist's shadow is visible on the street even before he enters. I remove shadow pixels with a test for "darker and bluer with uniform ratio". Dark hair, shoes and the dark jacket against dark doors are sometimes lost: head and rider tops can come out 2-5 px too low, and the bbox can miss jacket pixels.
- **Cyclist reference by frame range:**
  - **f13-79:** masked multi-scale template matching of the bicycle (template from f35). This is very smooth, about ±0.5 px, and agrees with the Hough hub midpoints within about 2 px. This is the best data.
  - **f80-89:** the bike is hidden behind the pink bicycle. I tracked the rider's upper body and added +6.4 px, which is the offset measured on f76-79. Expect about ±3 px.
  - **f2-12:** leading wheel edge + 133.4 px, or Hough front hub + 83.4 px for f11-12. Expect about ±3 px.
  - **f90-98:** trailing edge − 114 px. This is poor (±10 px); the per-frame steps are erratic. Do not use it for speeds.
  - Raw Hough hubs are noisy (±3-5 px); use them only as a size cue.
- **Cyclist apparent size.** `tm_scale` falls from 1.05 (f13) to 0.92 (f79). Hough wheelbase medians are 162→156→150→143 px, and the hub row rises from y 562 to 542. So the cyclist moves away from the camera while riding left. Pixel speeds therefore shrink partly because of depth, not only because of real deceleration.
- **Cyclist geometry at f35:**
  - wheelbase 156 px, wheel diameter ≈97 px
  - length (front wheel edge to rear wheel/rack) ≈257 px
  - height from head top (y 339) to ground (y 598) ≈259 px
  - saddle/pelvis ≈ (+40, −95)·tm_scale px from the hub midpoint
- **Cyclist bbox.** In f13-33 the bbox and length include walker pixels (flagged); use the wheel hubs ± radius instead. From f73 on, the bbox shows only the visible part.
- **Walker.**
  - Gait makes `length_px` oscillate between 59 and 138 px, and the head bobs about 5 px.
  - The torso-median reference is good to about ±2 px.
  - In f13-33 (behind the cyclist) the reference is head_x + 1.95 px, and ref_y is interpolated (±3 px).
  - Apparent height is 246 px (median, f0-12), 244 (f34-60) and 242 (f61-98), with a range of 236-252. His feet stay at y≈556-561, so he walks almost parallel to the image plane and recedes only slightly.
  - He never stands still, so a "rest standing height" can only be approximated by the largest walking height (≈248-252 px).
- **Events.** There are no stops, reversals, bounces or contacts. The cyclist's reference x passes the walker's between f21 and f22 (t≈0.65 s), with the cyclist in front of (nearer the camera than) the walker. The walker overlap lasts f13-33. The cyclist is behind the pink bicycle from f73.

## Ambiguities
- The "origin" of the cyclist could be the bicycle root or the rider's pelvis. Both are rigidly linked, so speeds are the same; positions differ by the saddle offset above.
- There are two bicycles: the moving dark-blue one (cyclist) and the static pink one at lower left.
- Shadows of both people fall to the left on the hedge, sidewalk and street. They are not part of the objects.
