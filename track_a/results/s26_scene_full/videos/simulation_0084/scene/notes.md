# simulation_0084: measurement record

**Scene:** 2D Blender render, 1920x1080 px, 24 fps, 72 frames (3.0 s). A static top-down camera looks at a uniform grey ground (RGB 158). There are no markings or props. Two cars drive horizontally in parallel lanes, in opposite directions, and pass side by side at the end:
- **dark_car**: dark grey/black body with a white front, lower lane (centreline y=637.5). Front points right; moves +x from x≈215 to 1184.
- **yellow_car**: yellow body, upper lane (centreline y=525.5). Front points left; moves −x from x≈1880 (estimated) to 1188.5.

## Files
- `scene.json`: inventory, extents, lanes, events, camera, key positions.
- `tracks/dark_car.csv`, `tracks/yellow_car.csv`: every frame 0–71, with frame, time, cx, cx_est, cy, bbox (including mirrors), length_px, width_incl_mirrors_px, body_width_px, truncated_at_edge, reference_reliable, occluded. The two cars never occlude each other or anything else.
- `scripts/`:
  - `track.py`: raw per-frame segmentation.
  - `yext.py`: y extents.
  - `finalize.py`: fixed y values, per-frame steps, passing gaps.
  - `add_est.py`: centre estimate for edge-cut frames.
  - `overlay.py`, `gapview.py`: visual checks.
  - `probe*.py`: threshold probes.

## How it was measured
- **Mask:** `gray<113 or gray>176 or saturation>40`. This excludes the soft grey shadow, which only gets down to about 116 and extends about 10 px ahead of and below each car, while keeping the white nose and dark outlines.
- **x extents:** measured per frame from core body rows only (yellow 480–570, dark 600–685).
- **Reference point:** cx = midpoint of the x extent (bumper to bumper); cy = lane centreline, which is constant because y never changes.
- **Origin:** the Blender origin is assumed to be the car's geometric centre. If the rig's root were at an axle, positions would only shift by a constant, so displacements and speeds are unaffected.
- **Checks:** overlays at frames 0, 36, 60 and 71 show the boxes on the full car (nose to rear, mirror to mirror) and no shadow.

## Motion (raw facts only; no fitted models)
- Both cars are in exactly the same position in frames 0 and 1. Each starts moving between frames 1 and 2, then moves at a constant pixel step to the end of the clip:
  - dark_car: +13.84 px/frame (steps 13.5/14; mean over frames 1→71 = 969/70).
  - yellow_car: −9.9 px/frame (front bumper steps −10, with an occasional −8/−12 from rounding; cx mean over frames 12→71 = −584/59 = −9.90; front-bumper mean over frames 1→71 = −688/70 = −9.83).
- No vertical motion, no direction change, no bounce or impact.
- **Speed as defined by the benchmark:** the backward-difference speed is 0 at frame 1 and at the constant value from frame 2 on. So the speed jumps between frames 1 and 2. If a question asks for acceleration, it is 0 apart from that start-up step.

## Events
| Event | Frame | Time |
|---|---|---|
| Motion starts | 1→2 | 0.042–0.083 s |
| Yellow car fully in view | 12 | 0.5 s |
| Front bumpers aligned / passing begins (x≈1163) | 60 | 2.5 s |
| Near-side mirrors pass each other, no contact (motion unchanged) | ≈66–67 | ≈2.75 s |
| Centres 4.5 px apart in x (crossing ≈ frame 71.2) | 71 | 2.958 s |

Centre distance between the cars: 1669 px at frame 0 (using the estimated yellow centre); 112.1 px at frame 71 (dy = 112 lane separation).

## Reliability and ambiguities
- **Dark car:** x extents are ±1 px in every frame.
- **Yellow car, frames 0–11:** its rear is cut off by the right image edge. `cx` there is the centre of the visible part only and is wrong. `cx_est` = front bumper + 137.25 px, which assumes a length of 275.5 px. It is good to about ±3 px and follows the same −10 px/frame step. Use `cx_est`.
- **Perspective:** car lengths vary about 4% with x position. They are largest near the image edges and smallest near the centre, an effect of the car's height under a perspective camera.
  - Dark car: 275 → 264 px.
  - Yellow car: 276 → 268 px.
  - For a length prior, use the length at the asked frame from the CSV, or the mid-clip values (dark ≈268, yellow ≈272).
  - Widths: yellow 116 px with mirrors / 92 px body; dark 115 px with mirrors / 86 px body.
  - Height cannot be measured from a top-down view.
- **Camera:** the background is textureless, so camera motion cannot be checked directly. It is taken as static, which the perfectly constant car steps support.
- **Reflections, not texture changes:** the glass and roof of both cars reflect the other car during frames 60–71. The roofs look different there, but this does not affect the extents.
- **Shadows:** the soft shadows mostly extend below and ahead of the cars and were deliberately excluded.
- **No metric scale is assumed anywhere.** It is a single 2D plane, so use one metres-per-pixel factor taken from the question's prior.
