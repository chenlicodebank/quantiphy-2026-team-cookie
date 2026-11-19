# q_1650: bird's maximum wingspan (m)

Prior: bird speed = 6 m/s. There is no depth_info. The video is 2D and filmed from the top: the bird flies along +x
and its wings span along image y. File fps = 22, question_fps = 24.

## Wingspan in pixels (span.py)
Mask threshold min(RGB) < 200 plus a 3x3 opening, keeping the main component and the nearby feather tips. A looser
threshold (< 235) adds the anti-aliased edge. I took the y-extent on every frame:
- Maxima: frame 0 = 252/255, frame 18 = 255/256, frame 33 = 254/255, frame 50 = 247/250.
- Wings fully spread, so maximum span = **255 px**. I checked this on a zoomed crop of frame 18: the wings are fully
  open and nothing is cut off.

## Speed in pixels
- The bird speeds up (about 7 px/frame), cruises at about 20 px/frame from frames 13 to 45, then slows down at the end.
- Two source frames are missing (steps 18→19 and 42→43 are double length; the wing phase also jumps there). With those
  counted, the wingbeat period is a steady 17 source frames.
- Cruise speed measured between the same wing phase (minima at frames 25 and 42, 17 source frames apart):
  - body_mid_x: 340.5 px / 17 = 20.03 px per frame
  - centroid: 340.7 px / 17 = 20.04 px per frame
- Second route: a fit of body_mid_x over frames 20-42 gives 19.98 px per frame.
- I took the prior's 6 m/s to be this steady cruise (peak) speed.

## Time base
- The dropped frames show this clip was re-timed from the original render. The reference values come from the
  original footage, so I used question_fps = 24 (the Blender default) for one source-frame step.
- Scale = 6 / 24 / 20.0 = 0.01248 m/px.

## Answer
255 px x 0.01248 = **3.18 m**

## Alternatives (not used)
- File fps of 22: 3.47 m.
- Prior read as the mean speed over the clip (about 15.6 px per source frame): about 4.1 m.

Confidence: moderate. The main uncertainty is which speed and which fps the prior refers to.
