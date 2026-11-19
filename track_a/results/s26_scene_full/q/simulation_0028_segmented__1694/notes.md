# Q1694: eagle wingspan (m)

Prior: eagle length = 0.8 m. depth_info: 100.14 m at t=1 s, 99.52 m at t=2 s. question_fps = 24; the file runs at 25 fps
(75 frames). Only frame numbers are used, and the answer is a size, so the time base hardly matters.

## Geometry (from zoomed crops: frames/z*.png, frames/d*.png)
- The eagle is seen almost exactly side-on, flying to the right. Depth changes by only 0.6 m/s against a lateral speed
  of about 15 m/s, so the yaw is about 2°. Its body/back line is horizontal in the image. The wings flap toward/away
  from the camera, so they appear vertical: the far wing points up on the upstroke and the near wing hangs down on the
  downstroke.
- At mid-stroke (frames 5-6, 17-18, 31-32) the wings are level and the bird is only 14.5-17.6 px tall, so the camera
  looks down by only a few degrees (≤ ~7°). Wing extents in the image are therefore close to true length.

## Measurements (measure.py, measure2.py; coverage mask = |frame − median bg| / contrast, 50% edges, subpixel)
- Body length (widest horizontal row = beak-to-tail line): 20.1-24.7 px on frames 0-20, mean 22.2 px. The integer
  bbox width on downstroke frames 9-13 is 21-23 px. Over the rock (frames 22-38) it is 20-23 px.
  -> L = 22.5 ± 0.7 px = 0.8 m, i.e. 28.1 px/m. This gives f ≈ 22.5 × 100.14 / 0.8 ≈ 2816 px (HFOV ≈ 19°), which is plausible.
- Half-span, measured vertically from the body line to the raised far-wing tip at the top of the upstroke:
  frame 0: 32.5, frame 1: 30.7, frame 22: 31.9, frame 24: 33.9, frame 25: 34.6, frame 26: 33.3 px.
  The plateau on frames 24-26, when the wing is closest to vertical, gives about 34.5 px (35-36 px if the slight forward
  lean of the tip is included). The downstroke reaches only 26 px below the body line, because the wing goes down
  only about 50°.
- Wingspan ≈ 2 × 34.6 = 69.2 px -> 69.2 / 28.1 = 2.46 m.

## Check
- Upstroke peaks in two different wingbeats (frames 0-1 at the clip start and frames 24-26) give a half-span of
  32.5-34.6 px. Including the lean gives 34-36 px. The span is 2.3-2.55 m; the best value is 2.46 m.
- Through depth: f = 2816 px, so span = 69.2 × 100.14 / 2816 = 2.46 m (consistent).
- The span/length ratio is 3.1, which is a bit high for a real eagle (about 2.5-2.8) but within the range of 3D models.
  The value could be low if the raised wing is bent or past vertical at the upstroke peak.

## Confidence
Moderate, about ±10%. The bird is tiny (body about 22 px), so a 1 px error is about 4%.
