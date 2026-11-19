# q 1792 — average speed of the boat (m/s)

Prior: boat length = 10 m. 2D video, 24 fps (question_fps = file fps = 24), static camera, white background.

## Scale
- Boat length at frame 57 (stern hull/rudder edge to bow tip), threshold mask in `measure.py`: x 666..1521 = 856 px.
- SAM 3 mask ("boat", frame 57): box x 666.7..1521.3, horiz 854 px; frame 25: 857 px. These agree with my 856 px to within 0.3 pct.
  (The SAM mask leaves out part of the lower keel band and the detached rudder pieces, but neither changes the horizontal extent.)
- Scale = 10 / 856 = 0.011682 m/px.

## Motion
- Frames 0-1 are identical (at rest); from frame 2 on, the boat translates horizontally at a constant rate.
- Bow-tip x (`measure.py`): 521 at frame 1, 1521 at frame 57 -> 1000 px / 56 frames = 17.86 px/frame.
- Phase correlation between consecutive frames: 17.8-18.3 per frame, mean 17.98 (slightly biased by the stern entering from the left edge).
- Scene record (template match): 17.86 px/frame; SAM box shift f25->f57: bow edge 570.8 px / 32 = 17.84 px/frame.
- Speed while moving = 17.86 x 24 x 0.011682 = 5.01 m/s.
- If the zero-speed frame 1 is included in the mean over frames 1..57, the result is 1000/57 x 24 x 0.011682 = 4.92 m/s.

## Answer
5.0 m/s. This is the constant moving speed and a round design value; the 4.92 reading differs from it by 1.7 pct.
Confidence: high, with an error of about 2 pct or less.
