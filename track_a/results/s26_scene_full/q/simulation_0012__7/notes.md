# Q7 — bird wingspan when spread (m)

Prior: bird speed = 6 m/s. 2D-style top-down (nadir) view, static camera; the wings and the flight path are at the
same height above the ground, so one m/px scale from the speed applies to the wingspan.

## Time base
File fps 22.925, question_fps 24. The record shows double-size steps at frames 18->19 and 42->43 (and noise around
50-58): source frames were dropped when the clip was re-timed, i.e. the original render is 24 fps and consecutive
file frames between drops are consecutive 24 fps source frames. So the speed uses px per source frame x 24.

## Speed -> scale
The bird speeds up (frames 0-18), cruises at a constant rate (frames 20-45), then slows down. I took the prior's
"speed" to be the steady cruise speed:
- beak x frames 20->42: (1549-1111)/22 = 19.91 px/frame
- body_x frames 28->42: (1484-1205)/14 = 19.93 px/frame
-> 19.9 px x 24 = 478 px/s -> scale = 6/478 = 0.01256 m/px.

## Wingspan
Max extent across the body (top-down AABB across the flight direction) at full spread, frames 0-1, 17, 33, 49-50:
record 255-258 px; my own masks (measure.py, overlays frames/m*.png) give 254/256 (f0/f1) and 254/258 (f49/f50).
Frames 17/33 come out lower in my masks (250) because the dark wing tips over dark grass are lost; the overlay shows
the tips reach the record's extent. Used 257 px.
Wingspan = 257 x 0.01256 = 3.23 m.

## Checks and alternatives
- If the file fps (22.93) were used without allowing for the dropped frames: 456 px/s -> 3.38 m.
- If 6 m/s were the mean speed over the whole clip (965 px over ~63 source frames = 368 px/s): 4.19 m.
  The long constant-speed stretch suggests the 6 m/s is the cruise speed, so I answered with that.
Confidence: moderate. The pixel measurements are good to about 2%; the main uncertainty is which speed the prior means.
