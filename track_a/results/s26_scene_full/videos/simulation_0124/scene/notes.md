# simulation_0124 – measurement record (pixels and seconds only)

**Scene:** 2D simulation (Blender), 24 fps, 72 frames (3.0 s), 1080×1080. Static top-down camera looking straight
down on an S-shaped two-lane road. Two cars drive from the top edge to the bottom edge. No metric scale is given
here. Because the camera looks straight down, one metres-per-pixel factor from a question's prior applies to the
whole ground plane.

## Objects
| name | how to tell it apart | moves | frames visible |
|---|---|---|---|
| `silver_car` | silver/white car with two red racing stripes. It is the **following** car (left one at frame 0) | yes | 0–60 (fully in frame 4–55) |
| `dark_car` | dark blue-black car with amber headlights. It is the **leading** car (right one at frame 0) | yes | 0–49 (fully in frame 3–45) |
| road | S-shaped asphalt road with white edge lines, a yellow dashed centre line and a white/dark striped kerb on the outer (right) side | no | all |
| trees | clumps along the right side. The clump at x 585–870, y 665–890 hangs over the road | no | all |
| grass field | dry grass inside the bend (left half of the image) | no | all |

Body sizes (top view, rigid, constant for the whole clip):
- **silver_car:** length 122 px, width 47 px (±2). The door mirrors make it about 51–53 px wide.
- **dark_car:** length 117 px, width 46 px (±4).

The length/width ratio of the silver car is 2.60. The dark car is about 4 % shorter than the silver car. That
difference is close to the uncertainty, so if a question uses one car's length as the prior and asks for the
other's, give the measured pixel ratio (117/122 = 0.96) and its uncertainty.

## Files
- `scene.json`: inventory, camera, events, static objects, sizes and visible frames.
- `tracks/silver_car.csv`, `tracks/dark_car.csv`: one row per frame in which the car is visible.
  - `cx, cy`: the reference point, i.e. the centre of the top-view body. This is the best image estimate of the car's origin.
  - `heading_deg`: the direction the car's front points, as an image angle (0 = right, 90 = down).
  - `bbox_*`: the axis-aligned box of the rotated L×W body rectangle. It can extend beyond the image when the car is partly out of frame. `bbox_vis_*` is the same box clipped to the image.
  - `length_px, width_px`: the rigid body size.
  - `mask_len_px, mask_wid_px`: the extents of the background-difference mask in that frame. They are filled in only for frames where the mask is clean (no cast shadow, fully in frame).
  - `visible_frac`, `frac_out_of_frame`, `frac_tree_occluded`, `occluded`: how much of the car is visible, outside the frame or behind trees, and a combined flag.
  - `match_score`, `method`, `reliability`: tracking quality and how each frame was measured.
- `scripts/`: every script. In order: `bg.py` (median background → `bg.png`), `track.py` (rotation-aware template tracking), `assemble.py` (merges segments → `poses.csv`), `extents.py` (per-frame masks → `extents.csv`), `avgtpl.py` / `avgprof.py` (averaged aligned crops used to fix the body outline, centre and size), `make_tracks.py`, `occlusion.py`, `steps.py`, `framediff.py`, `road.py`, `rotcrop.py` (viewer).

## How it was measured
- **Camera:** compared against a median background. The car-free last frames differ from it by 0.13 grey levels, with no shift, so the camera is static and there is no background shift to correct.
- **Tracking:** each car is matched with a car-aligned colour template, searching position and rotation, with sub-pixel peak refinement. Image area outside the frame is masked out.
  - **silver_car:** one template from frame 24. Match scores are 0.7–0.98.
  - **dark_car:** the car is dark on a dark, tree-shadowed road, so I used two templates: one from frame 9 for frames 0–27 and one from frame 38 for frames 28–45. Their centre conventions differed by 2.1/1.2 px and were reconciled using the 20 overlapping frames, where they agree to about 1–2 px.
  - **Checks:** averaging the aligned crops over 43–52 frames gives a sharp car image, so the tracks are consistent frame to frame. The rectangles drawn on frames match the cars (frames/overlay_sheet.png, a scratch file outside this record).
- **Edge frames:** where only part of the car is in the image (silver 56–60, dark 46–49), the angle is fixed by linear extrapolation and only the position is matched against the visible part. These frames are marked `reliability=low` and can be off by about 2–5 px; the last one or two frames are the worst (silver steps 20.3 and 17.6 px instead of 22.2).
- **Entry frames:** frames 0–3 (car partly above the top edge) are `medium` but agree well: the per-frame steps match the later steps within 1 px.
- **Body size and centre:** read from grey-level profiles of the averaged aligned crops: the outline edges, plus the stripe symmetry for the silver car and the headlight symmetry for the dark car. The corrections from template centre to body centre were (−1.5, −0.5) px for silver and (+1, +0.5) px for dark, in car-local coordinates.
- **Tree occlusion:** the share of green foliage pixels inside the car rectangle. This is a lower bound, because shaded foliage is missed. At frame 32 about 40 % of the dark car is visibly covered.

## Events (frame / time)
- **Frames 0 and 1:** identical (frame 1 duplicates frame 0). Both cars stand still, so the step between frames 0 and 1 is 0.
- **Frame 2 (t = 0.083 s):** both cars start moving at once at their full step. There is no visible acceleration phase.
- **During the clip, per-frame displacement is nearly constant** (computed only as a quality check):
  - silver: 22.25 ± 0.2 px/frame
  - dark: 26.95 ± 0.3 px/frame (ratio 1.21)
  - The path curves, so path length is longer than net displacement.
- **Bend:** both cars go round the right-hand bend at the top right (heading passes straight down at about frame 15 for the dark car and frame 18 for the silver car), then head down-left. Heading peaks at about 130° (silver, frames 38–42; dark, frame 31) and turns back to about 100–110° near the bottom.
- **Separation between the two centres:** 90.6 px at frame 0, 103 px at its minimum (frame 20), then growing to 199 px at frame 45 because the dark car is faster.
- **Exits:** the dark car leaves through the bottom edge in frames 46–49 (last visible at frame 49, t = 2.042 s). The silver car leaves in frames 56–60 (last visible at frame 60, t = 2.5 s). Frames 61–71 show the empty road.

## Static objects (pixel extents, from scripts/bg.png)
- **Road:** about 180–196 px wide between the white edge lines, measured perpendicular to the road (rough, ±10). It is roughly 1.5–1.6 car lengths wide. It enters at the top at x ≈ 350–700, reaches x ≈ 867 at the outer edge of the bend (y ≈ 300), and leaves at the bottom at x ≈ 265–470.
- **Trees and grass:** positions are given in `scene.json` as rough extents. I did not measure individual trees, kerb blocks or dash lengths.

## Ambiguities and caveats
- **Origin vs. body centre:** the reference point is the centre of the visible body outline. A Blender car rig's root may sit elsewhere (for example at the rear axle or on the ground under the centre). For a constant-speed car this does not change speeds, but positions and distances between cars could differ by up to about half a car length if the rig root is not central. Because the cars turn, speeds can also change slightly (about 1 %).
- **Shadows:** cast shadows fall forward and to the left of each car. They inflate raw difference masks, which is why the stated sizes come from the averaged crops and not from per-frame masks. `mask_len/mask_wid` are left blank wherever the shadow touched the mask.
- **Dark car:** its outline is less certain (±4 px in size, about 1–2 px in centre), especially in frames 29–37, when it is under trees and in shadow.
- **Similar objects:** none. The two cars are easy to tell apart by colour, and there are no other movers.
