# simulation_0286 – measurement record

2D simulation (Blender), 24 fps, 72 frames (t = frame/24, 0–2.958 s), 2560x1440. Black letterbox bars cover rows 0–79 and 1360–1439, so the picture is in rows 80–1359. All values are full-resolution pixels (x to the right, y down). No metric scale is assumed anywhere.

## Scene
- The camera looks straight down (top-down) at snowy ground: patches of bright bluish snow and dark brown earth or vegetation, with a lighter diagonal snow band. There are no road markings.
- **Camera is static.** Phase correlation of a background strip against frame 0 gives a shift under 0.02 px in every frame, so no background compensation is needed.
- A grey swept-wing **jet** flies right to left (-x) over three parked **tanks**. A small dark **shell** lies to the left of the lower tank.
- Everything moves in one plane facing the camera, and the jet stays the same size (wingspan 720 px in every frame). So one metres-per-pixel scale applies to the whole frame. The jet flies above the tanks, so it is in fact at a different depth, but the render shows no perspective change. Use the single scale from the prior's object.

## Files
- `scene.json`: inventory (moving and static objects, descriptions, pixel sizes, visible frames), events, camera.
- `tracks/jet.csv`: one row per frame, 0–71, with these columns:
  - `ref_x, ref_y`: reference point = jet bbox centre (taken as the origin).
  - `bbox_*`: the full bbox, which can extend past the left edge (negative x).
  - `vis_bbox_*`: the bbox clipped to the image.
  - `length_px`: 562, from nose (missile tips) to tail-cone tip, along x.
  - `width_px`: wingspan, 720, along y.
  - `visible_length_px`
  - `partially_out_of_frame`, `ref_point_in_frame`
  - `jet_over_tanks`: which tank hulls the jet covers in that frame.
  - `method`
  - Height is not observable in a top-down view.
- `tracks/shell.csv`: shell position and box per frame.
- `scripts/`: every script used.
  - `bg.py`: background and camera check.
  - `motion_scan.py`: search for all moving blobs.
  - `track_jet.py`: diff mask and bbox.
  - `match_jet*.py`, `match_tail.py`: template matching.
  - `static_objs.py`: tank and shell extents.
  - `shell.py`
  - `build_record.py`: writes the record.
- Scratch images and CSVs are in `../frames/` and are not part of the record.

## Jet (the only object that moves continuously)
- **Motion:** pure translation along -x. There is no y motion (dy = 0 ±1 px), no rotation and no scale change.
- **Frames 0 and 1 are pixel-identical,** so motion starts between frames 1 and 2. After that the per-frame steps are uniform: the residual about a straight line is 0.8 px rms over frames 2–59.
- **How it was measured:**
  - Frames 0–59: a masked template of the whole jet, cut from frame 24, with sub-pixel peak fitting. Accuracy is about ±0.5 px.
  - Frames 60–69: the jet is leaving the left edge, so a tail-only template was used. It had a systematic offset of -21.9 px against the whole-jet template, measured over frames 50–59, and that offset was added back. These frames are good to about ±5–9 px.
  - Frames 70–71: only the tail-cone tip is visible, so x is extrapolated from the line fitted to frames 2–69. These rows are flagged in `method`.
- **Size** (bbox of the frame-24 diff mask, checked on overlays): x 1116–1678, y 369–1089.
  - Length 562 px. This includes the underwing missiles, whose tips stick out ahead of the nose. The tail-cone tip is at the right end.
  - Wingspan 720 px.
  - Reliability about ±3 px. Motion blur softens the edges a little.
- **Reference point:** bbox centre, which is (1397 + dx, 729.0). It sits on the fuselage just behind the cockpit. The true Blender origin could be up to about 30 px away along x. That shifts distances to the tanks but not speeds.
- **Edge of frame:** the jet's front reaches the left edge at frame 57. The reference point leaves the image at about frame 65. Some of the jet is still visible in frame 71.
- **Overlap with tanks:** the jet is always on top and never occluded. It passes over each tank in the frame ranges given in `scene.json` → `over_tanks_frames`. While it covers a tank, that tank is hidden.

## Static objects (measured on the temporal-median background, so the jet is removed)
Hull = the tank body without the gun barrel, along the tank's own axis, which is parallel to x for all three tanks.

| tank | hull x | hull y | hull length × width | hull centre | barrel |
|---|---|---|---|---|---|
| `tank_upper_left` | 1090–1335 | 524–639 | 246 × 116 | (1212, 581) | Turret rotated; it overhangs the hull bottom to y 683. Barrel points up-left, tip at about (1130, 425); the barrel is not in the mask. |
| `tank_middle_right` | 1634–1881 | 674–785 | 248 × 112 | (1757, 730) | Points -x, tip at x 1576. Overall length with barrel is 308 px. |
| `tank_lower` | 1297–1541 | 925–1035 | 245 × 111 | (1419, 980) | Points -x, tip at x 1235. Overall length with barrel is 309 px. |

- The three tanks are the same model: hull about 246 px long and about 113 px wide. Hull edges are good to about ±4 px, because the dark hull blends into dark ground.
- `tank_middle_right` sits in the same row as the jet's fuselage.
- Tank height cannot be measured from this view.

**Shell:** a dark elongated projectile in line with the lower tank's barrel.
- Frames 0–1: a motion-blurred streak, x about 790–876, centre about (838, 983.5), ±8 px.
- Frames 2–71: sharp and stationary, bbox x 772–822, y 977–989, centre (797, 983), size 50 × 12 px.
- So it jumps about 41 px left between frames 1 and 2 and then stays still. This is odd, possibly a simulation artefact. The jet flies over it in about frames 42–52.

## Events
| frame | t (s) | event |
|---|---|---|
| 0–1 | 0–0.042 | Frames identical; nothing has moved yet. |
| 2 | 0.083 | Motion starts: the jet steps about 34 px left and the shell jumps about 41 px left, then stops. |
| 57 | 2.375 | The jet's front reaches the left edge. |
| ~65 | 2.708 | The jet's reference point leaves the image. |
| 71 | 2.958 | Only the jet's tail tip is visible; the jet is still moving. |

There are no bounces, impacts or direction changes.

## Ambiguities
- The jet's origin is taken as its bbox centre.
- The jet length includes the missiles.
- Edge-of-frame positions (frames 60–71) are less reliable.
- The shell's behaviour in frames 0–1 is blurred and odd.
- No shadows of the jet are visible.
