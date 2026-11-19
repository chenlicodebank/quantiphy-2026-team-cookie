# q3280: distance between the red package and the blue bag (internet_0073)

Prior: belt velocity = 0.3 m/s. The video is 2D/planar, and both parcels ride the same belt at the same height.
I used one scale: m/px = 0.3 / (belt px/frame x fps).

## Measurements
- **Belt pixel speed** (`steps2.py`): I tracked each parcel frame to frame with NCC, using the previous frame as the
  template, and subtracted the background step (a static strip of the belt side frame; camera drift is about
  -0.11 px/frame). Median steps were red_parcel 1.938, cardboard_box 1.949 and white_box 1.942 px/frame.
  I used **1.945 px/frame**. The steps are uniform (std 0.2) apart from one doubled step at frame 54, which is a
  single dropped frame, so the clip is not decimated. The scene record's background tracks agree (1.92-1.96).
- **Positions** (scene tracks, checked on 4x zoomed crops and HSV masks in `measure.py`):
  - Red package: x 369-462 at frame 0, centre 415.5.
  - Blue bag: x about 730-862 at frame 0, centre 796. The HSV mask misses the bag's dark right tail, so I used the
    record's box, which matches the zoomed view.
  - Centre-to-centre distance in background coordinates: 380.5 px at frame 0 and 375.5 px at frame 137. I used the
    mean, **378 px**, about ±4 px.

## Time base
The file is 25.11 fps and question_fps is 30. The steps are uniform with only one dropped frame, so the frames are
consecutive original frames. Two cases fit that:
- the clip is a 30 fps original that was re-timed, or
- it is a real ~25 fps recording.

Parcel sizes are plausible either way: the red package comes out at 0.48 m with 30 fps and 0.57 m with 25.11 fps.
There is no size cue at belt depth that can decide between them. I followed the rate stated with the question, 30 fps,
because the annotators converted using that rate.

## Result
- Scale = 0.3 / (1.945 x 30) = 0.005141 m/px.
- Distance = 378 x 0.005141 = **1.94 m** (centre to centre).
- With the file fps (25.11), it would be 2.32 m.
- Edge-to-edge gap (462 -> 730, 268 px) would be 1.38 m (1.65 m at 25.11 fps).

## Second-route check
- Image-coordinate positions without drift correction give a speed of 1.836 px/frame and a distance of 377.5 px,
  which is 2.06 m (5% higher).
- Per-object background speeds of 1.92-1.96 change the result by ±1%.

Confidence: moderate. The main uncertainty is the fps choice (±19%); the blue bag's centre is ±1%.
