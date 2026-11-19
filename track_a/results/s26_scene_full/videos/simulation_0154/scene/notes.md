# simulation_0154 — measurement record

2D simulation (Blender render), 1920x1080, 24 fps, 48 frames (t = frame/24, 0 … 1.958 s).
An underwater scene: one shark swims from right to left across a static view, above a sandy seabed with
floating particles. The camera is static. All values are in full-resolution pixels (x to the right, y down) and seconds.
No metric scale is assumed.

## Files
- `scene.json`: inventory (shark, seabed, particles, light rays), the camera, the shark's pixel sizes, and events.
- `tracks/shark.csv`: one row per frame, 0–47 (`visible`=0 at frame 47). Columns:
  - `center_x, center_y`: **the reference point** (body centre, standing in for the rig origin). `center_src` says how it was obtained:
    - `bbox` (frames 15–30): (snout_x+tail_x)/2. Here `center_y` is the middle of y_min..y_max.
    - `snout+L/2` (frames 0–14): the tail is cut off by the right border, so the centre is snout_x + 915.5/2.
    - `tail-L/2` (frames 31–46): the snout is cut off by the left border, so the centre is tail_x − 915.5/2. In frames 39–46 this centre lies off-screen (negative x).
    - In the partial frames `center_y` is fixed at 299, the median for the fully visible frames.
  - `snout_x`: the tip of the faint snout (low-threshold mask). `tail_x`: the tip of the caudal fin (= x_max). `full_len` = tail_x − snout_x (frames 15–30 only).
  - `x_min, x_max, y_min, y_max, bbox_w, bbox_h, bbox_cx, bbox_cy`: the main (opaque) mask. `*_lowthr`: the mask grown into the faint snout.
  - `centroid_x/y`: the mask's area centroid. `axis_len, axis_width, axis_angle_deg`: PCA extents of the mask along and across its main axis. `area_px`.
  - `trunc_left/right, occluded_or_truncated`: the mask touches the image border. Nothing ever occludes the shark; only small particles drift in front of it.
- `scripts/`: `load.py` (frame decoder); `segment.py` (pass 1, difference to frame 47); `make_pass1.py`; `segment2.py` (final mask); `snout*.py` (snout inspection); `finalize_track.py` (derived columns); `static_check.py`, `camera_check*.py`, `colors.py`, plus small json outputs.

## How the shark was measured
- **Background.** For each frame and each column, the background comes from the nearest-in-time frame in which the shark (pass-1 box ±80 px) does not cover that column. Because the background is so close in time, the drifting particles and flickering light rays hardly differ from the frame.
- **Mask.** The mask is the background difference (sum of |RGB| differences) above 20, after a light blur.
  - Pixels that look like particles (G>125 and G−R>50) in the frame or in the background are ignored.
  - The mask is then cleaned with open/close, reduced to the largest component, and its holes are filled.
  - The faint snout is added by a hysteresis grow: blurred difference above 10, within 120 px of the mask.
- **Check.** The masks were drawn on frames 2–46 and looked at. They cover the dorsal fin, the pectoral fins and both tail lobes. A few small particle blobs sometimes stick to the belly outline; they stay inside the box.

## Sizes (fully visible frames 15–30)
- **Full length**, snout tip to tail tip: median **915.5 px** (range 890–926, sd 12). It varies with the tail beat and the faint snout edge.
- **Opaque body length** (without the faint snout cap): about 865–900 px.
- **Height**, dorsal fin tip to lower tail lobe: median **~268 px** (range 262–273). y_min ≈ 162–168 and y_max ≈ 428–434.
- **Apparent size** is constant across the clip, so the shark stays at one depth (true 2D). Its body axis is horizontal (0–2°).
- **Which length to use.** If a prior gives the shark's length, the best pixel counterpart is the full length of 915.5 px. The world box presumably includes the semi-transparent snout geometry, but this is not certain. If the snout cap is excluded, use about 880 px. The difference is about 4%.

## Motion and events
- **Direction.** The shark moves steadily leftward the whole time, at y ≈ 299, with no vertical drift. There is no stop, reversal, contact or impact.
- **Tail tip.** It is the cleanest per-frame marker. In frames 15–46 it moves about 55–63 px per frame. It is slightly faster around frames 18–28 than near the end, which could be an eased animation or tail-beat wobble; fit as needed.
- **Snout tip.** It is noisier (±10–15 px per frame) because the semi-transparent snout fades into the water. The `bbox` centre inherits half of that noise.
- **Getting speeds.** For speeds, use a fit or multi-frame differences rather than single-frame differences of `center_x`. In frames 15–46, `tail_x` minus a constant gives the smoothest centre.
- **Events:**
  - Frame 0: the shark is already moving; only the snout and head are in view (snout at x 1777).
  - Frame 15: the whole body is in view.
  - Frames 23–24: the centre crosses x = 960.
  - Frame 31: the snout reaches the left border.
  - Frame 46: last visible frame (tail tip at x = 60).
  - Frame 47: the shark is gone.

## Camera and background
- **Camera.** It is static. The seabed skyline (dune crest against the water, x 560–1500) shows a median shift of 0 px from frame 0 in every frame. Some columns change, but only because the caustics animate.
- **Seabed.** It is static. The skyline crest is at y ≈ 797–800 for x 800–1160 and slopes down to ≈864 at x=560 and ≈866 at x=1440. The cyan caustic patches on the sand are moving light, not objects.
- **Particles.** They are small cyan or white specks, 3–25 px across, drifting about 0.3 px per frame. They are distractors and were not tracked. There is only one shark, so nothing is ambiguous about which animal is meant.

## Reliability
- **High:** camera static; direction and timing of events; `tail_x` (±2 px); vertical extents (±4 px, though y_min in frames 17–27 may be 4 px low on the fin tip because of the particle colour rule).
- **Medium:** `snout_x` (±10–15 px, faint snout), and so the full length (±1.5%) and the `bbox` centre.
- **Extrapolated:** centres in partial frames (0–14 and 31–46) assume the constant length L = 915.5 px.
