# simulation_0023: measurement record

Source: a simulation (Blender render), a **3D** scene, 960x960, 25 fps, 75 frames (t = frame/25, so 0 to 2.96 s).
Everything here is in **pixels and seconds**. No metric scale was assumed.

## Scene in one line
The camera is static. It looks across rippled water at a beach and a tan cliff. A red/white **fishing boat** ("AH805" on
the hull, bow pointing left) floats just in front of the shoreline and drifts steadily **left and slightly away** from the
camera for the whole clip. A single dark **bird** (eagle/hawk-like, flapping) flies **left to right** across the cliff at
about mast height. It passes the boat's mast around frames 10-14 and leaves through the right edge at frames 63-66.
There are no other moving objects and no contacts or impacts.

## Files
- `scene.json`: inventory (moving and static objects), camera, perspective cues, events, and frame-0/74 extents with
  summary ranges.
- `tracks/boat.csv` (frames 0-74):
  - `ref_x, ref_y`: the full-boat box centre. x is the midpoint of the bow tip and the stern extreme; y is the midpoint
    of the mast top and the hull bottom.
  - `hull_center_x/y`: centre of the hull-only box (from 30 px below the cabin roof down to the hull bottom).
  - `bbox_x0,y0,x1,y1`: the full boat, including the rails and the rear post. The top is the mast top and the bottom is
    the hull bottom.
  - `bow_x/y, stern_x/y`: the leftmost and rightmost hull points.
  - `hull_length_px`: bow to stern, along x.
  - `height_masttop_to_hullbottom_px`
  - `full_width_px`
  - `mast_top_x/y, cabin_x/y`: rigid key points.
  - `rigid_scale_vs_f0`: apparent-size factor of the superstructure relative to frame 0.
  - `body_mask_area`
  - `occluded`: 1 at frames 10-14, when the bird overlaps the mast.
- `tracks/bird.csv` (frames 0-66):
  - `ref_x, ref_y`: centroid of the bird mask (its visible centre).
  - `bbox_*`, `bbox_cx/cy`
  - `width_x_px`: horizontal extent, roughly the wingspan when the wings are level.
  - `height_y_px`
  - `major_px, minor_px, axis_angle_deg`: principal axes of the mask.
  - `area_px`
  - `occluded`: 1 at frames 10-14, crossing the mast.
  - `cut_by_frame_edge`: 1 at frames 63-66.
- `camera_shift.json`: per-frame phase-correlation shift of 3 background patches against frame 0 (all within 0.04 px,
  so the camera is static).
- `scripts/`:
  - `camera.py`: camera check.
  - `background.py`: the clean background plate. Columns x<275 come from frame 0 and x>=275 from frame 74, and the
    bird area is patched.
  - `boat_lk.py`: LK feature tracking plus a similarity fit, giving the rigid transform of the boat.
  - `boat_sil.py`: boat silhouette.
  - `export_tracks.py`: writes the final CSVs and overlays.
  - `make_scene.py`: writes `scene.json`.
  - `track.py, probe.py, diffprobe.py, shore.py, check_boat.py`: exploration and checks.

## How it was measured
- **Camera**: confirmed static, so a clean background plate was built from two frames. The boat moved 260 px, so its
  frame-0 and frame-74 positions do not overlap.
- **Boat silhouette**: per-pixel difference to the plate greater than 16, kept only above the shoreline (+2 px). Small
  bits were removed, then the mask was closed and its holes filled.
  - The bow and stern come straight from this silhouette. They are reliable to about ±2 px.
  - The hull below the waterline sits in animated water, so it **cannot be segmented**. The hull bottom
    (`bbox_y1`, frame-0 value y=618 at x≈420) and the mast top (frame 0: (390,304)) were therefore read by hand on
    frame 0. They were then carried to every frame by the boat's rigid similarity transform.
  - That transform comes from LK features on the cabin, mast and hull. It has 190 features at the start and 12 at the
    end, with forward-backward checks and RANSAC.
  - When overlaid on frames 0, 36, 40, 48, 64 and 74, the mapped mast top and cabin points land on the right spots.
    The mapped bow and stern do not, which is why the silhouette is used for those.
  - The rudder bottom is about 16 px below the hull bottom, at (517,634) in frame 0.
- **Bird**:
  - Starting point: pixels that differ from the plate by more than 28 and are dark (mean below 150), inside a window
    around the predicted position. The boat body and the mast column (±5 px) are excluded.
  - A 3x3 opening removes the rigging lines, then the mask is grown back geodesically inside the diff>20 mask to
    recover thin wing tips.
  - Overlays were checked at frames 0, 6, 12, 13, 30, 36, 48 and 64.

## Reliability and ambiguities
- **Boat position**: very smooth. The bow-stern midpoint moves about -3.8 px/frame in x, and y is almost constant (the
  box centre stays at y≈459-461).
- **Boat depth**: the apparent size shrinks over the clip, and the boat rises about 12 px in the image (hull bottom 618
  to 605.5), so it is also moving **away** from the camera.
  - The rigid scale goes from 1.000 to 0.929, which suggests depth grows by about 7.6 %.
  - The hull length shrinks more, from 263 to 228 px (0.867). The boat therefore also **yaws** a little (the bow-stern
    line turns toward the viewing direction; at the end the rigging appears on the other side of the mast).
  - For sizes, prefer frame-0 values or `rigid_scale_vs_f0` over `hull_length_px` at late frames.
- **Boat reference point**: the Blender origin of the boat is unknown. The record gives the full-box centre
  (`ref_*`), the hull-box centre and rigid points; their x positions are all close. For pixel-to-metric work, use
  differences between frames, which are insensitive to this choice.
- **Boat height**: the mast top to hull bottom is about 314 px at frame 0. The waterline is roughly y≈605 at frame 0,
  but the visible hull bottom against the water and its reflection is uncertain by about ±5 px. Including the rudder
  adds about 16 px.
- **Boat length and width**: the hull length (263 px at frame 0) is the visible bow-to-stern extent. The viewing angle
  is roughly side-on with slight obliquity, and the boat's beam (width) cannot be measured.
- **Bird position**: the centroid is noisy by ±3 px because the mask changes with the wing phase. Where it was hard to
  segment, the centroid is biased:
  - frames 10-14 (bird crossing the mast, parts cut out; frame 13 also includes a bit of rigging, so its bbox is
    56x44 there);
  - frames 4-6, 31-33 and 55-57 (wings edge-on or faint, so width is under-measured by up to about 15 px);
  - frames 63-66 (cut by the frame edge).
  - Smooth or fit over several frames before differencing.
- **Bird size**: wingspan is best taken as the larger `width_x_px` values among clean frames (about 41-56 px at frames
  34-45 and 58-62). The apparent size does not trend with time, so there is no clear depth change. The bird's depth
  relative to the boat is unknown; it passes behind or in front of the mast with no contact.
- **Reflections**: the boat's red reflection in the water (y>620) was deliberately excluded.
- **No events**: there are no bounces, collisions, release or stopping. Both objects are already moving at frame 0. The
  boat never stops; the bird exits at frames 63-66.
