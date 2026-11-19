# Q1021: height of the column below the drone (m)

The "column" is the dark cylindrical body (about 88 px wide) that hangs under the drone's wide top plate (about 230 px) and rises with it.
This is a 2D video: the camera is static and the motion is vertical in a plane facing the camera. I used the file rate, 24 fps, which matches question_fps.

## Scale (from the prior: the column moves at 0.96 m/s)
- The drone and column rise at a constant pixel speed after take-off.
  - Scene record, sub-pixel fit of the plate top over frames 2-71: 7.143 px/frame.
  - My integer plate-top fit over frames 30-71: 7.174 px/frame.
  - The column bottom edge, frames 30-60: 7.09-7.11 px/frame.
- I used about 7.13 px/frame, which is 171.1 px/s.
- Scale = 0.96 / 171.1 = 0.005611 m/px.

## Column pixel height (`column.py`, `rows.py`)
- Top of the column: the first row below the plate where the dark run through the centre narrows from about 230 px to about 88 px.
  - Frame 70: the plate spans rows 464-483 and the column starts at row 484.
- Bottom: the half-level crossing of the mean brightness of a centre strip.
- Over frames 30-60 the column height is 175.2 px (sd 0.5). Frame 70 by hand gives 484 → about 657.5, i.e. 174 px.
- From frame 61 on, the lid gets in the way of the automated bottom measurement, so I left those frames out.
- Column height = 175.2 × 0.005611 = **0.983 m**.

## Check and alternative reading
- Using the plate-top slope (7.143 px/frame) instead gives 0.981 m. Using the bottom-edge slope gives 0.988 m.
- If the column were taken to extend up through the plate, to the plate top (193.5 px), the answer would be 1.09 m.
  I did not use this, because the plate is visibly a separate wider part.
- Confidence: good, within about 2%, assuming the column is the visible cylinder below the plate.
