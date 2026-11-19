# simulation_0149 - measurement record

3D Blender render, 24 fps, 50 frames (t = frame/24, 0 to 2.0417 s), 1920x1080. Pixels: x right, y down.
There is no metric scale in this record. Each answering session sets it from its own prior and depth_info.

## Scene
- An underground car park (level "B1"), dimly lit. **One moving object: a yellow sports coupe** (RX-7 FD style:
  white 5-spoke rims, rear wing, California plate "PSHERO"). It starts at the back left, nearly head-on to the
  camera, and pulls away slowly from about frame 0-1. It speeds up while turning to the image right, passes
  broadside close to the camera (frames ~30-32), runs into the dark zone in front of the big foreground pillar on the
  right, and is gone after frame 47 (frames 48-49 show no car).
- There are no people, animals, balls or other vehicles. Also no bounces or impacts.
- **Camera is static.** Phase correlation of the ceiling (x 0-1450, y 0-450) against frame 0 gives |shift| <= 0.023 px
  in every frame, so no background correction is needed.

## Files
- `scene.json`: inventory (car plus static objects with pixel boxes measured on frame 49, where the car is gone),
  events, camera and perspective cues, apparent-size trend.
- `tracks/car.csv`: one row per frame 0-49 with these columns:
  - `visible`
  - `ref_x, ref_y` (= `mask_cx, mask_cy`, the visible-silhouette centroid)
  - `bbox_x0..y1, bbox_w, bbox_h`
  - `mask_len_major / mask_wid_minor` (PCA extents of the silhouette in px)
  - `mask_area`
  - `hub_front_x/y, hub_rear_x/y` (centres of the near-side wheel rims)
  - `wheelbase_px` (hub-to-hub distance in the image)
  - `touches_frame_edge`, `occlusion` (text), `quality` (good / fair / poor)
  - `ground_contact_y_est` (lowest tyre point = hub_y + 0.78 x rim height)
  - `height_px_roof_to_ground` (= ground_contact_y_est - bbox_y0)
- `tracks/car_wheels.csv`: rim detections per frame, with hub centre and rim box/width/height.
  `front_near` covers frames 10-32 and `rear_near` covers frames 20-39.
- `scripts/`: `common.py` (frame decoder), `camera_bg.py` (camera check and background),
  `segment.py` (first attempt, superseded), `segment2.py` (final mask), `wheels.py` (rims), `lines.py`
  (ceiling-tube and floor lines, vanishing point), `build.py` (assembles the tracks and makes the check sheet),
  `probe_cols.py` (debug). To rerun: camera_bg, then segment2, wheels and build. Scratch output goes to `../frames/`.

## How the car was measured
- Background: frame 49 for x<1000 and frame 0 for x>=1000 (the car is absent from each part).
- Mask: yellow-paint pixels (HSV hue 8-32, S>=120, V>=12) that differ from the background. Then: the largest
  component, plus nearby yellow components, plus strongly changed pixels above the body (roof glass); closed and
  filled.
- The mask is clipped at `ground_contact_y_est` to remove the shiny-floor reflection. That clip is only possible
  where a rim exists (frames 10-39).
- Frame 28 has one manual fix: a lit patch on the pillar base (x 1470-1630) was cut away. The real bumper ends at
  x≈1455.
- The overlays were checked by eye (`frames/final_sheet.png`). The outline fits the car well in frames 0-30.
- **Reference point:** the simulation origin (vehicle root) cannot be seen.
  - `mask_cx/cy` is the centroid of the visible body. It moves within the car as the car yaws, and it drifts once
    the front goes dark (frames 31 and later).
  - For a ground-level root between the axles, use the midpoint of `hub_front` and `hub_rear` in x with
    `ground_contact_y_est` (frames 20-32). Alternatively, track one hub; the rear hub is the cleanest in frames 23-37.
- Horizontal path in the image (mask centroid x): 259 (f0) → 305 (f10) → 504 (f20) → 974 (f30) → 1437 (f39) → 1863
  (f47). The centroid stays at about y 760-800, and the hubs stay at y 819-845 throughout.

## Reliability
- Frames 0-9: good, but the car is seen head-on. The left side of the car (x<60) sits in the dark pillar shadow.
  The tyres are dark and not in the mask, so bbox_y1 (864-888) is the bumper bottom. The true tyre bottom is about
  y 893 at frame 0.
- Frames 10-30: good (about ±5 px). The tyres are mostly outside the mask, so use `ground_contact_y_est` for the
  bottom.
- Frames 31-33: fair. The front end enters deep shadow in front of the right foreground pillar, so bbox_x1 (about
  1683-1695) is a lower bound.
- Frames 34-47: poor. The front half of the car is black and partly beyond the right edge. All extents are lower
  bounds, and the centroid is biased toward the visible rear.
- Rims:
  - The front rim is partly hidden or shaded at frames 10-16 (its height grows 54→107 partly from un-hiding) and
    again at frames 30-32 (dark).
  - The rear rim is partly hidden at frames 20-22.
  - Clean rim heights: front 17-29 and rear 23-37.
  - Hub positions are good to about ±3 px wherever a rim is detected.
- Static-object boxes come from a gridded zoom of frame 49 (about ±3 px).

## Perspective
- Vanishing point of the ceiling tubes is (4050, 829), and the floor colour edge points to the same place, so the
  **horizon is y≈829** and roll is about 0.
- The hubs sit almost on the horizon at every distance. So the camera is roughly at wheel-hub height, very low.
- The car's vertical image size grows a lot with approach: front rim 120→168 px over frames 20-29, rear rim 98→160 px
  over frames 23-36. Rim or tyre height is the cleanest yaw-independent inverse-depth cue. Tyre outer diameter is
  about 1.5 x rim height.
- Silhouette length and wheelbase mix approach with yaw. Wheelbase goes 247 px (f20) → 499 (f30) → 619 (f32); the car
  is broadside at about frames 30-32. At frame 30, broadside: silhouette x 452-1691 (about 1240 px, front end dark),
  roof y 540, ground y≈923 (rear tyre) to 958 (front tyre).
- Focal length is unknown. Estimate it from depth_info plus a known size. Car length, wheelbase, height or wheel
  diameter at a broadside frame such as 29-30 work best.

## Ambiguities
- Shiny floor: a yellow reflection under the car was excluded by the ground clip. Before frame 10 there is no clip,
  but the mask did not reach the reflection there.
- The car's headlights and body light up the floor and pillar bases (frame 28 artefact, fixed).
- "B1" is yellow paint on a background pillar, not part of the car (the mask never included it).
- No motion blur problems were noticed. Motion is smooth and continuous with no stops.
