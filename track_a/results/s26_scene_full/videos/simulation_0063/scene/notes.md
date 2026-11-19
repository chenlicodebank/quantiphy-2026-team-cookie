# simulation_0063 — measurement record (pixels and seconds only)

3D Blender render, 2160x1080, 24 fps, 72 frames (t = frame/24). **Static camera** (shift < 0.02 px per frame).
Street intersection: a taxi, a white van and a cyclist drive left to right on the road; a pedestrian (the man)
walks toward the camera on the near sidewalk. **Frame 1 is identical to frame 0.** All motion starts between
frames 1 and 2, so a one-frame backward difference at frame 1 gives zero.

## Files
- `scene.json`: inventory (moving and static objects with descriptions, visible frames, pixel extents), camera and
  perspective cues, events.
- `tracks/<object>.csv` (taxi, man, cyclist, van): one row per frame 0-71. Columns:
  `ref_x, ref_y` = reference point (see below); `bbox_x0, bbox_y0, bbox_x1, bbox_y1` = amodal bounding box
  (x0 can be < 0 when out of frame); width/height (`width_px`/`length_px`, `height_px`); object-specific extras;
  `occluded`, `truncated`; `interp` lists the fields at that frame that were **interpolated or estimated**
  rather than measured. Fields not listed in `interp` were measured.
- `check_overlay.jpg`: final boxes and reference points drawn on 10 frames (red = man, blue = taxi, green = cyclist,
  magenta = van). I checked these visually, and checked earlier stages on many more frames.
- `scripts/`: every script used. Order: `bg.py` → `bg2.py` (clean background) → `measure_man_taxi.py` →
  `measure_cyclist.py` → `clean.py` → `measure_van.py` → `clean_van.py` → `perspective.py`, `static.py`.
  `fgmask.py`, `colmask.py`, `common.py` are helpers. `propagate.py`/`flowviz.py` were a failed first attempt
  (optical-flow mask propagation leaked between touching objects) and are not used for the results.
  The raw per-frame measurements are in `../frames/raw_*.csv`, and the clean background is `../frames/bg_clean.png`.

## How it was measured
- Foreground = |frame − clean background| > 10 grey levels (render noise is ≤ 4). The clean background is frame 71
  for x<485 plus frame 0 for x≥485, because no mover overlaps itself across the two. Shadows are suppressed:
  uniform darkening of non-sky background, ratio 0.36-0.97.
- **Taxi**: yellow paint mask (hue 13-30, or the orange roof sign) gives the left/right extent and the top (roof
  sign top). Front and rear bumpers come from the foreground continuing ≤20 px past the paint, and the bottom from
  the lowest foreground below the paint (tyres). Hidden edges, read from zooms and replaced by interpolation:
  rear f31-37 (behind the man) and f43-44 (lamp post A); front f9-10 (lamp A), f53 and f55 (merged with the
  cyclist's wheel) and f59-62 (lamp post B). Frames 0-5: the rear is outside the image. There `bbox_x0` is an
  amodal estimate (front − pixel length, with the length extrapolated linearly from f6-12) and `visible_x0` = 0.
  `ref` = amodal bbox centre.
- **Man**: hip x = median x of the top 30 rows of the blue jeans. Feet = lowest foreground row below the jeans.
  Visual checks put it within ~4 px; light soles are sometimes under-counted by ~3-5 px. **Head top was read by
  eye** on 4x zooms at f0, 6, 12, …, 66, 71 (hair top; the face is an anonymising grey blur that is often not
  foreground) and interpolated in between (±3 px; the head bobs ~2-3 px with the gait). `height_px` = feet − head
  top. `ref` = pelvis estimate (hip_x, feet − 0.53·height). `waist_y` (jeans top) is also given. Left/right
  extents were measured only when he is isolated (f51-71). Before that they are hip ± median offsets (flagged
  `x0x1`), because the taxi/van behind him merge with his silhouette.
- **Cyclist**: masked template matching of the rider's head+torso (template from f52, where they are on clear
  background). The bbox is the f52 box (110x127 px: rear wheel to front wheel, head top to wheel bottom) scaled by
  the matched scale (1.07 early → 0.94 at f71). f0-21: rider hidden behind the taxi; only head/shoulders were
  matched, and f0/f1 were read by eye (head x 259). f60-61 interpolated (lamp post B). `ref` = rider
  pelvis/saddle estimate (x0+0.41w, y0+0.51h); `head_x` given too. The scale is held fixed at 1.07 for f0-21.
- **Van**: foreground minus the man/taxi/cyclist boxes, linked to the previous van box, tracked backward from f71.
  Measured: rear edge `rear_x` f28-71 (outside the image before f28), roof `roof_y` (~526, every frame), bottom where
  the wheels show (f28-57, except a few frames behind the man), and front edge only f69-71. **Estimated
  (flagged)**: bottom elsewhere (quadratic trend; f71 estimate 657 vs ~660 by eye), and the front edge
  x1 = rear + 2.757·height (length/height ratio at f69-71). The van's `ref`/centre depends on that estimate. Prefer
  `rear_x` / `roof_y` for motion. `visible_*` columns give the raw visible extents. In f0-27 `ref_x`, `bbox_x0`
  and `bbox_x1` are empty because the rear is out of frame and the front is hidden. Only roof_y, the estimated
  bottom and `visible_x1` (front of the visible part: cab/roof above the taxi, not the bumper) exist there.

## Reliability
- Good (±2-3 px): taxi front x1 and rear x0 where measured, taxi left/right in f6-30 and f38-71, man hip_x/feet,
  cyclist box position f22-71, van rear_x f28-71, van roof.
- Medium (±4-8 px): taxi top (roof sign is small and noisy f0-19: values 580-608), taxi bottom (late frames
  include up to ~10 px of dark contact shadow: at f71 the tyre bottom is ~825 vs bbox 835), man head top, man
  width, cyclist f2-21 (head only behind the taxi).
- Low / estimated: taxi rear f0-5 (out of frame), van front/centre/bottom where flagged, cyclist f0-1.
- Taxi width in the image is not a fixed length: it turns toward the camera (side view → ¾ front view), so pixel
  width falls from ~550 to ~420 (f48-60) then rises to 469 (f71) as it approaches. Height grows 150→241 px.

## Perspective (3D)
- Horizon ≈ y 532: the man's feet_y = 532.3 + 1.160·height_px over all frames (residual 1.3 px), so camera
  height ≈ 1.16 × man height. Cyclist: bottom ≈ 529 + 1.20·height. Van roof (y≈526) lies on the horizon, so van
  height ≈ camera height. Principal point assumed at the image centre (1080, 540). The camera is nearly level and
  the focal length is unknown.
- Apparent size vs time: man 243 → 296 px tall (approaching); taxi height 150-165 → 241 px (approaching, mostly
  after f40); cyclist scale 1.07 → 0.94 (receding slightly); van height 170 → ~129 px (receding).

## Ambiguities
- Two people besides the man: the cyclist (dark clothes, on a bicycle) and the taxi driver (inside the taxi, early
  frames). The cyclist's head is next to the driver's head at f0-1.
- Static occluders in front of movers: lamp post A (x 611-625), lamp post B (x 1202-1225), traffic-light pole
  (x 374-381), green bin (the man walks in front of it from f56).
- No collisions, contacts, bounces, stops or releases. Every mover is already moving from frame 2 and still moving
  at frame 71.
