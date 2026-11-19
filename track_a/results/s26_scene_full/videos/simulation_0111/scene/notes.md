# simulation_0111 – measurement record

**Scene.** A 2D Blender render, 24 fps, 211 frames, 1174×2048 px (portrait). The camera looks straight down on a canal. A small white rowboat moves straight down the image (+y) and passes under a cobblestone footbridge that spans the full image width. The canal is lined with building facades. Frame 0 is completely black. The camera is static: phase correlation of the bridge and facades against frame 5 gives shifts below 0.05 px. The boat is the only moving object. Water ripples are animated but are background.

## Files
- `scene.json`: the inventory (boat, bridge, lamp posts, bollards, canal, buildings), the camera, the events, and the boat's pixel sizes and motion summary.
- `tracks/boat.csv`: one row per frame from 1 to 210.
  - `state`: `full`, `partial_entering` (bow under the bridge), `hidden` or `partial_exiting` (stern still under the bridge). `occluded` = 1 unless the state is `full`.
  - `cx, cy`: the reference point, which is the centre of the solid hull (midpoint between the two hull tips). `cy` is the measured value where one is available, otherwise the value from the fit.
  - `cy_meas`: the measured centre.
    - `full` and `partial_exiting` frames: bow tip `y1` − 116.5.
    - `partial_entering` frames: `hull_top` + 116.5.
  - `cy_fit`: the linear fit `cy = 5.4961·frame + 273.78`. The residuals have an rms of 0.65 px and a maximum of 1.6 px.
  - `x0, y0, x1, y1`: the bounding box of the visible mask.
  - `hull_top, hull_bot`: the first and last mask rows that are at least 10 px wide, which excludes the thin stem post.
  - `length_axis, width_axis, angle_deg`: the extents and angle of the visible mask along its principal axes.
  - `area`, `cx_mask, cy_mask`: the area and centroid of the visible mask.
- `tracks/boat_raw.csv`: the raw per-frame mask measurements.
- `scripts/`:
  - `bg.py`: median background and camera-motion check.
  - `track_boat.py`: segmentation by background difference plus brightness, using the largest component and merging nearby pieces.
  - `build_track.py`: reference point, states and fit.
  - `static.py`: measurements of the bridge and canal.
  - `overlay.py`: draws the tracks for checking.
  - `check_speed.py`, `hull_profile.py`: diagnostics.

## Key numbers (pixels)
- **Boat solid hull length (tip to tip):** 233 px, the same before and after the bridge.
  - Before the bridge the mask also includes a faint thin post about 16 px long at the upper tip, which makes the bounding-box height 248–251 px.
  - After the bridge the bounding-box height is about 232 px.
  - If a prior gives the boat length, use 233 px for the solid hull; about 250 px is the outer extent including the post. This is the main ambiguity.
- **Boat width:** 84–85 px.
- **Boat axis:** tilted about 3.5° from vertical. The motion itself is exactly vertical: x stays at 631.3 ± 0.1.
- **Boat motion:** constant speed of 5.50 px/frame (131.9 px/s) straight down.
  - The fitted slope is the same before the bridge (5.48 from the bow tip) and after it (5.50).
  - Frames 1 and 2 show the same position, so motion starts at frame 2. From then on, per-frame differences of the bow tip alternate between 5 and 6 px because of integer pixels.
  - Use `cy_fit` for speed and distance questions; per-frame `cy_meas` carries about ±0.7 px of noise.
- **Path in view:** cy runs from about 285 (frame 1) to 1428 (frame 210), which is about 1143 px.
- **Occlusion by the bridge at x≈631:** y from about 807 to about 1265.
  - Bow hidden from frame 77.
  - Fully hidden from about frame 110 to 169. In these frames `cy` comes from the fit only.
  - Visible again from frame 170.
  - Fully visible from frame 203.
- **Bridge:** tilted about 6.9°, right end lower. It is about 437 px wide perpendicular to its axis (railing to railing) and about 440–450 px tall vertically. Its length runs off both image edges.
- **Canal:** about 840–870 px wide above the bridge and about 710–870 px below it, where the banks are irregular and slanted (±15 px).

## Reliability and ambiguities
- **Boat track:** good to about 1 px in `full` frames. Partial frames rely on the hull length being constant. Hidden frames are interpolated only.
- **Boat orientation:** the deck detail (positions of the seat openings and holes) looks reversed end-for-end after the bridge compared with before. The pixel size, x position and speed are unchanged, so it is treated as the same boat.
- **Static positions:** lamp posts and bollards are read off frame 42 by eye (±10 px).
- **Scene type:** this is a 2D scene, so use one metres-per-pixel scale from the prior. There are no depth cues; everything lies approximately in the water and bridge plane.
- **Image quality:** no motion blur of note. Small specular sparkles on the water were ignored.
