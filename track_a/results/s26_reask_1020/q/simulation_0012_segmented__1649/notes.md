# q_1649: length of the bird (m)

Prior: the bird's speed is 6 m/s. There is no depth_info. The video is 2D, a plan view from above or below: the bird flies along +x, with its wings spread along image y.
The file is 22 fps, but question_fps (24) is used for all timing, as the rules say.

## Measurements (measure.py, my own mask: min(RGB)<200 below row 850, opening, largest component)
- Bird length = bbox extent along the body (x). The median over 61 frames is 129 px (mean 129.5).
  At the wing-folded frames 9, 25, 42 and 58 it is 128-132 px. This matches the scene record (body_len_px median 129).
- Path of the centroid: 972 px over 60 frame steps. Its net displacement is 965 px (the path is nearly straight).
- The pixel speed is not constant. It rises from about 7 px/frame at the start to about 20 px/frame in the middle,
  then falls back to about 8 px/frame, with a wingbeat oscillation on top. This looks like a Bezier ease-in/out.
  There are two double steps (frames 18->19 and 42->43), each a skipped source frame.

## Scale
A constant prior speed with a varying pixel speed means the prior is most likely the average speed (path / time).
- Mean of the per-frame speeds at 24 fps = 388.9 px/s, so the scale is 0.01543 m/px and L = 1.99 m.
- If the two skipped source frames count as time (62 steps): L = 2.06 m.
- If the prior is instead the mid-flight plateau speed (about 477 px/s): L = 1.62 m.

## Answer
1.95 m: chosen near the average-speed reading (1.99), shaded slightly toward the plateau reading.

## Plausibility
Under any of these readings the bird is about 1.6-2.1 m long, which is large for a hawk or crow-like bird.
Its pixel proportions (wingspan about 2x length) are those of a raptor. No standard object of known size is in the
scene, so the scale is taken from the prior, as the prior is exact.

Confidence: moderate. The main uncertainty is which speed the prior refers to.
