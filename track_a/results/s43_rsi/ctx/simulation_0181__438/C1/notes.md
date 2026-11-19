# q_438 — speed of the box at t = 1.5 s (frame 36)

Prior: the box's acceleration after 0.75 s is 2.338 m/s². No depth_info. fps = question_fps = 24, so no re-timing.
Scene is labelled 2D: the box slides down a ramp in a plane roughly parallel to the image (track slope 28.8°).
Its apparent size stays constant while sliding (min-area rectangle 279 ± 2 px, frames 20–29), so the depth is
constant and one metres-per-pixel scale applies.

## Method
- `pair.py`: frame-to-frame masked template matching. Box pixels in frame i-1 are found as the difference from
  frame 0, with the frame-0 box ghost and the edges removed and the China Food crates excluded as an occluder.
  Only the upper 70 % of the box (away from the ramp) is used. The script finds the shift into frame i with
  sub-pixel accuracy, which gives the per-frame displacement directly (backward difference).
  Steps (px/frame) rise smoothly from 22.5 (frame 15) to 47.7 (frame 39); frame 36 = 44.14 px/frame.
  The match error stays low all the way to frame 39, while the box goes behind the crates.
- `fit3.py`: linear fit of step against frame, which is constant acceleration. Over frames 15–39:
  a = 593 px/s², rms 0.48 px. Over 18–39: 595. Over 24–39: 597. Over 18–30: 598. Locally around 0.75 s: 612.
  Speed at frame 36: 1056 px/s fitted, 1059 px/s raw.
- Scale from the prior: 2.338 / 594 = 3.94 mm/px.
- Speed at 1.5 s = 1056 px/s × 3.94 mm/px = **4.15 m/s**. Across fit windows the result is 4.14–4.23.
  This is the same as v/a × 2.338: the fitted speed reaches zero about 6.6 frames before t = 0.

## Checks / disagreements
- The scene record's centroid track gives 3.6–4.0 m/s, depending on the fit window. Its centroid is biased:
  - The silhouette changes in frames 12–20 as the box turns about the vertical axis (length goes 311 → 280 px).
  - From frame 30 on, the record uses template jitter instead (frames 35/36 step 44/27 px).
  Frame-to-frame texture matching avoids both problems and is much smoother (rms 0.5 px compared with about
  1.5 px), so I trust it more.
- Trailing-edge tracking was rejected: the box's left side face comes into view (perspective) as it moves right,
  which biases the edge.
- Free fall (frames 0–7): about 2300 px/s². With the prior scale that is about 9.1 m/s², close to g, which
  supports the scale (within about 7 %).

Confidence: fairly high (about ±5 %). The main risk is if the reference acceleration at 0.75 s differs from the
mean sliding acceleration.
