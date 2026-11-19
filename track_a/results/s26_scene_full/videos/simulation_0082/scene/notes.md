# simulation_0082 — measurement record (pixels, seconds)

2D simulation (Blender), 1920x1080, 24 fps, 72 frames (t = frame/24). Static top-down camera over a
uniform grey ground. Two pickup trucks drive side by side from right to left (−x), fronts pointing left:

* **yellow_truck** – upper lane (body rows y 348–455, centre y 401.5).
* **white_truck** – white hood/roof rails, black bed; lower lane (body rows y 489–590, centre y 539.5).

Nothing else is in the scene: no markings, lanes or props. The ground is flat grey (~158) with soft shadows.

## Files
* `scene.json` – inventory, sizes, start/end positions, per-frame pixel shift summary, events, camera.
* `tracks/yellow_truck.csv`, `tracks/white_truck.csv` – one row per frame (0–71; both visible all frames,
  never occluded). Columns:
  * `cx, cy` – centre of the body box (reference point ≈ vehicle root seen from above).
  * `cx_xcorr` – sub-pixel x centre: cx at frame 0 plus the summed frame-to-frame shifts from 1D cross-correlation of
    the body column profile. It is the smoothest series (rms 0.05–0.3 px from a straight line), so use it for per-frame differences.
  * `bbox_x0/x1` (= `front_x`/`rear_x`), `bbox_y0/y1` – body box without the mirrors. `length_px` = along the motion
    (x), `width_body_px` = across.
  * `mirror_top_y/bottom_y`, `width_with_mirrors_px` – width including the side mirrors (raw; see caveat below).
  * `*_raw`, `y_raw_polluted` – raw y-extent measurements before the shadow fix.
  * `occluded` – always 0. There is no height column: in a top-down view the vertical extent is not visible.
* `scripts/track.py` – segmentation and tracking (writes the CSVs and overlays). `scripts/postprocess.py` – fixes the y extents.
  `scripts/summary.py` – linear fits that check the motion is constant. `scripts/probe.py`, `profile.py`, `inspect_tracks.py` – diagnostics.
  `scripts/bg.png` is the median background (small).

## Method
Mask = pixels with min channel < 100 (glass, black bed, tyres), max channel > 172 (white paint) or HSV saturation > 50
(yellow paint). The soft unsaturated ground shadow (105–170) is excluded. The trucks are separated at the emptiest row
between them (y ≈ 464–473). front/rear x = the extreme columns inside a core band of rows (yellow 375–430, white 515–580),
which avoids mirrors and shadow. I checked overlays at frames 0, 12, 24, 36, 47, 60 and 71: the contours follow the
truck outlines, including the bumpers and tailgates.

## Key numbers
* Sizes (px). Yellow: length 304 near the image centre (frame 55), 314 at frame 0 and 308 median; body width 108;
  width with mirrors 131. White: length 302 near the centre (frame 40), 312 at frame 0 and 305 median; body width 102;
  width with mirrors 131 (mirror rows 474–605). The two trucks are almost the same size; the yellow body looks ~6 px wider.
* Motion: frames 0 and 1 are identical (both at rest). From frame 1→2 both move at constant velocity in pure −x, with no
  vertical motion (the outer body edges stay at y = 348 and y = 590 in every frame). Per-frame x shift:
  * yellow: −11.40 px (cx_xcorr), −11.33 (box centre), −11.26 (front edge), −11.41 (rear edge);
  * white: −15.96 px (cx_xcorr, frames 1–36), −15.88 (frames 36–71), −15.86 (box centre), −15.81 (front), −15.91 (rear);
    the white rear edge moves exactly 16.00 px/frame over frames 1–36.
  * Ratio white/yellow ≈ 1.40.
* Positions. At frame 0 both centres are at x ≈ 1588 with fronts aligned at x = 1432. At frame 71: yellow cx 795.5
  (xcorr 790.2), white cx 477.5 (xcorr 484.8). The centres are 138 px apart vertically; the gap between the bodies is 33 px.
* Events: start of motion between frames 1 and 2; white front edge reaches x = 960 at frame 31; yellow front edge at
  frame 43; white is fully ahead of yellow from frame 68 (t = 2.833 s); both are still moving at the end.

## Reliability / ambiguities
* **Perspective.** The camera is a perspective camera, even though the scene is labelled 2D. Pixel length shrinks
  ~3% from right to left, and points at different heights move at slightly different pixel rates (~1%). So the
  origin's true pixel rate is uncertain by about ±0.1 px/frame (yellow 11.26–11.41, white 15.81–15.96). Use one scale
  per the convention. For a size prior, the length near the image centre (304 / 302) or the median (308 / 305) are the best values.
* **Shadow between the trucks.** In frames 0–37 the dark contact shadow in the gap merges with the inner body edges.
  The body-box y values in the CSVs were therefore set to the clean constants from later frames; the raw values are kept.
  The early-frame mirror rows (yellow bottom 468–479, white top 470–481) are polluted too. Use 131 px for both widths with mirrors.
* Box-centre `cx` is quantised to 0.5 px with ±0.5–1 px edge jitter. `cx_xcorr` drifts up to ~6 px from cx over the clip
  because it follows the high cab/roof texture; it is precise for differences.
* No metric scale is assumed anywhere.
