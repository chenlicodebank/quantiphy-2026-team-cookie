# Q43: speed of the bicycle at 1.0 s (m/s)

The video is a 2D top-down orthographic render. The file runs at 24 fps and question_fps is also 24, so t = 1.0 s is frame 24.
Prior: the yellow car (the peach sedan) is 5.44 m long. I used one metres-per-pixel scale for the whole scene.

## Scale (car length)
- My own measurement (measure.py): the peach-paint component's extent along the car's axis is 218 px at frame 0 (car vertical) and 219 px at frame 71 (car horizontal).
  The non-road bounding box is 221-222 px, but that includes the soft shadow, so I did not use it.
- SAM 3 ("yellow car"): length 217.3 px at frame 0. At frame 71 the box spans 219.3 px horizontally (the tool reports 224 for length_px and horiz_px; I used the box span).
  These agree with my numbers to within 1 %. The scene record gives 220 px.
- I used 219 px, so the scale is 5.44 / 219 = 0.02484 m/px.

## Bicycle motion
- The bicycle rides straight up at x ≈ 918 at a constant rate. Both quadratic fits give an acceleration close to 0.
- Route 1, the mask centroid from the scene record (frames 3-71): the linear slope is 8.92 px/frame, and 8.86 px/frame locally over frames 14-34.
  The one-frame back-difference at frame 24 is 9.12 px, but that value carries about ±2 px of mask jitter.
- Route 2, my own template matching (template taken at frame 24, sub-pixel peak): 20→28 gives 8.95 px/frame, 10→60 gives 8.97, 24→25 gives 8.91, and the overall slope is 8.91.
- Route 3, SAM 3 track ("person", box prompt at frame 24): a linear fit gives 214.2 px/s, which is 8.93 px/frame. This matches routes 1 and 2.
- Adopted value: 8.93 px/frame × 24 = 214.3 px/s.

## Answer
214.3 px/s × 0.02484 m/px = 5.32 m/s. Using 220 px for the car length instead would give 5.30.
Confidence: high, about ±2 %.
