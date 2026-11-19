# q3275: distance between the blue bag and the yellow bag (internet_0073, 2D planar convention)

Prior: the conveyor belt moves at 0.3 m/s. depth_info: none. File: 25.111529 fps (constant PTS, odd timebase 1/20039).
question_fps: 30.

## Time base
The per-frame steps of the parcels (`steps.py`) are uniform at about 1.98 px/frame. There is no pattern of
dropped or duplicated frames, so the clip has the original frames and only its timestamps were re-scaled. This fits
a 30 fps original that was re-timed to 25.11 fps. Both rates give plausible parcel sizes: a courier pouch is 0.44 m
at 30 fps and 0.53 m at 25.11 fps, so the scene does not decide between them. I used question_fps = 30, the rate
stated with the question.

## Scale
- Belt pixel speed: the mean of the five reliable rigid parcels in background coordinates, with the camera drift
  removed (scene tracks, linear fit over frames 0-137). The parcels give 1.96-2.01 px/frame, mean 1.98. The blue bag
  itself gives 1.93 px/frame.
- I used 1.97 px/frame, which is 59.1 px/s at 30 fps. Scale = 0.3 / 59.1 = 0.00508 m/px.

## Distance in pixels (frame 0, centre to centre)
- blue bag: bbox x 730-866, y 357-407. Centre (798, 382). My colour mask (`seg.py`) misses the dark right tail; the
  record's bbox gives a centre of (796, 381).
- yellow bag (the moving one on the belt, not the static one inside the truck): bbox x 912-1083, y 290-412. Centre
  (997.5, 351). The colour mask gives the same box.
- Centre to centre: dx ≈ 200 px, dy ≈ 31 px, giving |d| ≈ 202 px.
- The yellow bag moves a little faster (2.14 px/frame), so the gap grows over time: about 209 px at frame 30 and
  216 px at frame 56. No time is given, so I used frame 0.

## Answer
- 202 px × 0.00508 m/px = **1.03 m**.
- Under the other fps (25.11), the answer would be 1.22 m.
- Under the other reading of "distance", the edge-to-edge gap is about 44 px, which is 0.22 m.

## Check
- Second route, from the scene-record tracks: the background-coordinate centres at frame 0 are 998.5 - 796.0 = 202.5
  px horizontally (205 px in 2D), which gives 1.03-1.04 m.
- Confidence: moderate. The main uncertainties are the fps choice (±18%) and the frame at which the annotators
  measured (+5% if mid-clip).
