# q_1963 — acceleration of the "red general chess" at t = 1 s (prior: cat speed = 1.041 m/s)

File fps = question_fps = 24, so t = 1 s is frame 24.

## Asked object is not in the video
- The contact sheet (frames/sheet.png) shows only a walking cat, a sliding flamingo float and six static lounge
  chairs plus a small round item, all on a white background. There is no chess piece.
- find.py looks for red pixels (R>140, G<90, B<90) and for every non-white pixel in the full frame. It found no red
  pixels in any sampled frame. Every non-white pixel lies inside the known cat, float and chair region
  (x 512–1431, y 712–1019).
- So the answer cannot be measured. The value below is a best-effort stand-in, not a measurement.

## Scale (2D, from the prior)
- Cat centroid, linear fit over frames 0–49: 5.465 px/frame (fits on the bbox front and back edges give 5.463 and
  5.439) = 131.2 px/s.
- Scale = 1.041 / 131.2 = 0.00794 m/px.

## Stand-in: the flamingo float (the only accelerating object)
- Per-frame dx rises from 0.8 to about 13.5 px/frame at frames 22–25, then falls to 1.0 px/frame at frame 49. The
  shape is a smooth ease-in/ease-out (peak/mean ≈ 1.54), so its true acceleration at frame 24 is near 0.
- One-frame convention at frame 24: speed(24) − speed(23) = 0.6 px/frame² → 2.74 m/s². This comes from noisy
  centroid differences.
- Speeding-up phase, peak speed over time: 13.5 px/frame / 24 frames ≈ 0.56 px/frame² → 2.57 m/s².
- Quadratic fits: frames 2–22 give 2.43 m/s², frames 1–20 give 2.76 m/s². A piecewise fit gives +2.19 then
  −2.23 m/s².
- Answer: about 2.5 m/s², the typical acceleration magnitude in the scene.

## Confidence
Very low. The asked object (red general chess) does not appear in this segmentation video. The question is
probably mismatched with this clip.
