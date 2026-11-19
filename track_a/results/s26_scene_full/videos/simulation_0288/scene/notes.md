# simulation_0288 – measurement record

2D simulation (Blender render), 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).
All values are in pixels and frames. No metric scale is assumed anywhere.

## Scene content
- **koi_fish**: the only object in the scene. One koi carp seen from directly above. Its body is orange/red and white with a
  few black spots; the head is a translucent pale pink shape and the fins are white and grey. The head points LEFT and the
  fish swims from right to left, roughly along image row y ≈ 725–770.
- **fish_shadow**: the fish's dark-grey cast shadow on the ground. It moves with the fish. Early in the clip it is offset
  up and to the right. Late in the clip it lies up and to the LEFT, ahead of the nose. Do not mistake it for the fish:
  the shadow's tail reaches about 100–150 px beyond the fish's real tail tip.
- **ground_plane**: a plain light-grey background with a vignette (brighter in the centre). It has no markings and there
  are no other objects.
- **Camera**: static, top-down, with no perspective cues. A median background reproduces every frame to within 9 grey
  levels (sum over RGB) away from the fish and its shadow.

## Files
- `scene.json`: inventory, manual extents, summary numbers and events.
- `tracks/koi_fish.csv`: one row per frame (0–71). Columns:
  - `frame`, `time_s`
  - `body_cx, body_cy`: centroid of the body-core mask. The mask is the saturated orange or white pixels brighter than
    the background, closed, hole-filled, largest component. It excludes most of the fins and the translucent nose and
    tail.
  - `match_x, match_y`: a smoother position. It accumulates `match_dx, match_dy`, the frame-to-frame shift of the front
    55 % of the body found by template matching on the Lab a* channel, with subpixel precision (score ≥ 0.95). This path
    is offset so that its mean equals the mean `body_c*` over frames 12–71. **Use this column for speeds, accelerations
    and path lengths.** Its per-frame |d| is 23.5–24.0 px/frame. `body_c*` differences jitter by ±3 px/frame because the
    mask edges change. The two positions drift apart by about 10 px over the clip, because the body bends as it swims.
  - `cx, cy, bbox_*, length_main_axis, width_across, axis_angle_deg, head_*, tail_*, area_px`: the automatic "full fish"
    mask (the part of the fish+shadow union that is not shadow-dark). **It misses the grey translucent tail tip and parts
    of the fins**, so its length (about 510–630 px) is too short. Use the manual extents below for sizes. `head_x` is
    reliable up to about frame 36. After that the nose lies over the shadow and the mask nose sits 15–30 px behind the
    real nose.
  - `touches_frame_edge`: 1 only for frame 0. Through about frame 10 the tail fin is cut off by the right edge or close
    to it, so the auto mask extents are clipped there.
  - `shadow_cx, shadow_cy`: approximate centroid of the dark-shadow pixels.
- `scripts/`:
  - `probe.py`: background median; it also regenerates `frames/bg720.npy`, which `seg.py` needs.
  - `seg.py`: masks and track (`seg.py N …` also writes overlays to `frames/ovNN.png`).
  - `match.py`: template-match track. Run it after `seg.py`.
  - `zoom.py`: gridded crops used for manual reading.
  - `check.py`, `dup.py`: frame-to-frame differences.
  - `drawtrack.py`: draws the track for visual checking.
  - `write_scene.py`: builds `scene.json`.

## Fish size (manual, read by eye from 1.6x gridded crops, ±4 px per point)
| frame | nose (x,y) | tail-fin tip (x,y) | nose→tail px | upper / lower pectoral fin tip | fin span px | bbox w×h px |
|---|---|---|---|---|---|---|
| 12 | 1776,761 | 2446,739 | 670 | 1971,648 / 1993,879 | 232 | 670×231 |
| 24 | 1503,766 | 2163,735 | 661 | 1719,666 / 1728,919 | 253 | 660×253 |
| 36 | 1210,704 | 1866,751 | 658 | 1444,649 / 1437,911 | 262 | 656×262 |
| 48 | 937,705 | 1584,783 | 652 | 1175,621 / 1134,850 | 233 | 647×229 |
| 60 | 658,717 | 1316,782 | 661 | 894,614 / 875,851 | 238 | 658×237 |
| 71 | 436,733 | 1099,757 | 663 | 666,617 / 666,857 | 240 | 663×240 |

- **Fish length (nose to tail-fin tip):** about 661 px (mean, range 652–670). The tail fin bends while swimming. The fish
  points within about 10° of the x axis, so the axis-aligned bbox width is about the same as the length.
- **Width:**
  - Across the pectoral fins: 230–262 px. This is the bbox height and is largest at frame 36, when the fish is yawed and
    the fins are spread.
  - Trunk without fins: about 150–160 px by eye. The body-core mask height has a median of 198 px, but it includes the
    fin bases.
- **Body-core mask:** about 475–525 px long (it excludes the translucent nose and tail).

## Motion and events
- **Frames 0 and 1 are identical**: the fish is still. Motion starts at frame 2 at full speed, with a per-frame shift of
  about 23.9 px.
- **Per-frame displacement:** nearly constant. From the template match: 23.9–24.0 px/frame in frames 2–15, a slight dip
  to about 23.6 px/frame in frames 19–40, and 23.8–23.9 px/frame by frame 70.
- **Path:** slightly S-shaped.
  - vertical drift:
    - y increases by about 2 px/frame until frame 19
    - about 0 in frames 20–26
    - y decreases by about 2 px/frame in frames 27–49
    - about 0 from frame 50 on
  - heading (`axis_angle_deg`) turns from about +177° to about −169° (nose up) near frames 36–42, then back to about −178°
    by frame 71.
- **Frame 71 is almost a copy of frame 70** (shift 0.15 px), so the motion effectively ends at frame 70. Speeds taken at
  t = 2.958 s (frame 71) are about 0. This hold looks like a render artefact.
- **Total path:** frames 0→71, from match_x ≈ 2294 to ≈ 654 (about 1640 px) at nearly constant y.
- There are no bounces, impacts or contacts.

## Reliability and ambiguities
- **Motion:** the template-match track is very reliable, to about 0.1 px/frame. Its absolute position depends on the
  choice of reference point. The rig origin is not visible; it is probably inside the trunk, close to `body_c*`.
- **Sizes:** the manual nose and tail values are good to about ±1 %. Pale fin tips against the grey background and the
  grey translucent tail tip make exact edges uncertain by a few px.
- **Shadow:** it is separate from the fish. Do not use it for sizes.
- **Motion blur:** none noticeable.
