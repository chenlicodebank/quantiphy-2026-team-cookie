# Q5: width of the house from eave to eave (m)

Prior: the bird flies at 6 m/s. Scene: a top-down (nadir) view treated as 2D, so one m/px scale comes from the bird's speed.

## Time base
The file is 22.93 fps and the question says 24 fps. The steps at 18->19 and 42->43 are twice the size of their neighbours,
which means source frames were dropped (61 frames at 22.93 fps is about 64 frames at 24 fps). So each step between
neighbouring frames lasts 1/24 s, and I used 24 fps.

## Scale
Cruise frames 19-42 contain no skipped frames. Over them the beak moves 20.0 px/frame and the body centre 19.96 px/frame
(the 20-41 and 22-40 windows give 20.0 and 20.2). The bird accelerates and decelerates at the ends of the clip, so I took
the cruise value as the prior's speed: 20.0 x 24 = 480 px/s, which gives 6/480 = 0.0125 m/px.
(At 22.93 fps the scale would be 0.0131 m/px, about 5% larger.)

## House width (measure.py plus 3x zoomed crops of frame 0)
The ridge runs along image y, so the width runs along x.
- Roof planks: eave edges at x ~426-434 (left) and ~1350-1352 (right), so about 920 px wide, or 11.5 m.
- The crossed bargeboards at the front gable stick out past the eaves to x ~398 and ~1389, about 990 px, or 12.4 m.
- Answer: the midpoint of the two readings, about 955 px, or 11.9 m. It is within about 4% of either reading.

## Confidence
Moderate. The two eave readings differ by about 7%. The answer also assumes the prior's 6 m/s means the cruise speed; if it
means the clip's mean speed (about 15.4 px/frame), the answer would be about 30% larger. The roof is higher than the
ground, but it is treated with the same planar scale as the bird.
