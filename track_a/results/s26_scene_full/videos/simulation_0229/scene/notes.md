# simulation_0229: measurement record

**Scene.** A 2D Blender render, 1920x1080, 24 fps, 50 frames (t = frame/24). The view looks straight at a classroom
front wall: a large green blackboard, a wall clock, a teacher's counter on the left, and student chairs and desks
in the foreground. Diagonal sunbeams cross the left side. The **camera is static**: phase correlation against
frame 0 gives a shift of at most 0.03 px.
The only moving object is a **white paper airplane** seen from the side, nose to the right. It flies left to right
in an arc in front of the board. It rises until about frame 23 (image y ≈ 343 px), then descends and leaves through
the right image edge. Its pixel length stays at about 140 px the whole time, so it moves in one plane at constant
depth. Use a single metres-per-pixel scale.

## Files
- `scene.json`: inventory, static object pixel extents, camera, events, and a path summary.
- `tracks/paper_airplane.csv`: one row per frame, frames 11–41. Columns:
  - `bbox_*`: bbox of the hysteresis mask. `bbox_cx/cy` is its centre.
  - `mask_cx/cy`: pixel centroid. It is biased toward the wide rear wing.
  - `len_main_axis_px`, `width_across_px`: from the min-area rectangle of the mask.
  - `axis_angle_deg_imgdown`: angle of the principal axis, image y down, positive means nose down.
  - `area_px`: mask pixel count.
  - `peak_contrast`: capped at 63.8.
  - `at_image_edge`, `gate_clipped`: flags.
  - `axis_fit_deg`: linear fit of the axis angle over frames 14–35.
  - `nose_x/y`, `tail_x/y`: tip points along the fitted axis.
  - `nose_tail_len_px`: distance between the tips.
  - **`ref_x_px`, `ref_y_px`**: recommended origin proxy.
  - `ref_method`: how the reference point was obtained for that frame.
- `scripts/`:
  - `track.py`: segmentation and tracking.
  - `refpoint.py`: tips and reference point.
  - `static.py`: board edges and camera shift (writes `camera_shift.json`).
  - `probe.py`: colour profiles.
  - `clock_check.py`: clock region check.
  - `overlay.py`, `view.py`: visual checks.
  - `fit_segment.py`: an abandoned matched-filter attempt. Its output was overwritten and is not used.

## Method
1. Background: per-pixel median of frames 0–5 and 44–49, when the plane is absent.
2. Difference: d = max over RGB of |blur5(frame) − blur5(background)|, with the clock region masked out.
3. Hysteresis mask: pixels with d > 4.5 in components that contain a pixel with d > 9.
4. Tracking: starts at frame 20 and runs forward and backward. Each frame's search is gated around a linear
   prediction from the two previous centres.
5. Reference point: in frames 13–36 it is the midpoint of the nose and tail tips. In frames 11–12 it is nose − 70.3 px
   along the axis; in frames 37–41 it is tail + 70.3 px along the axis.

I drew bbox and centre overlays on frames 10–42 and checked them by eye. They sit on the plane and cover its full
length in frames 13–36.

## Reliability
- **Frames 14–35 (plane on the dark board):** very clean.
  - Centre to about ±1–2 px.
  - Length 135–146 px. The mask is from a blurred difference, so it reads about 3 px long. A sharp threshold
    on the same frames gave 133–140 px; the true silhouette is about 137 ± 4 px.
  - For a size prior on the plane's length, use about 140 px (median 2H = 140.6).
  - Height across the body: about 10–15 px sharp; the blurred mask including the raised rear wing gives 18–30 px.
- **Frames 13 and 36:** the plane is on the bright beam or the pale wall, but the full outline was recovered.
  About ±3 px.
- **Frames 11–12:** the tail is lost in the sunbeam; the reference point is extrapolated from the nose. About ±5–8 px.
- **Frames 37–41:**
  - Frame 37: the nose is faint on the wall.
  - Frames 38–41: the nose is beyond the right edge.
  - The reference point comes from the faint tail and is noisy, ±5–10 px (x steps are uneven: 54, 32, 32, 41, 18).
  - Prefer frames 13–36 for speed or acceleration.
- **Frames 9–10:** the plane is faintly visible at the left edge but not segmented.

## Caveats
- The `bbox_cx` and `mask_cx` columns are not origins. `mask_cx` is pulled toward the wide rear.
- The Blender origin of a paper airplane is presumably near its geometric centre, so `ref_*` (equivalently, the bbox
  centre in frames 13–36) is the best proxy.
- Motion blur is small; the plane moves about 45–73 px per frame horizontally.
- The plane's own pixel speed slows from about 72 to about 45 px per frame in x across the clip. No motion model is
  fitted here.
- There is no bounce or contact. Static extents are in `scene.json`:
  - Board green surface: 1327 × 401 px.
  - Board with frame: 1372 × 443 px.
  - Clock diameter: about 105–110 px.
