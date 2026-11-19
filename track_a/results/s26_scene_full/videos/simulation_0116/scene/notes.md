# simulation_0116 — measurement record

**Scene.** This is a 2D Blender render, 1386x1920 portrait, 24.006 fps, 32 frames (t = frame/24.006, from 0 to 1.291 s). The camera is static and looks straight at a flat blue corrugated building facade. In front of the facade are a yellow fire-escape staircase with three landings, three yellow doors and a framed window. One object moves: an **American football** (dark brown, white stripes near the tips). It falls straight down on the right side (x ≈ 1036 px) from y ≈ 228 px at frame 0 to y ≈ 1731 px at frame 31. Pixel coordinates use y pointing down.

## Files
- `scene.json`: inventory, static object extents, events and camera.
- `tracks/football.csv`: one row per frame (0–31) with these columns:
  - `cx, cy`: mask centroid, used as the ball-origin reference point.
  - `bbox_cx, bbox_cy`: centre of the bounding box.
  - `bbox_x0..y1, bbox_w, bbox_h`: the bounding box.
  - `mask_len, mask_wid`: minimum-area-rectangle long and short sides.
  - `area`: mask area in pixels.
  - `occluded`: always 0.
- `scripts/diff.py`: first-pass difference to a median background. `scripts/seg.py`: the final segmentation, which writes the track CSV and `frames/overlay.png`.

## Method
- The background for each pixel row is a frame where the ball is elsewhere: frame 31 for rows above y = 1000, frame 0 for rows below.
- The mask is the pixels that are (difference > 50) AND ball-coloured (B−R < 45: brown leather, or bright white stripe). This test leaves out the ball's blue-tinted shadow on the wall, which falls below-left of the ball.
- The largest component is kept and its holes are filled.
- I checked the overlays visually (frames 0, 6, 12, 16, 20, 24, 28, 31). The outline hugs the ball with no shadow included.

## Ball size and motion
- **Size:** about 63 px long (vertical long axis) × 39 px wide at frame 0. The median over all frames is 61 × 39.
- **Tumbling:** the ball turns slowly as it falls. The white stripe moves from the bottom tip to the top tip, so the apparent length varies between 57 and 64 px.
- **Motion blur:** small; mask height does not grow with speed.
- **Start:** the ball starts essentially at rest at frame 0 (dy = 1.25 px between frames 0 and 1).
- **Fall:** dy per frame then grows almost linearly, by about 3.3 px per frame each frame, reaching about 96 px/frame at frames 30→31. That fits uniform acceleration from rest. Horizontal motion is under ±2 px (noise).
- **End of clip:** at frame 31 the ball's bottom (y = 1763) has reached the wall base / ground line (≈1765–1770). There is no visible bounce or impact before the clip ends.

## Reliability
- **Centroid:** about ±1 px.
- **Frame 17 is an outlier:** the bbox widens to x0 = 1002 because a dark wall seam is included (the centroid is off by about 2 px). For frame 17, use `bbox_cy` or interpolate.
- **Ball sizes:** ±2 px.
- **Static extents** (doors, window, landings): read from a grid, ±5 px.

## Possible scale references
- Doors: about 155 px wide; the middle and bottom doors are about 342 px tall.
- Window: about 165 × 164 px.
- Landing width: about 363 px.
- Total drop from frame 0 to 31: 1502 px.

Because this is a 2D scene, one m/px scale from the question's prior applies everywhere. The ball and the wall features are nearly in the same plane, but the stairs stand slightly in front of the wall.
