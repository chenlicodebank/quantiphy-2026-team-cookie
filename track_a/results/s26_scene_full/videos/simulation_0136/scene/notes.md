# simulation_0136 – measurement record (2D, 24 fps, 60 frames, 1920x1080)

## Files
- `scene.json` – inventory (moving + static objects, pixel positions/sizes), camera, events.
- `tracks/blue_cup.csv` – per-frame track of the only moving object (frames 0-59; `visible=0` when off-screen).
  Columns: frame, t, visible, cx/cy_bbox (bbox centre), cx/cy_mask (pixel centroid; biased up because the cup
  is wider at the top), cx/cy_rect (minAreaRect centre), x0,y0,x1,y1, bbox_w, bbox_h, len_main (mask length
  along main axis), width_across, tilt_deg (main axis vs vertical, negative = top leaning right), area,
  occluded_or_cut (touches image edge), **cx_est, cy_est = recommended reference point**, est_method.
- `scripts/track_cup.py` (HSV blue segmentation, largest component), `scripts/add_est.py` (reference point),
  `scripts/static_objs.py` (static objects, camera check).

## Scene
Straight-on static view of a kitchen counter: red toaster (upper left), grey outlet plate, black hood (upper
right), Miele induction cooktop with two white burner rings (right), counter front edge at y≈757, wood floor
below. A dark-blue tapered cup (~121 px wide at top, 256 px tall) slides horizontally left→right along the
counter at y_centre≈649.5 (bottom ≈778 px), enters at frame 5, leaves at frame 57. No other object moves.
Camera static (background shift < 0.005 px). Motion is purely horizontal (cy constant within ±1 px).

## Motion summary (pixels/frame from cx_est; for orientation only)
- Frames 7-13: ~74-71 px/frame (near uniform, slight slowing).
- Frames 13-28: smooth deceleration from ~70 to ~28 px/frame (counter region, x≈575→1250).
- Frames 28-51: ~24.6 px/frame nearly constant (over the cooktop); linear fit x = 24.563·frame + 570.5.
- Cup tilts from frame ~31 (up to ~-11° at frame 51) while crossing the cooktop; tilt makes bbox width grow
  120→178 px but minAreaRect length stays 256-261 px.

## Reliability
- Mask hits the full cup (checked on overlays at frames 0,6,...,54,56,57); blue on black cooktop segments well.
- cx_est frames 7-51: ±2-3 px (minAreaRect vs bbox centre differ by up to ~6 px when tilted, e.g. frames 14-21,
  37, 42 – bbox centre has occasional 3-8 px jumps from the tilted base; frame 29 has a small glitch ~3 px).
  For per-frame speeds consider light smoothing or using cx_bbox / x1 (right edge) as cross-checks.
- Frames 5-6: left-cut; cx_est = x1 − 60.5 (≈-10.5, 62.5). Frames 52-57: right-cut; cx_est is a linear
  extrapolation of frames 44-51 (unreliable if the cup changed speed while exiting).
- Cup sizes: upright height 256 px (bbox 256-259), top width 120-124 px – best measured frames 7-28.
- Static sizes: from frame 0 thresholds/Hough, ±3 px. Toaster red body 434×298 px; cooktop glass 635 px wide
  (660 with frame); left burner Ø248 px, right burner Ø216 px; outlet plate 232×33 px.
- 2D video: one metres-per-pixel scale should apply to everything (all objects appear at similar depth;
  the cup slides in front of/over the cooktop region).
- Ambiguities: the cup's origin is likely its geometric centre; the mask centroid is shifted up (~6 px) by
  the taper, so prefer cx_est/cy_est. The cup has a faint shadow, excluded by the saturation threshold.
