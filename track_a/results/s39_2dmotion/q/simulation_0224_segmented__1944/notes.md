# q_1944 — speed of the red general chess piece at t = 0.5 s (m/s)

File fps = question_fps = 24, so t = 0.5 s is frame 12. 2D video. Prior: piece diameter = 0.097 m.

## Object
The scene record calls the only moving object a "block". It is actually the chess piece, a disc lying flat in the
ramp's trough and seen at an angle, so it looks like an elongated ellipse. It slides down the ramp at 26°.
The long axis of the ellipse is the disc's diameter.

## Scale (measure.py, size43.py, compare_mask.py)
- My own mask (colour difference from the median background): long-axis length is 81.0 px (median over frames on
  the ramp, 80.6–82). On frame 43, where the piece is in the air against white: 82.9 px (threshold 120–200) and
  82.25 px (half-maximum profile). Chosen D = 81.5 px, so the scale is 0.097/81.5 = 1.190e-3 m/px.
- The scene record's value of 81.3 px agrees with mine.
- The SAM 3 masks give 89.9–91.9 px on frames 0, 12 and 43, more than 3 % above mine. On the zoomed overlay of
  frame 43 (frames/cmp_f43.png) the SAM outline sits about 2–3 px outside the piece's edge all the way round, and its
  area (2636 px) is larger than my mask's (2300 px). So SAM is too large, and I used my own mask. SAM's centroids match
  mine to within about 1 px on frames 0 and 43. On frame 12 the SAM mask takes in some trough and rim, which shifts
  its centroid by up to 5 px in y.

## Speed (speed.py)
- In the video, frames 6, 13, 25, 28, 35 and 38 repeat the previous frame, and frames 5, 10, 23, 27, 34 and 37 jump
  about two steps. Raw one-frame differences are therefore unreliable.
- Raw backward difference at video frame 12: 11.97 px/frame (record template track) and 12.82 (my centroid).
- I remapped the frames to estimated true render indices and fitted a quadratic: a = 1.00–1.02 px/frame²,
  rms 0.7–1.2 px. The backward difference at render frame 12 is 11.20–11.28 px/frame. Video frame 12 shows render
  frame 13, where it is 12.22–12.28. The instantaneous speed at render frame 12 is 11.71–11.78.
- Chosen speed: 11.75 px/frame × 24 = 282 px/s, which gives **0.336 m/s**.
  The other readings give 0.322 m/s (render frame 12) and 0.346 m/s (raw video frame 12), both within about 4 %.

## Second route
The template track from the scene record and my mask-centroid track give the same fit to within 0.1 px/frame.

## Confidence
Moderate to good. The main uncertainty is whether the reference uses render frame 12 or video frame 12 (±4 %).
The scale is uncertain by about 1 %.
