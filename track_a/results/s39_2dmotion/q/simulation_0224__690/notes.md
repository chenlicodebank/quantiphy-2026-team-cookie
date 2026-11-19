# q_690 — speed of the moving chess piece at t = 0.5 s

The question fps and the file fps are both 24, so t = 0.5 s is frame 12. This is a 2D scene, so one m/px scale comes
from the prior (the piece's diameter is 0.097 m).

## Object
The "block" in scene/ is the Chinese chess piece. It is a disc seen almost edge-on while it slides down the inclined
board, so its long extent along the slope is its diameter.

## Diameter in pixels (my own measurement, diffmask.py)
- Method: subtract a background frame (frame 30) and take the largest blob. I measured its extent along the slope
  direction (25.9°) on frames 11, 12 and 14.
- Results by threshold: 81.0 to 81.9 px at T=40, 79.3 px at T=60, 78.5 to 78.9 px at T=90. The record gives 81.5 px
  (range 80.2-82.7).
- The higher thresholds trim the soft edges, and the T=40 mask is close to the record. I used **80 px ±1.5**.
- SAM 3 check ("white object" with a box, frames 11 and 12):
  - SAM's length is 95.9-97.2 px, which is 18% larger.
  - On the zoomed overlay (frames/diff_f12.png, red = SAM, green = my mask), the SAM mask includes the piece's
    shadow on the board at its lower-left end. So SAM's length is wrong, and my value and the record's are right.
  - SAM's centroid moves 13.1 px from frame 11 to frame 12. My own centroid moves 12.8 px. These agree within 3%.
- Scale: 0.097 / 80 = 1.2125e-3 m/px.

## Speed
- Some video frames are duplicates and some are skipped (see scene/notes.md). Video frame 12 shows render frame
  about 13, and frame 13 duplicates it.
  - The raw backward difference at video frame 12 is 12.83 px. This step is really render 12→13.
  - At video frame 13 the raw difference is 0.
- The along-slope distance s, fitted against the render-frame index (non-duplicate frames), is a clean quadratic:
  - Window 8-16: rms 0.22 px.
  - Window 5-20: rms 0.31 px.
  - Window 3-24: rms 0.40 px.
  - Window 3-38: rms 0.8 px.
- Backward difference at render frame 12, s(12) - s(11): 11.17 / 11.20 / 11.25 / 11.26 px/frame across the windows.
  I used **11.22 px/frame**, which is 269.3 px/s.
- Speed = 269.3 × 1.2125e-3 = **0.326 m/s**.
  - With a diameter of 81.5 px: 0.321 m/s.
  - With 78.5 px: 0.333 m/s.

## Second route and confidence
- The second route is the SAM centroids, the record's centroids and my centroids, compared over frames 11-14:
  - Average over video frames 11→14 (render 12→14, 2 steps): (92.02 - 65.66) / 2 = 13.18 px per frame. That is
    the speed at about render frame 13, and the fit gives 13.3. This is consistent.
- A risk: if the reference used the video's raw frame step (12.8 px/frame), the answer would be 0.373 m/s (+14%).
  I judge that the Blender ground truth is per render frame, so I kept 0.326.
- Confidence: moderate-high (about ±3% from the scale, plus the frame-mapping risk above).
