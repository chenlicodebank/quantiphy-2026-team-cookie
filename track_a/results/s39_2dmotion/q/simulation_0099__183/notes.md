# Q183 — speed of the boat at 1.0 s (m/s)

Prior: boat length = 10 m. 2D video, question_fps = file fps = 24, so t = 1.0 s -> frame 24.

## Scale
- My own edge measurement (measure.py: |frame - right-side background| > 25 in hull rows 380-560): stern-to-bow
  extent 854-857 px over frames 0-45 (857 at frame 0, 854 at frame 24).
- SAM 3 "boat" mask: horiz_px 859 (f0), 858 (f24), 856 (f23). This agrees with my value to within 0.5 %. The scene
  record gives 851-860.
- I used L = 856 px, so the scale is 10/856 = 0.01168 m/px.

## Speed
- Bow and stern edges move linearly from frame 1 (at rest in frames 0-1) to frame 45. Stern: 226 -> 1015, so
  17.93 px/frame. Bow: 1083 -> 1494 (f24) -> 1870, so 17.89 px/frame. Frames 23 -> 24 give 18 px/frame (integer edges).
- The scene record gives 17.88 px/frame from the mast, rail post and stern, which agrees.
- Phase correlation on the hull band gives about 18.4 px/frame. It is biased by reflections sliding over the glossy hull
  (the record found the same effect), so I rejected it.
- SAM centroid check: f23 -> f24 is 1050.9 -> 1067.4 = 16.5 px. Box x0 shifts by 19.0 px and x1 by 18.1 px. These are
  noisy single-frame values, consistent with ~17.9.
- The speed is constant, so v = 17.91 px/frame x 24 x 10/856 = **5.02 m/s**. With L = 859 px (SAM) it is 5.00 m/s.

Confidence: high (likely 5 m/s by design).
